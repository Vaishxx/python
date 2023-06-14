#this function adds counter an iterable and returns it
list1=['vaish',21,False,2.2,00]
index=0
# for item in list1:
#     print(item,'index no.:',index)
#     index +=1

for index ,item in enumerate(list1):  #does the same work as the above comment
    print(item,index)