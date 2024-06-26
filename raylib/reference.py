

test = [0 for i in range(10)]

print(test)

copy = test[:]
test[4] = 1

print(f'Copy -> {copy}')
print(f'Test -> {test}')
