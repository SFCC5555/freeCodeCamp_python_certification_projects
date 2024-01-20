# --Arithmetic Formatter--

def arithmetic_arranger(problems, answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    line_1_list = []
    line_2_list = []
    line_3_list = []
    line_4_list = []

    formatted_problems = [problem.split() for problem in problems]

    for number_1, operator, number_2 in formatted_problems:
        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        if len(number_1) > 4 or len(number_2) > 4:
            return "Error: Numbers cannot be more than four digits."
        try:
            number_1_digit = int(number_1)
            number_2_digit = int(number_2)

        except ValueError:
            return "Error: Numbers must only contain digits."

        answer = (
            str(number_1_digit + number_2_digit)
            if operator == "+"
            else str(number_1_digit - number_2_digit)
        )
        spaces = max(len(number_1), len(number_2)) + 2
        line_1_list.append(" " * (spaces - len(number_1)) + number_1)
        line_2_list.append(operator + " " * (spaces - len(number_2) - 1) + number_2)
        line_3_list.append("-" * spaces)
        line_4_list.append(" " * (spaces - len(answer)) + answer)

    line_1 = "    ".join(line_1_list)
    line_2 = "    ".join(line_2_list)
    line_3 = "    ".join(line_3_list)
    line_4 = "    ".join(line_4_list)

    arranged_problems = line_1 + "\n" + line_2 + "\n" + line_3
    arranged_problems += "\n" + line_4 if answers == True else ""

    return arranged_problems


if __name__ == "__main__":
    print(
        arithmetic_arranger(
            ["98 + 34", "3801 - 2", "45 + 43", "123 + 49"],
            True,
        )
    )
