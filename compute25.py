from typing import List

def check_zero_division(expression: str) -> bool:
    
    """Check if the given expression is a zero-division expression
    
    Arguments:
        expression [str]: expression to check


    Returns:
        bool: Boolean indicating if the expression is a zero-division
    """    
      

    try:
        eval(expression)
        return True
    except ZeroDivisionError:
        return False


def compute25(number: str, expression: str = "") -> str:
    
    """Create an expression with the numbers of [number] that evaluates to 25
    
    Arguments:
        number [str]: Number to decompose
        expression (optional) [str]: temporally computed expression

    Returns:
        str: computed expression
    """    

    operations: List[str] = ["+", "-", "*", "/"]

    # initial case: there is no expression, we put a number to start computing
    if not expression:
        for first_number in number:
            result = compute25(number.replace(first_number, "", 1), expression=first_number)
            if result != "SIN SOLUCIÓN":
                return result


    else:
        # base case: the expression evaluated is 25 and there are no more numbers left
        if eval(expression) == 25 and not number:
            return expression

        # there are still numbers
        elif number:
            for first_operation in operations:
                for first_number in number:

                    aux_number: str = number.replace(first_number, "", 1)

                    # first basic expression, we operate a number with the rest of the expression
                    first_expression: str = (f"({first_number} {first_operation} {expression})")
                    if check_zero_division(first_expression):
                        result = compute25(aux_number, expression=first_expression)
                        if result != "SIN SOLUCIÓN":
                            return result

                    # second basic expression, subtraction and division are not commutative
                    second_expression: str = (f"({expression} {first_operation} {first_number})")
                    if first_operation in ["/", "-"] and check_zero_division(second_expression):
                        result = compute25(aux_number, expression=second_expression)
                        if result != "SIN SOLUCIÓN":
                            return result

                    aux_number_2: str = aux_number
                    for second_number in aux_number:

                        second_aux_number: str = aux_number_2.replace(second_number, "", 1)
                        for second_operation in operations:
                            thrid_expression: str = f"( {first_number} {first_operation} {second_number} ) {second_operation} {expression}"
                            if check_zero_division(thrid_expression):
                                result = compute25(second_aux_number, expression=thrid_expression)
                                if result != "SIN SOLUCIÓN":
                                    return result

    return "SIN SOLUCIÓN"

solutions = {
    "8251": "1 + (8 * (5 - 2))",
    "6153": "SIN SOLUCIÓN",
    "9735": "(9 - 5) + (7 * 3)",
    "1821": "1 + (8 * (2 + 1))",
    "3515": "5 + (5 * (3 + 1))",
    "2365": "(2 + 5) + (3 * 6)",
    "4249": "9 + (2 * (4 + 4))",
    "2544": "SIN SOLUCIÓN",
    "2837": "(8 + 3) + (2 * 7)",
    "8716": "SIN SOLUCIÓN",
    "1669": "SIN SOLUCIÓN",
    "7191": "7 + (9 * (1 + 1))",
    "1259": "5 + (2 * (1 + 9))",
    "1674": "7 + (6 * (4 - 1))",
    "2897": "SIN SOLUCIÓN",
    "4519": "9 + (4 * (5 - 1))",
    "4667": "(7 - 6) + (4 * 6)",
    "4716": "7 + (6 * (4 - 1))",
    "4215": "5 * (4 + (2 - 1))",
    "1331": "SIN SOLUCIÓN",
    "4349": "(4 + 9) + (3 * 4)",
    "7179": "SIN SOLUCIÓN",
    "8722": "(7 + 2) + (8 * 2)",
    "5517": "((7 - 1) * 5) - 5",
    "4416": "4 * (6 + (1 / 4))",
    "9135": "(9 + 1) + (3 * 5)",
    "4448": "SIN SOLUCIÓN",
    "5513": "5 + (5 * (1 + 3))",
    "3899": "(3 * 8) + (9 / 9)",
    "3396": "(3 * 9) - (6 / 3)",
    "6956": "SIN SOLUCIÓN",
    "8779": "SIN SOLUCIÓN",
    "6477": "7 + (6 * (7 - 4))",
    "2663": "SIN SOLUCIÓN",
    "3476": "(7 + 6) + (3 * 4)",
    "7166": "SIN SOLUCIÓN",
    "8743": "(8 - 4) + (7 * 3)",
    "1888": "(1 + 8) + (8 + 8)",
    "3718": "((3 + 1) * 8) - 7",
    "4355": "(4 - 3) * (5 * 5)",
    "2723": "(2 + 2) + (7 * 3)",
    "2681": "1 + (6 * (8 / 2))",
    "3176": "1 + (6 * (7 - 3))",
    "9592": "(9 + 5) + (9 + 2)",
    "6173": "1 + (6 * (7 - 3))",
    "8755": "(8 + 7) + (5 + 5)",
    "1729": "9 + (2 * (1 + 7))",
    "3761": "1 + (6 * (7 - 3))",
    "5878": "((5 * 8) - 7) - 8",
    "9289": "((8 + 9) * 2) - 9",
    "9689": "SIN SOLUCIÓN",
    "6152": "5 * (6 + (1 - 2))",
    "7633": "3 * (6 + (7 / 3))",
    "7135": "(5 - 1) + (7 * 3)",
    "4523": "(2 + 3) + (4 * 5)",
    "8564": "SIN SOLUCIÓN",
    "9328": "((9 + 2) * 3) - 8",
    "1779": "SIN SOLUCIÓN",
    "5717": "SIN SOLUCIÓN",
    "5195": "5 * (1 + (9 - 5))",
    "5755": "((7 * 5) - 5) - 5",
    "7656": "5 * (6 + (6 - 7))",
    "9537": "(9 - 5) + (3 * 7)",
    "7329": "SIN SOLUCIÓN",
    "2692": "9 + (2 * (6 + 2))",
    "6674": "(7 - 6) + (6 * 4)",
    "3384": "(4 - 3) + (3 * 8)",
    "4698": "(9 - 8) + (4 * 6)",
    "3642": "(3 - 2) + (6 * 4)",
    "8239": "((2 + 9) * 3) - 8",
    "4921": "((4 + 9) * 2) - 1",
    "5179": "((5 * 7) - 9) - 1",
    "4277": "(4 + 7) + (2 * 7)",
    "4199": "SIN SOLUCIÓN",
    "5618": "SIN SOLUCIÓN",
    "8797": "SIN SOLUCIÓN",
    "9587": "9 + (8 * (7 - 5))",
    "1394": "9 + (4 * (1 + 3))",
    "4331": "1 + (4 * (3 + 3))",
    "2329": "3 + (2 * (2 + 9))",
    "7831": "((3 + 1) * 8) - 7",
    "2537": "5 + (2 * (3 + 7))",
    "6267": "(6 + 7) + (2 * 6)",
    "8739": "SIN SOLUCIÓN",
    "8153": "(8 - 3) * (1 * 5)",
    "7737": "SIN SOLUCIÓN",
    "5487": "(5 - 8) + (4 * 7)",
    "2373": "7 + (2 * (3 * 3))",
    "6861": "SIN SOLUCIÓN",
    "2237": "(2 + 2) + (3 * 7)",
    "7945": "(7 + 9) + (4 + 5)",
    "8685": "5 * (6 - (8 / 8))",
    "8983": "(9 - 8) + (8 * 3)",
    "7583": "(7 + 8) * (5 / 3)",
    "2446": "SIN SOLUCIÓN",
    "8237": "(8 + 3) + (2 * 7)",
    "4624": "SIN SOLUCIÓN",
    "1368": "(8 - 1) + (3 * 6)",
    "6448": "SIN SOLUCIÓN",
    "8885": "SIN SOLUCIÓN",
}

for key, value in solutions.items():
    result = compute25(key)
    

    if result == "SIN SOLUCIÓN" and value != "SIN SOLUCIÓN":
        print(f"El test para {key} fallo")
        break

    elif result != "SIN SOLUCIÓN" and eval(result) != 25:
        print(f"El test para {key} fallo")
        break