import treePredict
import re
import formalize

data=[formalize.formalize(line.split('\t')) for line in file('data.txt')]

print treePredict.giniimpurity(data[1:])
print treePredict.entropy(data[1:])

tree=treePredict.buildTree(data[1:])
treePredict.printTree(tree)