#offline version of the api thats in github
#nteractible script
"""requirement: should run forever untill user press quit
the user should be able to purchase avavlible shoes from store
the avalkible shoes should be pre defined by me.
user should be able to sell their shoes on the store.
user shopuld be able to see all of their shoes that they purchased."""







print('Welcome To Shoestore!')
print('Here you can purchase and sell any amount of shoes. ')

brands = [ 'Nike', 'Adidas', 'VANS', 'Timberlands', 'Jordans']

while True:

    print('to view shoes eneter "View" ') 
    print('to Buy shoes enter "Buy" ')
    print('to sell Shoes enter "Sell" ')
    print('to quit application enter "quit" ')

   
    choice = input()
    
    if choice == 'view':
        list_brands = ' | '.join(brands)
        print(list_brands)
        continue
    elif choice == 'buy': 
        # logic for buy.
        print('what brand do you want to purchase: ')
        choice = input()
        if choice in brands:
            print('Are you sure you want to purchase?: ')
            choice = input()
            if choice == 'yes':
                print('purchase successful! ')
            else:
                print('pruchase cancelled')
        else:
            print('brand not found')
    elif choice == 'sell':
        #logic for sell.
        print('What brand do you want to sell?: ')
        choice = input()
        if choice in brands:
            print('Brand found! ')
            print('sell item? ')
            choice = input()
            if choice == 'yes':
                print('Item posted to Market')
            else:
                print('Ticket aborted')
        else:
            print('brand not found')    
    elif choice == 'quit':
        quit()
    else:
        print('command not recongnized')

        
    
    
   
    



   

   









# brands = 'Nike'
# choice = input('what is a brand that you are seartching for:')

# while choice != brands:
#     choice = input('selection not found - try again. Find brand:') 

# print('brand found')


 



