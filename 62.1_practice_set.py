#wap to print third,fifth,seventh element from a list using enumeration function
list1=['one','two','three','four','five','six','seven','eight']
index=0

for index,item in enumerate(list1):
    if item=='three'or item=='five'or item=='seven':
        print(index,item)