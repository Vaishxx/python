#we can raise custom error using the raise keyword in py
def increment(num):
    try:
        return int(num)+1
    except:
        print("bhai shi value dal le chup chap...chpri giri mt kreee")
a=increment('eqf243r')    
print(a)    