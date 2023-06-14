# wap to print goodafternoon with input name 
a="Goodafternoon "
b=input("enter the name ")
print(a+b)


# wap to fill the template of a letter as given below
# letter= '''dear <name>
#            you are selected!
#            <date>'''
letter= '''dear <name>
you are selected!
<date>''' 
name=input("enter name ")
date=input("enter date ")
letter=letter.replace("<name>",name)
letter=letter.replace("<date>",date)
print(letter)


# wap to create double spaces in a  string 
story="this is the variable to check double  space"
doublespace=story.find("  ")
print(doublespace)  

# replace 
story=story.replace("  "," ")
print(story)