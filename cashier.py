__author__ = 'Joanette'

#Simple tutorial for highschool students part of the ignite CS google initiative#
combo = ""
#total amount of money owed
total = 0
combo_one ="Grilled Cheese"
combo_two = "Red Velvet"
combo_three = "Pizza"
#a list with all the combos ordered
order_list=[]
#initially the user does not want to sign out
sign_out = "N"
restart = "Y" # restart for a new customer!
contOrdering = "Y" #does the current user want to continue ordering?
#prices for combos:
price_of_pizza = 5
price_of_red = 1
price_of_gc = 3
while restart == "Y" or restart == "y":#while the cashier wants to restart
    #begin with an empty order list
    order_list= []
    #total = 0
    total = 0
    contOrdering = "y"
    while contOrdering =="Y" or contOrdering == "y":
        #GUI:
        print( "                    |Welcome to Mc Joa|\n\
                    |Combo #1         |\n\
                    |Grilled Cheese $3|\n\
                    |Combo #2         |\n\
                    |Red Velvet     $1|\n\
                    |Combo #3         |\n\
                    |Pizza          $5|\n\
                    |All combos       |\n\
                    |include a water  |\n\
                    |bottle and fries!|\n" )
        #Prompt the user for the combo number or name
        combo = raw_input("Which combo would you like enter combo number or name: ")
        #Now we have to analyze which combo was choosen with control flow:
        if combo ==combo_one.lower() or combo == "1":
            #if its combo one use the price of grilled cheese:
            total +=(price_of_gc*1.07)
            order_list.append(combo_one)
            #Now print out the current orders!
            print("Your current orders are: ")
            for i in range(len(order_list)):
                print("Order %d: %s" %(i+1,order_list[i]))
            #Now print the total + a 0.07 tax
            print ("Your current total plus tax is "+ str(total))
            #Prompt if they would like to order anything else.
            contOrdering = raw_input("Would you like to make another order? Y/N ")

        elif combo =="Red Velvet" or combo == "2" or combo == "red velvet":
            #if its combo two use the price of red velvet:
            total +=(price_of_red*1.07)
            order_list.append(combo_two)
            #Now print out the current orders!
            print("Your current orders are: ")
            for i in range(len(order_list)):
                print("Order %d: %s" %(i+1,order_list[i]))
            #Now print the total + a 0.07 tax
            print ("Your current total plus tax is " + str(total))
            #Prompt if they would like to order anything else.
            contOrdering = raw_input("Would you like to make another order? Y/N ")

        elif combo == "Pizza" or combo == "3" or combo == "pizza":
            #if its combo three use the price of pizza:
            total +=(price_of_pizza*1.07)
            order_list.append(combo_three)
            #Now print out the current orders!
            print("Your current orders are: ")
            for i in range(len(order_list)):
                print("Order %d: %s" %(i+1,order_list[i]))
            #Now print the total + a 0.07 tax
            print ("Your current total plus tax is " + str(total))
            #Prompt if they would like to order anything else.
            contOrdering = raw_input("Would you like to make another order? Y/N")

        else:
            #if none of the available combos where choosen do this:
            print ("Sorry we don't currently serve that!")
            print ("Your current total plus tax is " + str(total))
            #Prompt if they would like to order anything else.
            contOrdering = raw_input("Would you like to make another order? Y/N ")
    #Ask for the money and cast it to a float to avoid messy unsuported type errors
    money = float(raw_input("How much will you be paying?"))
    change =money - total
    print("your change will be: %.2f"%(change))
    restart = raw_input("Would you like to restart again? Y/N?")
raw_input("Bye Come again soon!!")
