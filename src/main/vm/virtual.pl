:- consult('vm.pl').

go :- 	open('input.txt',read,Stream),
		read_term(Stream,Y,[]),
		close(Stream),
		open('output.txt',write,Stream1),
		set_output(Stream1),
		catch(reduce_prog(Y),Exception,process(Exception))        
		,close(Stream1).

% Error handling

process(redeclare_identifier(X)):- write('Redeclared identifier: '),write(X),!. 
process(redeclare_function(X)):- write('Redeclared function: '),write(X),!. 
process(redeclare_procedure(X)):- write('Redeclared procedure: '),write(X),!. 
process(invalid_expression(X)):- write('Invalid expression: '),write(X),!.		
process(undefined_variable(X)):- write('Undefined variable: '),write(X),!.	
process(type_mismatch(X)):- write('Type mismatch: '),write(X),!. 
process(undeclare_identifier(X)):- write('Undeclared identifier: '),write(X),!. 
process(wrong_number_of_argument(X)):- write('Wrong number of arguments: '),write(X),!.
process(undeclare_function(X)):- write('Undeclared function: '),write(X),!. 
process(undeclare_procedure(X)):- write('Undeclared procedure: '),write(X),!. 
process(break_not_in_loop(X)):- write('Break not in a loop: '),write(X),!. 
process(continue_not_in_loop(X)):- write('Continue not in a loop: '),write(X),!. 
process(cannot_assign(X)) :- write('Cannot assign to a constant: '),write(X),!.

is_builtin(X,V):-member((X,V),[(readInt,func),(writeIntLn,proc),(writeInt,proc),(readReal,func),(writeRealLn,proc),(writeReal,proc),(readBool,func),(writeBoolLn,proc),(writeBool,proc),(writeLn,proc),(writeStrLn,proc),(writeStr,proc)]).

p_call_builtin(writeInt,[V]) :- (integer(V);throw(type_mismatch(call(writeInt,[V])))),write(V),!.
p_call_builtin(writeIntLn,[V]) :- (integer(V);throw(type_mismatch(call(writeIntLn,[V])))),writeln(V),!.
p_call_builtin(readInt,V) :- read(V),(integer(V);throw(type_mismatch(call(readInt,[])))),!.
p_call_builtin(writeReal,[V]) :- (float(V);throw(type_mismatch(call(writeReal,[V])))),write(V),!.
p_call_builtin(writeRealLn,[V]) :- (float(V);throw(type_mismatch(call(writeRealLn,[V])))),writeln(V),!.
p_call_builtin(readReal,V) :- read(V),(float(V);throw(type_mismatch(call(readReal,[])))),!.
p_call_builtin(writeBool,[V]) :- (boolean(V);throw(type_mismatch(call(writeBool,[V])))),write(V),!.
p_call_builtin(writeBooleanLn,[V]) :- (boolean(V);throw(type_mismatch(call(writeBool,[V])))),writeln(V),!.
p_call_builtin(readBool,V) :- read(V),(boolean(V);throw(type_mismatch(call(readBool,[])))),!.
p_call_builtin(writeLn,[]) :- nl,!.
p_call_builtin(writeStrLn,[V]) :- (string(V);throw(type_mismatch(call(writeStrLn,[V])))),writeln(V),!.
p_call_builtin(writeStr,[V]) :- (string(V);throw(type_mismatch(call(writeStrLn,[V])))),write(V).