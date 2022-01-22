# pylint:disable=C0111,C0103

def order_rank_per_customer(db):
    results =  db.execute('''SELECT OrderID, CustomerID, OrderDate,
    RANK() OVER(PARTITION BY CustomerID
    ORDER BY OrderDate) AS OrderRank
    FROM Orders''')
    results = db.fetchall()
    return results

def order_cumulative_amount_per_customer(db):
    results = db.execute('''SELECT Orders.OrderID, Orders.CustomerID, Orders.OrderDate,
    SUM(SUM(OrderDetails.UnitPrice * OrderDetails.Quantity)) OVER(PARTITION BY CustomerID
    ORDER BY OrderDate) AS OrderCumulativeAmount
    FROM Orders
    JOIN OrderDetails ON OrderDetails.OrderID = Orders.OrderID
    GROUP BY Orders.OrderID''')
    results = db.fetchall()
    return results
