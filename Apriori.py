import sets

def apriori(transactionData,minSupport):
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
    frequentOneSet=[]
    for key in data:
        for item in data[key]:
            if item not in tuple(frequentOneSet):
                frequentOneSet.append(item)
    return tuple(frequentOneSet)

def aprioriGen(itemSetLevelK,data):
    itemSetLevelKPlus=[]
    if type(itemSetLevelK[0])==type(0):
        lengthK=1
    else:
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
    newItemSet=[]
    if type(item1)==type(0):
        return (item1,item2)
    for each in item1:
        if each not in tuple(newItemSet):
            newItemSet.append(each)
    for each in item2:
        if each not in tuple(newItemSet):
            newItemSet.append(each)
    return tuple(newItemSet)

def IsValid(itemSet,data):
    setItem=sets.Set(itemSet)
    for key in data:
        if setItem.issubset(sets.Set(data[key])):
            return True
    return False

def subsetCount(itemSet,data):
    setItem=sets.Set(itemSet)
    count=0
    for key in data:
        if setItem.issubset(sets.Set(data[key])):
            count=count+1
    return count
