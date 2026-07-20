'''COFFEE MACHINE REQUIREMENTS
1. Ask from user for coffee type by prompting:
"What would you like to have?(Latte/Expresso/cappuccino)."
once the drink is dispensed this prompt should be show to serve the next customer.

2.When user enters "report" as an input then a report should be generated that shows the current resources value.
  e.g: Water = 200ml
       Milk = 50ml
       Coffee = 75g
       Money = Rs. 150

3. If user enters "off" as an input then your program should end execution.
4. check sufficient resources are available or not.
5. If sufficient resources are available then machine should ask to insert coins and calculate total money received.
[Coffee Machine only accept 5rs. 10rs. Coins 20rs.]
6.Check payment is successful or not
  If user had entered sufficient money,the cost of drink gets added to the machine as profit.
  If user has entered too much money,machine should offer change to the user
  if money is not sufficient to purchase the drink user has selected, it should print a message "Sorry That's not enough money.Money refunded"
7.Make Coffee
  if payment is successful,ingredients to make the selected deink should be deducted from the coffee machne resource. And it will print a message "Here is your Cappuccino."(if cappuccino was their choice)  

'''
Menu = {
    "Latte":{
    "ingredients":{
        "water":200,
        "milk":150,
        "coffee":24,
    },
    "cost":150
    },
    "Espresso":{
        "ingredients":{
            "water":50,
            "coffee": 18,
        },
        "cost": 100,
    },
    "Cappuccino":{
        "ingredients":{
        "water": 250,
        "milk": 100,
        "coffee": 24,
    },
    "cost": 200,
    }
}    



profit = 0
resources = {
    "water":500,
    "milk" :200,
    "coffee":100,
}
def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item]>resources[item]:
            print(f"sorry there is not enough {item}")
            return False
    return True    
def process_coins():
    print("Please insert coins.")
    total = 0
    coins_five=int(input("How many 5rs coin?: "))
    coins_ten=int(input("How many 10rs coin?: "))
    coins_twenty=int(input("How many 20rs coin?: "))
    total=coins_five*5 + coins_ten*10 + coins_twenty*20
    return total
    
is_on = True
while is_on:
    choice = input("What would you like to have?(Latte/Espresso/cappuccino).")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water={resources['water']}ml")
        print(f"Milk={resources['milk']}ml")
        print(f"Coffee={resources['coffee']}g")
        print(f"Money=Rs{profit}")
    else:
        coffee_type = Menu[choice]
        print(coffee_type)
        if check_resources(coffee_type['ingredients']):
            payment=process_coins()
            # 26 min se video 87