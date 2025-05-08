%main program
reduce_prog([Var,Func,Body]) :-
	% Add vars/consts to the symbol table
	create_env(Var,env([[]],false),Env),
	% Add functions to the symbol table
	create_env(Func,Env,Env1),
	reduce_stmt(config(Body,Env1),_).

% Define boolean values
boolean(true).
boolean(false).

% --- Helper predicates - START ---
%check if X has been declared in the first list of the environment
has_declared(X,[id(X,Y,Z,_)|_],id(X,Y,Z,_)):- !.
has_declared(X,[_|L],R) :-  has_declared(X,L,R).

% Determine type of the literal
type_of(V, boolean) :- boolean(V),!.
type_of(V, integer) :- integer(V),!.
type_of(V, float) :- float(V),!.
type_of(V, string) :- string(V),!.
% --- Helper predicates - END ---

% --- Symbol table - START ---
% create a symbol table from the list of variable or constant declarations 
%% Base case: Not add anything to the environment
create_env([],Env,Env).

%% Variable declaration
create_env([var(I,type)|_],env([_],_),_):- % Global scope
	is_builtin(I,_),!,throw(redeclare_identifier(I)).
create_env([var(I,type)|_],env([L1|_],_),_):-
	has_declared(I,L1,_),!,throw(redeclare_identifier(I)).
create_env([var(I,type)|L],env([L1|L2],T),EnvOut):- 
	create_env(L,env([[id(I,var,type,null)|L1]|L2],T),EnvOut).

%% Constant declaration
create_env([const(I,E)|_],env([_],_),_):- % Global scope
	is_builtin(I,_),!,throw(redeclare_identifier(I)).
create_env([const(I,E)|_],env([L1|_],_),_):-
	has_declared(I,L1,_),!,throw(redeclare_identifier(I)).
create_env([const(I,E)|L],env([L1|L2],T),EnvOut):-
	(type_of(E,type) ->% Determine the type of const
		create_env(L,env([[id(I,const,type,E)|L1]|L2],T),EnvOut)
		; throw(type_mismatch(const(I,E)))).

%% Parameter declaration
create_env([par(I,type)|_],env([L1|_],_),_):-
	has_declared(I,L1,_),!,throw(redeclare_identifier(I)).
create_env([par(I,type)|L],env([L1|L2],T),EnvOut):-
	create_env(L,env([[id(I,par,type,null)|L1]|L2],T),EnvOut).

%% Function declaration
% Only care Global scope
create_env([func(I,Params,RetType,Stmts)|_],env([_],_),_):- 
	is_builtin(I,_),!,
	throw(redeclare_function(I)).
create_env([func(I,Params,RetType,Stmts)|_],env([L1|_],_),_):-
	has_declared(I,L1,_),!,
	throw(redeclare_function(I)).
% Add function to the symbol table
create_env([func(I,Params,RetType,Stmts)|L],env([L1|L2],T),EnvOut):-
	create_env(L,env([[id(I,func,RetType,null)|L1]|L2],T),EnvOut1).

%% Procedure declaration
create_env([proc(I,Params,Stmts)|_],env([_],_),_):- 
	is_builtin(I,_),!,
	throw(redeclare_procedure(I)).
create_env([proc(I,Params,Stmts)|_],env([L1|_],_),_):-
	has_declared(I,L1,_),!,
	throw(redeclare_procedure(I)).
% Add procedure to the symbol table
create_env([proc(I,Params,Stmts)|L],env([L1|L2],T),EnvOut):-
	create_env(L,env([[id(I,proc,null,null)|L1]|L2],T),EnvOut1).
%% --- Symbol table - END ---

% --- Expression reduction - START ---
%% --- Numerical expressions - START ---
% Addition
reduce(config(add(E1,E2),Env),config(R,Env)) :-  
	reduce_all(config(E1,Env),config(V1,Env)),
	reduce_all(config(E2,Env),config(V2,Env)),
	(number(V1), number(V2) -> R is V1 + V2 ; throw(type_mismatch(add(E1,E2)))).

% Subtraction
reduce(config(sub(E1,E2),Env),config(R,Env)) :-  
	reduce_all(config(E1,Env),config(V1,Env)),
	reduce_all(config(E2,Env),config(V2,Env)),
	(number(V1), number(V2) -> R is V1 - V2 ; throw(type_mismatch(sub(E1,E2)))).

% Multiplication
reduce(config(times(E1,E2),Env),config(R,Env)) :-  
	reduce_all(config(E1,Env),config(V1,Env)),
	reduce_all(config(E2,Env),config(V2,Env)),
	(number(V1), number(V2) -> R is V1 * V2 ; throw(type_mismatch(times(E1,E2)))).

% Real division
reduce(config(rdiv(E1,E2),Env),config(R,Env)) :-
	reduce_all(config(E1,Env),config(V1,Env)),
	reduce_all(config(E2,Env),config(V2,Env)),
	(number(V1), number(V2) -> R is V1 / V2 ; throw(type_mismatch(rdiv(E1,E2)))).

% Integer division
reduce(config(idiv(E1,E2),Env),config(R,Env)) :-  
	reduce_all(config(E1,Env),config(V1,Env)),
	reduce_all(config(E2,Env),config(V2,Env)),
	(integer(V1), integer(V2) -> R is V1 div V2 ; throw(type_mismatch(idiv(E1,E2)))).

% Modulo
reduce(config(imod(E1,E2),Env),config(R,Env)) :-  
	reduce_all(config(E1,Env),config(V1,Env)),
	reduce_all(config(E2,Env),config(V2,Env)),
	(integer(V1), integer(V2) -> R is V1 mod V2 ; throw(type_mismatch(imod(E1,E2)))).
%% --- Numerical expressions - END ---

%% --- Logical expressions - START ---
reduce(config(bnot(E),Env),config(R,Env)) :-  
	reduce_all(config(E,Env),config(V,Env)),
	(boolean(V) -> (V == true -> R = false ; R = true)).

reduce(config(band(E1, E2), Env), config(R, Env)) :-
	reduce_all(config(E1, Env), config(V1, Env)),
	(boolean(V1) -> (
		V1 == false -> R = false ; 
		reduce_all(config(E2, Env), config(V2, Env)),
		(boolean(V2) -> (V2 == false -> R = false ; R = true) 
			; throw(type_mismatch(band(E1,E2))))
	) ; throw(type_mismatch(band(E1,E2)))).

reduce(config(bor(E1, E2), Env), config(R, Env)) :-
	reduce_all(config(E1, Env), config(V1, Env)),
	(boolean(V1) -> (
		V1 == true -> R = true ;
		reduce_all(config(E2, Env), config(V2, Env)),
		(boolean(V2) -> (V2 == true -> R = true ; R = false) 
			; throw(type_mismatch(bor(E1,E2))))
	) ; throw(type_mismatch(bor(E1,E2)))).
%% --- Logical expressions - END ---

%% --- Relational expressions - START ---
reduce(config(greater(E1, E2), Env), config(R, Env)) :-
    reduce_all(config(E1, Env), config(V1, Env)),
    reduce_all(config(E2, Env), config(V2, Env)),
    (number(V1), number(V2) -> (V1 > V2 -> R = true ; R = false)
    ; throw(type_mismatch(greater(E1,E2)))).

reduce(config(less(E1, E2), Env), config(R, Env)) :-
	reduce_all(config(E1, Env), config(V1, Env)),
	reduce_all(config(E2, Env), config(V2, Env)),
	(number(V1), number(V2) -> (V1 < V2 -> R = true ; R = false)
	; throw(type_mismatch(less(E1,E2)))).

reduce(config(ge(E1, E2), Env), config(R, Env)) :-
	reduce_all(config(E1, Env), config(V1, Env)),
	reduce_all(config(E2, Env), config(V2, Env)),
	(number(V1), number(V2) -> (V1 >= V2 -> R = true ; R = false)
	; throw(type_mismatch(ge(E1,E2)))).

reduce(config(le(E1, E2), Env), config(R, Env)) :-
	reduce_all(config(E1, Env), config(V1, Env)),
	reduce_all(config(E2, Env), config(V2, Env)),
	(number(V1), number(V2) -> (V1 =< V2 -> R = true ; R = false)
	; throw(type_mismatch(le(E1,E2)))).


reduce(config(eql(E1, E2), Env), config(R, Env)) :-
	reduce_all(config(E1, Env), config(V1, Env)),
	reduce_all(config(E2, Env), config(V2, Env)),
	( (integer(V1), integer(V2)); (float(V1), float(V2)); (boolean(V1), boolean(V2)) ) -> %??? Both be Float
		(V1 =:= V2 -> R = true ; R = false)
	; throw(type_mismatch(eql(E1,E2))).

reduce(config(ne(E1, E2), Env), config(R, Env)) :-
	reduce_all(config(E1, Env), config(V1, Env)),
	reduce_all(config(E2, Env), config(V2, Env)),
	( (integer(V1), integer(V2)); (float(V1), float(V2)); (boolean(V1), boolean(V2)) ) -> %??? Both be Float
		(V1 =\= V2 -> R = true ; R = false)
	; throw(type_mismatch(ne(E1,E2))).
%% --- Relational expressions - END ---
% --- Expression reduction - END ---


reduce_all(config(V,Env),config(V,Env)):- (number(V);boolean(V);string(V)),!.
reduce_all(config(E,Env),config(E2,Env)):-
		reduce(config(E,Env),config(E1,Env)),!,
		reduce_all(config(E1,Env),config(E2,Env)).


% --- Statement reduction - START ---
reduce_stmt(config([call(F,[X])|Body],_),_) :- 
		is_builtin(F,_),!,
		reduce_all(config(X,Env),config(V,Env)),
		p_call_builtin(F,[V]), % Read stmt's input
		reduce_stmt(config(Body,_),_).

