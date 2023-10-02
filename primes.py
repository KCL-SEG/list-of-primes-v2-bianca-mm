"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes <=0:
        raise ValueError("invalid number typed")
    
    list = []
    counter = 2
    while len(list) < number_of_primes:
        divisible = False
    
        for i in range(counter, 1, -1):
            if counter%i==0 and counter != i:
                divisible=True
                break

        if (not divisible):
            list.append(counter)

        counter+= 1
        
    return list

primes(1)