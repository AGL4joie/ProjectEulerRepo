# Definition of the task
# 1. Understand the question and break it down in smaller a, b ,c steps.
# 2. Make a toy example. 
# 3. Get the answer right.
# 4. Optimize the code.

# Notes
# largest palidrome from 2-digit mult = 9009 (from 91 and 99)  
# lagest from 3-digit mult

# PREPROCESSOR 
import time

# FUNCTIONS
def question_004():
    # Constants
    question_number = "001"
        
    # Logic 
    number_max = int("9"*n_digit)
    mult_list = list(reversed(range(1,number_max+1,1)))
    palindorme_dict = {"101":0} 

    for number_1 in mult_list:
        for number_2 in mult_list:
            # Generate palindrome prospect
            prospect = number_1*number_2
            
            # Check prospect
            if is_palindrome(prospect):
                key = str(number_1)+"*"+str(number_2)
                palindorme_dict[key] = prospect

    # Answer
    answer_value, key = max(palindorme_dict.values()), max(palindorme_dict, key=palindorme_dict.get)

    # Format
    result = "The answer to question "+str(question_number)+" is: "+str(key)+" "+str(answer_value)+"."
    return result

# MAINCODE
start_time = time.perf_counter()
result = question_004(n_digit=3)

# TIME TRACKING
end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"\n{result}\nExecution time: {execution_time:.4f} seconds\n")
