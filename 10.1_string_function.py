story="do you know vaishnavi is the most prettiet girl that i'd ever saw in my life with the most humble,polite,soft hearted personality.sometimes she gets rude but its in her nature.she's always real and never fake her personality.she cares about others.she dont know how to say no to people.people around her are smart enough.she aint a good manupulator.you will enjoy her company.shes funny and intellectual.always on her phone.shes learning new things nowadays and trying to match others.shes childish.she want to become mature.she is insecure about herself and less confident.she gets manupulated very easily.but however she will become a what she wants to.i have a firm believe in her.shes the the best person and people like such personalities"
print(len(story))
print(story.endswith("personalities"))
print(story.count("on"))
print(story.count("and"))
print(story.capitalize()) #-->this function will capatilize the first word of the string
print(story.find("intellectual")) #-->this will say the index no. of the index
print(story.find("yoyo"))  #-->whenever the element is not present in the string then the output will always be -1
# when the occurance of element is more than 1 then it will only show the index of first occurance of that element
print(story.replace("vaishnavi","prettyvaish")) #-->syntax:("old word","new word")   #replaces all the words with the new word

greet="   hello   "
print(greet)
print(greet.strip())    #--->Removes extra space from the string