# pylint:disable=C0111,C0103

def query_orders(db):
    # return a list of orders displaying each column
    results = db.execute('''SELECT *
    FROM Orders
    ORDER BY OrderID
    ''')
    results = results.fetchall()
    return results

def get_orders_range(db, date_from, date_to):
    # return a list of orders displaying all columns with OrderDate between date_from and date_to
    results = db.execute(f'''SELECT *
    FROM Orders
    WHERE OrderDate > "{date_from}" AND OrderDate < "{date_to}"
    ORDER BY OrderDate
    ''')
    results = results.fetchall()
    return results

def get_waiting_time(db):
    # get a list with all the orders displaying each column
    # and calculate an extra TimeDelta column displaying the number of days
    # between OrderDate and ShippedDate, ordered by ascending TimeDelta
    results = db.execute('''SELECT *, JULIANDAY(ShippedDate) - JULIANDAY(OrderDate) AS DeliveryTime
    FROM Orders
    ORDER BY DeliveryTime
    ''')
    results = results.fetchall()
    return results
