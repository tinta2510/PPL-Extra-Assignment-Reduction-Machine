import unittest
from TestUtils import TestVM


class VMSuite(unittest.TestCase):
    # def test_401(self):        
    #     input = """[[],[],[call(writeInt,[3])]]."""
    #     expect = "3"
    #     self.assertTrue(TestVM.test(input, expect, 401))

    # def test_402(self):        
    #     input = """[[],[],[call(writeInt,[add(3,1)])]]."""
    #     expect = "4"
    #     self.assertTrue(TestVM.test(input, expect, 402))

    # def test_403(self):        
    #     input = """[[var(a,integer),var(b,integer),var(a,float)],[],[call(writeInt,[1])]]."""
    #     expect = "Redeclared identifier: var(a,float)"
    #     self.assertTrue(TestVM.test(input, expect, 403))

    # def test_404(self):        
    #     input = """[[],[],[call(writeInt,[sub(3,1)])]]."""
    #     expect = "2"
    #     self.assertTrue(TestVM.test(input, expect, 404))

    # def test_405(self):        
    #     input = """[[],[],[call(writeInt,[add(4,sub(3,1))])]]."""
    #     expect = "6"
    #     self.assertTrue(TestVM.test(input, expect, 405))
        
    # def test_406(self):
    #     input = """[[],[],[call(writeReal,[10.0])]]."""
    #     expect = "10.0"
    #     self.assertTrue(TestVM.test(input, expect, 406))
        
    # def test_407(self):
    #     input = """[[const(a,10)],[],[call(writeInt,[a])]]."""
    #     expect = "10"   
    #     self.assertTrue(TestVM.test(input, expect, 407))
        
    # def test_408(self):
    #     input = """[[var(a,integer)],[],[call(writeInt,[a])]]."""
    #     expect = "Invalid expression: a"   
    #     self.assertTrue(TestVM.test(input, expect, 408))

    # def test_409(self):
    #     input = """[[],[],[
    #         call(writeIntLn,[times(3,2)]),
    #         call(writeRealLn,[rdiv(3,2)]),
    #         call(writeIntLn,[sub(-10)]),
    #         call(writeIntLn,[idiv(5,2)]),
    #         call(writeInt,[imod(5,2)])
    #     ]]."""
    #     expect = "6\n1.5\n10\n2\n1"
    #     self.assertTrue(TestVM.test(input, expect, 409))
        
    # def test_410(self):
    #     input = """[[],[],[
    #         call(writeBool,[bnot(true)]),
    #         call(writeBool,[band(true,false)]),
    #         call(writeBool,[bor(true,false)])
    #         ]]."""
    #     expect = "falsefalsetrue"
    #     self.assertTrue(TestVM.test(input, expect, 410))

    # def test_411(self):
    #     input = """[[var(a,integer)],[],[assign(a,3),call(writeInt,[a])]]."""
    #     expect = "3"
    #     self.assertTrue(TestVM.test(input, expect, 411))
        
    # def test_412(self):
    #     input = """[[const(a,10)],[],[assign(a,3),call(writeInt,[a])]]."""
    #     expect = "Cannot assign to a constant: assign(a,3)"
    #     self.assertTrue(TestVM.test(input, expect, 412))
        
    # def test_413(self):
    #     input = """[[var(c,integer),const(b,10),var(a,integer)],[],[assign(a,3),call(writeInt,[a])]]."""
    #     expect = "3"
    #     self.assertTrue(TestVM.test(input, expect, 413))
        
    def test_414(self):
        input = """
[[var(a,integer)],
[func(foo,[par(a,integer),par(b,integer)],integer,[assign(a,add(a,b)),assign(foo,a)])], 
[assign(a,3),call(writeIntLn,[call(foo,[a,3])]),call(writeIntLn,[a])]]."""
        expect = "6\n3"
        self.assertTrue(TestVM.test(input, expect, 414))