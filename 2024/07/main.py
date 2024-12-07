def read_input(file_path):
    with open(file_path, "r") as f:
        return f.read()


def op_iter(sum, test_value, numbers, op):
    if sum > test_value:
        return 0

    if len(numbers) == 0:
        return sum if sum == test_value else 0

    next = numbers.pop()
    if op == "+":
        calc = sum + next
    elif op == "*":
        calc = sum * next
    elif op == "||":
        calc = int(str(sum) + str(next))

    op1 = op_iter(calc, test_value, numbers.copy(), "+")
    op2 = op_iter(calc, test_value, numbers.copy(), "*")
    op3 = op_iter(calc, test_value, numbers.copy(), "||")
    if op1 == test_value:
        return op1
    elif op2 == test_value:
        return op2
    elif op3 == test_value:
        return op3
    else:
        return 0


def operation(test_value, numbers):
    res = numbers.pop()

    sum = op_iter(res, test_value, numbers.copy(), "+")
    prod = op_iter(res, test_value, numbers.copy(), "*")
    conc = op_iter(res, test_value, numbers.copy(), "||")
    if sum == test_value:
        return sum

    if prod == test_value:
        return prod

    if conc == test_value:
        return conc

    return 0


def main():
    input_data = read_input("input.txt")

    sum = 0
    for line in input_data.split("\n"):
        data = line.split(":")
        test_value = int(data[0].strip())
        numbers = [int(n) for n in data[1].strip().split(" ")]
        numbers.reverse()
        sum += operation(test_value, numbers)
    print(sum)  # 3749


if __name__ == "__main__":
    main()
