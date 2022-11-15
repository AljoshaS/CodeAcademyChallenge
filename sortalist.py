#Sort a list
#Create a function in Python that accepts two parameters. The first will be a list of numbers. 
#The second parameter will be a string that can be one of the following values: asc, desc, and none.
#If the second parameter is "asc," then the function should return a list with the numbers in ascending order. 
#If it's "desc," then the list should be in descending order, and if it's "none," it should return the original list unaltered.

def sortalist(*list_elements,y):
    list=[]
    if y=="desc":
        for x in list_elements:
            list.append(x)
            list.sort(reverse=True)
        print(list)
    elif y=="asc":
        for x in list_elements:
            list.append(x)
            list.sort()
        print(list)
    elif y=="none":
        for x in list_elements:
            list.append(x)
        print(list)

sortalist(5,7,50,10, y="none") #example


