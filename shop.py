####################### DO NOT MODIFY THIS CODE ########################
menu = {
    "original cupcake": 2,
    "signature cupcake": 2.750,
    "coffee": 1,
    "tea": 0.900,
    "bottled water": 0.750
}
original_flavors = ["vanilla", "chocolate", "strawberry", "caramel", "raspberry"]
original_price = 2
signature_price = 2.750

############################# Start Here! ##############################
cupcake_shop_name = "CakeCups" #complete me!
signature_flavors = ["saffron", "oreo", "twix", "popcorn", "bubble gum"] #complete me!
order_list = []


def print_menu():
    """
    Print the items in the menu dictionary.
    """
    # your code goes here!
    print ("The menu includes the below items:")
    for item in menu:
        print (" - ", item, "=", menu[item], "KD")



def print_originals():
    """
    Print the original flavor cupcakes.
    """
    print("Our original flavor cupcakes (KD %s each):" % original_price)
    # your code goes here!
    for item in original_flavors:
        print (" - ", item)


def print_signatures():
    """
    Print the signature flavor cupcakes.
    """
    print("Our signature flavor cupcake (KD %s each):" % signature_price)
    # your code goes here!
    for item in signature_flavors:
        print (" - ", item)


def is_valid_order(order):
    """
    Check if an order exists in the shop.
    """
    # your code goes here!
    if order in menu:
        return True
    elif order in original_flavors:
        return True
    elif order in signature_flavors:
        return True
    else:
        return False


def get_order():
    """
    Repeatedly ask customer for order until they end their order by typing "Exit".
    """
    order_list = []
    # your code goes here!
    print ("What is your order? To end you order please type in 'Exit'")
    order = " "
    while order != "Exit":
        order = input().lower()
        if order == "exit":
            return order_list
            break
        elif order == "original cupcake" or order == "signature cupcake":
            print ("Please write in a flavor of cupcake")
        else:
            if is_valid_order(order) == True:
                order_list.append(order)
            else:
                print (order + " not on menu, please order something else.")


def accept_credit_card(total):
    """
    Return whether an order is eligible for credit card payment.
    """
    # your code goes here!
    if total >= 5:
        print ("This order is eligible for credit card payment.")
    else:
        print ("This order is NOT eligible for credit card payment and must be paid in cash.")

def get_total_price(order_list):
    """
    Calculate and return total price of the order.
    """
    total = 0
    # your code goes here!
    for item in order_list:
        if item in menu:
            total = total + menu[item]
        elif item in original_flavors:
            total = total + menu["original cupcake"]
        elif item in signature_flavors:
            total = total + menu["signature cupcake"]
    return total


def print_order(order_list):
    """
    Print the order of the customer.
    """
    print()
    print("Your order is: ")
    # your code goes here!
    for item in order_list:
        print (item)
    total = get_total_price(order_list)
    print ("The price of the order is " + str(total) + " KD")
    accept_credit_card(total)
    print ("Thank you for ordering at CakeCups.")





