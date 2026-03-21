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
def question_006(number):
    # Constants
    question_number = "006"
        
    # Logic 
    sum1 = 0
    for i in range(1,number+1,1):
        sum1+=i**2
 
    sum2 = sum(range(1,number+1,1))**2

    answer_value = sum2 - sum1

    # Format
    result = "The answer to question "+str(question_number)+" is: "+str(answer_value)+"."
    return result

# MAINCODE
start_time = time.perf_counter()
result = question_006(number=100)

# TIME TRACKING
end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"\n{result}\nExecution time: {execution_time:.4f} seconds\n")
