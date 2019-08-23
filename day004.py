#Day 4

km = 0.621371
m = 1.60934
num = None
print(f"\nConversion of Length Units")
while True:
    conversion = input(f"""If you want to convert kilometre to mile type (k) then inter.
If you wnat to convert mile to kilometre type (m) then inter.
To close the program type (x) then enter.\n... """)
    if conversion.lower() == 'm':
        while True:
            num = (input("How many miles?\n..."))
            try:
                num = float(num)
                print(f"{round(num,2)}m ----> {round(num / km, 2)}km\n")
            except:
                print('Only numbers are allowed')
            else:
                break
    elif conversion.lower() == 'k':
        while True:
            num = input("How many kilometres?\n...")
            try:
                num = float(num)
                print(f"{round(num,2)}km ----> {round(num / m, 2)}m\n")
            except:
                print('Only numbers are allowed')
            else:
                break
    elif conversion.lower() == 'x':
        print("Thank you for using this program\n")
        break
    else:
        print('(m) for mile or (k) for kilometre, (x) to close the program.\n')