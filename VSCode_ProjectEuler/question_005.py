# Definition of the task
# 1. Understand the question and break it down in smaller a, b ,c steps.
# 2. Make a toy example. 
# 3. Get the answer right.
# 4. Optimize the code.

# Notes
# 10 : 0 
# zero
# odd even
# 5, 10 ,15 ,20
# 2 4 8 16 
# 1
# 5 10 20
# 9 18
# 7 14
# 3 6 12
# 
# [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]

# PREPROCESSOR 
import time

# FUNCTIONS
def question_005(starting_point,range_Q5):
    # Constants
    question_number = "005"
        
    # Logic 
    prospect = starting_point
    cond1, cond2 = True, True
    # Check if the prospect satisfies 1-20
    while cond1:
        prospect+=max(range_Q5)

        for i in [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]:
            # Check if there is a remainder
            if prospect%i == 0:
                cond2 = True
            # Confirm that at least one division results in a remainder
            else :
                cond2 = False
                break 
        if cond2 : 
            # Confirmation
            cond1 = False
            answer_value = prospect

    # Format
    result = "The answer to question "+str(question_number)+" is: "+str(answer_value)+"."
    return result

# MAINCODE
start_time = time.perf_counter()
result = question_005(starting_point=0,range_Q5=range(1,21,1))

# TIME TRACKING
end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"\n{result}\nExecution time: {execution_time:.4f} seconds\n")
