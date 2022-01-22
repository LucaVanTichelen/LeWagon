# pylint:disable=C0111,C0103

def get_average_purchase(db):
    # return the average amount spent per order for each customer ordered by customer ID
    results = db.execute('''WITH average AS (
    SELECT
    sum(orderdetails.UnitPrice * orderdetails.Quantity) as value, orderdetails.OrderID
    FROM OrderDetails
    group by OrderID)
    SELECT
    customers.CustomerID, ROUND(avg(average.value), 1)
    FROM customers
    join orders on customers.customerID = orders.customerID
    join average on average.OrderID = orders.OrderID
    group by customers.CustomerID''')
    results = db.fetchall()
    return results

def get_general_avg_order(db):
    # return the average amount spent per order
    pass  # YOUR CODE HERE

def best_customers(db):
    # return the customers who have an average purchase greater than the general average purchase
    pass  # YOUR CODE HERE

def top_ordered_product_per_customer(db):
    # return the list of the top ordered product by each customer based on the total ordered amount
    pass  # YOUR CODE HERE

def average_number_of_days_between_orders(db):
    # return the average number of days between two consecutive orders of the same customer
    pass  # YOUR CODE HERE
