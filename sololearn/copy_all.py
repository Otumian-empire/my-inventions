''' Basically, it reads the name of all the files in the pwd, then reads their content into a file '''
from glob import glob
from random import randint as rdt, shuffle as shf

def genfilename(targetfile='hellomybabyhellomygirl', fileextension='.txt'):
    """ takes file name as first arg, the file extension as second arg
    if the file name is not give a default is given like wise a .txt 
    as the extention"""
    targetfile = list(targetfile + str(rdt(121, 2123)))
    shf(targetfile)
    targetfile = ''.join(targetfile) + fileextension

    return [targetfile, fileextension]
    

def copyall(targetfile=''.join(genfilename()[0]), fileextension=''.join(genfilename()[1]), mode='w+'):
    """ takes file name as first arg, else it calls the genfilename(), 
    fileextension as second arg, this  refers to the extension of the files 
    you want to read, by default, it takes the extension of the target file
    and if none is given, txt is then given.
    The 3rd arg is mode, mode (r+, w+, a+) in which you want 
    to open the target file. w+ or a+ is ok. by default, w+. """
    myfile = open(str(targetfile), mode)

    filenames = glob('*' + str(fileextension))

    for i in filenames:
        filecontent = open(i, 'r').read()
        print('\n#filename: ' + str(i) , filecontent, sep='\n', file=myfile)

    myfile.close()

    return "Content copied successfully :- " + str(targetfile)


targetfile, mode = ''.join(genfilename('copyingcontent')[0]), 'w+'
print(copyall(targetfile))
print(copyall('sololearn.py', '.py'))
print(copyall())

# This is the second version
# from glob import glob

# def copyall(filepath='newcopyallfile.txt', fileextension='.py' , filemode='w+'):
#     """ filepath: this is the directed file, by default, 'newcopyallfile.txt'
#     fileextension: this is the file extension and by default is .txt
#     filemode: this is the file mode(a+, w+, r+)"""
#     for i in glob('*'+ fileextension):
#         print("#file name: " + str(i), open(i, 'r').read(), sep='\n', file=open(filepath, filemode))
    
#     return 'Copied: True' + ' into File: ' + filepath

# print(copyall())
