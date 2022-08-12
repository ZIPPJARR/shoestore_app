"""requirement: should run forever untill user press quit
the user should be able to purchase avavlible shoes from store
the avalkible shoes should be pre defined by me.
user should be able to sell their shoes on the store.
user shopuld be able to see all of their shoes that they purchased."""

print('Welcome To Shoestore!')
print('Here you can purchase and sell your shoes. ')

brands = [ 'Nike', 'Adidas', 'VANS', 'Timberlands', 'Jordans']
user_cart = {'Nike':0, 'Adidas':0, 'VANS':0, 'Timberlands':0, 'Jordans':0}

def view_func():
    for i in user_cart:
        print(i + ' : ' + str(user_cart[i]))

def buy_func():
    print('what brand do you want to purchase: ')
    choice = input()
    if choice in brands:
        print('Are you sure you want to purchase?: ')
        yes_or_no = input()
        if yes_or_no == 'yes':
            print('purchase successful! ')
            user_cart[choice] += 1
        else:
            print('pruchase cancelled')
    else:
        print('brand not found')

def sell_func():
    print('What brand do you want to sell?: ')
    choice = input()
    if choice in brands:
        print('Brand found! ')
        print('sell item? ')
        yes_or_no = input()
        if yes_or_no == 'yes':
            print('amount of items you want to sell:')
            user_cart[choice] -= max(user_cart[choice] - int(input()), 0)
            for i in user_cart:
                print(i + ' : ' + str(user_cart[i]))
                print('showing amount sold')
        else:
            print('Ticket aborted')
    else:
        print('brand not found') 

def quit_func():
    quit()

while True:
    print('to view shoes eneter "View" ') 
    print('to Buy shoes enter "Buy" ')
    print('to sell Shoes enter "Sell" ')
    print('to quit application enter "quit" ')

    choice = input()
    if choice == 'view':
        view_func()
        
    elif choice == 'buy': 
       buy_func()

    elif choice == 'sell':
       sell_func()  

    elif choice == 'quit':
        quit_func()