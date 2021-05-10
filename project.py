import string
beyond =open(r"Beyond the Wall of Sleep.txt", encoding="utf8")
jane = open(r"Jane Austin’s Pride and Prejudice.txt", encoding="utf8")
book1 =beyond.read().lower()  
book2=jane.read().lower()
#here we make all words in the two text file are in lower case 
book1set=set(book1.translate(str.maketrans('', '', string.punctuation)).split()) 
book2set=set(book2.translate(str.maketrans('', '', string.punctuation)).split())
#here we split words and remove string punctuation 
intersect = book1set.intersection(book2set) #to get simillar words 
print("set of simillar words")
print()
print(intersect) 
print()
print()
print("number of simillar words in two text file ") 
print(len(intersect))