# somma i multipli di 3 e 5 fino a 9230
def quest0():
    result = 0
    for number in range(3, 9230):
        if number % 3 == 0 or number % 5 == 0:
            result += number

    print(result)


quest0()