import random

def math():
    # the operator (+, -, *, /) will be randomly assigned
    operator = random.randint(1, 4)

    # addition problems
    if operator == 1:
        x = int(random.randint(0, 10))
        y = int(random.randint(0, 10))
        question = int(input(f'{x} + {y} = '))
        answer = x + y
        if question == answer:
            print("Correct!")

    # subtraction problems
    elif operator == 2:
        x = int(random.randint(0, 10))
        y = int(random.randint(0, 10))
        question = int(input(f'{x} - {y} = '))
        answer = x - y
        if question == answer:
            print('Correct!')

    # multiplication problems
    elif operator == 3:
        x = int(random.randint(0, 10))
        y = int(random.randint(0, 10))
        question = int(input(f'{x} x {y} = '))
        answer = x * y
        if question == answer:
            print('Correct!')

    # division problems
    elif operator == 4:
        x = int(random.randint(1, 10))
        y = int(random.randint(0, 10))
        z = x * y
        question = int(input(f'{z} / {x} = '))
        answer = z / x
        if question == answer:
            print('Correct!')

for i in range(10):
    math()