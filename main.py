def main():
    valid_characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '+', '-', 'x']
    equation = []
    input_equation = input('enter equation: ').lower()
    print(input_equation, '= 0')
    operator_index = []
    x_index = []
    x2_index = []
    first_term_used, second_term_used, third_term_used = False, False, False
    a, b, c = 0, 0, 0

    def isolating_equation():
        for character in input_equation:  # to eliminate any whitespaces
            if not character == ' ':
                equation.append(character)
        if not equation[0] == '-':  # to get positive or negative coefficient of first term
            equation.insert(0, '+')
        for index, character in enumerate(equation):
            if character == '+' or character == '-':
                operator_index.append([index, character])  # saving index of operators
            if character == 'x':
                if not index == len(equation) - 1:
                    if equation[index + 1] == '2' or equation[index + 1] == '²':  # index of x squared
                        x2_index.append(index)
                    else:
                        x_index.append(index)
                else:
                    x_index.append(index)

    def check():  # function to check if a valid equation was entered
        if equation[-1] == '+' or equation[-1] == '-':  # last character cannot be an operator
            return False
        if len(equation) < 6:  # minimum character length of a quadratic equation
            return False
        if not len(operator_index) == 3:  # there must be atleast 3 operator symbols including the positive negative
            # coefficient
            return False
        for index, i in enumerate(operator_index):  # two operators cannot be together
            if not index == len(operator_index) - 1:
                if i[index] == operator_index[index + 1][0] - 1:
                    return False
        if not len(x2_index) == 1 or not len(x_index) == 1:  # there cannot be more than one x squared or x term
            print(x_index, x2_index)
            return False
        for character in equation:
            if character not in valid_characters:  # characters must be number or operator
                return False
        return True

    def isolating_term(index, check):  # isolating the term
        term_str = ''
        if check:  # if check is False then the term is the third term hence the upper index should be the final number
            upper_index = operator_index[index + 1][0]
        else:
            upper_index = len(equation)
        for _ in range(operator_index[index][0] + 1, upper_index):
            if not equation[_] == ' ':  # to remove the blank spaces which were previously x and x2
                term_str += equation[_]  # add non operator characters to a string
        if not term_str:  # if no coeffecient was entered then it was 1
            term_str = 1
        number = float(term_str)
        if operator_index[index][1] == '-':  # if coefficient was negative the resultant number must be too
            number = number * -1
        return number

    isolating_equation()
    if check():
        x_index = x_index[0]  # convert list to the single integer value present in it
        x2_index = x2_index[0]
        equation[x2_index] = ' '  # converting x2 into blank space which our isolating_term function will remove
        equation[x2_index + 1] = ' '
        equation[x_index] = ' '

        if x2_index > operator_index[1][0]:
            if x2_index > operator_index[2][0]:
                a = isolating_term(2, False)
                third_term_used = True  # we have to keep track which terms are x2 and x terms,so we can deduce variable
                # term
            else:
                a = isolating_term(1, True)
                second_term_used = True
        else:
            a = isolating_term(0, True)
            first_term_used = True

        if x_index > operator_index[1][0]:
            if x_index > operator_index[2][0]:
                b = isolating_term(2, False)
                third_term_used = True
            else:
                b = isolating_term(1, True)
                second_term_used = True
        else:
            b = isolating_term(0, True)
            first_term_used = True

        if not first_term_used:  # term of constant is deduced based on
            c = isolating_term(0, True)
        if not second_term_used:
            c = isolating_term(1, True)
        if not third_term_used:
            c = isolating_term(2, False)

        round(a)
        round(b)
        round(c)

        discriminant = (b ** 2) - (4 * a * c)  # determining if real solutions, no real solutions, or one solution
        if discriminant >= 0:
            x1 = round((- b + (discriminant ** 0.5)) / (2 * a), 2)
            x2 = round((- b - (discriminant ** 0.5)) / (2 * a), 2)
            if x1 == x2:
                print('x is ', x1)
                print('ax² + bx + c')
                print(f"{a} * {x1}² + {b} * {x1} + {c}")
                print(f'{a*x1**2} + {b*x1} + {c}')
                print('0')
            else:
                print('x1 is', x1)
                print('ax² + bx + c')
                print(f"{a} * {x1}² + {b} * {x1} + {c}")
                print(f'{a * x1 ** 2} + {b * x1} + {c}')
                print('0')
                print('x2 is', x2)
                print('ax² + bx + c')
                print(f"{a} * {x2}² + {b} * {x2} + {c}")
                print(f'{a * x2 ** 2} + {b * x2} + {c}')
                print('0')

        else:
            discriminant = (discriminant * -1) ** 0.5
            print('x1 is', (-b / 2 / a), '+', discriminant / 2 / a, 'i')
            print('x2 is', (-b / 2 / a), '-', discriminant / 2 / a, 'i')
    else:  # if check fails, reenter equation
        print('Enter a valid quadratic equation')
        main()


main()
