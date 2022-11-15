#Are the Xs equal to the Os?
#Create a Python function that accepts a string. This function should count the number of Xs and the number of Os in the string. 
#It should then return a boolean value of either True or False.
#If the count of Xs and Os are equal, then the function should return True. If the count isn't the same, it should return False. 
#If there are no Xs or Os in the string, it should also return True because 0 equals 0. The string can contain any type and number of characters.

def count(x):
    charx=["x","X"]
    charo=["o","O"]
    count1=0
    count2=0
    for i in x:
        if i in charx:
            count1+=1
    print(count1)
    for y in x:
        if y in charo:
            count2+=1
    print(count2)
    if count1==count2:
        first=True
        print(bool(first))
    elif count1!=count2:
        second=False
        print(bool(second))
    elif i not in charx and y not in charo:
        third=True
        print(bool(third))

count("kkk")
