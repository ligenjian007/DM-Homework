import Apriori

transSet={}
transSet['T100']=(1,2,5)
transSet['T200']=(2,4)
transSet['T300']=(2,3)
transSet['T400']=(1,2,4)
transSet['T500']=(1,3)
transSet['T600']=(2,3)
transSet['T700']=(1,3)
transSet['T800']=(1,2,3,5)
transSet['T900']=(1,2,3)

print Apriori.apriori(transSet, 2)