# Definition of the task
# 1. Understand the question and break it down in smaller a, b ,c steps.
# 2. Make a toy example. 
# 3. Get the answer right.
# 4. Optimize the code.

# Notes
#   
#

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

def question_007():
    # Constants
    question_number = "007"
        
    # Logic
    prime_list = [2,3,5,7,11,13] 
    while len(prime_list)<10001:
        prime_list.append(next_prime(prime_list))
    
    answer_value = prime_list[-1]

    # Format
    result = "The answer to question "+str(question_number)+" is: "+str(answer_value)+"."
    return result

# MAINCODE
start_time = time.perf_counter()
result = question_007()

# TIME TRACKING
end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"\n{result}\nExecution time: {execution_time:.4f} seconds\n")
