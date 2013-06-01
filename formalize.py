import re
def formalize(line):
    numRe=re.compile(r'[+-]?[0-9]+(.[0-9]+)?')
    intRe=re.compile(r'[+-]?[0-9]+')
    newList=[]
    for item in line:
        if numRe.match(item):
            if intRe.match(item):
                newList.append(int(item))
            else:
                newList.append(float(item))
        else:
            newList.append(item)
    return newList