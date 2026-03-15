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
def question_004():
    # Constants
    question_number = "004"
        
    # Logic 
    answer_value = 10

    # Format
    result = "The answer to question "+str(question_number)+" is: "+str(answer_value)+"."
    return result

# MAINCODE
start_time = time.perf_counter()
result = question_002()

# TIME TRACKING
end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"\n{result}\nExecution time: {execution_time:.4f} seconds\n")
