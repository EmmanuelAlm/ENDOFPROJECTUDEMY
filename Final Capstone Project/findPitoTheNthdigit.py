"""import math 



def ask_user():#ask user how many digits they want out of pi
    try:
        global user_input, int_user_input
        user_input = (input("Enter how many digits you want pi to go to: "))
        int_user_input = int(user_input)
    except TypeError:
        print()
        return user_input, int_user_input

    
pizza = math.pi
#print(pizza)
#using the format method to make a = user_input and use that as the nth digit
#print('This is how many digits pi is: {d:.2f} '.format(d = pizza,a = user_input))


if __name__ == "__main__":
    playing = True
    while playing:
        try:
            ask_user()
            if int_user_input > 16:
                print("The interger was too high don't go above ten ")
                ask_user()
            elif int_user_input <= 15:
                print('This is how many digits pi is: {d:.{a}f} '.format(d = pizza,a = user_input))
                ask_user()
            else:
                print("Program quit because you didnt put in an interger")
                playing = False
        except ValueError:
            pass"""
            
def calcPi(limit):  # Generator function
    """
    Prints out the digits of PI
    until it reaches the given limit
    """

    q, r, t, k, n, l = 1, 0, 1, 1, 3, 3

    decimal = limit
    counter = 0

    while counter != decimal + 1:
            if 4 * q + r - t < n * t:
                    # yield digit
                    yield n
                    # insert period after first digit
                    if counter == 0:
                            yield '.'
                    # end
                    if decimal == counter:
                            print('')
                            break
                    counter += 1
                    nr = 10 * (r - n * t)
                    n = ((10 * (3 * q + r)) // t) - 10 * n
                    q *= 10
                    r = nr
            else:
                    nr = (2 * q + r) * l
                    nn = (q * (7 * k) + 2 + (r * l)) // (t * l)
                    q *= k
                    t *= l
                    l += 2
                    k += 1
                    n = nn
                    r = nr


def main():  # Wrapper function

    # Calls CalcPi with the given limit
    pi_digits = calcPi(int(input(
        "Enter the number of decimals to calculate to: ")))

    i = 0

    # Prints the output of calcPi generator function
    # Inserts a newline after every 40th number
    for d in pi_digits:
            print(d, end='')
            i += 1
            if i == 40:
                print("")
                i = 0

if __name__ == '__main__':
    main()