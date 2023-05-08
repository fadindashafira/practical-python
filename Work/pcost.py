# pcost.py
#
# Exercise 1.27
import sys
import csv

def portfolio_cost(filename):
    total_cost = 0.0
    f = open(filename)
    rows = csv.reader(f)
    headers = next(rows)

    for rownumber, row in enumerate(rows, start=1):
        record = dict(zip(headers, row))
        try:
            nshares = int(record['shares'])
            price = float(record['price'])
            total_cost += nshares * price
        except ValueError:
            print(f'Row {rownumber}: Bad row: {row}')
    return total_cost

# def portfolio_cost(filename):
#     total_cost = 0.0
#     f = open(filename)
#     rows = csv.reader(f)
#     headers = next(rows)

#     for rownumber, row in enumerate(rows, start=1):
#         try:
#             shares = int(row[1])
#         except ValueError:
#             print(f'Row {rownumber}: Bad row: {row}')

#         price = float(row[2])
#         total_cost += shares * price  
    
#     f.close()
    
#     return total_cost

# if len(sys.argv) == 2:
#     filename = sys.argv[1]
# else:
#     filename = 'Data/missing.csv'

# cost = portfolio_cost(filename)
# print('Total cost:', cost)

####

# def portfolio_cost(filename):
#     total_cost = 0.0

#     with open(filename, 'rt') as f: # open and file
#         # calculate cost to purchase all of the shares in the portfolio
#         headers = next(f)
#         for line in f:
#             row = line.split(',')

#             try:
#                 shares = int(row[1])
#             except ValueError:
#                 print("Warning: Couldn't parse", line, '. Missing values detected')

#             price = float(row[2])
#             total_cost += shares * price  
    
#     return total_cost

###

# def portfolio_cost(filename):
#     total_cost = 0.0

#     with open(filename, 'rt') as f: # open and file
#         # calculate cost to purchase all of the shares in the portfolio
#         headers = next(f)
#         for line in f:
#             row = line.split(',')
#             shares = int(row[1])
#             price = float(row[2])
#             total_cost += shares * price
    
#     return total_cost

### 

# total_cost = 0.0

# with open('Data/portfolio.csv', 'rt') as f: # open and file
#     # calculate cost to purchase all of the shares in the portfolio
#     headers = next(f)
#     total = []
#     for line in f:
#         row = line.split(',')
#         shares = int(row[1])
#         price = float(row[2])
#         total_cost += shares * price

# print('Total cost ', total_cost )
 
