# Author: Lucia Floan
# Date: Feb 7, 2025
# Title: Hot Dog

# There are two kinds of hot dogs sold:  
# Hot Dog ($3.50), Chili Dog ($4.50).  
# Additionally, a person can order cheese ($0.50), peppers ($0.75), or grilled onions ($1.00).  
# Also, tax is 7%. 
# Write a program that inputs the type of hot dog wanted and optional toppings.  
# The program then displays the hot dog cost, tax, and total cost.

# Flowchart
# Start
# User selects either a "Hot Dog" or a "Chili Dog."
# User chooses a topping or enters "none."
# The program calculates the cost of the hot dog, any selected toppings, and adds the tax (7%).
# The program then displays the final total cost.
# End

def calculate_cost(hot_dog_type, toppings):
    # Prices for hot dogs and toppings
    hot_dog_price = 3.50
    chili_dog_price = 4.50
    cheese_price = 0.50
    peppers_price = 0.75
    onions_price = 1.00
    tax_rate = 0.07

    # Make sure the user enters a valid hot dog type
    if hot_dog_type == "hot dog":
        hot_dog_cost = hot_dog_price
    elif hot_dog_type == "chili dog":
        hot_dog_cost = chili_dog_price
    else:
        print("Invalid choice. Please choose either 'Hot Dog' or 'Chili Dog'.")
        return  # Exit if the choice is invalid

    # Calculate topping cost
    if toppings == "cheese":
        topping_cost = cheese_price
    elif toppings == "peppers":
        topping_cost = peppers_price
    elif toppings == "grilled onions":
        topping_cost = onions_price
    else:
        topping_cost = 0  # If no toppings selected

    # Calculate total before tax
    total_before_tax = hot_dog_cost + topping_cost

    # Calculate tax (7%)
    tax = total_before_tax * tax_rate

    # Calculate total cost
    total_cost = total_before_tax + tax

    # Show the final cost to the user
    print(f"\nTotal cost: ${total_cost:.2f}")


# Main program
def main():
    # Get user input for hot dog type
    hot_dog_type = input("Do you want a Hot Dog or a Chili Dog? ").lower()

    # Get user input for toppings
    toppings = input("Would you like cheese, peppers, grilled onions, or none? ").lower()

    # Call the calculate_cost() function here
    calculate_cost(hot_dog_type, toppings)  # Now the function is being called

# Start the program
main()
