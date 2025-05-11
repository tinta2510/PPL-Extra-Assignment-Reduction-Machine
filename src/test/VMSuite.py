import unittest
from TestUtils import TestVM


class VMSuite(unittest.TestCase):
#     def test_401(self):        
#         input = """[[],[],[call(writeInt,[3])]]."""
#         expect = "3"
#         self.assertTrue(TestVM.test(input, expect, 401))

#     def test_402(self):        
#         input = """[[],[],[call(writeInt,[add(3,1)])]]."""
#         expect = "4"
#         self.assertTrue(TestVM.test(input, expect, 402))

#     def test_403(self):        
#         input = """[[var(a,integer),var(b,integer),var(a,float)],[],[call(writeInt,[1])]]."""
#         expect = "Redeclared identifier: var(a,float)"
#         self.assertTrue(TestVM.test(input, expect, 403))

#     def test_404(self):        
#         input = """[[],[],[call(writeInt,[sub(3,1)])]]."""
#         expect = "2"
#         self.assertTrue(TestVM.test(input, expect, 404))

#     def test_405(self):        
#         input = """[[],[],[call(writeInt,[add(4,sub(3,1))])]]."""
#         expect = "6"
#         self.assertTrue(TestVM.test(input, expect, 405))
        
#     def test_406(self):
#         input = """[[],[],[call(writeReal,[10.0])]]."""
#         expect = "10.0"
#         self.assertTrue(TestVM.test(input, expect, 406))
        
#     def test_407(self):
#         input = """[[const(a,10)],[],[call(writeInt,[a])]]."""
#         expect = "10"   
#         self.assertTrue(TestVM.test(input, expect, 407))
        
#     def test_408(self):
#         input = """[[var(a,integer)],[],[call(writeInt,[a])]]."""
#         expect = "Invalid expression: a"   
#         self.assertTrue(TestVM.test(input, expect, 408))

#     def test_409(self):
#         input = """[[],[],[
#             call(writeIntLn,[times(3,2)]),
#             call(writeRealLn,[rdiv(3,2)]),
#             call(writeIntLn,[sub(-10)]),
#             call(writeIntLn,[idiv(5,2)]),
#             call(writeInt,[imod(5,2)])
#         ]]."""
#         expect = "6\n1.5\n10\n2\n1"
#         self.assertTrue(TestVM.test(input, expect, 409))
        
#     def test_410(self):
#         input = """[[],[],[
#             call(writeBool,[bnot(true)]),
#             call(writeBool,[band(true,false)]),
#             call(writeBool,[bor(true,false)])
#             ]]."""
#         expect = "falsefalsetrue"
#         self.assertTrue(TestVM.test(input, expect, 410))

#     def test_411(self):
#         input = """[[var(a,integer)],[],[assign(a,3),call(writeInt,[a])]]."""
#         expect = "3"
#         self.assertTrue(TestVM.test(input, expect, 411))
        
#     def test_412(self):
#         input = """[[const(a,10)],[],[assign(a,3),call(writeInt,[a])]]."""
#         expect = "Cannot assign to a constant: assign(a,3)"
#         self.assertTrue(TestVM.test(input, expect, 412))
        
#     def test_413(self):
#         input = """[[var(c,integer),const(b,10),var(a,integer)],[],[assign(a,3),call(writeInt,[a])]]."""
#         expect = "3"
#         self.assertTrue(TestVM.test(input, expect, 413))
        
#     def test_414(self):
#         input = """
# [[var(a,integer)],
# [func(foo,[par(a,integer),par(b,integer)],integer,[assign(a,add(a,b)),assign(foo,a)])], 
# [assign(a,3),call(writeIntLn,[call(foo,[a,3])]),call(writeInt,[a])]]."""
#         expect = "6\n3"
#         self.assertTrue(TestVM.test(input, expect, 414))

    # def test_415(self):
    #     input = """[[const(a,10),var(b,integer)],[],[assign(b,5),assign(a,b),call(writeInt,[a])]]."""
    #     expect = "Cannot assign to a constant: assign(a,b)"
    #     self.assertTrue(TestVM.test(input, expect, 415))
    
    # def test_416(self):
    #     input = """[
    #         [var(x, integer)],
    #         [func(addTwo, [par(a, integer)], integer, [
    #             assign(addTwo, add(a, 2))
    #         ])],
    #         [assign(x, call(addTwo, [3])), call(writeInt, [x])]
    #     ]."""
    #     expect = "5"
    #     self.assertTrue(TestVM.test(input, expect, 416))

    # def test_417(self):
    #     input = """[
    #         [var(x, integer)],
    #         [],
    #         [assign(y, 5)]
    #     ]."""
    #     expect = "Undeclared identifier: y"
    #     self.assertTrue(TestVM.test(input, expect, 417))

    # def test_418(self):
    #     input = """[
    #         [],
    #         [func(identity, [par(x, integer)], integer, [assign(identity, x)])],
    #         [call(writeInt, [call(identity, [10])])]
    #     ]."""
    #     expect = "10"
    #     self.assertTrue(TestVM.test(input, expect, 418))
        

    # def test_419(self):
    #     input = """[
    #         [],
    #         [func(double, [par(x, integer)], integer, [assign(double, times(x, 2))])],
    #         [call(writeInt, [call(double, [3, 5])])]
    #     ]."""
    #     expect = "Wrong number of arguments: call(double,[3,5])"
    #     self.assertTrue(TestVM.test(input, expect, 419))

    # def test_420(self):
    #     input = """[
    #         [var(x, integer)],
    #         [func(negate, [par(a, integer)], integer, [assign(negate, sub(a))])],
    #         [assign(x, call(negate, [5])), call(writeInt, [x])]
    #     ]."""
    #     expect = "-5"
    #     self.assertTrue(TestVM.test(input, expect, 420))
        
    # def test_421(self):
    #     input = """[[var(x,integer)],[],[call(writeInt,[x])]]."""
    #     expect = "Invalid expression: x"
    #     self.assertTrue(TestVM.test(input, expect, 421))
        
    # def test_422(self):
    #     input = """[[],
    #     [proc(printSum, [par(a,integer),par(b,integer)], [
    #         call(writeInt,[add(a,b)])
    #     ])],
    #     [call(printSum,[2,3])]]."""
    #     expect = "5"
    #     self.assertTrue(TestVM.test(input, expect, 422))
        
    # def test_423(self):
    #     input = """[
    #         [],
    #         [],
    #         [call(writeInt, [call(double, [3, 5])])]
    #     ]."""
    #     expect = "Undeclared function: call(double,[3,5])"
    #     self.assertTrue(TestVM.test(input, expect, 423))

    # def test_424(self):
    #     input = """[[],
    #     [],
    #     [call(printSum,[2,3])]]."""
    #     expect = "Undeclared procedure: call(printSum,[2,3])"
    #     self.assertTrue(TestVM.test(input, expect, 424))
            
    # def test_425(self):
    #     input = """[[var(x,integer)],[],
    #     [assign(x,1),
    #     block([var(x,integer)], [assign(x,2), call(writeIntLn,[x])]),
    #     call(writeInt,[x])]]."""
    #     expect = "2\n1"
    #     self.assertTrue(TestVM.test(input, expect, 425))

    # def test_426(self):
    #     input = """[[],[],
    #     [block([var(a,integer),var(a,real)], [call(writeInt,[1])])]]."""
    #     expect = "Redeclared identifier: var(a,real)"
    #     self.assertTrue(TestVM.test(input, expect, 426))

    # def test_427(self):
    #     input = """[[],[],[
    #         block([var(a,integer)], [assign(a,3), call(writeIntLn,[a])]),
    #         call(writeInt,[a])
    #     ]]."""
    #     expect = "3\nUndeclared identifier: a"
    #     self.assertTrue(TestVM.test(input, expect, 427))

    # def test_428(self):
    #     input = """[[var(x,integer)],[],[
    #         assign(x,0),
    #         if(true, assign(x,1), assign(x,2)),
    #         call(writeInt,[x])
    #     ]]."""
    #     expect = "1"
    #     self.assertTrue(TestVM.test(input, expect, 428))

    # def test_429(self):
    #     input = """[[var(x,integer)],[],[
    #         assign(x,0),
    #         if(false, assign(x,1), assign(x,2)),
    #         call(writeInt,[x])
    #     ]]."""
    #     expect = "2"
    #     self.assertTrue(TestVM.test(input, expect, 429))

    # def test_430(self):
    #     input = """[[var(x,integer)],[],[
    #         assign(x,1),
    #         if(x, assign(x,2), assign(x,3)),
    #         call(writeInt,[x])
    #     ]]."""
    #     expect = "Type mismatch: if(x,assign(x,2),assign(x,3))"
    #     self.assertTrue(TestVM.test(input, expect, 430))

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