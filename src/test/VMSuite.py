import unittest
from TestUtils import TestVM


class VMSuite(unittest.TestCase):
    # def test_1(self):
    #     input = """
    #         [[var(x,integer)],[],
    #         [assign(x,10),call(writeInt,[x])]]."""
    #     expect = "10"
    #     self.assertTrue(TestVM.test(input, expect, 1))

    # def test_2(self):
    #     input = """[[const(a,5)],[],[call(writeInt,[a])]]."""
    #     expect = "5"
    #     self.assertTrue(TestVM.test(input, expect, 2))

    # def test_3(self):
    #     input = """[[],[func(f,[],float,[assign(f,2.5)])],[call(writeReal,[add(call(f,[]),1.5)])]]."""
    #     expect = "4.0"
    #     self.assertTrue(TestVM.test(input, expect, 3))

    # def test_4(self):
    #     input = """
    #     [[var(x,integer)],[proc(p,[par(a,integer)],[assign(x,a),call(writeInt,[x])])],[call(p,[10])]]."""
    #     expect = "10"
    #     self.assertTrue(TestVM.test(input, expect, 4))

    # def test_5(self):
    #     input = """[[var(a,boolean),var(b,boolean)],[],[assign(a,true),assign(b,false),call(writeBool,[band(a,b)])]]."""
    #     expect = "false"
    #     self.assertTrue(TestVM.test(input, expect, 5))

    # def test_6(self):
    #     input = """[[var(a,boolean)],[],[assign(a,false),call(writeBool,[band(a,3)])]]."""
    #     expect = "false"
    #     self.assertTrue(TestVM.test(input, expect, 6))

    # def test_7(self):
    #     input = """[[var(i,integer)],[],[assign(i,0),while(less(i,3),assign(i,add(i,1))),call(writeInt,[i])]]."""
    #     expect = "3"
    #     self.assertTrue(TestVM.test(input, expect, 7))

    # def test_8(self):
    #     input = """[[var(i,integer)],[],[assign(i,0),loop(3,assign(i,add(i,1))),call(writeInt,[i])]]."""
    #     expect = "3"
    #     self.assertTrue(TestVM.test(input, expect, 8))

    # def test_9(self):
    #     input = """[[var(i,integer)],[],[assign(i,0),while(true,block([],[if(eql(i,2),break(null)),assign(i,add(i,1))])),call(writeInt,[i])]]."""
    #     expect = "2"
    #     self.assertTrue(TestVM.test(input, expect, 9))

    # def test_10(self):
    #     input = """[[var(i,integer)],[],[assign(i,0),do([assign(i,add(i,1)),if(eql(i,2),continue(null))],less(i,3)),call(writeInt,[i])]]."""
    #     expect = "3"
    #     self.assertTrue(TestVM.test(input, expect, 10))

    # def test_11(self):
    #     input = """[[var(x,integer)],[],[block([var(x,integer)], [assign(x,20),call(writeInt,[x])])]]."""
    #     expect = "20"
    #     self.assertTrue(TestVM.test(input, expect, 11))

    # def test_12(self):
    #     input = """[[var(x,integer)],[],[assign(x,1),if(eql(x,1),call(writeInt,[10]),call(writeInt,[20]))]]."""
    #     expect = "10"
    #     self.assertTrue(TestVM.test(input, expect, 12))

    # def test_13(self):
    #     input = """[[var(x,integer)],[],[assign(x,1),if(eql(x,2),call(writeInt,[10]),call(writeInt,[20]))]]."""
    #     expect = "20"
    #     self.assertTrue(TestVM.test(input, expect, 13))

    # def test_14(self):
    #     input = """[[var(x,integer),const(y,5)],[],[
    #         assign(x,add(y,10)),
    #         call(writeIntLn,[x]),
    #         call(writeInt,[y])
    #     ]]."""
    #     expect = "15\n5"
    #     self.assertTrue(TestVM.test(input, expect, 14))

    # def test_15(self):
    #     input = """[[],
    #         [func(sum,[par(a,integer),par(b,integer)],integer,[assign(sum,add(a,b))])],
    #         [call(writeIntLn,[call(sum,[2,3])]), call(writeInt,[call(sum,[10,5])])]]."""
    #     expect = "5\n15"
    #     self.assertTrue(TestVM.test(input, expect, 15))

    # def test_16(self):
    #     input = """[[var(i,integer)],[],[
    #         assign(i,0),
    #         while(less(i,3),
    #             block([],[
    #                 call(writeIntLn,[i]),
    #                 assign(i,add(i,1))
    #             ])
    #         )
    #     ]]."""
    #     expect = "0\n1\n2\n"
    #     self.assertTrue(TestVM.test(input, expect, 16))

    # def test_17(self):
    #     input = """[[var(i,integer)],[],[
    #         assign(i,0),
    #         do([
    #             call(writeIntLn,[i]),
    #             assign(i,add(i,1))
    #         ], less(i,3))
    #     ]]."""
    #     expect = "0\n1\n2\n"
    #     self.assertTrue(TestVM.test(input, expect, 17))

    # def test_18(self):
    #     input = """[[var(i,integer)],[],[
    #         assign(i,0),
    #         loop(3, block([],[
    #             call(writeIntLn,[i]),
    #             assign(i,add(i,10))
    #         ]))
    #     ]]."""
    #     expect = "0\n10\n20\n"
    #     self.assertTrue(TestVM.test(input, expect, 18))

    # def test_19(self):
    #     input = """[[var(i,integer)],[],[
    #         assign(i,0),
    #         while(less(i,5),
    #             block([],[
    #                 if(eql(i,3), break(null)),
    #                 call(writeIntLn,[i]),
    #                 assign(i,add(i,1))
    #             ])
    #         )
    #     ]]."""
    #     expect = "0\n1\n2\n"
    #     self.assertTrue(TestVM.test(input, expect, 19))

    # def test_20(self):
    #     input = """[[var(i,integer)],[],[
    #         assign(i,0),
    #         while(less(i,5),
    #             block([],[
    #                 assign(i,add(i,1)),
    #                 if(eql(i,3), continue(null)),
    #                 call(writeIntLn,[i])
    #             ])
    #         )
    #     ]]."""
    #     expect = "1\n2\n4\n5\n"
    #     self.assertTrue(TestVM.test(input, expect, 20))

    # def test_21(self):
    #     input = """[[var(a,integer)],[],[
    #         assign(a,call(undefined_func,[]))
    #     ]]."""
    #     expect = "Undeclared function: call(undefined_func,[])"
    #     self.assertTrue(TestVM.test(input, expect, 21))

    # def test_22(self):
    #     input = """[[var(a,integer)],[],[
    #         assign(b,1)
    #     ]]."""
    #     expect = "Undeclared identifier: b"
    #     self.assertTrue(TestVM.test(input, expect, 22))

    # def test_23(self):
    #     input = """[[const(a,3)],[],[
    #         assign(a,5)
    #     ]]."""
    #     expect = "Cannot assign to a constant: assign(a,5)"
    #     self.assertTrue(TestVM.test(input, expect, 23))

    # def test_24(self):
    #     input = """[[var(a,integer)],[],[
    #         assign(a,true)
    #     ]]."""
    #     expect = "Type mismatch: assign(a,true)"
    #     self.assertTrue(TestVM.test(input, expect, 24))

    # def test_25(self):
    #     input = """[[var(x,integer),var(x,real)],[],[]]."""
    #     expect = "Redeclared identifier: var(x,real)"
    #     self.assertTrue(TestVM.test(input, expect, 25))

    # def test_26(self):
    #     input = """[[],[func(foo,[],integer,[]),proc(foo,[],[])],[]]."""
    #     expect = "Redeclared procedure: foo"
    #     self.assertTrue(TestVM.test(input, expect, 26))
    
    # def test_27(self):
    #     input = """[[var(a,integer)],[],[
    #         assign(a,sub(10,3)),
    #         call(writeIntLn,[a])
    #     ]]."""
    #     expect = "7\n"
    #     self.assertTrue(TestVM.test(input, expect, 27))

    # def test_28(self):
    #     input = """[[var(a,integer)],[],[
    #         assign(a,times(4,2)),
    #         call(writeIntLn,[a])
    #     ]]."""
    #     expect = "8\n"
    #     self.assertTrue(TestVM.test(input, expect, 28))

    # def test_29(self):
    #     input = """[[var(a,float)],[],[
    #         assign(a,rdiv(5,2)),
    #         call(writeRealLn,[a])
    #     ]]."""
    #     expect = "2.5\n"
    #     self.assertTrue(TestVM.test(input, expect, 29))

    # def test_30(self):
    #     input = """[[var(a,integer)],[],[
    #         assign(a,idiv(5,2)),
    #         call(writeIntLn,[a])
    #     ]]."""
    #     expect = "2\n"
    #     self.assertTrue(TestVM.test(input, expect, 30))

    # def test_31(self):
    #     input = """[[var(a,integer)],[],[
    #         assign(a,imod(5,3)),
    #         call(writeIntLn,[a])
    #     ]]."""
    #     expect = "2\n"
    #     self.assertTrue(TestVM.test(input, expect, 31))

    # def test_32(self):
    #     input = """[[var(a,boolean)],[],[
    #         assign(a,bnot(false)),
    #         call(writeBool,[a])
    #     ]]."""
    #     expect = "true"
    #     self.assertTrue(TestVM.test(input, expect, 32))

    # def test_33(self):
    #     input = """[[var(a,boolean),var(b,boolean)],[],[
    #         assign(a,true),
    #         assign(b,false),
    #         call(writeBool,[bor(a,b)])
    #     ]]."""
    #     expect = "true"
    #     self.assertTrue(TestVM.test(input, expect, 33))

    # def test_34(self):
    #     input = """[[var(a,integer)],[],[
    #         assign(a,add(true,1))
    #     ]]."""
    #     expect = "Type mismatch: add(true,1)"
    #     self.assertTrue(TestVM.test(input, expect, 34))

    # def test_35(self):
    #     input = """[[var(a,boolean)],[],[
    #         assign(a,greater(true,1))
    #     ]]."""
    #     expect = "Type mismatch: greater(true,1)"
    #     self.assertTrue(TestVM.test(input, expect, 35))

    # def test_36(self):
    #     input = """[[var(a,integer)],[],[
    #         assign(a,greater(2,1)),
    #         call(writeIntLn,[a])
    #     ]]."""
    #     expect = "Type mismatch: assign(a,greater(2,1))"
    #     self.assertTrue(TestVM.test(input, expect, 36))

    # def test_37(self):
    #     input = """[[var(x,boolean)],[],[
    #         assign(x,eql(1,true))
    #     ]]."""
    #     expect = "Type mismatch: eql(1,true)"
    #     self.assertTrue(TestVM.test(input, expect, 37))

    # def test_38(self):
    #     input = """[[var(a,integer),var(b,float),var(c,integer)],[],[
    #         assign(a,add(2,3)),
    #         assign(b,rdiv(5.0,2)),
    #         assign(c,imod(10,3)),
    #         call(writeIntLn,[a]),
    #         call(writeRealLn,[b]),
    #         call(writeIntLn,[c])
    #     ]]."""
    #     expect = "5\n2.5\n1\n"
    #     self.assertTrue(TestVM.test(input, expect, 38))

    # def test_39(self):
    #     input = """[[var(a,boolean),var(b,boolean),var(c,boolean)],[],[
    #         assign(a,true),
    #         assign(b,false),
    #         assign(c,bor(bnot(a),b)),
    #         call(writeBool,[c])
    #     ]]."""
    #     expect = "false"
    #     self.assertTrue(TestVM.test(input, expect, 39))

    # def test_40(self):
    #     input = """[[var(a,boolean),var(b,boolean),var(x,integer),var(y,float)],[],[
    #         assign(x,3),
    #         assign(y,3.0),
    #         assign(a,ge(x,y)),
    #         assign(b,le(x,y)),
    #         call(writeBool,[a]),
    #         call(writeBool,[b])
    #     ]]."""
    #     expect = "truetrue"
    #     self.assertTrue(TestVM.test(input, expect, 40))

    # def test_41(self):
    #     input = """[[var(a,boolean),var(b,boolean)],[],[
    #         assign(a,eql(true,true)),
    #         assign(b,ne(false,true)),
    #         call(writeBool,[a]),
    #         call(writeBool,[b])
    #     ]]."""
    #     expect = "truetrue"
    #     self.assertTrue(TestVM.test(input, expect, 41))

    # def test_42(self):
    #     input = """[[],
    #     [func(inc,[par(x,integer)],integer,[assign(inc,add(x,1))])],
    #     [block(
    #         [var(a,integer)],[
    #         assign(a,add(call(inc,[2]),3)),
    #         call(writeIntLn,[a])])
    #     ]]."""
    #     expect = "6\n"
    #     self.assertTrue(TestVM.test(input, expect, 42))

    def test_43(self):
        input = """[[var(a,integer),var(b,integer),var(c,integer),var(d,float),var(e,integer),var(f,integer)],[],[
            assign(a,add(1,2)),
            assign(b,sub(5)),
            assign(c,times(2,4)),
            assign(d,rdiv(5.0,2)),
            assign(e,idiv(9,2)),
            assign(f,imod(7,4)),
            call(writeIntLn,[a]),
            call(writeIntLn,[b]),
            call(writeIntLn,[c]),
            call(writeRealLn,[d]),
            call(writeIntLn,[e]),
            call(writeIntLn,[f])
        ]]."""
        expect = "3\n-5\n8\n2.5\n4\n3\n"
        self.assertTrue(TestVM.test(input, expect, 43))

    def test_44(self):
        input = """[[var(a,boolean),var(b,boolean),var(c,boolean),var(d,boolean)],[],[
            assign(a,true),
            assign(b,false),
            assign(c,band(a,b)),
            assign(d,bor(a,b)),
            call(writeBool,[bnot(b)]),
            call(writeLn,[]),
            call(writeBool,[c]),
            call(writeLn,[]),
            call(writeBool,[d]),
            call(writeLn,[])
        ]]."""
        expect = "true\nfalse\ntrue\n"
        self.assertTrue(TestVM.test(input, expect, 44))

    def test_45(self):
        input = """[[var(a,boolean),var(b,boolean),var(c,boolean),var(d,boolean)],[],[
            assign(a,greater(4,2)),
            assign(b,less(2,4)),
            assign(c,ge(3,3)),
            assign(d,le(5,6)),
            call(writeBool,[a]),
            call(writeLn,[]),
            call(writeBool,[b]),
            call(writeLn,[]),
            call(writeBool,[c]),
            call(writeLn,[]),
            call(writeBool,[d]),
            call(writeLn,[])
        ]]."""
        expect = "true\ntrue\ntrue\ntrue\n"
        self.assertTrue(TestVM.test(input, expect, 45))

    def test_46(self):
        input = """[[var(a,boolean),var(b,boolean)],[],[
            assign(a,eql(3,3)),
            assign(b,ne(false,true)),
            call(writeBool,[a]),
            call(writeLn,[]),
            call(writeBool,[b]),
            call(writeLn,[])
        ]]."""
        expect = "true\ntrue\n"
        self.assertTrue(TestVM.test(input, expect, 46))

    def test_47(self):
        input = """[[],
        [func(sum2,[par(x,integer),par(y,integer)],integer,[assign(sum2,add(x,y))])],
        [block(
            [var(a,integer),var(b,integer)],
            [
                assign(a,call(sum2,[2,3])),
                assign(b,times(call(sum2,[1,2]),2)),
                call(writeIntLn,[a]),
                call(writeIntLn,[b])
            ])
        ]]."""
        expect = "5\n6\n"
        self.assertTrue(TestVM.test(input, expect, 47))
