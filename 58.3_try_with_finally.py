#python offers a finaaly clause which ensues execution of a piece of code irrespective of the exception
try:
    i=int(input('enter a no.'))
    c=1/i

except Exception as e:
    print(e)
    exit()
    
finally: #------------>runs regardless of error ,aur agr except ne program ko exit bhi lr diya tb bhi chlega yeto
    print('we are done')

print('thanks for using this program')  
#jb exit hogya exception se to sirf finally wala code run hoga pr baki ka code nhi hoga  
