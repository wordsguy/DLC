numbers = '01X01X00X0188X433X47X999'
num = []
for digits in numbers.split('X'):
    num.append(int(digits))
print(num)
