%main program
reduce_prog([Var,Func,Body]) :-
	% Add vars/consts to the symbol table
	create_env(Var,env([[]],_),Env),
	% Add functions to the symbol table
	create_env(Func,Env,Env1),
	% Reduce the body of the program
	reduce_stmt(config(Body,Env1),_).	

% Define boolean values
boolean(true).
boolean(false).

% --- Helper predicates - START ---
%check if X has been declared in a list of the environment
has_declared(X,[id(X,Y,Z,V)|_],id(X,Y,Z,V)):- !.
has_declared(X,[_|L],R) :-  has_declared(X,L,R).

% Determine type of the literal
type_of(V, boolean) :- boolean(V),!.
type_of(V, integer) :- integer(V),!.
type_of(V, float) :- float(V),!.
type_of(V, string) :- string(V),!.

% Loop through the environment to find the identifier
lookup(Id, [L|_], id(X,Y,Z,V)):-
	has_declared(Id,L,id(X,Y,Z,V)),!.
lookup(Id, [_|L2], R):-
	lookup(Id,L2,R).

% Bind the args to the parameters
bind_args([],[],Env,Env):-!.
bind_args([par(Id,_)|Params],[Val|Args],Env,EnvOut):-
	update_env(Id,Val,Env,Env1),
	bind_args(Params,Args,Env1,EnvOut).

eval_args([],[],_):-!.
eval_args([E|T],[V|T1],Env):-
	reduce_all(config(E,Env),config(V,Env)),
	eval_args(T,T1,Env).
% --- Helper predicates - END ---

% --- Symbol table - START ---
% create a symbol table from the list of variable or constant declarations 
%% Base case: Not add anything to the environment
create_env([],Env,Env).

%% Variable declaration
create_env([var(I,Type)|_],env([_],_),_):- % Global scope
	is_builtin(I,_),!,throw(redeclare_identifier(var(I,Type))).
create_env([var(I,Type)|_],env([L1|_],_),_):-
	has_declared(I,L1,_),!,throw(redeclare_identifier(var(I,Type))).
create_env([var(I,Type)|L],env([L1|L2],Context),EnvOut):- 
	create_env(L,env([[id(I,var,Type,null)|L1]|L2],Context),EnvOut).

%% Constant declaration
create_env([const(I,E)|_],env([_],_),_):- % Global scope
	is_builtin(I,_),!,throw(redeclare_identifier(const(I,E))).
create_env([const(I,E)|_],env([L1|_],_),_):-
	has_declared(I,L1,_),!,throw(redeclare_identifier(const(I,E))).
create_env([const(I,E)|L],env([L1|L2],T),EnvOut):-
	(type_of(E,Type) -> % Determine the type of const
		create_env(L,env([[id(I,const,Type,E)|L1]|L2],T),EnvOut)
		; throw(type_mismatch(const(I,E)))).

%% Parameter declaration
create_env([par(I,Type)|_],env([L1|_],_),_):-
	has_declared(I,L1,_),!,throw(redeclare_identifier(par(I,Type))).
create_env([par(I,Type)|L],env([L1|L2],T),EnvOut):-
	create_env(L,env([[id(I,par,Type,null)|L1]|L2],T),EnvOut).

%% Function declaration
% Only care Global scope
create_env([func(I,_,_,_)|_],env([_],_),_):- 
	is_builtin(I,_),!,
	throw(redeclare_function(I)).
create_env([func(I,_,_,_)|_],env([L1|_],_),_):-
	has_declared(I,L1,_),!,
	throw(redeclare_function(I)).
%# Add function to the symbol table
create_env([func(I,Params,RetType,Stmts)|L],env([L1|L2],T),EnvOut):-
	create_env(Params,env([[]|[L1|L2]],_),_),
	create_env(
		L,env([[id(I,func,func(I,Params,RetType,Stmts),null)|L1]|L2],T),
		EnvOut).

%% Procedure declaration
create_env([proc(I,_,_)|_],env([_],_),_):- 
	is_builtin(I,_),!,
	throw(redeclare_procedure(I)).
create_env([proc(I,_,_)|_],env([L1|_],_),_):-
	has_declared(I,L1,_),!,
	throw(redeclare_procedure(I)).
%# Add procedure to the symbol table
create_env([proc(I,Params,Stmts)|L],env([L1|L2],T),EnvOut):-
	create_env(Params,env([[]|[L1|L2]],_),_),
	create_env(
		L,env([[id(I,proc,proc(I,Params,Stmts),null)|L1]|L2],T),
		EnvOut).

%% Update the symbol table
update_env(Id,_,env([],_),env(_,_)):-
	throw(undeclare_identifier(Id)).

update_env(Id,Val,env([Scope|L],context(CurrFunc,InLoop)),env([ScopeOut|L],context(CurrFunc,InLoop))):-
	update_scope(Id,Val,Scope,ScopeOut,CurrFunc),!.

update_env(Id,Val,env([Scope|L],Context),env([Scope|LOut],Context)):-
	update_env(Id,Val,env(L,_),env(LOut,Context)).

update_scope(_,_,[],[],_):- fail.
update_scope(Id,Val,[id(Id,const,_,_)|_],_,_):-
	% Cannot assign to a constant
	throw(cannot_assign(assign(Id,Val))).
update_scope(Id,Val,[id(Id,func,Type,_)|T],[id(Id,func,Type,Val)|T],CurrFunc):-
	!,CurrFunc == Id,
	Type = func(_,_,RetType,_),
	(type_of(Val,RetType) -> true ; throw(type_mismatch(assign(Id,Val)))).
update_scope(Id,Val,[id(Id,Kind,Type,_)|T],[id(Id,Kind,Type,Val)|T],_):-
	(Kind == var ; Kind == par),!,
	(type_of(Val,Type) -> true ; throw(type_mismatch(assign(Id,Val)))).
update_scope(Id,Val,[H|T],[H|NewT],CurrFunc):-
	update_scope(Id,Val,T,NewT,CurrFunc).

%% --- Symbol table - END ---

% --- Expression reduction - START ---
%% --- Numerical expressions - START ---
reduce(config(sub(E),Env),config(R,EnvOut)) :-  
	reduce_all(config(E,Env),config(V,EnvOut)),
	(number(V) -> R is -V ; throw(type_mismatch(sub(E)))).
% Addition
reduce(config(add(E1,E2),Env),config(R,EnvOut)) :-
	reduce_all(config(E1,Env),config(V1,Env1)),
	reduce_all(config(E2,Env1),config(V2,EnvOut)),
	(number(V1), number(V2) -> R is V1 + V2 ; throw(type_mismatch(add(E1,E2)))).

% Subtraction
reduce(config(sub(E1,E2),Env),config(R,EnvOut)) :-  
	reduce_all(config(E1,Env),config(V1,Env1)),
	reduce_all(config(E2,Env1),config(V2,EnvOut)),
	(number(V1), number(V2) -> R is V1 - V2 ; throw(type_mismatch(sub(E1,E2)))).

% Multiplication
reduce(config(times(E1,E2),Env),config(R,EnvOut)) :-  
	reduce_all(config(E1,Env),config(V1,Env1)),
	reduce_all(config(E2,Env1),config(V2,EnvOut)),
	(number(V1), number(V2) -> R is V1 * V2 ; throw(type_mismatch(times(E1,E2)))).

% Real division
reduce(config(rdiv(E1,E2),Env),config(R,EnvOut)) :-
	reduce_all(config(E1,Env),config(V1,Env1)),
	reduce_all(config(E2,Env1),config(V2,EnvOut)),
	(number(V1), number(V2) -> R is V1 / V2 ; throw(type_mismatch(rdiv(E1,E2)))).

% Integer division
reduce(config(idiv(E1,E2),Env),config(R,EnvOut)) :-  
	reduce_all(config(E1,Env),config(V1,Env1)),
	reduce_all(config(E2,Env1),config(V2,EnvOut)),
	(integer(V1), integer(V2) -> R is V1 div V2 ; throw(type_mismatch(idiv(E1,E2)))).

% Modulo
reduce(config(imod(E1,E2),Env),config(R,EnvOut)) :-  
	reduce_all(config(E1,Env),config(V1,Env1)),
	reduce_all(config(E2,Env1),config(V2,EnvOut)),
	(integer(V1), integer(V2) -> R is V1 mod V2 ; throw(type_mismatch(imod(E1,E2)))).
%% --- Numerical expressions - END ---

%% --- Logical expressions - START ---
reduce(config(bnot(E),Env),config(R,EnvOut)) :-  
	reduce_all(config(E,Env),config(V,EnvOut)),
	(boolean(V) -> (V == true -> R = false ; R = true)).

reduce(config(band(E1, E2), Env), config(R, EnvOut)) :-
	reduce_all(config(E1, Env), config(V1, Env1)),
	(boolean(V1) -> (
		V1 == false -> R = false , EnvOut = Env1 ; 
		reduce_all(config(E2, Env1), config(V2, EnvOut)),
		(boolean(V2) -> (V2 == false -> R = false ; R = true) 
			; throw(type_mismatch(band(E1,E2))))
	) ; throw(type_mismatch(band(E1,E2)))).

reduce(config(bor(E1, E2), Env), config(R, EnvOut)) :-
	reduce_all(config(E1, Env), config(V1, Env1)),
	(boolean(V1) -> (
		V1 == true -> R = true, EnvOut = Env1 ;
		reduce_all(config(E2, Env1), config(V2, EnvOut)),
		(boolean(V2) -> (V2 == true -> R = true ; R = false) 
			; throw(type_mismatch(bor(E1,E2))))
	) ; throw(type_mismatch(bor(E1,E2)))).
%% --- Logical expressions - END ---

%% --- Relational expressions - START ---
reduce(config(greater(E1, E2), Env), config(R, EnvOut)) :-
    reduce_all(config(E1, Env), config(V1, Env1)),
    reduce_all(config(E2, Env1), config(V2, EnvOut)),
    (number(V1), number(V2) -> (V1 > V2 -> R = true ; R = false)
    ; throw(type_mismatch(greater(E1,E2)))).

reduce(config(less(E1, E2), Env), config(R, EnvOut)) :-
	reduce_all(config(E1, Env), config(V1, Env1)),
	reduce_all(config(E2, Env1), config(V2, EnvOut)),
	(number(V1), number(V2) -> (V1 < V2 -> R = true ; R = false)
	; throw(type_mismatch(less(E1,E2)))).

reduce(config(ge(E1, E2), Env), config(R, EnvOut)) :-
	reduce_all(config(E1, Env), config(V1, Env1)),
	reduce_all(config(E2, Env1), config(V2, EnvOut)),
	(number(V1), number(V2) -> (V1 >= V2 -> R = true ; R = false)
	; throw(type_mismatch(ge(E1,E2)))).

reduce(config(le(E1, E2), Env), config(R, EnvOut)) :-
	reduce_all(config(E1, Env), config(V1, Env1)),
	reduce_all(config(E2, Env1), config(V2, EnvOut)),
	(number(V1), number(V2) -> (V1 =< V2 -> R = true ; R = false)
	; throw(type_mismatch(le(E1,E2)))).


reduce(config(eql(E1, E2), Env), config(R, EnvOut)) :-
	reduce_all(config(E1, Env), config(V1, Env1)),
	reduce_all(config(E2, Env1), config(V2, EnvOut)),
	(((integer(V1), integer(V2))
	  ; (float(V1), float(V2))
	  ; (boolean(V1), boolean(V2))) -> %??? Both be Float
			(V1 == V2 -> R = true; R = false)
			; throw(type_mismatch(eql(E1,E2)))).

reduce(config(ne(E1, E2), Env), config(R, EnvOut)) :-
	reduce_all(config(E1, Env), config(V1, Env1)),
	reduce_all(config(E2, Env1), config(V2, EnvOut)),
	( (integer(V1), integer(V2)); (float(V1), float(V2)); (boolean(V1), boolean(V2)) ) -> %??? Both be Float
		(V1 \= V2 -> R = true ; R = false)
		; throw(type_mismatch(ne(E1,E2))).
%% --- Relational expressions - END ---

%% --- Variable, Constant expressions - START ---
reduce(config(Id,Env),config(Value,Env)):-
	atom(Id), %??? simple identifier,
	Env = env(SymTable,_),
	(lookup(Id,SymTable,id(Id,Kind,_,Value)) -> % Lookup in the environment
		((Kind \= var, Kind \= const, Kind \= par -> 
		 	throw(undeclare_identifier(Id)) ; true),
		  (Value == null -> throw(invalid_expression(Id)) ; true)
		);
		throw(undeclare_identifier(Id))).
%% --- Variable, Constant expression - END ---

%% --- Function call - START --- 
reduce(config(call(F,X),_),config(X,_)):-
	is_builtin(F,func),!,
	p_call_builtin(F,X).

reduce(config(call(F,Args),Env),config(R,EnvOut)):-
	Env = env(SymTable,context(InitFunc,InLoop)),
	lookup(F,SymTable,id(F,func,func(F,Params,_,Stmts),_)),!,
	(length(Args, N),length(Params, M),N==M-> % Check the number of arguments
		(
			eval_args(Args,Args1,Env), % Evaluate the arguments
			% Add the parameters to the symbol table
			create_env(Params,env([[]|SymTable],_),Env1),
			% Bind the arguments to the parameters
			catch(
				bind_args(Params,Args1,Env1,Env2),
				type_mismatch(_),
				throw(type_mismatch(call(F,Args)))
			),
			% Reduce the function body
			Env2 = env(SymTable1,_),
			reduce_stmt(config(Stmts,env(SymTable1,context(F,_))),Env3),
			Env3 = env([_|SymTable2],_),
			EnvOut = env(SymTable2,context(InitFunc,InLoop)),
			lookup(F,SymTable2,id(_,_,_,R)),
			(R == null -> throw(invalid_expression(call(F,Args))) ; true)
		)
		; throw(wrong_number_of_argument(call(F,Args)))).
	
reduce(config(call(F,Args),_),_):-
	throw(undeclare_function(call(F,Args))).
% --- Expression reduction - END ---


reduce_all(config(V,Env),config(V,Env)):- (number(V);boolean(V);string(V)),!.
reduce_all(config(E,Env),config(E2,EnvOut)):-
	reduce(config(E,Env),config(E1,Env1)),!,
	reduce_all(config(E1,Env1),config(E2,EnvOut)).


% --- Statement reduction - START ---
reduce_stmt(config([],Env),Env):- !. % Base case
%% --- Procedure - Call - START ---
reduce_stmt(config([call(F,[])|Rest],Env),EnvOut) :- 
	is_builtin(F,proc),!,
	p_call_builtin(F,[]),
	reduce_stmt(config(Rest,Env),EnvOut).

reduce_stmt(config([call(F,[X])|Rest],Env),EnvOut) :- 
	is_builtin(F,proc),!,
	reduce_all(config(X,Env),config(V,Env1)),
	catch(
		p_call_builtin(F,[V]), %!!! Read stmt's input
		type_mismatch(_),
		throw(type_mismatch(call(F,[X])))
	), %!!! Read stmt's input
	reduce_stmt(config(Rest,Env1),EnvOut).

reduce_stmt(config([call(F,Args)|Rest],Env),EnvOut) :-
	Env = env(SymTable,context(_,InLoop)),
	lookup(F,SymTable,id(F,proc,proc(F,Params,Stmts),_)),!,
	((length(Args, N),length(Params, M),N==M)-> % Check the number of arguments
		(
			eval_args(Args,Args1,Env), % Evaluate the arguments
			% Add the parameters to the symbol table
			create_env(Params,env([[]|SymTable],_),Env1),
			% Bind the arguments to the parameters
			catch(
				bind_args(Params,Args1,Env1,Env2),
				type_mismatch(_),
				throw(type_mismatch(call(F,Args)))
			),
			% Reduce the function body
			Env2 = env(SymTable1,_),
			reduce_stmt(config(Stmts,env(SymTable1,context(F,_))),Env3),
			Env3 = env([_|SymTable2],_),
			Env4 = env(SymTable2,context(_,InLoop))
		)
		; throw(wrong_number_of_argument(call(F,Args)))),
	reduce_stmt(config(Rest,Env4),EnvOut).
	
reduce_stmt(config([call(F,Args)|_],_),_):-
	throw(undeclare_procedure(call(F,Args))).
%% --- Procedure-Call - END ---

%% --- Assignment ---
reduce_stmt(config([assign(Id,E)|Rest],Env),EnvOut) :-
	reduce_all(config(E,Env),config(V,Env1)),
	catch(
		update_env(Id,V,Env1,Env2), 
		Error,
		(
			(   compound(Error),
				Error =.. [ErrName, assign(_,_)]
			->
				NewError =.. [ErrName, assign(Id, E)],
				throw(NewError)
			;
				throw(Error)  % re-throw all other errors
			)
		)
	),
	reduce_stmt(config(Rest,Env2),EnvOut).

%% --- Compound statement ---
reduce_stmt(config([block(Decls,Stmts)|Rest],Env),EnvOut) :-
	Env = env(SymTable,Context),
	% Add the declarations to the local scope
	create_env(Decls,env([[]|SymTable],Context),Env1),
	% Perform stmts in the new env
	reduce_stmt(config(Stmts,Env1),Env2),
	% Remove the local scope
	Env2 = env([_|SymTable2],Context2),
	reduce_stmt(config(Rest,env(SymTable2,Context2)),EnvOut).

%% --- If statement ---
reduce_stmt(config([if(Cond,Then,Else)|Rest],Env),EnvOut) :-
	reduce_all(config(Cond,Env),config(V,Env1)),
	(boolean(V) -> (
		V == true -> reduce_stmt(config([Then],Env1),Env2)
		; reduce_stmt(config([Else],Env1),Env2)
	) ; throw(type_mismatch(if(Cond,Then,Else)))),
	reduce_stmt(config(Rest,Env2),EnvOut).

reduce_stmt(config([if(Cond,Then)|Rest],Env),EnvOut) :-
	reduce_all(config(Cond,Env),config(V,Env1)),
	(boolean(V) -> (
		V == true -> reduce_stmt(config([Then],Env1),Env2)
		; Env2 = Env1 % Skip 'Then'
	) ; throw(type_mismatch(if(Cond,Then)))),
	reduce_stmt(config(Rest,Env2),EnvOut).

%% --- While statement ---
reduce_stmt(config([while(Cond,Stmt)|Rest],Env),EnvOut):-
	reduce_all(config(Cond,Env),config(V,Env1)),
	(boolean(V) -> (
		(V == true -> 
			catch(
				(	
					Env1 = env(SymTable,context(Func,_)),
					reduce_stmt(config([Stmt],env(SymTable,context(Func,true))),Env2),
					reduce_stmt(config([while(Cond, Stmt)|Rest], Env2), EnvOut)
				),
				Error,
				(
					Error = break(BreakEnv)->
					 	reduce_stmt(config(Rest, BreakEnv), EnvOut);
					Error = continue(ContEnv) ->
						reduce_stmt(config([while(Cond, Stmt)|Rest], ContEnv), EnvOut);
					throw(Error)
				)
			)
			
		; 
			reduce_stmt(config(Rest, Env1), EnvOut))
	) ; throw(type_mismatch(while(Cond,Stmt)))).

%% -- Do-while statement ---
reduce_stmt(config([do(Stmt,Cond)|Rest],Env),EnvOut):-
	\+ is_list(Stmt),!,
	reduce_stmt(config([do([Stmt],Cond)|Rest],Env),EnvOut).

reduce_stmt(config([do(List,Cond)|Rest],Env),EnvOut):-
	catch(
		(
			Env = env(SymTable,context(Func,_)),
			reduce_stmt(config(List,env(SymTable,context(Func,true))),Env1),
			reduce_all(config(Cond,Env1),config(V,Env2)),
			(boolean(V) -> 
				(V == true -> 
					Next = [do(List,Cond)|Rest]
					; Next = Rest
				) 
				; throw(type_mismatch(do(List,Cond)))), 
			reduce_stmt(config(Next,Env2),EnvOut)
		),
		Error,
		(
			Error = break(BreakEnv) ->
				reduce_stmt(config(Rest, BreakEnv), EnvOut)
			; Error = continue(ContEnv) ->
				reduce_all(config(Cond, ContEnv), config(V, Env3)),
				(boolean(V) ->
					(V == true ->
						reduce_stmt(config([do(List, Cond)|Rest], Env3), EnvOut)
					;
						reduce_stmt(config(Rest, Env3), EnvOut)
					)
				; throw(type_mismatch(do(List,Cond))))
			; throw(Error)
		)
	).

%% --- Loop statement ---
reduce_stmt(config([loop(E,S)|Rest],Env),EnvOut):-
	reduce_all(config(E,Env),config(V,Env1)),
	(integer(V) -> 
		(V > 0  ->
			catch(
				(
					Env1 = env(SymTable,context(Func,_)),
					reduce_stmt(config([S],env(SymTable,context(Func,true))),Env2), 
					V1 is V - 1,
					reduce_stmt(config([loop(V1,S)|Rest], Env2), EnvOut)
				),
				Error,
				(
					Error = break(BreakEnv) ->
						reduce_stmt(config(Rest, BreakEnv), EnvOut);
					Error = continue(ContEnv) ->
						V1 is V - 1,
						reduce_stmt(config([loop(V1,S)|Rest], ContEnv), EnvOut);
					throw(Error)
				)
			)
		; 
			reduce_stmt(config(Rest, Env1), EnvOut)
		)
		; throw(type_mismatch(loop(E,S)))).

%% --- Break statement ---
reduce_stmt(config([break(null)|_],env(SymTable,context(_,InLoop))),_):-
	InLoop == true,!,
	throw(break(env(SymTable,context(_,true)))).

reduce_stmt(config([break(null)|_],_),_):-
	throw(break_not_in_loop(break(null))).

%% --- Continue statement ---
reduce_stmt(config([continue(null)|_],env(SymTable,context(_,InLoop))),_):-
	InLoop == true,!,
	throw(continue(env(SymTable,context(_,true)))),!.

reduce_stmt(config([continue(null)|_],_),_):-
	throw(continue_not_in_loop(continue(null))).