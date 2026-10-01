adults = 2
children = 2
day = 1
child_price = 12
if day <= 5:
    child_price = 6
total = adults * 12 + children * child_price
if adults >= 2:
    if children >= 2:
        total = total - 2 * 12 - 2 * child_price + 30
print(total)