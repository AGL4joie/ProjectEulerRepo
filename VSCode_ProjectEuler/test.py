def next_prime(current_prime, prime_list):
    prospect = current_prime
    confirmation = True

    while confirmation:
        prospect+=1
        
        for prime in prime_list:
            # Check if the prospect can be divided by a smaller prime number and return an integer.
            if prospect%prime == 0: # True = not prime
                break
            
            else:
                confirmed_prospect = prospect 
                confirmation = False
                break
    
    return confirmed_prospect


confirmed_prospect = next_prime(3, [2,3])

print(confirmed_prospect)

prime_number_list = [2,3]

print(prime_number_list[-1])

