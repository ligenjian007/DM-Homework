import sets

def apriori(transactionData,minSupport):
    """
    input:
        transactionData: a map from title to a set of items.
        minSupport: a number that is required to be met
    """
    l=[]
    l.append(findFrequentOneItems(transactionData))
    k=0
    while len(l[k])!=0:
        itemSetCount={}
        newItemSet=aprioriGen(l[k],transactionData)
        newItemSetToBeAdd=[]
        for transaction in newItemSet:
            itemSetCount[transaction]=subsetCount(transaction,transactionData)
            if itemSetCount[transaction]>=minSupport:
                newItemSetToBeAdd.append(transaction)
        if len(newItemSetToBeAdd)==0:
            return l[k]
        k=k+1
        l.append(newItemSetToBeAdd)
        
def findFrequentOneItems(data):
    """
    to find the items that in the data map
    """
    frequentOneSet=[]
    for key in data:
        for item in data[key]:
            if item not in tuple(frequentOneSet):
                frequentOneSet.append((item,))
    return tuple(frequentOneSet)

def aprioriGen(itemSetLevelK,data):
    """
    Generate item set from level K to level K+1 with a given set and a 
    data map.
    """
    itemSetLevelKPlus=[]
    lengthK=len(itemSetLevelK[0])
    for itemLevelK1 in itemSetLevelK:
        for itemLevelK2 in itemSetLevelK:
            if itemLevelK1==itemLevelK2:
                continue
            newItemSet=linkItems(itemLevelK1,itemLevelK2)
            if len(newItemSet)==lengthK+1 and IsValid(newItemSet,data):
                included=False
                for itemSets in itemSetLevelKPlus:
                    if sets.Set(itemSets).issuperset(sets.Set(newItemSet)) and sets.Set(itemSets).issubset(sets.Set(newItemSet)) :
                        included=True
                if not included:
                    itemSetLevelKPlus.append(newItemSet)
    return itemSetLevelKPlus

def linkItems(item1,item2):
    """
    only to find the union of two sets, before I find that sets library may 
    be better.
    """
    newItemSet=[]
    for each in item1:
        if each not in tuple(newItemSet):
            newItemSet.append(each)
    for each in item2:
        if each not in tuple(newItemSet):
            newItemSet.append(each)
    return tuple(newItemSet)

def IsValid(itemSet,data):
    """
    To judge the new itemSet is a valid subset of the data
    """
    setItem=sets.Set(itemSet)
    for key in data:
        if setItem.issubset(sets.Set(data[key])):
            return True
    return False

def subsetCount(itemSet,data):
    """
    count of itemSet that appears in data map
    """
    setItem=sets.Set(itemSet)
    count=0
    for key in data:
        if setItem.issubset(sets.Set(data[key])):
            count=count+1
    return count

import itertools

def findSubsets(S,m):
    return set(itertools.combinations(S, m))

def findAllTrueSubsetsWithNull(S):
    subsets=[]
    for i in range(1,len(S)):
        subsets+=findSubsets(S,i)
    return subsets

def generateAssociationRules(frequentSets,minConfidence,data):
    rules=[]
    for frequentItem in frequentSets:
        subsets=findAllTrueSubsetsWithNull(frequentItem)
        for priorSet in subsets:
            inferredSet=set(frequentItem)-set(priorSet)
            confidence=float(subsetCount(frequentItem,data))/float(subsetCount(priorSet,data))
            if confidence>=minConfidence:
                rules.append((tuple(priorSet),tuple(inferredSet),confidence))
    return rules