# report.py
#
# Exercise 2.4

import csv

def read_portfolio(filename):

    '''
    Read a stock portfolio file into a list of dictionaries with keys :
    name, shares, and price
    '''

    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        # print(headers)
        # for row in rows:
        #     record = dict(zip(headers, row))
        #     name = record['name']
        #     nshares = int(record['shares'])
        #     price = float(record['price'])

        for row in rows:            
            stock = {
                'name' : row[0], 
                'shares' : int(row[1]), 
                'price' : float(row[2])}
            portfolio.append(stock)
            # portfolio.append(name)
            # portfolio.append(nshares)
            # portfolio.append(price)
            # print(portfolio)
    return portfolio

def read_prices(filename):
    
    '''
    Read a CSV file of price data into a dict mapping names to prices
    '''
    prices = {}

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:   
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass
    return prices

def make_report(portfolio, prices):
    """
    Takes a list of stocks and dictionary of prices as input
    returns a list of tuples containing the rows of table (name, shares, price, change)
    """

    rows = []

    for stock in portfolio:
        current_price = prices[stock['name']] # Current price is from prices.csv file, choose the price of stock name in portfolio.csv
        change = current_price - stock['price'] # Calculate change from current_price - price in portfolio.csv
        summary = (stock['name'], stock['shares'], current_price, change)
        rows.append(summary)
        
    # for stock in portfolio:
    #     current_price = prices[stock['name']] # Current price is from prices.csv file, choose the price of stock name in portfolio.csv
    #     change = current_price - stock['price'] # Calculate change from current_price - price in portfolio.csv
    #     summary = (stock['name'], stock['shares'], current_price, change)
    #     rows.append(summary)
    
    return rows

# Read data files and create the report data        

portfolio = read_portfolio('Data\portfolio.csv')
prices = read_prices('Data\prices.csv')

# Generate the report data
report = make_report(portfolio,prices)

# Output the report data
headers = ('Name', 'Shares', 'Price', 'Change')
print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
strip = '-' * 10 
space = ' '
print(f'{strip:>10s}{space:>1s}{strip:>10s}{space:>1s}{strip:>10s}{space:>1s}{strip:>10s}')
for name, shares, price, change in report:
    print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')


# # Output the report
# headers = ('Name', 'Shares', 'Price', 'Change')
# print('%10s %10s %10s %10s' % headers)
# print(('-' * 10 + ' ') * len(headers))
# for row in report:
#     print('%10s %10d %10.2f %10.2f' % row)

#######

# # Calculate the total cost of the portfolio
# total_cost = 0.0
# for s in portfolio:
#     total_cost += s['shares'] * s['price']
# print('Total cost', total_cost)

# # Compute the current value of the portfolio
# total_value = 0.0
# for s in portfolio:
#     total_value += s['shares'] * prices[s['name']]

# print('Current value', total_value)
# print('Gain', total_value - total_cost)

##############

# import csv

# def read_portfolio(filename):
#     # opens portfolio file 
#     # reads into a dictionary

#     portfolio = []

#     with open(filename, 'rt') as f:
#         rows = csv.reader(f)
#         headers = next(rows)
#         for row in rows:            
#             holding = {
#                 'name' : row[0], 
#                 'shares' : int(row[1]), 
#                 'price' : float(row[2])}
#             portfolio.append(holding)

#     total = 0.0
#     for s in portfolio:
#         total += s['shares'] * s['price']
#     return total

#####

# import csv

# def read_portfolio(filename):
#     # opens portfolio file 
#     # reads into a list of tuples

#     portfolio = []

#     with open(filename, 'rt') as f:
#         rows = csv.reader(f)
#         headers = next(rows)
#         for row in rows:
#             # turn each row into a tuple
#             holding = (row[0], int(row[1]), float(row[2]))
#             portfolio.append(holding)
    
#     total = 0.0
#     # for s in portfolio:
#     #     total += s[1] * s[2]

#     for name, shares, price in portfolio:
#         total += shares * price
#     return total