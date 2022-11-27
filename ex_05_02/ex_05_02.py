smallest_n = None
biggest_n = None
while True:
    num = input("Enter a number:")
    if num == "done":
        break
    try:
        i_num = int(num)
        if smallest_n is None:
            smallest_n = i_num
        if i_num < smallest_n:
            smallest_n = i_num
        if biggest_n is None:
            biggest_n = i_num
        if i_num > biggest_n:
            biggest_n = i_num
    except:
        print("Invalid input")
        print("Enter a number")
        continue

print("Maximum is",biggest_n)
print("Minimum is",smallest_n)

        
