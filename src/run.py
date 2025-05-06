import sys
import os

import unittest


for path in ['./test/']:
    sys.path.append(path)



def main(argv):
    if len(argv) < 2:
        printUsage()
    elif argv[0] == 'test' and argv[1] == 'VMSuite':
        from VMSuite import VMSuite
        getAndTest(VMSuite)         
    else:
        printUsage()


def getAndTest(cls):
    suite = unittest.makeSuite(cls)
    test(suite)

# for new version of Python
#def getAndTest(cls):
#    suite = unittest.TestSuite()
#    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(cls)
#    test(suite)

def test(suite):
    from pprint import pprint
    from io import StringIO
    stream = StringIO()
    runner = unittest.TextTestRunner(stream=stream)
    result = runner.run(suite)
    print('Tests run ', result.testsRun)
    print('Errors ', result.errors)
    pprint(result.failures)
    stream.seek(0)
    print('Test output\n', stream.read())


def printUsage():
    print("python3 run.py test VMSuite")


if __name__ == "__main__":
    main(sys.argv[1:])
