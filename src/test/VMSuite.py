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

    # def test_43(self):
    #     input = """[[var(a,integer),var(b,integer),var(c,integer),var(d,float),var(e,integer),var(f,integer)],[],[
    #         assign(a,add(1,2)),
    #         assign(b,sub(5)),
    #         assign(c,times(2,4)),
    #         assign(d,rdiv(5.0,2)),
    #         assign(e,idiv(9,2)),
    #         assign(f,imod(7,4)),
    #         call(writeIntLn,[a]),
    #         call(writeIntLn,[b]),
    #         call(writeIntLn,[c]),
    #         call(writeRealLn,[d]),
    #         call(writeIntLn,[e]),
    #         call(writeIntLn,[f])
    #     ]]."""
    #     expect = "3\n-5\n8\n2.5\n4\n3\n"
    #     self.assertTrue(TestVM.test(input, expect, 43))

    # def test_44(self):
    #     input = """[[var(a,boolean),var(b,boolean),var(c,boolean),var(d,boolean)],[],[
    #         assign(a,true),
    #         assign(b,false),
    #         assign(c,band(a,b)),
    #         assign(d,bor(a,b)),
    #         call(writeBool,[bnot(b)]),
    #         call(writeLn,[]),
    #         call(writeBool,[c]),
    #         call(writeLn,[]),
    #         call(writeBool,[d]),
    #         call(writeLn,[])
    #     ]]."""
    #     expect = "true\nfalse\ntrue\n"
    #     self.assertTrue(TestVM.test(input, expect, 44))

    # def test_45(self):
    #     input = """[[var(a,boolean),var(b,boolean),var(c,boolean),var(d,boolean)],[],[
    #         assign(a,greater(4,2)),
    #         assign(b,less(2,4)),
    #         assign(c,ge(3,3)),
    #         assign(d,le(5,6)),
    #         call(writeBool,[a]),
    #         call(writeLn,[]),
    #         call(writeBool,[b]),
    #         call(writeLn,[]),
    #         call(writeBool,[c]),
    #         call(writeLn,[]),
    #         call(writeBool,[d]),
    #         call(writeLn,[])
    #     ]]."""
    #     expect = "true\ntrue\ntrue\ntrue\n"
    #     self.assertTrue(TestVM.test(input, expect, 45))

    # def test_46(self):
    #     input = """[[var(a,boolean),var(b,boolean)],[],[
    #         assign(a,eql(3,3)),
    #         assign(b,ne(false,true)),
    #         call(writeBool,[a]),
    #         call(writeLn,[]),
    #         call(writeBool,[b]),
    #         call(writeLn,[])
    #     ]]."""
    #     expect = "true\ntrue\n"
    #     self.assertTrue(TestVM.test(input, expect, 46))

    # def test_47(self):
    #     input = """[[],
    #     [func(sum2,[par(x,integer),par(y,integer)],integer,[assign(sum2,add(x,y))])],
    #     [block(
    #         [var(a,integer),var(b,integer)],
    #         [
    #             assign(a,call(sum2,[2,3])),
    #             assign(b,times(call(sum2,[1,2]),2)),
    #             call(writeIntLn,[a]),
    #             call(writeIntLn,[b])
    #         ])
    #     ]]."""
    #     expect = "5\n6\n"
    #     self.assertTrue(TestVM.test(input, expect, 47))

    # def test_48(self):
    #     input = """[[],
    #     [func(inc,[par(x,integer)],integer,[assign(inc,add(x,1))])],
    #     [block(
    #         [var(a,integer),var(b,integer),var(c,float)],
    #             [
    #             assign(a,5),
    #             assign(b,call(inc,[a])),
    #             assign(c,rdiv(add(b,5.0),2)),
    #             call(writeIntLn,[a]),
    #             call(writeIntLn,[b]),
    #             call(writeRealLn,[c])
    #         ])
    #     ]]."""
    #     expect = "5\n6\n5.5\n"
    #     self.assertTrue(TestVM.test(input, expect, 48))

    # def test_49(self):
    #     input = """[[var(a,boolean),var(b,boolean),var(c,boolean)],[],[
    #         assign(a,false),
    #         assign(b,true),
    #         assign(c,bor(band(a,b),bnot(a))),
    #         call(writeBool,[c]),
    #         call(writeLn,[])
    #     ]]."""
    #     expect = "true\n"
    #     self.assertTrue(TestVM.test(input, expect, 49))

    # def test_50(self):
    #     input = """[[var(a,boolean),var(b,boolean)],
    #     [func(get3,[],integer,[assign(get3,3)])],
    #     [
    #         assign(a,le(call(get3,[]),3.0)),
    #         assign(b,greater(4.5,call(get3,[]))),
    #         call(writeBool,[a]),
    #         call(writeLn,[]),
    #         call(writeBool,[b]),
    #         call(writeLn,[])
    #     ]]."""
    #     expect = "true\ntrue\n"
    #     self.assertTrue(TestVM.test(input, expect, 50))

    # def test_51(self):
    #     input = """[[],
    #     [func(equalOr,[par(x,boolean),par(y,boolean)],boolean,[
    #         assign(equalOr,bor(eql(x,y),band(x,y)))
    #     ])],
    #     [block(
    #         [var(r,boolean)],
    #         [
    #             assign(r,call(equalOr,[true,false])),
    #             call(writeBool,[r]),
    #             call(writeLn,[])
    #         ])
    #     ]]."""
    #     expect = "false\n"
    #     self.assertTrue(TestVM.test(input, expect, 51))

    # def test_52(self):
    #     input = """[[var(a,integer),var(b,integer),var(c,integer)],[],[
    #         assign(a,idiv(times(4,5),2)),
    #         assign(b,imod(sub(20,5),4)),
    #         assign(c,add(a,b)),
    #         call(writeIntLn,[a]),
    #         call(writeIntLn,[b]),
    #         call(writeIntLn,[c])
    #     ]]."""
    #     expect = "10\n3\n13\n"
    #     self.assertTrue(TestVM.test(input, expect, 52))

    # def test_53(self):
    #     input = """[[var(x,integer),const(y,5)],[],[
    #         assign(x,add(y,1)),
    #         call(writeIntLn,[x]),
    #         call(writeIntLn,[y])
    #     ]]."""
    #     expect = "6\n5\n"
    #     self.assertTrue(TestVM.test(input, expect, 53))

    # def test_54(self):
    #     input = """[[],
    #     [proc(printTwice,[par(a,integer)],[
    #         block([var(b,integer)],[
    #             assign(b,add(a,a)),
    #             call(writeIntLn,[b])
    #         ])
    #     ])],
    #     [block([var(x,integer)],[
    #         assign(x,4),
    #         call(printTwice,[x])
    #     ])]]."""
    #     expect = "8\n"
    #     self.assertTrue(TestVM.test(input, expect, 54))

    # def test_55(self):
    #     input = """[[var(i,integer)],[],[
    #         assign(i,0),
    #         while(less(i,3),block([],[
    #             call(writeIntLn,[i]),
    #             assign(i,add(i,1))
    #         ]))
    #     ]]."""
    #     expect = "0\n1\n2\n"
    #     self.assertTrue(TestVM.test(input, expect, 55))

    # def test_56(self):
    #     input = """[[var(i,integer)],[],[
    #         assign(i,0),
    #         do([
    #             call(writeIntLn,[i]),
    #             assign(i,add(i,1))
    #         ],less(i,3))
    #     ]]."""
    #     expect = "0\n1\n2\n"
    #     self.assertTrue(TestVM.test(input, expect, 56))

    # def test_57(self):
    #     input = """[[var(i,integer)],[],[
    #         assign(i,0),
    #         loop(3,block([],[
    #             call(writeIntLn,[i]),
    #             assign(i,add(i,1))
    #         ]))
    #     ]]."""
    #     expect = "0\n1\n2\n"
    #     self.assertTrue(TestVM.test(input, expect, 57))

    # def test_58(self):
    #     input = """[[var(a,integer)],[],[
    #         assign(a,2),
    #         if(eql(a,2), call(writeIntLn,[1]), call(writeIntLn,[0]))
    #     ]]."""
    #     expect = "1\n"
    #     self.assertTrue(TestVM.test(input, expect, 58))

    # def test_59(self):
    #     input = """[[var(a,integer)],[],[
    #         assign(a,3),
    #         if(eql(a,3), call(writeIntLn,[99]))
    #     ]]."""
    #     expect = "99\n"
    #     self.assertTrue(TestVM.test(input, expect, 59))

    # def test_60(self):
    #     input = """[[var(i,integer)],[],[
    #         assign(i,0),
    #         while(true,block([],[
    #             if(eql(i,2), break(null)),
    #             call(writeIntLn,[i]),
    #             assign(i,add(i,1))
    #         ]))
    #     ]]."""
    #     expect = "0\n1\n"
    #     self.assertTrue(TestVM.test(input, expect, 60))

    # def test_61(self):
    #     input = """[[var(i,integer)],[],[
    #         assign(i,0),
    #         while(less(i,4),block([],[
    #             assign(i,add(i,1)),
    #             if(eql(i,2), continue(null)),
    #             call(writeIntLn,[i])
    #         ]))
    #     ]]."""
    #     expect = "1\n3\n4\n"
    #     self.assertTrue(TestVM.test(input, expect, 61))

    # def test_62(self):
    #     input = """[[],
    #     [proc(printTwice,[par(a,integer)],[
    #         block([var(b,integer)],[
    #             assign(b,add(a,a)),
    #             call(writeIntLn,[b])
    #         ])
    #     ])],
    #     [
    #         block([var(x,integer)],[
    #             assign(x,4),
    #             call(printTwice,[x])
    #         ])
    #     ]]."""
    #     expect = "8\n"
    #     self.assertTrue(TestVM.test(input, expect, 62))

    # def test_63(self):
    #     input = """[[var(i,integer)],[],[
    #         assign(i,0),
    #         while(true,block([],[
    #             if(eql(i,2), break(null)),
    #             call(writeIntLn,[i]),
    #             assign(i,add(i,1))
    #         ]))
    #     ]]."""
    #     expect = "0\n1\n"
    #     self.assertTrue(TestVM.test(input, expect, 63))

    # def test_64(self):
    #     input = """[[var(i,integer)],[],[
    #         assign(i,0),
    #         do([
    #             if(eql(i,2), break(null)),
    #             call(writeIntLn,[i]),
    #             assign(i,add(i,1))
    #         ],true)
    #     ]]."""
    #     expect = "0\n1\n"
    #     self.assertTrue(TestVM.test(input, expect, 64))

    # def test_65(self):
    #     input = """[[var(i,integer)],[],[
    #         assign(i,0),
    #         loop(5, block([],[
    #             if(eql(i,3), break(null)),
    #             call(writeIntLn,[i]),
    #             assign(i,add(i,1))
    #         ]))
    #     ]]."""
    #     expect = "0\n1\n2\n"
    #     self.assertTrue(TestVM.test(input, expect, 65))

    # def test_66(self):
    #     input = """[[var(i,integer)],[],[
    #         assign(i,0),
    #         while(less(i,4),block([],[
    #             assign(i,add(i,1)),
    #             if(eql(i,2), continue(null)),
    #             call(writeIntLn,[i])
    #         ]))
    #     ]]."""
    #     expect = "1\n3\n4\n"
    #     self.assertTrue(TestVM.test(input, expect, 66))

    # def test_67(self):
    #     input = """[[var(i,integer)],[],[
    #         assign(i,0),
    #         do([
    #             assign(i,add(i,1)),
    #             if(eql(i,2), continue(null)),
    #             call(writeIntLn,[i])
    #         ],less(i,4))
    #     ]]."""
    #     expect = "1\n3\n4\n"
    #     self.assertTrue(TestVM.test(input, expect, 67))

    # def test_68(self):
    #     input = """[[var(i,integer)],[],[
    #         assign(i,0),
    #         loop(5, block([],[
    #             assign(i,add(i,1)),
    #             if(eql(i,3), continue(null)),
    #             call(writeIntLn,[i])
    #         ]))
    #     ]]."""
    #     expect = "1\n2\n4\n5\n"
    #     self.assertTrue(TestVM.test(input, expect, 68))

    # def test_69(self):
    #     input = """[[var(a,integer),var(a,real)],[],[]]."""
    #     expect = "Redeclared identifier: var(a,real)"
    #     self.assertTrue(TestVM.test(input, expect, 69))

    # def test_70(self):
    #     input = """[[],[proc(p,[par(a,integer),par(a,real)],[])],[]]."""
    #     expect = "Redeclared identifier: par(a,real)"
    #     self.assertTrue(TestVM.test(input, expect, 70))

    # def test_71(self):
    #     input = """[[],[],[block([var(a,integer),var(a,real)],[])]]."""
    #     expect = "Redeclared identifier: var(a,real)"
    #     self.assertTrue(TestVM.test(input, expect, 71))

    # def test_72(self):
    #     input = """[[],[func(readInt,[],integer,[])],[]]."""
    #     expect = "Redeclared function: readInt"
    #     self.assertTrue(TestVM.test(input, expect, 72))

    # def test_73(self):
    #     input = """[[var(a,integer)],[],[assign(a,add(1,true))]]."""
    #     expect = "Type mismatch: add(1,true)"
    #     self.assertTrue(TestVM.test(input, expect, 73))

    # def test_74(self):
    #     input = """[[var(a,integer)],[],[assign(a,add(b,1))]]."""
    #     expect = "Undeclared identifier: b"
    #     self.assertTrue(TestVM.test(input, expect, 74))

    # def test_75(self):
    #     input = """[[],[proc(p,[par(x,integer)],[])],[call(p,[])]]."""
    #     expect = "Wrong number of arguments: call(p,[])"
    #     self.assertTrue(TestVM.test(input, expect, 75))

    # def test_76(self):
    #     input = """[[var(a,integer)],[func(f,[],integer,[])],[assign(a,call(f,[]))]]."""
    #     expect = "Invalid expression: call(f,[])"
    #     self.assertTrue(TestVM.test(input, expect, 76))

    # def test_77(self):
    #     input = """[[var(a,integer)],[],[assign(a,call(nonexistent,[]))]]."""
    #     expect = "Undeclared function: call(nonexistent,[])"
    #     self.assertTrue(TestVM.test(input, expect, 77))

    # def test_78(self):
    #     input = """[[],[],[call(unknown,[])]]."""
    #     expect = "Undeclared procedure: call(unknown,[])"
    #     self.assertTrue(TestVM.test(input, expect, 78))

    # def test_79(self):
    #     input = """[[],[],[break(null)]]."""
    #     expect = "Break not in a loop: break(null)"
    #     self.assertTrue(TestVM.test(input, expect, 79))

    # def test_80(self):
    #     input = """[[],[],[continue(null)]]."""
    #     expect = "Continue not in a loop: continue(null)"
    #     self.assertTrue(TestVM.test(input, expect, 80))

    # def test_81(self):
    #     input = """[[const(a,5)],[],[assign(a,6)]]."""
    #     expect = "Cannot assign to a constant: assign(a,6)"
    #     self.assertTrue(TestVM.test(input, expect, 81))

    # def test_82(self):
    #     input = """[[var(a,integer)],[],[
    #         block([var(b,integer)],[assign(b,5)]),
    #         assign(a,b)
    #     ]]."""
    #     expect = "Undeclared identifier: b"
    #     self.assertTrue(TestVM.test(input, expect, 82))

    # def test_83(self):
    #     input = """[[var(a,integer)],[],[
    #         assign(a,1),
    #         if(a, call(writeIntLn,[1]), call(writeIntLn,[0]))
    #     ]]."""
    #     expect = "Type mismatch: if(a,call(writeIntLn,[1]),call(writeIntLn,[0]))"
    #     self.assertTrue(TestVM.test(input, expect, 83))

    # def test_84(self):
    #     input = """[[],
    #     [func(f,[],boolean,[assign(f,1)])],
    #     [call(writeBool,[call(f,[])])]]."""
    #     expect = "Type mismatch: assign(f,1)"
    #     self.assertTrue(TestVM.test(input, expect, 84))

    # def test_85(self):
    #     input = """[[var(a,integer)],
    #     [func(f,[],integer,[assign(f,x)])],
    #     [assign(a,call(f,[]))]]."""
    #     expect = "Undeclared identifier: x"
    #     self.assertTrue(TestVM.test(input, expect, 85))

    # def test_86(self):
    #     input = """[[],
    #     [proc(printInt,[par(x,integer)],[
    #         call(writeIntLn,[x])
    #     ])],
    #     [call(printInt,[true])]]."""
    #     expect = "Type mismatch: call(printInt,[true])"
    #     self.assertTrue(TestVM.test(input, expect, 86))

    def test_87(self):
        input = """[[],
        [func(double,[par(x,integer)],integer,[assign(double,times(x,2))])],
        [block([var(x,integer)],[
            assign(x,3),
            block([var(x,integer)],[
                assign(x,call(double,[5])),
                call(writeIntLn,[x])
            ]),
            call(writeIntLn,[x])
        ])]]."""
        expect = "10\n3\n"
        self.assertTrue(TestVM.test(input, expect, 87))

    def test_88(self):
        input = """[[var(result,integer)],
        [func(fact,[par(n,integer)],integer,[
            if(le(n,1),assign(fact,1),
            assign(fact,times(n,call(fact,[sub(n,1)]))))
        ])],
        [
            assign(result,call(fact,[5])),
            call(writeIntLn,[result])
        ]]."""
        expect = "120\n"
        self.assertTrue(TestVM.test(input, expect, 88))

    def test_89(self):
        input = """[[var(x,boolean)],[],[
            assign(x,false),
            call(writeBool,[band(x,add(1,true))]),
            call(writeLn,[])
        ]]."""
        expect = "false\n"
        self.assertTrue(TestVM.test(input, expect, 89))

    def test_90(self):
        input = """[[],
        [func(f,[par(x,integer)],integer,[
            assign(f,add(x,1))
        ])],
        [call(writeIntLn,[call(f,[4])])]]."""
        expect = "5\n"
        self.assertTrue(TestVM.test(input, expect, 90))

    def test_91(self):
        input = """[[var(x,integer)],[],[
            assign(x,1),
            block([const(y,10)],[
                call(writeIntLn,[add(x,y)])
            ])
        ]]."""
        expect = "11\n"
        self.assertTrue(TestVM.test(input, expect, 91))
