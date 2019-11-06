import sys

def preprocess(inputfile1, inputfile2):

    myoutput = open('preprocessing.log', 'w')
    if '1' in inputfile2:
        myoutput.write(inputfile1 + ' ' + inputfile2 + ': ALIGN')
    else:
        myoutput.write(inputfile1 + ' ' + inputfile2 + ': MISMATCH')
    myoutput.close()


def main():

    argv = sys.argv
    if len(argv) < 3:
        print('Usage: python preprocess.py inputfile1 inputfile2')
    else:
        preprocess(argv[1], argv[2])

if __name__ == '__main__':
    main()
