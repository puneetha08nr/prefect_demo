from prefect import flow, task

import random
@task
def generate_a_number():
    return random.randint(0, 100)


@flow
def is_number_even(number: int):
    return number % 2 == 0


@flow
def even_or_odd():
    number = generate_a_number()
    if is_number_even(number):
        print("The number is even")
    else:
        print("The number is odd")
