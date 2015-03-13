import inspect
import time
from pymclevel import infiniteworld
import os
import test


class NotAModule(Exception):
    pass



def organizeParameters(func):
    params = []
    for arg in func:
        if arg != "self":
            params.append(arg)
    params = ", ".join(params)
    return params

def getDescription(desc):
    if desc is not None:
        return desc.split(":")[0].strip()
    else:
        return "**Undocumented**"


def create_docs():
    lines = []
    classes = inspect.getmembers(infiniteworld, inspect.isclass)
    for clazz in classes:
        lines.append("## "+str(clazz[0])+"\n\n")
        print clazz[1]
        doc = str(clazz[1].__doc__).replace("    ", "")
        if doc == "None":
            doc = "**Undocumented**"
        lines.append(doc+"\n\n")
        methods = inspect.getmembers(clazz[1], inspect.ismethod)
        if methods != []:
            lines.append("| Function name | Arguments | Description |\n| ------------- | --------- | ----------- |\n")
            for method in methods:
                print method[1].func_code.co_varnames
                print method[1].__doc__
                params = organizeParameters(method[1].func_code.co_varnames)
                print params
                print "| {0} | {1} | {2} |".format(method[0], params, getDescription(method[1].__doc__))
                lines.append("| {0} | {1} | {2} |\n".format(method[0], params, getDescription(method[1].__doc__)))
        lines.append("\n")
        '''
        for method in methods:
            print method[1].__doc__
        '''
        
    print "======="
    out = "test_doc_"+str(time.ctime()).replace(":", "-")+".md"
    with open("DOC TESTS"+os.path.sep+out, 'w') as f:
        f.writelines(lines)
    print "Wrote: "+str(out)


if __name__ == "__main__":
    create_docs()
else:
    raise NotAModule(str(__name__)+" is not a module!")