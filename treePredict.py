class DecisionNode:
    
    def __init__(self,col=-1,value=None,results=None,trueBranch=None,falseBranch=None):
        self.col=col
        self.value=value
        self.results=results
        self.trueBranch=trueBranch
        self.falseBranch=falseBranch
    """
    just to define a node structure to store the entire tree
    """
    
def divideSet(rows,column,value):
    splitFunction=None
    if isinstance(value,int) or isinstance(value,float):
        splitFunction=lambda row:row[column]>=value
    else:
        splitFunction=lambda row:row[column]==value
    set1=[row for row in rows if splitFunction(row)]
    set2=[row for row in rows if not splitFunction(row)]
    return (set1,set2)

def uniqueCounts(rows):
    results={}
    for row in rows:
        r=row[len(row)-1]
        #for the last item is the item to be decided
        if r not in results: results[r]=0
        results[r]+=1
    return results

import math

def giniimpurity(rows):
    total=len(rows)
    counts=uniqueCounts(rows)
    imp=1
    for k in counts:
        imp-=math.pow(float(counts[k])/total,2)
    return imp

def entropy(rows):
    log2=lambda x:math.log(x)/math.log(2)
    results=uniqueCounts(rows)
    ent=0.0
    for r in results.keys():
        p=float(results[r])/len(rows)
        ent=ent-p*log2(p)
    return ent

def buildTree(rows,scoreFunction=entropy):
    if len(rows)==0: return DecisionNode()
    currentScore=scoreFunction(rows)
    bestGain=0.0
    bestCriteria=None
    bestSets=None
    
    columnCount=len(rows[0])-1
    for col in range(0,columnCount):
        columnValues={}
        for row in rows:
            columnValues[row[col]]=1
        
        for value in columnValues.keys():
            (set1,set2)=divideSet(rows,col,value)
            p=float(len(set1)/len(rows))
            gain=currentScore-p*scoreFunction(set1)-(1-p)*scoreFunction(set2)
            if gain>bestGain and len(set1)>0 and len(set2)>0:
                bestGain=gain
                bestCriteria=(col,value)
                bestSets=(set1,set2)
    if bestGain>0:
        trueBranch=buildTree(bestSets[0])
        falseBranch=buildTree(bestSets[1])
        return DecisionNode(col=bestCriteria[0],value=bestCriteria[1],
                            trueBranch=trueBranch,falseBranch=falseBranch)
    else:
        return DecisionNode(results=uniqueCounts(rows))
    
def printTree(tree,indent=''):
    if tree.results!=None:
        print str(tree.results)
    else:
        print str(tree.col)+':'+str(tree.value)+'?'
        print indent+'T->',
        printTree(tree.trueBranch,indent+' ')
        print indent+'F->',
        printTree(tree.falseBranch,indent+' ')