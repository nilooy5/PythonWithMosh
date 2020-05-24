numbers = [12, 43, 545, 345, 565, 12, 43, 56]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)

print(uniques.sort())