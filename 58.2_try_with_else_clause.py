try:
    i=int(input('enter a no.'))
    c=1/i

except Exception as e:
    print(e)
    
else:   #jb try wala code shi kam krega bina exception kiye to else bhi chlega....in short jb try chlega successfully to else bhi chlega
    print('no exception!code is running succesfully!')