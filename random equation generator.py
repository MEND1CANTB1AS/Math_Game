import arcade
import random
class Problem():

    def equation(self):
        # the operator (+, -, *, /) will be randomly assigned
        operator = random.randint(1, 4)

        # addition problems
        if operator == 1:
            x = int(random.randint(0, 10))
            y = int(random.randint(0, 10))
            question = int(input(f'{x} + {y} = '))
            answer = x + y
            print(question)
            if question == answer:
                print("Correct!")

        # subtraction problems
        elif operator == 2:
            x = int(random.randint(0, 10))
            y = int(random.randint(0, x))
            question = int(input(f'{x} - {y} = '))
            answer = x - y
            print(question) 
            if question == answer:
                print('Correct!')

        # multiplication problems
        elif operator == 3:
            x = int(random.randint(0, 11))
            y = int(random.randint(0, 9))
            question = int(input(f'{x} x {y} = '))
            answer = x * y
            print(question)
            if question == answer:
                print('Correct!')

        # division problems
        else:
            x = int(random.randint(1, 10))
            y = int(random.randint(0, 10))
            z = x * y
            question = int(input(f'{z} / {x} = '))
            answer = z / x
            print(question)
            if question == answer:
                print('Correct!')


def main():
    """ Main method """
    problem = Problem()
    problem.equation()

if __name__ == "__main__":
    main()