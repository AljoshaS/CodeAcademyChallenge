#Give me the discount
#Create a function in Python that accepts two parameters. The first should be the full price of an item as an integer. 
#The second should be the discount percentage as an integer.
#The function should return the price of the item after the discount has been applied. For example, if the price is 100 and the discount is 20, the function should return 80.

def discount(price,discount_percentage):
    result1=discount_percentage*price
    result2=result1/100
    result=price-result2
    print("Your price after discount is {}".format(result))

discount(450,20) #example