#Create a calculator function
#Write a Python function that accepts three parameters. The first parameter is an integer. 
#The second is one of the following mathematical operators: +, -, /, or . The third parameter will also be an integer.
#The function should perform a calculation and return the results. For example, if the function is passed 6 and 4, it should return 24.

def calculator(n1,operator,n2):
    if operator=="+":
        res=n1+n2
    if operator=="-":
        res=n1-n2
    if operator=="*":
        res=n1*n2
    if operator=="/":
        res=n1/n2
    print("The result is {}".format(res))

calculator(10,"*",5) #example