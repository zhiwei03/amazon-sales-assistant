few_shots = [
    {'Question' : "What are the total number of pending order?",
     'SQLQuery' : "SELECT COUNT(`Order ID`) FROM amazon_sales_data WHERE Status = 'Pending'",
     'SQLResult': "Result of the SQL query",
     'Answer' : "85"},
    {'Question': "Which day has the most sales?",
     'SQLQuery':"SELECT Date AS Day, SUM(`Quantity`) AS TotalSales FROM amazon_sales_data WHERE Status = 'Completed' GROUP BY Day ORDER BY TotalSales DESC LIMIT 1",
     'SQLResult': "Result of the SQL query",
     'Answer': "2025-02-10"},
    {'Question': "Which item is most popular?" ,
     'SQLQuery' : "SELECT Product, SUM(Quantity) AS TotalSold FROM amazon_sales_data WHERE Status = 'Completed' GROUP BY Product ORDER BY TotalSold DESC LIMIT 1",
     'SQLResult': "Result of the SQL query",
     'Answer': "Smartwatch"} ,
     {'Question' : "How much revenue our store has obatained in Febuary this year?" ,
      'SQLQuery': "SELECT SUM(Quantity * Price) AS Revenue FROM amazon_sales_data WHERE Status = 'Completed' AND MONTH(Date) = 2",
      'SQLResult': "Result of the SQL query",
      'Answer' : "40865"},
    {'Question': "Which top 3 products have generated the highest total revenue?",
     'SQLQuery' : "SELECT Product, SUM(Quantity * Price) AS Revenue FROM amazon_sales_data WHERE Status = 'Completed' GROUP BY Product ORDER BY Revenue DESC LIMIT 3",
     'SQLResult': "Result of the SQL query",
     'Answer' : "Laptop, refrigerator and smartphone"
     }
]