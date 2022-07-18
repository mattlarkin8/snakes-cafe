print("""
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**                                  **
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Cookies
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
""")
#create list of menu items
menu = ["wings", "spring rolls", "salmon", "steak", "meat tornado", "a literal garden",
        "ice cream", "cake", "cookies", "pie", "coffee", "tea", "unicorn tears"]

#create empty meal dictionary
meal = {}

#loop until user quits
quit = False
while not quit:
    # Take user's input
    order = input("> ").lower()

    #Check if user quit
    if order == "quit":
        quit = True

    else:
        #check if user input a valid menu item
        if order not in menu:
            print("Sorry, that's not on the menu. Check your spelling and try again.")

        #Check if order exists in meal. If not, create new property to track that order.
        elif order not in meal:
            meal[order] = 1
            reply = f"** {meal[order]} order of {order} has been added to your meal **"

            print(reply)

        #Increment order number in meal
        else:
            meal[order] += 1
            reply = f"** {meal[order]} order of {order} has been added to your meal **"

            print(reply)

print(f"** Your final order: {meal} **")