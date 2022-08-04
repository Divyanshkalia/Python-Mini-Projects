
#COMBOFINDER
#Problem Statement:
#Find all the list of products whose sum-of-price is between 290 and 310.
#ProductList = {p1: 10, p2: 15, p3: 20, p4: 25, p5: 30, p6: 35, p

import random as r

ProductList = {'product1':10, 'product2':15, 'product3':20, 'product4':25, 'product5':30, 'product6':35, 'product7':50,
               'product8':40, 'product9':55, 'product10':60, 'product11':65, 'product12':75, 'product13':70,
               'product14':45}
LowerBound          = 290
UpperBound          = 310
Result  = set()   # Store Result List i.e. list of sets whose sum is between 90 and 210.
Iterations  = 1000    # Number of Iterations

for i in range(Iterations):
  
    SetSize = r.randint(2, len(ProductList)-1) # Select combo size 
    
    ComboList = r.sample(list(ProductList.keys()),SetSize)# Select number of elements from Set
    ComboList.sort()

    ComboSum = sum([ ProductList[i] for i in ComboList])# Sum the products in ComboList
    
    if ComboSum>= LowerBound and ComboSum<= UpperBound:# Check the Sum Between LowerBound and UpperBound
      Result.add(tuple(ComboList))

for r in Result:
	print (r)

print ("\nTotal Sets: ", len(Result), "\n")