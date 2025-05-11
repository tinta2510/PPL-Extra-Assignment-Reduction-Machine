import unittest
from TestUtils import TestVM


class VMSuite(unittest.TestCase):
    def test_1(self):
        input = """
            [[var(x,integer)],[],
            [assign(x,10),call(writeInt,[x])]]."""
        expect = "10"
        self.assertTrue(TestVM.test(input, expect, 1))

    def test_2(self):
        input = """[[const(a,5)],[],[call(writeInt,[a])]]."""
        expect = "5"
        self.assertTrue(TestVM.test(input, expect, 2))

    def test_3(self):
        input = """[[],[func(f,[],float,[assign(f,2.5)])],[call(writeReal,[add(call(f,[]),1.5)])]]."""
        expect = "4.0"
        self.assertTrue(TestVM.test(input, expect, 3))

    def test_4(self):
        input = """
        [[var(x,integer)],[proc(p,[par(a,integer)],[assign(x,a),call(writeInt,[x])])],[call(p,[10])]]."""
        expect = "10"
        self.assertTrue(TestVM.test(input, expect, 4))

    def test_5(self):
        input = """[[var(a,boolean),var(b,boolean)],[],[assign(a,true),assign(b,false),call(writeBool,[band(a,b)])]]."""
        expect = "false"
        self.assertTrue(TestVM.test(input, expect, 5))

    def test_6(self):
        input = """[[var(a,boolean)],[],[assign(a,false),call(writeBool,[band(a,3)])]]."""
        expect = "false"
        self.assertTrue(TestVM.test(input, expect, 6))

    def test_7(self):
        input = """[[var(i,integer)],[],[assign(i,0),while(less(i,3),assign(i,add(i,1))),call(writeInt,[i])]]."""
        expect = "3"
        self.assertTrue(TestVM.test(input, expect, 7))

    def test_8(self):
        input = """[[var(i,integer)],[],[assign(i,0),loop(3,assign(i,add(i,1))),call(writeInt,[i])]]."""
        expect = "3"
        self.assertTrue(TestVM.test(input, expect, 8))

    def test_9(self):
        input = """[[var(i,integer)],[],[assign(i,0),while(true,block([],[if(eql(i,2),break(null)),assign(i,add(i,1))])),call(writeInt,[i])]]."""
        expect = "2"
        self.assertTrue(TestVM.test(input, expect, 9))

    def test_10(self):
        input = """[[var(i,integer)],[],[assign(i,0),do([assign(i,add(i,1)),if(eql(i,2),continue(null))],less(i,3)),call(writeInt,[i])]]."""
        expect = "3"
        self.assertTrue(TestVM.test(input, expect, 10))

    def test_11(self):
        input = """[[var(x,integer)],[],[block([var(x,integer)], [assign(x,20),call(writeInt,[x])])]]."""
        expect = "20"
        self.assertTrue(TestVM.test(input, expect, 11))

    def test_12(self):
        input = """[[var(x,integer)],[],[assign(x,1),if(eql(x,1),call(writeInt,[10]),call(writeInt,[20]))]]."""
        expect = "10"
        self.assertTrue(TestVM.test(input, expect, 12))

    def test_13(self):
        input = """[[var(x,integer)],[],[assign(x,1),if(eql(x,2),call(writeInt,[10]),call(writeInt,[20]))]]."""
        expect = "20"
        self.assertTrue(TestVM.test(input, expect, 13))
