### Prime numbers ###

import random

def is_prime(num):
    # try_list = list()
    if num < 2:
        return False
    
    for number in range(2, num, 1):
        # try_list.append(number)
        if num % number == 0:
            # print_tries(num, try_list)
            return False
    # print_tries(num, try_list)
    return True

def filter_prime_numbers(initial_numbers):
    prime_numbers = list()
    for num in initial_numbers:
        if is_prime(num):
            prime_numbers.append(num)
    prime_numbers.sort()
    print (f"Los números dados son:\n{initial_numbers}\n\nLos números primos en el rango dado son:\n{prime_numbers}")

def create_random_numbers(my_set: set = set()):
    # El parámetro recibido es opcional, sirve en
    # caso que se quiera forzar algunos números.

    while len(my_set) < 100:
        my_set.add(round(random.random() * 1000))

    return my_set

if __name__ == "__main__":
    filter_prime_numbers (create_random_numbers())