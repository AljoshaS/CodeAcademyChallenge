#Count the vowels in a string
#Create a function in Python that accepts a single word and returns the number of vowels in that word. 
#In this function, only a, e, i, o, and u will be counted as vowels — not y.

#Count with loop
def countvowels(word):
    vowels=["a","e","i","o","u","A","E","I","O","U"]
    count=0
    for i in word:
        if i in vowels:
            count+=1
    print("Number of vowels in a string is : {}".format(count))

countvowels("aaaa") #example

#Count with List Comprehension
def countvowels2(word):
    count=len([letter for letter in word if letter in "aeiouAEIOU"])
    print("Number of vowels in a string is : {}".format(count))

countvowels2("aaaa") #example

