num = 0
tot = 0.0
while True :
    sval = input("Enter a number:")
    if sval == "#":
        continue
    elif sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print("Invalid input")
        continue
    print (fval)
    num = num + 1
    tot = tot + fval
print(num,tot,tot/num)
