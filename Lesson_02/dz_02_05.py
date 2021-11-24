prices = [56.32, 73.15, 27, 49.57, 11.28, 16.25, 35.9, 81.02, 29.77, 47.22, 63.6, 99.99]

# Task A
for idx, price in enumerate(prices):
    price = str(f'{price:.2f}')
    prices[idx] = [price[:2], price[3:]]
    # print(f'{prices[idx][0]} руб {prices[idx][1]} коп')
    prices[idx] = f'{prices[idx][0]} руб {prices[idx][1]} коп'
print(', '.join(prices))

# Task B
# print(id(prices))
# prices.sort()
# print(prices)
# print(id(prices))

# Task C
# print(sorted(prices, reverse=True))

# Task D
# prices.sort()
# print(prices[-5:])