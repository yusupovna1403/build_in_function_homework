def main(x, y):
    """Integer type variables 'x' and 'y' are given. Return the value of the expression in README.md file.
    https://github.com/codeschool43/Build_in_function_homework#build_func10

    Args:
        x (int): integer
        y (int): integer
        
    Returns:
        int: the value of the expression
    """
    answer = 3 * pow( y , 1/2) + pow(x , 2/3)
    answer = round(answer,1)
    return answer
print(main(8 , 4))