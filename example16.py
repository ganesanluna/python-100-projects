#example16.py sorted on string
a = str(input("enter your quotes : "))      #1
words = a.split()                           #2
words.sort()                                #3
print("The sorted words are:")              #4
for word in words:                          #5
   print(word)                              #6
