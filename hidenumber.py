#Hide the credit card number
#Write a function in Python that accepts a credit card number. It should return a string where all the characters are hidden with an asterisk except the last four. 
#For example, if the function gets sent "4444444444444444", then it should return "4444".

def hidenumber(number):
    x=len(number)
    hidden=x-4
    shown=number[hidden:]
    print("*"*hidden+shown)

hidenumber('4289982640269299')
