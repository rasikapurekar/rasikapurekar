items={1:"samosa",2:"tea",3:"poha",4:"kachori",5:"idali",6:"vadapav"}
price={1:20,2:10,3:25,4:15,5:30,6:15}
it=[]
qu=[]

# items: Dictionary containing item numbers as keys and item names as values.
# price: Dictionary containing item numbers as keys and their respective prices as values.
# it: An empty list to store selected item numbers.
# qu: An empty list to store quantities corresponding to selected items.

print("-"*100)
print("\t\t\t\t\tTaj Hotel")
print("-"*100)

# Prints a header for the restaurant

while True:
    print("""
            MENU CARD
        1.samosa     4.kachori
        2.tea        5.idali
        3.poha       6.vadapav
    """)
    print("-"*100)

    # Displays a menu with item numbers, names, and prompts the user for input

    i=eval(input("enter items number from menu: "))
    q=eval(input("quantity: "))
    it.append(i)
    qu.append(q)
    ch=input("do you want to continue: ").lower()

# Takes user input for item number (i) and quantity (q).
# Appends the item number and quantity to the respective lists (it and qu).
# Asks the user if they want to continue ordering

    if ch=="n":
        print("-"*85)
        print("|{:^20}|{:^20}|{:^20}|{:^20}|".format("NAME","QUANTITY","PRICE","AMOUNT"))
        print("-"*85)
        sum=0
        for i in range(len(it)):
            print("|{:^20}|{:^20}|{:^20}|{:^20}|".format(items[it[i]],qu[i],price[it[i]],qu[i]*price[it[i]]))
            print("-"*85)
            sum=sum+qu[i]*price[it[i]]
        print("Your total amount is",sum ,"rs")
        break
 
# If the user chooses not to continue (ch == "n"), it displays a table with the selected items, quantities, prices, and total amount.
# Exits the loop using break


