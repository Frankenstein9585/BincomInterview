import random


def binary_search(haystack: list[int], needle: int, left: int, right: int) -> int:
    if left > right:
        return -1

    mid = (left + right) // 2

    if haystack[mid] == needle:
        return mid

    elif haystack[mid] < needle:
        return binary_search(haystack, needle, mid + 1, right)

    else:
        return binary_search(haystack, needle, left, mid - 1)


def binary_to_decimal() -> int:
    # Generate random binary string
    binary_string = ""
    base10_value = 0
    for i in range(4):  # 4 digits binary string
        bit = str(random.randint(0, 1))
        binary_string += bit
    print(binary_string)

    # Convert Binary string to base 10
    size = len(binary_string)
    for i in range(size):
        base10_value += int(binary_string[i]) * (2 ** (size - i - 1))
    return base10_value


def fibonacci_sum():
    fib_list = [0, 1]
    for i in range(2, 50):
        next_value = fib_list[i - 1] + fib_list[i - 2]
        fib_list.append(next_value)
    return sum(fib_list)

