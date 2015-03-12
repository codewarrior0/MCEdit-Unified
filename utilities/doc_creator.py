import inspect
import time
from pymclevel import infiniteworld
import os


class NotAModule(Exception):
    pass



def create_docs():
    lines = []
    classes = inspect.getmembers(infiniteworld, inspect.isclass)
    for clazz in classes:
        lines.append("## "+str(clazz[0])+"\n\n")
        print clazz[1]
        print clazz[1].__doc__
        lines.append(str(clazz[1].__doc__)+"\n\n")
        methods = inspect.getmembers(clazz[1], inspect.ismethod)
        '''
        for method in methods:
            print method[1].__doc__
        '''
        
    print "======="
    with open("DOC TESTS"+os.path.sep+"test_doc_"+str(time.ctime()).replace(":", "-")+".md", 'w') as f:
        f.writelines(lines)


if __name__ == "__main__":
    create_docs()
else:
    raise NotAModule(str(__name__)+" is not a module!")