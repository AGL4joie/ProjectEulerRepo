# Definition of the task
# 1. Understand the question and break it down in smaller a, b ,c steps.
# 2. Make a toy example. 
# 3. Get the answer right.
# 4. Optimize the code.

# Find the sum of all the multiples of 3 or 5 below 1000
# a) ID 3 or 5 multiple
# b) sum

# Notes:
# Modulo operator: remainder = dividend % divisor  

# PREPROCESSOR 
import time

# FUNCTIONS
def question_001(upper_limit,factors):
    # Constants
    question_number = "001"
    
    # Logic 
    multiple_list = []
    number = 0
    while number < upper_limit:
        cond1 = False
        for factor in factors:
            # Check 1
            if number%factor == 0: 
                cond1 = True
                break

        if cond1:  
            multiple_list.append(number)    

        number+=1
    
    #print(multiple_list)
    answer_value = sum(multiple_list)
    # Format
    result = "The answer to question "+str(question_number)+" is: "+str(answer_value)+"."
    return result

# MAINCODE
start_time = time.perf_counter()
result = question_001(upper_limit=1e3, factors=[3,5])

# TIME TRACKING
end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"\n{result}\nExecution time: {execution_time:.4f} seconds\n")
