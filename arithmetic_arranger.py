def arithmetic_arranger(problems,display_answer=False):
    arithmetic_problems = ''
    space1 = ''
    space2 = ''
    dashes = ''
    answer = ''

    if len(problems) > 5:
        return 'Error: Too many problems.'
        
    for problem in problems:
        problem_items = problem.split()
        if problem_items[1] not in '+-':     # Check if the problem contains '+' or '-'
            return "Error: Operator must be '+' or '-'."
        for p_item in problem:
            if p_item not in '0123456789+- ': # Check if the problem contains only digits
                return "Error: Numbers must only contain digits."
        operand1_len = len(problem_items[0])
        operand2_len = len(problem_items[2])
        max_operand_len = max(operand1_len,operand2_len)     
        if max_operand_len > 4:
            return "Error: Numbers cannot be more than four digits."
    
        # space1 is for calculating the space for the first operand
        if operand2_len > operand1_len:
            space1 += (' ') * (operand2_len - operand1_len + 2)  # Adding 2 : 1 space for operator and one for the space after the operator
        else : 
            space1 += (' ') * 2
        space1 += problem_items[0] 
        space1 += (' ') * 4

        # space2 is for calculating the space for the second operand 
        space2 += problem_items[1]
        if operand1_len >= operand2_len:
            space2 += ((' ') * (operand1_len - operand2_len))
        space2 += (' ') + problem_items[2]
        space2 += (' ') * 4
    
        # dashes calculation
        dashes += '-' * (max_operand_len + 2)
        dashes += 4 * (' ')

        # Evaluation of answer
        answer += (' ') * (max_operand_len + 2 - len(str(eval(problem))))
        answer += str(eval(problem))
        answer += (' ') * 4

    space1 = space1[:-4]
    space2 = space2[:-4]
    dashes = dashes[:-4]
    answer = answer[:-4]

        
    if display_answer == False:
        arithmetic_problems = space1 + '\n' + space2 + '\n' + dashes
    else:
        arithmetic_problems = space1 + '\n' + space2 + '\n' + dashes + '\n' + answer

    return arithmetic_problems