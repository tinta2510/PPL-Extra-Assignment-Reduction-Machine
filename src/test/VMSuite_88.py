import unittest
from TestUtils import TestVM


class VMSuite(unittest.TestCase):
    def test_401(self):        
        input = """[[],[],[call(writeInt,[3])]]."""
        expect = "3"
        self.assertTrue(TestVM.test(input, expect, 401))

    def test_402(self):        
        input = """[[],[],[call(writeInt,[add(3,1)])]]."""
        expect = "4"
        self.assertTrue(TestVM.test(input, expect, 402))

    def test_403(self):        
        input = """[[var(a,integer),var(b,integer),var(a,float)],[],[call(writeInt,[1])]]."""
        expect = "Redeclared identifier: var(a,float)"
        self.assertTrue(TestVM.test(input, expect, 403))

    def test_404(self):        
        input = """[[],[],[call(writeInt,[sub(3,1)])]]."""
        expect = "2"
        self.assertTrue(TestVM.test(input, expect, 404))

    def test_405(self):        
        input = """[[],[],[call(writeInt,[add(4,sub(3,1))])]]."""
        expect = "6"
        self.assertTrue(TestVM.test(input, expect, 405))
        
    def test_406(self):
        input = """[[],[],[call(writeReal,[10.0])]]."""
        expect = "10.0"
        self.assertTrue(TestVM.test(input, expect, 406))
        
    def test_407(self):
        input = """[[const(a,10)],[],[call(writeInt,[a])]]."""
        expect = "10"   
        self.assertTrue(TestVM.test(input, expect, 407))
        
    def test_408(self):
        input = """[[var(a,integer)],[],[call(writeInt,[a])]]."""
        expect = "Invalid expression: a"   
        self.assertTrue(TestVM.test(input, expect, 408))

    def test_409(self):
        input = """[[],[],[
            call(writeIntLn,[times(3,2)]),
            call(writeRealLn,[rdiv(3,2)]),
            call(writeIntLn,[sub(-10)]),
            call(writeIntLn,[idiv(5,2)]),
            call(writeInt,[imod(5,2)])
        ]]."""
        expect = "6\n1.5\n10\n2\n1"
        self.assertTrue(TestVM.test(input, expect, 409))
        
    def test_410(self):
        input = """[[],[],[
            call(writeBool,[bnot(true)]),
            call(writeBool,[band(true,false)]),
            call(writeBool,[bor(true,false)])
            ]]."""
        expect = "falsefalsetrue"
        self.assertTrue(TestVM.test(input, expect, 410))

    def test_411(self):
        input = """[[var(a,integer)],[],[assign(a,3),call(writeInt,[a])]]."""
        expect = "3"
        self.assertTrue(TestVM.test(input, expect, 411))
        
    def test_412(self):
        input = """[[const(a,10)],[],[assign(a,3),call(writeInt,[a])]]."""
        expect = "Cannot assign to a constant: assign(a,3)"
        self.assertTrue(TestVM.test(input, expect, 412))
        
    def test_413(self):
        input = """[[var(c,integer),const(b,10),var(a,integer)],[],[assign(a,3),call(writeInt,[a])]]."""
        expect = "3"
        self.assertTrue(TestVM.test(input, expect, 413))
        
    def test_414(self):
        input = """
[[var(a,integer)],
[func(foo,[par(a,integer),par(b,integer)],integer,[assign(a,add(a,b)),assign(foo,a)])], 
[assign(a,3),call(writeIntLn,[call(foo,[a,3])]),call(writeInt,[a])]]."""
        expect = "6\n3"
        self.assertTrue(TestVM.test(input, expect, 414))

    def test_415(self):
        input = """[[const(a,10),var(b,integer)],[],[assign(b,5),assign(a,b),call(writeInt,[a])]]."""
        expect = "Cannot assign to a constant: assign(a,b)"
        self.assertTrue(TestVM.test(input, expect, 415))
    
    def test_416(self):
        input = """[
            [var(x, integer)],
            [func(addTwo, [par(a, integer)], integer, [
                assign(addTwo, add(a, 2))
            ])],
            [assign(x, call(addTwo, [3])), call(writeInt, [x])]
        ]."""
        expect = "5"
        self.assertTrue(TestVM.test(input, expect, 416))

    def test_417(self):
        input = """[
            [var(x, integer)],
            [],
            [assign(y, 5)]
        ]."""
        expect = "Undeclared identifier: y"
        self.assertTrue(TestVM.test(input, expect, 417))

    def test_418(self):
        input = """[
            [],
            [func(identity, [par(x, integer)], integer, [assign(identity, x)])],
            [call(writeInt, [call(identity, [10])])]
        ]."""
        expect = "10"
        self.assertTrue(TestVM.test(input, expect, 418))
        

    def test_419(self):
        input = """[
            [],
            [func(double, [par(x, integer)], integer, [assign(double, times(x, 2))])],
            [call(writeInt, [call(double, [3, 5])])]
        ]."""
        expect = "Wrong number of arguments: call(double,[3,5])"
        self.assertTrue(TestVM.test(input, expect, 419))

    def test_420(self):
        input = """[
            [var(x, integer)],
            [func(negate, [par(a, integer)], integer, [assign(negate, sub(a))])],
            [assign(x, call(negate, [5])), call(writeInt, [x])]
        ]."""
        expect = "-5"
        self.assertTrue(TestVM.test(input, expect, 420))
        
    def test_421(self):
        input = """[[var(x,integer)],[],[call(writeInt,[x])]]."""
        expect = "Invalid expression: x"
        self.assertTrue(TestVM.test(input, expect, 421))
        
    def test_422(self):
        input = """[[],
        [proc(printSum, [par(a,integer),par(b,integer)], [
            call(writeInt,[add(a,b)])
        ])],
        [call(printSum,[2,3])]]."""
        expect = "5"
        self.assertTrue(TestVM.test(input, expect, 422))
        
    def test_423(self):
        input = """[
            [],
            [],
            [call(writeInt, [call(double, [3, 5])])]
        ]."""
        expect = "Undeclared function: call(double,[3,5])"
        self.assertTrue(TestVM.test(input, expect, 423))

    def test_424(self):
        input = """[[],
        [],
        [call(printSum,[2,3])]]."""
        expect = "Undeclared procedure: call(printSum,[2,3])"
        self.assertTrue(TestVM.test(input, expect, 424))
            
    def test_425(self):
        input = """[[var(x,integer)],[],
        [assign(x,1),
        block([var(x,integer)], [assign(x,2), call(writeIntLn,[x])]),
        call(writeInt,[x])]]."""
        expect = "2\n1"
        self.assertTrue(TestVM.test(input, expect, 425))

    def test_426(self):
        input = """[[],[],
        [block([var(a,integer),var(a,real)], [call(writeInt,[1])])]]."""
        expect = "Redeclared identifier: var(a,real)"
        self.assertTrue(TestVM.test(input, expect, 426))

    def test_427(self):
        input = """[[],[],[
            block([var(a,integer)], [assign(a,3), call(writeIntLn,[a])]),
            call(writeInt,[a])
        ]]."""
        expect = "3\nUndeclared identifier: a"
        self.assertTrue(TestVM.test(input, expect, 427))

    def test_428(self):
        input = """[[var(x,integer)],[],[
            assign(x,0),
            if(true, assign(x,1), assign(x,2)),
            call(writeInt,[x])
        ]]."""
        expect = "1"
        self.assertTrue(TestVM.test(input, expect, 428))

    def test_429(self):
        input = """[[var(x,integer)],[],[
            assign(x,0),
            if(false, assign(x,1), assign(x,2)),
            call(writeInt,[x])
        ]]."""
        expect = "2"
        self.assertTrue(TestVM.test(input, expect, 429))

    def test_430(self):
        input = """[[var(x,integer)],[],[
            assign(x,1),
            if(x, assign(x,2), assign(x,3)),
            call(writeInt,[x])
        ]]."""
        expect = "Type mismatch: if(x,assign(x,2),assign(x,3))"
        self.assertTrue(TestVM.test(input, expect, 430))

    def test_431(self):
        input = """[[var(x,integer)],[],[
            assign(x,0),
            if(eql(add(x,3),3), assign(x,5), assign(x,9)),
            call(writeInt,[x])
        ]]."""
        expect = "5"
        self.assertTrue(TestVM.test(input, expect, 431))
        
    def test_432(self):
        input = """[[var(x,integer)],[],[
            assign(x,1),
            if(band(eql(x,1),eql(add(2,2),4)), assign(x,10), assign(x,20)),
            call(writeInt,[x])
        ]]."""
        expect = "10"
        self.assertTrue(TestVM.test(input, expect, 432))
    
    def test_433(self):
        input = """[[var(i,integer)],[],[
            assign(i,0),
            while(less(i,3), assign(i, add(i,1))),
            call(writeInt,[i])
        ]]."""
        expect = "3"
        self.assertTrue(TestVM.test(input, expect, 433))
        
    def test_434(self):
        input = """[[var(i,integer)],[],[
            assign(i,0),
            do([assign(i, add(i,1)),call(writeIntLn,[i])], less(i,3)),
            call(writeInt,[i])
        ]]."""
        expect = "1\n2\n3\n3"
        self.assertTrue(TestVM.test(input, expect, 434))
        
    def test_435(self):
        input = """[[var(i,integer)],[],[
            assign(i,0),
            loop(3, assign(i, add(i,1))),
            call(writeInt,[i])
        ]]."""
        expect = "3"
        self.assertTrue(TestVM.test(input, expect, 435))
            
    def test_436(self):
        input = """[[var(i,integer)],[],[
            assign(i,7),
            loop(0, assign(i, 999)),
            call(writeInt,[i])
        ]]."""
        expect = "7"
        self.assertTrue(TestVM.test(input, expect, 436))
        
    def test_437(self):
        input = """[[var(i,integer)],[],[
            assign(i, 0),
            while(less(i, 5), block([], [
                assign(i, add(i,1)),
                if(eql(i,3), break(null))
            ])),
            call(writeInt,[i])
        ]]."""
        expect = "3"
        self.assertTrue(TestVM.test(input, expect, 437))

    def test_438(self):
        input = """[[],[proc(foo,[],[break(null)])],[loop(2,call(foo,[]))]]."""
        expect = "Break not in a loop: break(null)"
        self.assertTrue(TestVM.test(input, expect, 438))
        
    def test_439(self):
        input = """[[var(i,integer), var(sum,integer)],[],[
            assign(i, 0), assign(sum, 0),
            while(less(i, 5), block([], [
                assign(i, add(i,1)),
                if(eql(i,3), continue(null)),
                assign(sum, add(sum,1))
            ])),
            call(writeInt,[sum])
        ]]."""
        expect = "4"
        self.assertTrue(TestVM.test(input, expect, 439))

    def test_440(self):
        input = """[[var(i,integer)],[],[
            assign(i,0),
            do([block([], [
                assign(i, add(i,1)),
                if(eql(i,2), break(null))
            ])], less(i, 5)),
            call(writeInt,[i])
        ]]."""
        expect = "2"
        self.assertTrue(TestVM.test(input, expect, 440))
        
    def test_441(self):
        input = """[[var(i,integer)],[],[
            assign(i,0),
            loop(5, block([], [
                assign(i, add(i,1)),
                if(eql(i,2), break(null))
            ])),
            call(writeInt,[i])
        ]]."""
        expect = "2"
        self.assertTrue(TestVM.test(input, expect, 441))
        
    def test_442(self):
        input = """[[var(i,integer), var(s,integer)],[],[
            assign(i, 0), assign(s, 0),
            do([block([], [
                assign(i, add(i,1)),
                if(eql(i,2), continue(null)),
                assign(s, add(s,1))
            ])], less(i, 5)),
            call(writeInt,[s])
        ]]."""
        expect = "4"
        self.assertTrue(TestVM.test(input, expect, 442))
        
    def test_443(self):
        input = """[[var(i,integer), var(sum,integer)],[],[
            assign(i,0), assign(sum,0),
            loop(5, block([], [
                assign(i, add(i,1)),
                if(eql(i,3), continue(null)),
                assign(sum, add(sum,1))
            ])),
            call(writeInt,[sum])
        ]]."""
        expect = "4"
        self.assertTrue(TestVM.test(input, expect, 442))

    def test_444(self):
        input = """[[var(a,integer)],
        [func(foo,[par(a,integer),par(b,integer)],integer,[assign(a,add(a,b)),assign(foo,a)])],
        [assign(a,3),call(writeIntLn,[call(foo,[a,3])]),call(writeIntLn,[a])]]."""
        expect = "6\n3\n"
        self.assertTrue(TestVM.test(input, expect, 444))

    def test_445(self):
        input = """[[],[func(foo,[],integer,[assign(foo,3)])],
        [call(writeIntLn,[call(foo,[])])]]."""
        expect = "3\n"
        self.assertTrue(TestVM.test(input, expect, 445))

    def test_446(self):
        input = """[[],[func(foo,[par(a,integer)],integer,[assign(foo,1)])],
        [call(writeInt,[call(foo,[true])])]]."""
        expect = "Type mismatch: call(foo,[true])"
        self.assertTrue(TestVM.test(input, expect, 446))

    def test_447(self):
        input = """[[],[],[call(writeInt,[add(10,true)])]]."""
        expect = "Type mismatch: add(10,true)"
        self.assertTrue(TestVM.test(input, expect, 447))

    def test_448(self):
        input = """[[],[],[call(writeBool,[add(10,3)])]]."""
        expect = "Type mismatch: call(writeBool,[add(10,3)])"
        self.assertTrue(TestVM.test(input, expect, 448))

    def test_449(self):
        input = """[[var(a,integer)],[],[assign(a,3),if(a,call(writeInt,[3]))]]."""
        expect = "Type mismatch: if(a,call(writeInt,[3]))"
        self.assertTrue(TestVM.test(input, expect, 449))

    def test_450(self):
        input = """[[],[func(foo,[],float,[assign(foo,3.0)])],
        [call(writeInt,[call(foo,[])])]]."""
        expect = "Type mismatch: call(writeInt,[call(foo,[])])"
        self.assertTrue(TestVM.test(input, expect, 450))

    def test_451(self):
        input = """[[var(a,integer)],[func(foo,[],integer,[])],[assign(a,call(foo,[]))]]."""
        expect = "Invalid expression: call(foo,[])"
        self.assertTrue(TestVM.test(input, expect, 451))

    def test_452(self):
        input = """[[var(a,integer)],[],[call(writeInt,[a])]]."""
        expect = "Invalid expression: a"
        self.assertTrue(TestVM.test(input, expect, 452))

    def test_453(self):
        input = """[[var(a,integer)],[],[assign(a,add(b,1)),call(writeIntLn,[a])]]."""
        expect = "Undeclared identifier: b"
        self.assertTrue(TestVM.test(input, expect, 453))

    def test_454(self):
        input = """[[var(a,integer)],
        [proc(foo,[],[[var(b,integer)],[assign(b,1),assign(a,b)]])],
        [call(writeIntLn,[b])]]."""
        expect = "Undeclared identifier: b"
        self.assertTrue(TestVM.test(input, expect, 454))

    def test_455(self):
        input = """[[],[proc(foo,[],[])],[call(foo,[1])]]."""
        expect = "Wrong number of arguments: call(foo,[1])"
        self.assertTrue(TestVM.test(input, expect, 455))

    def test_456(self):
        input = """[[],[proc(foo,[par(a,integer)],[])],[call(foo,[])]]."""
        expect = "Wrong number of arguments: call(foo,[])"
        self.assertTrue(TestVM.test(input, expect, 456))

    def test_457(self):
        input = """[[var(a,integer)],[],[assign(a,call(foo,[]))]]."""
        expect = "Undeclared function: call(foo,[])"
        self.assertTrue(TestVM.test(input, expect, 457))

    def test_458(self):
        input = """[[],[],[call(foo,[])]]."""
        expect = "Undeclared procedure: call(foo,[])"
        self.assertTrue(TestVM.test(input, expect, 458))

    def test_459(self):
        input = """[[],[],[break(null)]]."""
        expect = "Break not in a loop: break(null)"
        self.assertTrue(TestVM.test(input, expect, 459))

    def test_460(self):
        input = """[[],[proc(foo,[],[break(null)])],[do(call(foo,[]),true)]]."""
        expect = "Break not in a loop: break(null)"
        self.assertTrue(TestVM.test(input, expect, 460))

    def test_461(self):
        input = """[[],[],[continue(null)]]."""
        expect = "Continue not in a loop: continue(null)"
        self.assertTrue(TestVM.test(input, expect, 461))

    def test_462(self):
        input = """[[const(a,7)],[],[assign(a,8)]]."""
        expect = "Cannot assign to a constant: assign(a,8)"
        self.assertTrue(TestVM.test(input, expect, 462))

    def test_463(self):
        input = """[[var(a,integer),var(b,real),var(a,boolean)],[],[]]."""
        expect = "Redeclared identifier: var(a,boolean)"
        self.assertTrue(TestVM.test(input, expect, 463))

    def test_464(self):
        input = """[[],[proc(foo,[par(a,integer),par(b,integer),par(a,real)],[])],[]]."""
        expect = "Redeclared identifier: par(a,real)"
        self.assertTrue(TestVM.test(input, expect, 464))

    def test_465(self):
        input = """[[const(a,7),var(a,real)],[proc(proce,[],[assign(a,10.0)])],[]]."""
        expect = "Redeclared identifier: var(a,real)"
        self.assertTrue(TestVM.test(input, expect, 465))

    def test_466(self):
        input = """[[],[func(readInt,[],real,[])],[]]."""
        expect = "Redeclared function: readInt"
        self.assertTrue(TestVM.test(input, expect, 466))

    def test_467(self):
        input = """[[],[func(foo,[],integer,[]),proc(foo,[a],[])],[]]."""
        expect = "Redeclared procedure: foo"
        self.assertTrue(TestVM.test(input, expect, 467))

    def test_468(self):
        input = """[[var(foo,integer)],[proc(foo,[a],[])],[]]."""
        expect = "Redeclared procedure: foo"
        self.assertTrue(TestVM.test(input, expect, 468))

    def test_469(self):
        input = """[[var(x,integer),var(r,integer)],
        [func(double,[par(x,integer)],integer,[assign(double,times(x,2))]),
        func(triple,[par(x,integer)],integer,[assign(triple,times(x,3))])],
        [
            assign(x,2),
            assign(r,call(double,[call(triple,[x])])),
            call(writeIntLn,[r])
        ]]."""
        expect = "12\n"
        self.assertTrue(TestVM.test(input, expect, 469))
        
    def test_470(self):
        input = """[[],
        [func(fib,[par(n,integer)],integer,[
            if(le(n,1),
                assign(fib,n),
                assign(fib,add(call(fib,[sub(n,1)]), call(fib,[sub(n,2)])))
            )
        ])],
        [block([var(result,integer)],[
            assign(result,call(fib,[8])),
            call(writeIntLn,[result])
        ])]]."""
        expect = "21\n"
        self.assertTrue(TestVM.test(input, expect, 470))
        
    def test_471(self):
        input = """[[],
        [
        func(add1,[par(x,integer)],integer,[assign(add1,add(x,1))]),
        func(times2,[par(x,integer)],integer,[assign(times2,times(x,2))]),
        func(addThenDouble,[par(x,integer)],integer,[
            assign(addThenDouble,
                   call(times2,[call(add1,[x])]))])
        ],
        [block([var(result,integer)],[
            assign(result,call(addThenDouble,[3])),
            call(writeIntLn,[result])
         ])
        ]]."""
        expect = "8\n"
        self.assertTrue(TestVM.test(input, expect, 471))

    def test_472(self):
        input = """[[],
        [func(valid,[par(a,integer),par(b,integer)],boolean,[
            assign(valid,band(less(a,b),greater(b,0)))
        ])],
        [call(writeBool,[call(valid,[1,2])]), call(writeLn,[]),
        call(writeBool,[call(valid,[2,1])]), call(writeLn,[])]]."""
        expect = "true\nfalse\n"
        self.assertTrue(TestVM.test(input, expect, 472))

    def test_473(self):
        input = """[[],
        [func(id,[par(x,integer)],integer,[assign(id,x)])],
        [block([var(x,integer)],[
            assign(x,add(call(id,[5]),call(id,[6]))),
            call(writeIntLn,[x])
        ])]]."""
        expect = "11\n"
        self.assertTrue(TestVM.test(input, expect, 473))

    def test_474(self):
        input = """[[var(r,boolean)],
        [func(match,[par(x,boolean),par(y,boolean)],boolean,[
            assign(match,bor(x,y))
        ])],
        [
            assign(r,call(match,[true,false])),
            call(writeBool,[r]),
            call(writeLn,[])
        ]]."""
        expect = "true\n"
        self.assertTrue(TestVM.test(input, expect, 474))

    def test_475(self):
        input = """[[var(x,integer)],[],[
            assign(x,1),
            block([var(x,integer)],[
                assign(x,add(x,2)),
                block([var(x,integer)],[
                    assign(x,add(x,3)),
                    call(writeIntLn,[x])
                ]),
                call(writeIntLn,[x])
            ]),
            call(writeIntLn,[x])
        ]]."""
        expect = "Invalid expression: x"
        self.assertTrue(TestVM.test(input, expect, 475))

    def test_476(self):
        input = """[[const(p,3.0)],[],[
            call(writeRealLn,[rdiv(times(p,2),3)])
        ]]."""
        expect = "2.0\n"
        self.assertTrue(TestVM.test(input, expect, 476))

    def test_477(self):
        input = """[[var(a,integer)],
        [func(positive,[par(x,integer)],boolean,[
            assign(positive,greater(x,0))
        ])],
        [
            assign(a,1),
            if(call(positive,[a]), call(writeStrLn,["yes"]), call(writeStrLn,["no"]))
        ]]."""
        expect = "yes\n"
        self.assertTrue(TestVM.test(input, expect, 477))

    def test_478(self):
        input = """[[var(a,boolean)],
        [func(trueFunc,[],boolean,[assign(trueFunc,true)])],
        [
            assign(a,band(call(trueFunc,[]),true)),
            call(writeBool,[a]),
            call(writeLn,[])
        ]]."""
        expect = "true\n"
        self.assertTrue(TestVM.test(input, expect, 478))

    def test_479(self):
        input = """[[],
        [func(ten,[],integer,[assign(ten,10)])],
        [if(greater(call(ten,[]),5), call(writeStrLn,["big"]), call(writeStrLn,["small"]))]]."""
        expect = "big\n"
        self.assertTrue(TestVM.test(input, expect, 479))

    def test_480(self):
        input = """[[],
        [func(adder,[par(x,integer)],integer,[assign(adder,add(x,5))])],
        [block([var(r,integer)],[
            assign(r,call(adder,[10])),
            call(writeIntLn,[r])
        ])]]."""
        expect = "15\n"
        self.assertTrue(TestVM.test(input, expect, 480))
        
    def test_481(self):
        input = """[[var(i,integer)],[],[
            assign(i,0),
            while(less(i,6), block([],[
                assign(i,add(i,1)),
                if(ne(imod(i,2),0), continue(null)),
                call(writeIntLn,[i])
            ]))
        ]]."""
        expect = "2\n4\n6\n"
        self.assertTrue(TestVM.test(input, expect, 481))

    def test_482(self):
        input = """[[var(i,integer)],[],[
            assign(i,11),
            while(true, block([],[
                if(eql(imod(i,7),0), block([],[
                    call(writeIntLn,[i]),
                    break(null)
                ])),
                assign(i,add(i,1))
            ]))
        ]]."""
        expect = "14\n"
        self.assertTrue(TestVM.test(input, expect, 482))

    def test_483(self): 
        input = """[[var(i,integer),var(sum,integer)],[],[
            assign(i,0),
            assign(sum,0),
            loop(10, block([],[
                assign(i,add(i,1)),
                if(eql(imod(i,2),0), continue(null)),
                assign(sum,add(sum,i))
            ])),
            call(writeIntLn,[sum])
        ]]."""
        expect = "25\n"
        self.assertTrue(TestVM.test(input, expect, 483))

    def test_484(self):
        input = """[[var(i,integer)],[],[
            assign(i,0),
            while(less(i,5), block([],[
                assign(i,add(i,1)),
                if(eql(i,3), break(null)),
                call(writeIntLn,[i])
            ]))
        ]]."""
        expect = "1\n2\n"
        self.assertTrue(TestVM.test(input, expect, 484))

    def test_485(self):
        input = """[[var(i,integer),var(j,integer)],[],[
            assign(i,0),
            loop(2, block([],[
                assign(i,add(i,1)),
                assign(j,0),
                loop(2, block([],[
                    assign(j,add(j,1)),
                    call(writeIntLn,[i]),
                    call(writeIntLn,[j])
                ]))
            ]))
        ]]."""
        expect = "1\n1\n1\n2\n2\n1\n2\n2\n"
        self.assertTrue(TestVM.test(input, expect, 485))

    def test_486(self):
        input = """[[var(i,integer),var(j,integer)],[],[
            assign(i,0),
            loop(2, block([],[
                assign(i,add(i,1)),
                assign(j,0),
                loop(3, block([],[
                    assign(j,add(j,1)),
                    if(eql(j,2), continue(null)),
                    call(writeIntLn,[i]),
                    call(writeIntLn,[j])
                ]))
            ]))
        ]]."""
        expect = "1\n1\n1\n3\n2\n1\n2\n3\n"
        self.assertTrue(TestVM.test(input, expect, 486))

    def test_487(self):
        input = """[[var(i,integer)],[],[
            assign(i,0),
            loop(7, block([],[
                assign(i,add(i,1)),
                if(bor(eql(i,1),band(greater(i,2),less(i,5))), call(writeIntLn,[i]))
            ]))
        ]]."""
        expect = "1\n3\n4\n"
        self.assertTrue(TestVM.test(input, expect, 487))

    def test_488(self):
        input = """[[],
        [func(sumTo,[par(n,integer)],integer,[
            if(le(n,1),
                assign(sumTo,n),
                assign(sumTo,add(n,call(sumTo,[sub(n,1)])))
            )
        ])],
        [block([var(s,integer)],[
            assign(s,call(sumTo,[5])),
            call(writeIntLn,[s])
        ])]]."""
        expect = "15\n"
        self.assertTrue(TestVM.test(input, expect, 488))
