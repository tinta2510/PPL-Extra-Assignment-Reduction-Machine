import sys
import os
import traceback
from swiplserver import PrologMQI, PrologThread, create_posix_path

TEST_DIR = "./test/testcases/"
SOL_DIR = "./test/solutions/"
MAIN_FILE="./main/vm/virtual.pl"

class TestUtil:
    @staticmethod
    def makeSource(inputStr, num):
        filename = TEST_DIR + str(num) + ".txt"
        file = open(filename, "w")
        file.write(inputStr)
        file.close()
        #return FileStream(filename)
        
class TestVM:
    @staticmethod
    def test(input, expect, num):
        TestUtil.makeSource(input, num)
        TestVM.check(SOL_DIR, TEST_DIR, num)
        dest = open(os.path.join(SOL_DIR, str(num) + ".txt"), "r")
        line = dest.read()
        return line == expect
    

    @staticmethod
    def check(soldir, testdir, num):
        destname = os.path.join(soldir, str(num) + ".txt")
        srcname = os.path.join(testdir, str(num) + ".txt")
        os.replace(srcname,"input.txt")
        with PrologMQI() as mqi:
            with mqi.create_thread() as prolog:
                path = create_posix_path(MAIN_FILE)
                prolog.query(f'consult("{path}").')
                prolog.query('go')
        os.replace("input.txt",srcname)       
        os.replace("output.txt",destname)
