tekst= ["sllloooowoooo", "inne", "kolejne", "pozostale", "asdfgh", "aedsfg"]

slowa_o_2_lub_wiecej_samogloskach = {}
for slowo in tekst:
    count = 0
    for char in slowo:
        if char in 'aeiouyAEIOUY':
            count += 1
    if count>=2:
        slowa_o_2_lub_wiecej_samogloskach[slowo] = count

print(slowa_o_2_lub_wiecej_samogloskach)
print(len(slowa_o_2_lub_wiecej_samogloskach))