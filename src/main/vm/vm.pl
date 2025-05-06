%main program


reduce_prog([Var,_,Body]) :-
		create_env(Var,env([[]],false),Env),
		reduce_stmt(config(Body,Env),_).
											
%check if X has been declared in the first list of the environment
has_declared(X,[id(X,Y,Z)|_],id(X,Y,Z)):- !.
has_declared(X,[_|L],R) :-  has_declared(X,L,R).

%create a symbol table from the list of variable or constant declarations
create_env([],L,L).
create_env([var(X,Y)|_],env([_],_),_):- is_builtin(X,_),!,throw(redeclare_identifier(var(X,Y))).
create_env([var(X,Y)|_],env([L1|_],_),_):-has_declared(X,L1,_),!,throw(redeclare_identifier(var(X,Y))).
create_env([var(X,Y)|L],env([L1|L2],T),L3):- create_env(L,env([[id(X,var,Y)|L1]|L2],T),L3).


reduce(config(add(E1,E2),Env),config(R,Env)) :-  
		reduce_all(config(E1,Env),config(V1,Env)),
		reduce_all(config(E2,Env),config(V2,Env)),
		R is V1+V2.
reduce(config(sub(E1,E2),Env),config(R,Env)) :-  
		reduce_all(config(E1,Env),config(V1,Env)),
		reduce_all(config(E2,Env),config(V2,Env)),
		R is V1-V2.
reduce_all(config(V,Env),config(V,Env)):- integer(V),!.
reduce_all(config(E,Env),config(E2,Env)):-
		reduce(config(E,Env),config(E1,Env)),!,
		reduce_all(config(E1,Env),config(E2,Env)).

reduce_stmt(config([call(writeInt,[X])],_),_) :- 
		reduce_all(config(X,Env),config(V,Env)),
		write(V)
		.
