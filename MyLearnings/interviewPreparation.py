
#Demonstrate Remove empty List

testlist = ['abc', 6, [4,5], 3.6, [], (5,6),(), 9]
arr =list(val for i, val in enumerate(testlist) if type(val) != [])
print(arr)




import copy
testlist = ['abc', 6, [4,5], 3.6, [], (5,6),(), 9]



print("========Deep Copy ===")
arrD = copy.deepcopy(testlist) 
print(testlist,id(testlist)) #['abc', 6, [4, 5], 3.6, [], (5, 6), (), 9] 140437476291136
print(arrD,id(arrD)) #['abc', 6, [4, 5], 3.6, [], (5, 6), (), 9] 140437476294336
arrD[0]='LLL'
print(arrD,id(arrD)) #140086086021824
print(testlist,id(testlist)) #140086086021824



print("========Shallow Copy ===")

arrS = copy.copy(testlist)
print(testlist,id(testlist)) #['abc', 6, [4, 5], 3.6, [], (5, 6), (), 9] 140445595579072
print(arrS,id(arrS)) #['abc', 6, [4, 5], 3.6, [], (5, 6), (), 9] 140445595582272
arrS[0]='mmM'
print(arrS,id(arrS)) #140086086021824
print(testlist,id(testlist)) #140086086021824

print("========equal ===")
arr = testlist
print(id(testlist)) #140086086021824
print(id(arr)) #140086086021824
arr[0]='xyz'
print(arr,id(arr)) #140086086021824
print(testlist,id(testlist)) #140086086021824





# find occurance

import copy
ll = [1,2,5,4,6,7,3,4,5,3,2,4,5,6,7,8,3,4.6,4,]
m=0
fnd =4
cnt= {itm:ll.count(itm) for itm in ll}

print(cnt.get(3))





#  Break a list into chunks of size N in Python using List comprehension

import numpy as np
my_list = ['geeks', 'for', 'geeks', 'like',
           'geeky','nerdy', 'geek', 'love',
               'questions','words', 'life']
ln = len(my_list)
res_lst =np.array_split(my_list,int(round(ln/4)))
print(res_lst)

# Python program for the above approach

S = "hello geeks for geeks is computer science portal"
K = 5
S = S.split(" ")
cnt = list(filter(lambda x:len(x)>K,S))
print(cnt)

# Program to add two matrices
# using zip()

import numpy as np
X = [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]
  
Y = [[9,8,7],
    [6,5,4],
    [3,2,1]]

Z = np.array(X)+np.array(Y)
print(Z)





# Python3 program to find a list of uncommon words
from collections import Counter
def uncommon(st1,st2):
    st1 = st1.split(" ")
    st2 = st2.split(" ")
    res = []
    cnt_wd1 = Counter(st1)
    cnt_wd2 = Counter(st2)
    
    for key in cnt_wd1:
        if key not in cnt_wd2:
            res.append(key)
    for key in cnt_wd2:
        if key not in cnt_wd1:
            res.append(key)
    print(res)
    

sentence1 = "hello geeks for geeks is computer science portal"
sentence2 = "this is geeks application for learning"
uncommon(sentence1,sentence2)