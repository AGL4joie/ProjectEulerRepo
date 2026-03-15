from project_001 import answer_project_001

def print_answer(): 
    # Execution
    question_number, anwser_value = answer_project_001()

    # Format
    result = "The answer to question "+str(question_number)+" is: "+str(anwser_value)+"."

    return result
