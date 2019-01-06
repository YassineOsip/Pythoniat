import re
#we defined a string sentence
str = "yassine lafkih is a good developer"
#change a string with other string
changeStr = re.sub("yassine" , "imad" , str,1)
print(changeStr)
#find all string with the same pattern
findAll = re.findall("imad" , changeStr)
print(findAll)
# using search
search = re.search("imad" , changeStr)
print(search)
# using match to show if the patter is foud
match = re.match("yassine",str)
print(match)

