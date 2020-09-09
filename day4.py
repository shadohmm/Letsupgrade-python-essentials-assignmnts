
lower = 1042000
upper = 702648265
a=5
while a==5:
    for num in range(lower, upper + 1):
        order = len(str(num))
        sum = 0
        temp = num
        while temp > 0:
            digit = temp % 10
            sum += digit ** order
            temp //= 10

        if num == sum:
            print("The First armstrong number is"+" "+str(num))
            exit(0)
