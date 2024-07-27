#help('zipfile')        info about zipfile
#usage: python zip-pwd.zip .f 'ZIPFILE' -d 'DICTIONARY'
import zipfile
from threading import Thread
import optparse

def extractFile(zfile, password):
    try:
        zfile.extractall(pwd=str.encode(password))
        print(f"The password for {zfile.filename} is: {password}\n")
    except:
        pass

def main():
    parser = optparse.OptionParser("usage%prog " + "-f <zipfile> -d <dictionary>")
    parser.add_option('-f', dest='zname', type='string', help='specify zip file')
    parser.add_option('-d', dest='dname', type='string', help='specify zip file')
    (options, args) = parser.parse_args()
    if (options.zname == None) or (options.dname == None):
        print (parser.usage)
        exit(0)
    else:
        zname = options.zname
        dname = options.dname
    zfile = zipfile.ZipFile(zname)
    passfile = open(dname)
    for line in passfile.readlines():
        password = line.strip('\n')
        t = Thread(target=extractFile, args=(zfile, password))
        t.start()

if __name__ == '__main__':
    main()
 
