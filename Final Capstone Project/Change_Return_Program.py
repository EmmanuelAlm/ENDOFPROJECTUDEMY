"""Change Return Program - The user enters a cost and then the amount of 
money given. The program will figure out the change and the number of
 quarters, dimes, nickels, pennies needed for the change."""
 
in_cost = float(input("Enter the cost of the Item: "))
in_pay = float(input("Enter the amount of money given: "))
 
def change_return(cost,pay):
    if pay < cost:
        print("The amount you pay has to be more or equal to the cost of the item")
    elif pay > cost:
        change = pay - cost 
        print("Your change is {c}".format(c = change))
        
change_return(in_cost,in_pay)