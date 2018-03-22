import uuid

menu = {
    'Appetizers': {
        'Wings': [8.00, 0],
        'Spring Rolls': [5.00, 0],
        'Cookies': [2.00, 0],
        'Grilled Squid': [8.00, 0],
        'Crab Wonton': [6.00, 0],
        'Satay': [7.00, 0]
    },
    'Entrees': {
        'Salmon': [15.00, 0],
        'Steak': [20.00, 0],
        'Meat Tornado': [25.00, 0],
        'A Literal Garden': [12.00, 0],
        'Pad Thai': [10.00, 0],
        'Spicy Meatballs': [12.00, 0]
    },
    'Desserts': {
        'Ice Cream': [6.00, 0],
        'Cake': [6.00, 0],
        'Pie': [7.00, 0],
        'Mango with Sicky Rice': [6.00, 0],
        'Mushroom Yogurt': [5.00, 0],
        'Popsicle': [3.00, 0]
    },
    'Drinks': {
        'Coffee': [3.00, 0],
        'Tea': [2.00, 0],
        'Blood of the Innocent': [50.00, 0],
        'Champagne': [8.00, 0],
        'Martini': [11.00, 0],
        'Italian Lemondrop': [10.00, 0]
    },
    'Sides': {
        'Bread': [2.00, 0],
        'Hot Peppers': [1.00, 0],
        'Potatoes': [3.00, 0],
        'Bacon': [5.00, 0],
        'Apples': [1.00, 0],
        'Rice': [4.00, 0]
    }
}

user_order = {}


def welcome_message():
    welcome = print('**************************************\n\
** Welcome to the Snakes Cafe! **\n\
** Please see our menu below. **\n\
** To quit at any time, type "quit" **\n\
**************************************')
    return welcome


def print_menu():
    return_value = ''
    for key, value in menu.items():
        print('\n{}\n----------\n' .format(key))
        '''
        Input from the user for menu item
        '''
        for item, price in value.items():
            item_str = item.ljust(20)
            price_str = ('$' + str(price[0]) + '0').rjust(15)
            new_str = item_str + price_str
            print(new_str)
            return_value += '{}: ${p:0.2f}\n' .format(item, p=price[0])
    return return_value


def get_user_input():
    '''
    Input from the user for menu item
    '''
    return input('***********************************\n\
** What would you like to order? ''**\n\
***********************************\n->')


def exit_program():
    exit(0)


# def check_menu(input_in, answers):
#     for answer in answers:
#         if input_in in [item.lower() for item in answer]:
#             return True

def check_user_input():
    user_input = input('->')
    if user_input == 'quit':
        print('Order Complete')
        exit_program()
    elif user_input == 'order':
        print(print_order(user_order))
    else:
        add_order(user_input)
    return user_input


def print_order(user_order):
    order_summary = 'Order #{}\n'.format(uuid.uuid4())
    for item, quantity in user_order.items():
        for category in menu.values():
            import pdb; pdb.set_trace()
            if item in item.lower() for item in menu[course]]category:
                order_summary += '\n{}: {} total: {}'.format(item, quantity, category)
    return order_summary


def add_order(item):
    for course in menu:
        if item in [item.lower() for item in menu[course]]:
            if item in user_order:
                user_order[item] = user_order[item] + 1
            else:
                user_order[item] = 1
            print('{} has been added to your order' .format(item))
            return item


def remove_item(item):
    if item in user_order:
        user_order[item] -= 1
        if user_order[item] == 0:
            del user_order[item]
            print('{} has been removed from your order' .format(item))
        else:
            print('{} not found' .format(item))


def main():
    welcome_message()
    print_menu()
    # get_user_input()

    while True:
        user_input = check_user_input()
        if user_input is None:
            print('Not on the Menu. Try again...')
            continue

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass