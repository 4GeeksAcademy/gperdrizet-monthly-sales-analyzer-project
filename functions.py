'''Helper functions for sales analysis'''

def total_sales_by_product(data, product_key):
    """Calculates the total sales of a specific product in 30 days."""

    # Start sales sum at zero
    sales_sum = 0

    # Loop on days in sales list
    for item in data:

        # Add today's sales of the product to the total
        sales_sum += item[product_key]

    return sales_sum


def average_daily_sales(data, product_key):
    """Calculates the average daily sales of a specific product."""

    # Get total sales for the product
    total_sales = total_sales_by_product(data, product_key)

    # Divide by number of days to get average
    average_sales = total_sales / len(data)
    
    return average_sales


def best_selling_day(data):
    """Finds the day with the highest total sales."""

    # Initialize variables to track maximum sales and the winning day
    max_sales = 0
    winner = None

    # Loop through each day's sales data
    for item in data:

        # Calculate total sales for the day (sum of all products)
        # Exclude the 'day' key from the su
        total_sales = sum(item.values()) - item['day']  # Exclude the 'day' key
        
        # Check if today's total sales are greater than the current max
        # If so, update max_sales and winner
        if total_sales > max_sales:
            max_sales = total_sales
            winner = item['day']

    return winner


def days_above_threshold(data, product_key, threshold):
    """Counts how many days the sales of a product exceeded a given threshold."""
    
    # Initialize a counter for days exceeding the threshold
    count = 0

    # Loop through each day's sales data
    for item in data:

        # Check if the sales of the specified product exceed the threshold
        # If so, increment the counter
        if item[product_key] > threshold:
            count += 1

    return count

def top_product(data):
    """Determines which product had the highest total sales in 30 days."""
    
    total_sales = 0
    winner = None

    # Loop on the sales data keys
    for product in data[0].keys():

        # Skip the 'day' key
        if product != 'day':
        
            # Calculate total sales for the current product
            product_sales = total_sales_by_product(data, product)

            # Check if this product has higher sales than the current winner
            if product_sales > total_sales:
                total_sales = product_sales
                winner = product
    
    return winner