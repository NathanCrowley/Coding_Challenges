'''
Nathan Crowley - 14/7/2020

take list of products as input and return total profit for each product
profit = sell_price - cost_price
multiply profit by inventory
round to nearest dollar --> {:2f}
'''
def calculate_profit(shop):
    profits = {}
    for product in shop:
        profit_per_item = (product['sell_price']) - (product['cost_price'])
        total_profit = profit_per_item*product['inventory']
        profit = '${:.0f}'.format(total_profit)
        profits[product['id']]=profit
    return profits

brodale = [
    {
            'id': 'milk',
               "cost_price": 32.67,
               "sell_price": 45.00,
               "inventory": 1200
    },
    {
            'id': 'chicken roll',
              "cost_price": 225.89,
              "sell_price": 550.00,
              "inventory": 100
    },
    {
            'id': 'jambon',
              "cost_price": 2.77,
              "sell_price": 7.95,
              "inventory": 8500
    }
]
print(calculate_profit(brodale))