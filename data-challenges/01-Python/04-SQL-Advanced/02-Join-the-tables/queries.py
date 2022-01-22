# pylint:disable=C0111,C0103

def detailed_orders(db):
    '''return a list of all orders (order_id, customer.contact_name,
    employee.firstname) ordered by order_id'''
    results = db.execute('''SELECT OrderID, Customers.ContactName , Employees.FirstName
    FROM Orders
    JOIN Customers ON Customers.CustomerID = Orders.CustomerID
    JOIN Employees ON Employees.EmployeeID = Orders.EmployeeID
    ORDER BY OrderID''')
    results = results.fetchall()
    return results

def spent_per_customer(db):
    '''return the total amount spent per customer ordered by ascending total
    amount (to 2 decimal places)
    Exemple :
        Jean   |   100
        Marc   |   110
        Simon  |   432
        ...
    '''
    results = db.execute('''SELECT Customers.ContactName,
    SUM(OrderDetails.UnitPrice * OrderDetails.Quantity) AS TotalAmount
    FROM OrderDetails
    JOIN Orders ON Orders.OrderID = OrderDetails.OrderID
    JOIN Customers ON Customers.CustomerID = Orders.CustomerID
    GROUP BY Customers.ContactName
    ORDER BY TotalAmount''')
    results = results.fetchall()
    return results


def best_employee(db):
    '''Implement the best_employee method to determine who’s the best employee!
    By “best employee”, we mean the one who sells the most.
    We expect the function to return a tuple like:
    ('FirstName', 'LastName', 6000 (the sum of all purchase)).
    The order of the information is irrelevant'''
    results = db.execute('''SELECT Employees.FirstName, Employees.LastName,
    SUM(OrderDetails.UnitPrice * OrderDetails.Quantity) AS TotalAmount
    FROM Employees
    JOIN Orders ON Orders.EmployeeID = Employees.EmployeeID
    JOIN OrderDetails ON OrderDetails.OrderID = Orders.OrderID
    GROUP BY Employees.EmployeeID
    ORDER BY TotalAmount DESC''')
    results = results.fetchone()
    return results

def orders_per_customer(db):
    '''TO DO: return a list of tuples where each tupe contains the contactName
    of the customer and the number of orders they made (contactName,
    number_of_orders). Order the list by ascending number of orders'''
    results = db.execute('''SELECT Customers.ContactName, COUNT(Orders.OrderID) AS TotalOrders
    FROM Customers
    LEFT JOIN Orders ON Orders.CustomerID = Customers.CustomerID
    GROUP BY Customers.ContactName
    ORDER BY TotalOrders''')
    results = results.fetchall()
    return results
