i = 0

while i < 5:
    i += 1
    print(i)

# does the same as...
while True:
    i += 1
    print(i)
    if i == 5:
        break
