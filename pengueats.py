import datetime

# days when a certain animal gets a discount
animal_days = {
"Monday": ("Penguin", 0.10),
"Tuesday": ("Seal", 0.15),
"Wednesday": ("Polar Bear", 0.05),
"Thursday": ("Walrus", 0.20),
"Friday": ("Otter", 0.10),
"Saturday": ("Orca", 0.15),
"Sunday": ("Narwhal", 0.05)
}

# dictionary for def record_preference(animal, fish_type, quantity): and def show_customer_preferences():
customer_preferences = {}

# dictionary and start values for fish
inventory = {
    "salmon": {
        "price": 8.50,
        "fish": [
            {"freshness": "high", "buy_price": 3.00},
            {"freshness": "high", "buy_price": 3.00},
            {"freshness": "average", "buy_price": 2.00},
        ],
    },
    "herring": {
        "price": 4.99,
        "fish": [
            {"freshness": "high", "buy_price": 1.50},
            {"freshness": "low", "buy_price": 0.50},
        ],
    },
    "tuna": {
        "price": 12.00,
        "fish": [
            {"freshness": "high", "buy_price": 5.00},
            {"freshness": "high", "buy_price": 5.00},
            {"freshness": "low", "buy_price": 3.50},
            {"freshness": "average", "buy_price": 4.00},
        ],
    },
    "mackerel": {
        "price": 6.99,
        "fish": [
            {"freshness": "high", "buy_price": 2.00},
            {"freshness": "average", "buy_price": 1.50},
        ],
    },
    "lanternfish": {
        "price": 9.99,
        "fish": [
            {"freshness": "high", "buy_price": 4.00},
            {"freshness": "low", "buy_price": 2.00},
            {"freshness": "average", "buy_price": 3.00},
        ],
    },
    "shrimp": {
        "price": 15.00,
        "fish": [
            {"freshness": "high", "buy_price": 6.00},
            {"freshness": "high", "buy_price": 6.00},
            {"freshness": "average", "buy_price": 5.00},
            {"freshness": "low", "buy_price": 4.50},
        ],
    },
    "pike": {
        "price": 7.50,
        "fish": [
            {"freshness": "high", "buy_price": 3.00},
            {"freshness": "average", "buy_price": 2.50},
            {"freshness": "low", "buy_price": 2.00},
        ],
    },
    "cod": {
        "price": 10.00,
        "fish": [
            {"freshness": "high", "buy_price": 4.50},
            {"freshness": "high", "buy_price": 4.50},
            {"freshness": "average", "buy_price": 4.00},
            {"freshness": "low", "buy_price": 3.50},
            {"freshness": "low", "buy_price": 3.50},
        ],
    },
    "sardine": {
        "price": 5.50,
        "fish": [
            {"freshness": "high", "buy_price": 2.00},
        ],
    },
    "anchovy": {
        "price": 3.99,
        "fish": [
            {"freshness": "high", "buy_price": 1.50},
            {"freshness": "average", "buy_price": 1.00},
        ],
    }
}

#dictionary for recipes
recipes = {
    "Sushi Plate": ["tuna", "salmon"],
    "Fish Stew": ["cod", "herring", "shrimp"],
    "Mediterranean Mix": ["mackerel", "sardine", "anchovy"],
    "Surf Combo": ["shrimp", "cod"],
}

# Sets starting values for revenue, costs (adds up the cost of fish already in stock) and loss.
total_revenue = 0.0
total_fish_cost = 0.0
for fish_type in inventory:
    for fish in inventory[fish_type]["fish"]:
        total_fish_cost = total_fish_cost + fish["buy_price"]
total_waste_value = 0.0
total_discounts_granted = 0.0
order_history = []
purchase_history = []
general_expenses = []
total_general_expenses = 0.0

# Shows the quantity, selling price and average buying pricefor each fish type currently in stock.
def show_inventory():
    print(f"{'Fish Type':<12}{'Quantity':<12}{'Selling Price per Piece (EUR)':<33}{'Average Buying Price (EUR)'}")
    for fish_type in inventory:
        price = inventory[fish_type]["price"]
        stock = inventory[fish_type]["fish"]
        count = len(stock)
        total = 0.0
        for fish in stock:
            total = total + fish["buy_price"]
        if count > 0:
            average = total / count
        else:
            average = 0.0
        print(f"{fish_type:<11} {count:<11} {price:<32} {average:.2f}")

# Shows details about the freshness of each fish type in the inventory.
def show_freshness_details():
    print(f"{'Fish':<12}{'High':<12}{'Average':<12}{'Low'}")
    for fish_type in inventory:
        counts = {"high": 0, "average": 0, "low": 0}
        for fish in inventory[fish_type]["fish"]:
            freshness = fish["freshness"]
            counts[freshness] = counts[freshness] + 1
        print(f"{fish_type:<12}{counts['high']:<12}{counts['average']:<12}{counts['low']}")

# Fish with low freshness can be removed from the stock with this function.
def remove_expired_fish():
    global total_waste_value
    for fish_type in inventory:
        stock = inventory[fish_type]["fish"]
        good_fish = []
        for fish in stock:
            if fish["freshness"] != "low":
                good_fish.append(fish)
            else:
                total_waste_value = total_waste_value + fish["buy_price"]
        inventory[fish_type]["fish"] = good_fish
    
# Fish can be added to the inventory with this function.
def add_fish (fish_type, quantity, buy_price, freshness):
    global total_fish_cost
    if fish_type in inventory:
        for i in range(quantity):
            inventory[fish_type]["fish"].append({"freshness": freshness, "buy_price": buy_price})
        total_fish_cost = total_fish_cost + (quantity * buy_price)
        print(f"{quantity} {fish_type} added to inventory.")
    else:
        print(f"{fish_type} is not a valid fish type in the inventory.")

# Shows the current financial totals: revenue, cost, loss and overall profit (before taxes)
def show_finance_report():
    profit_before_taxes = total_revenue - total_fish_cost - total_general_expenses
    total_expenses = total_fish_cost + total_general_expenses
    print(f"Total revenue: EUR {total_revenue:.2f}")
    print(f"Sum total fish cost and other expenses: EUR {total_expenses:.2f}")
    print(f"Total fish cost: EUR {total_fish_cost:.2f}")
    print(f"Total other expenses: EUR {total_general_expenses:.2f}")
    print(f"Wasted fish cost: EUR {total_waste_value:.2f}")
    print(f"Total discounts granted: EUR {total_discounts_granted:.2f}")
    print(f"Profit before taxes: EUR {profit_before_taxes:.2f}")

# Sells fish, if available, and updates total revenue
def order_fish(fish_type, quantity):
    if fish_type in inventory:
        stock = inventory[fish_type]["fish"]
        if len(stock) >= quantity:
            price = inventory[fish_type]["price"]
            for i in range(quantity):
                stock.pop(0)
                subtotal = price * quantity
            return subtotal
        else:
            print(f"Sorry, only {len(stock)} {fish_type} available - not enough for your order.")
            return 0.0
    else:
        print(f"{fish_type} is not on the menu.")
        return 0.0

# Collects Customer preferences about orders (quantity and fish type) -- add to user interaction section
def record_preference(animal, fish_type, quantity):
    if animal not in customer_preferences:
        customer_preferences[animal] = {}
    if fish_type not in customer_preferences[animal]:
        customer_preferences[animal][fish_type] = 0
    customer_preferences[animal][fish_type] = customer_preferences[animal][fish_type] + quantity

# Shows the collected data about the orders of the different customers
def show_customer_preferences():
    print(f"{'Animal':<12}{'Fish Type':<12}{'Quantity'}")
    for animal in customer_preferences:
        for fish_type in customer_preferences[animal]:
            quantity = customer_preferences [animal][fish_type]
            print(f"{animal:<12}{fish_type:<12}{quantity}")

# Shows which animal gets a discount on which day of the week.
def show_animal_days():
    print(f"{'Day':<12}{'Animal':<12}{'Discount'}")
    for day in animal_days:
        animal, discount = animal_days[day]
        print(f"{day:<12}{animal:<12}{int(discount * 100)}%")

# Shows a history of evry order with timestamp
def show_financial_report_details():
    print("Order history ")
    for order in order_history:
        print(f"{order['timestamp']}   {order['animal']} - discount: {int(order['discount'] * 100)}% - discount EUR: {order['discount_amount']:.2f}   Total: EUR {order['final_total']:.2f}")
        for item in order['items']:
            price_per_piece = item['subtotal'] / item['quantity']
            print(f"{item['quantity']}x {item['fish_type']} @ EUR {price_per_piece:.2f} each - EUR {item['subtotal']:.2f}")
    print("Purchase history")
    for purchase in purchase_history:
        print(f"{purchase['timestamp']}   {purchase['quantity']}x {purchase['fish_type']} ({purchase['freshness']}) from {purchase['supplier']} - EUR {purchase['buy_price']:.2f} each - Total: EUR {purchase['total_cost']:.2f}")
    print("General expenses")
    for expense in general_expenses:
        print(f"{expense['timestamp']}   {expense['description']} - EUR {expense['amount']:.2f}")

# Tracks general business expenses
def add_expense(description, amount):
    global total_general_expenses
    general_expenses.append({
         "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
         "description": description,
         "amount": amount
    })
    total_general_expenses = total_general_expenses + amount
    print(f"Expense recorded: {description} - EUR {amount:.2f}")

# Shows the most frequent customer by day of the week.
def show_top_animal_per_day():
    day_animal_counts = {}
    for order in order_history:
        order_date = datetime.datetime.strptime(order['timestamp'], "%Y-%m-%d %H:%M:%S")
        day = order_date.strftime("%A")
        animal = order['animal']
        if day not in day_animal_counts:
            day_animal_counts[day] = {}
        if animal not in day_animal_counts[day]:
            day_animal_counts[day][animal] = 0
        day_animal_counts[day][animal] = day_animal_counts[day][animal] + 1

    print("Most frequent customer by day:")
    for day in day_animal_counts:
        animals = day_animal_counts[day]
        top_animal = None
        top_count = 0
        for animal in animals:
            if animals[animal] > top_count:
                top_count = animals[animal]
                top_animal = animal
        print(f"{day}: {top_animal} ({top_count} orders)")

# Checks if the current ingredient to make a recipe is in stock
def check_ingredient(recipe_name):
    required_fish = recipes[recipe_name]
    for fish_type in required_fish:
        if fish_type not in inventory:
            return False
        if len(inventory[fish_type]["fish"]) == 0:
            return False
    return True

# Shows which recipes can be made from the current stock.

def suggest_recipe():
    print("Recipes that can be currently made based on available stock")
    for recipe_name in recipes:
        if check_ingredient(recipe_name):
            print(f"- {recipe_name}: needs {recipes[recipe_name]}")    

# User Interaction Section
name = input("Enter your name: ").strip()
employee_code = input("Enter your employee code: ").strip()
print(f"Hello {name} ({employee_code})! Welcome to the PenguEats business management system.")

while True:
    print("1  -  Show inventory")
    print("2  -  Show freshness details")
    print("3  -  Remove expired fish")
    print("4  -  Add fish to the inventory")
    print("5  -  Create an order")
    print("6  -  Show discount schedule")
    print("7  -  Show customer preferences")
    print("8  -  Suggest recipe")
    print("9  -  Show financial report - overview")
    print("10 -  Show financial report - details")
    print("11 -  Add an expense")
    print("12 -  Exit")
    choice = input("Please select an option:")

    if choice == "1":
        show_inventory()
    elif choice == "2":
        show_freshness_details()
    elif choice == "3":
        remove_expired_fish()
        print("Expired fish removed from inventory.")
        show_freshness_details()
    elif choice == "4":
        fish_type = input("Enter the type of fish you want to add:").strip()
        quantity = int(input("Enter the quantity of fish you want to add:"))
        buy_price = float(input("Enter the buy price of the fish:"))
        freshness = input("Enter the freshness of the fish (high, average, low):").strip()
        supplier = input("Enter the supplier name").strip()
        add_fish(fish_type, quantity, buy_price, freshness)
        if fish_type in inventory:
            purchase_history.append({
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "fish_type": fish_type,
            "quantity": quantity,
            "buy_price": buy_price,
            "freshness": freshness,
            "supplier": supplier,
            "total_cost": quantity * buy_price
            })
    elif choice == "5":
        customer_animal = input("What animal are you ordering for?").strip()
        order_items = []
        while True:
            fish_type = input("Enter the type of fish you want to order:").strip()
            quantity = int(input("Enter the quantity of fish you want to order:"))
            subtotal = order_fish(fish_type, quantity)
            if subtotal > 0:
                order_items.append({"fish_type": fish_type, "quantity": quantity, "subtotal": subtotal})
                record_preference(customer_animal, fish_type, quantity)
            another_fish = input("Order another fish type? (yes/no): ").strip()
            if another_fish != "yes":
                break
        print("Invoice:")
        total = 0.0
        total_quantity = 0
        for item in order_items:
            print(f"{item['quantity']} x {item['fish_type']} - EUR {item['subtotal']}")
            total = total + item['subtotal']
            total_quantity = total_quantity + item['quantity']
        quantity_discount = 0.0
        if total_quantity >= 5:
            quantity_discount = 0.10
            print("Quantity discount applied: 10% off (5+ fish ordered)")
        today = datetime.datetime.today().strftime("%A")
        today_animal, today_discount = animal_days[today]
        animal_discount = 0.0
        if customer_animal == today_animal:
            animal_discount = today_discount
            print(f"Today is {today_animal} Day - {int(today_discount * 100)}% discount!")
        else:
             print(f"Today is {today_animal} Day (discount only applies to {today_animal} customers)")
        total_discount = quantity_discount + animal_discount
        discounted_total = total * (1 - total_discount)
        print(f"Subtotal: EUR {total:.2f}")
        discount_amount = total - discounted_total
        total_discounts_granted = total_discounts_granted + discount_amount
        print(f"Discount: -EUR {discount_amount:.2f}")
        print(f"Final total: EUR {discounted_total:.2f}")
        total_revenue = total_revenue + discounted_total
        order_history.append({
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "animal": customer_animal,
            "items": order_items,
            "discount": total_discount,
            "discount_amount": discount_amount,
            "final_total": discounted_total
        })
    elif choice == "6":
        show_animal_days()
    elif choice == "7":
        show_customer_preferences()
        show_top_animal_per_day()
    elif choice == "8":
        suggest_recipe()
    elif choice =="9":
        show_finance_report()
    elif choice == "10":
        show_financial_report_details()
    elif choice == "11":
        description = input("Enter a description for the expense: ").strip()
        amount = float(input("Enter the amount (EUR): "))
        add_expense(description, amount)
    elif choice == "12":
        print("Goodbye!")
        break
    