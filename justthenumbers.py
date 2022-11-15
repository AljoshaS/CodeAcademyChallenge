#Just the numbers
#Write a function in Python that accepts a list of any length that contains a mix of non-negative integers and strings. 
#The function should return a list with only the integers in the original list in the same order.

def justthenumbers(*elements):
    list=[]
    for i in elements:
        if isinstance(i,int):
            list.append(i)
    print(list)

justthenumbers(5,4,8,"list") #example