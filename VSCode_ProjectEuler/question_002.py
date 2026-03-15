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
def question_002(upper_limit):
    # Constants
    question_number = "001"
        
    # Logic 
    Fibonacci_list,Fibonacci_list_even = [1,2],[]
    while Fibonacci_list[-1] < upper_limit:
        Fibonacci_list.append(sum(Fibonacci_list[-2:]))

    Fibonacci_list = Fibonacci_list[:-1]
    print(Fibonacci_list)
    
    i=1
    while i < len(Fibonacci_list):
        if Fibonacci_list[i]%2==0:
            Fibonacci_list_even.append(Fibonacci_list[i])
        i+=1      
    
    print(Fibonacci_list_even)
    answer_value = sum(Fibonacci_list_even)

    # Format
    result = "The answer to question "+str(question_number)+" is: "+str(answer_value)+" ."
    return result






# MAINCODE
start_time = time.perf_counter()
result = question_002(upper_limit=4e6)

# TIME TRACKING
end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"\n{result}\nExecution time: {execution_time:.4f} seconds\n")
