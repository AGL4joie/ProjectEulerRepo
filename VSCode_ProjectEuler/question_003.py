# Definition of the task
# 1. Understand the question and break it down in smaller a, b ,c steps.
# 2. Make a toy example. 
# 3. Get the answer right.
# 4. Optimize the code.

# Notes

# PREPROCESSOR 
import time

# FUNCTIONS
def next_prime(prime_list):
    prospect = prime_list[-1]
    confirmation = True

    while confirmation:
        prospect+=1
        for prime in prime_list:
            # Check if the prospect can be divided by a smaller prime number and return an integer.
            if prospect%prime == 0: # True = not prime
                break
            
            else:
                # Check if the found prime is already in the list.
                if prime == prime_list[-1]:
                    confirmed_prospect = prospect 
                    confirmation = False
                    break
    
    return confirmed_prospect

def question_003(number_to_evaluate):
    # Constants
    question_number = "003"
        
    # Logic
    # a) Make the list of prime numbers
    prime_number_list = [2,3]
    while prime_number_list[-1]<1e5:#(number_to_evaluate/2):
        next_prime_value = next_prime(prime_number_list)
        prime_number_list.append(next_prime_value)
        print(next_prime_value)

    # b) Divide by the smallest prime to get an integer.
    factor_list = []
    current_value = number_to_evaluate
    while current_value>prime_number_list[-1]:  
        for prime in prime_number_list:
            # True => store the factor and repeat
            if current_value%prime == 0:
                factor_list.append(prime)
                current_value = current_value/prime
            # False => try another factor

    # c) Store de biggest prime required.
    answer_value = factor_list[-1]

    # Format
    result = "The answer to question "+str(question_number)+" is: "+str(answer_value)+"."
    return result

# MAINCODE
start_time = time.perf_counter()
result = question_003(number_to_evaluate=600851475143) # 600851475143

# TIME TRACKING
end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"\n{result}\nExecution time: {execution_time:.4f} seconds\n")