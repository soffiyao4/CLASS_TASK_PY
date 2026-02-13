import random

NUMBER_LIST = list(range(1000, 9999))

def generate_tickets(count):
    if count > len(NUMBER_LIST):
        raise ValueError("Count exceeds available unique ticket numbers.")
    
    tickets = random.sample(NUMBER_LIST, count)
    return tickets

print(generate_tickets(5))


