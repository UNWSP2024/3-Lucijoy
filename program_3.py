# Author: Lucia Floan
# Date: Feb 7, 2025
# Title: Shipping Charges

# The Fast Freight Shipping Company charges the following rates:

# Weight    	Price Per Pound
# 2 pounds or less   	$1.50
# Over 2 pounds but not more than 6 pounds  	$3.00
# Over 6 pounds but not more than 10 pounds	$4.00
# Over 10 pounds	$4.75
# Write a program which calculates the shipping charge and displays the total.

def weight_conversion(weight):
    # Pseudocode:
    # START
    # 1. IF weight is less than or equal to 2, calculate shipping cost at $1:50 per pound.
    # 2. IF weight is more than 2 and less than or equal to 6, calculate shipping cost at $3.00 per pound.
    # 3. IF weight is more than 6 and less than or equal to 10, calculate shipping cost at $4.00 per pound.
    # 4. IF weight is more than 10, calculate shipping cost at $4.75 per pound. 
    # END

    ######################
    if weight <= 2:
        shippingCost = weight * 1.50
    elif weight > 2 and weight <= 6:
        shippingCost = weight * 3.00
    elif weight > 6 and weight <= 10:
        shippingCost = weight * 4.00
    else:
        shippingCost = weight * 4.75
    ######################

    return shippingCost

#### This piece of the code has been done for you,
#### you only need to worry about the actual shipping 
#### charge logic in the weight_conversion function
if __name__ == '__main__':
    # Local variables
    weight = 0.0
    shippingCost = 0.0
    # Get package weight from the user.
    weight = float(input('Enter the weight of the package: '))
    # Display the shipping charge.
    shippingCost = weight_conversion(weight)
    print ('Shipping charge: $', format(shippingCost, '.2f'))
