print("1.add")
print("2.sub")
print("3.div")
print("4.mul")
print("5.quit")


choosing = True

while choosing:
    choice = int(input("choice"))
    firstNum = int(input("first number"))
    secNum = int(input("second number"))
    if choice == 5:
        print("the answer is", firstNum + secNum)
        choosing = 5
        break

    elif choice == 2:
        print("the answer is", firstNum - secNum)

    elif choice == 3:
        print("the answer is", firstNum / secNum)

    elif choice == 4:
        print("the answer is", firstNum * secNum)

    elif choosing == 1:
        choosing = True
        
        