#! Python 3
# * Arithmetic Arranger.py - A simple programme that takes in a list of problems to be printed in a vertical manner side by side for easy understanding for kids.

# The first part is a function for finding out errors in the questions based on the situations mentioned.
def arithmetic_arranger_error(questions):
    errors = ''
    if len(questions) > 5:
        errors = "Error: Too many problems."
    for question in questions:
        currentquestion = question.split()
        if currentquestion[1] not in '+-':
            errors = "Error: Operator must be '+' or '-'."
        if not currentquestion[0].isdigit() or not currentquestion[2].isdigit():
            errors = "Error: Numbers must only contain digits."
        if len(currentquestion[0]) > 4 or len(currentquestion[2]) > 4:
            errors = "Error: Numbers cannot be more than four digits."
    return errors

def arithmetic_arranger(problems, result=False):
    
    # This function starts by calling the error function so that if any error is present in the problems it does not run the whole way and prints the error.
    if arithmetic_arranger_error(problems) != '':
        return arithmetic_arranger_error(problems)

    
    # Creating a variable storing the total number of problems
    numberofproblems = len(problems)
    longestLen = {}  # A dictonary for storing the longest length in a given problem
    answers = {}  # A Dictonary to store answers to each problems, if the second argument is True

    for probNo, problem in enumerate(problems):
        # Each problem is assigned to 'currentProblem' as a list containing the numbers and operators
        currentProblem = problem.split()
        length1 = len(currentProblem[0])
        length2 = len(currentProblem[2])
        longestLen[probNo] = max(length2, length1)

        # Checking the operators for addition or subtraction
        if currentProblem[1] == '+':
            answers[probNo] = int(currentProblem[0])+int(currentProblem[2])
        else:
            answers[probNo] = int(currentProblem[0])-int(currentProblem[2])

    line1 = ''
    line2 = ''
    line3 = ''
    line4 = ''

    # The Main loop that makes the 4 lines that will be printed
    for i in range(numberofproblems):
        currentProblem = problems[i].split()

        line1 += currentProblem[0].rjust(longestLen[i]+2)+'    '
        line2 += currentProblem[1] + " " + \
            currentProblem[2].rjust(longestLen[i])+"    "
        line3 += "-"*int(longestLen[i]+2)+'    '
        if result:
            line4 += str(answers[i]).rjust(longestLen[i]+2)+'    '
    if line4.rstrip() == "": # checking for this since an extra line was getting added when no answers were called for.
        return line1.rstrip()+'\n'+line2.rstrip()+'\n'+line3.rstrip()
    else:
        return line1.rstrip()+'\n'+line2.rstrip()+'\n'+line3.rstrip()+'\n'+line4.rstrip()
