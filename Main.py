import random

NUMBER_LIST = list(range(1000, 10000))  # 4-digit numbers

def generate_tickets(count):
    if count <= 0:
        raise ValueError("Number of tickets must be greater than 0.")
    
    if count > len(NUMBER_LIST):
        raise ValueError("Requested tickets exceed available unique numbers.")
    
    return random.sample(NUMBER_LIST, count)