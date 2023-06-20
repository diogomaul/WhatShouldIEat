import random
import datetime
import os

snacks_file = 'snacks.txt'
dinner_file = 'dinner.txt'
takeOut_file = 'takeOut.txt'

snacks = ['Banana and Granola', 'Nuts', 'Mini Carrots and Hummus', 'Popcorn', 'cookies', 'any fruit']
dinner = ['Crepioca', 'Tuna Wrap', 'Hamburguer Flights']
takeOut = ['Domino\'s', 'Papi Shawarma', 'Burguer Priest', 'Mandarim 2 Go']

if not os.path.exists(snacks_file):
    with open(snacks_file, 'w') as f:
        for snack in snacks:
            f.write(snack + '\n')

if not os.path.exists(dinner_file):
    with open(dinner_file, 'w') as f:
        for dish in dinner:
            f.write(dish + '\n')

if not os.path.exists(takeOut_file):
    with open(takeOut_file, 'w') as f:
        for restaurant in takeOut:
            f.write(restaurant + '\n')

with open(snacks_file, 'r') as f:
    snacks = f.read().splitlines()

with open(dinner_file, 'r') as f:
    dinner = f.read().splitlines()

with open(takeOut_file, 'r') as f:
    takeOut = f.read().splitlines()

now = datetime.datetime.now()
hour = now.hour

option = input ('what do you want to do? (getSuggestion/addItem/removeItem/listItems)')

if option == 'listItems':
    list_name = input('Which list do you want to see? (snacks/dinner/takeOut)')
    if list_name == 'snacks':
        print('Snacks:')
        for snack in snacks:
            print(snack)
        option = input ('what do you want to do? (getSuggestion/addItem/removeItem/listItems)')
    elif list_name == 'dinner':
        print('Dinner:')
        for dish in dinner:
            print(dish)
        option = input ('what do you want to do? (getSuggestion/addItem/removeItem/listItems)')
    elif list_name == 'takeOut':
        print('Take Out:')
        for restaurant in takeOut:
            print(restaurant)
        option = input ('what do you want to do? (getSuggestion/addItem/removeItem/listItems)')

if option == 'addItem':
    list_name = input('Which list do you want to add to? (snacks/dinner/takeOut)')
    new_option = input('Enter the new option: ')

    if list_name == 'snacks':
        snacks.append(new_option)
        with open(snacks_file, 'a') as f:
            f.write(new_option + '\n')
    elif list_name == 'dinner':
        dinner.append(new_option)
        with open(dinner_file, 'a') as f:
            f.write(new_option + '\n')
    elif list_name == 'takeOut':
        takeOut.append(new_option)
        with open(takeOut_file, 'a') as f:
            f.write(new_option + '\n')
    print('New option added to the ' + list_name + ' list: ' + new_option)

elif option == 'removeItem':
    list_name = input('Which list do you want to remove from? (snacks/dinner/takeOut)')
    remove_option = input('Enter the option you want to remove: ')

    if list_name == 'snacks':
        snacks.remove(remove_option)
        with open(snacks_file, 'w') as f:
            for snack in snacks:
                f.write(snack + '\n')   
    elif list_name == 'dinner':
        dinner.remove(remove_option)
        with open(dinner_file, 'w') as f:
            for dish in dinner:
                f.write(dish + '\n')
    elif list_name == 'takeOut':
        takeOut.remove(remove_option)
        with open(takeOut_file, 'w') as f:
            for restaurant in takeOut:
                f.write(restaurant + '\n')
    print('Option removed from the ' + list_name + ' list: ' + remove_option)

elif option == 'getSuggestion':
    if hour < 18:
        suggestion = random.choice(snacks)
        print ('You should eat a ' + suggestion)
    else:
        print( 'It\'s past 6 pm, time for dinner!')
        option = input('Do you feel like cooking? (y/n)')

        if option == 'y':
            suggestion = random.choice(dinner)
            print ('You should cook ' + suggestion + ' for dinner!')
        else:
            suggestion = (random.choice(takeOut))
            print ('You should order ' + suggestion + ' for dinner!')
                
print('Goodbye!')