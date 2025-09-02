import random

def rand_number(n: int) -> list:
    return [random.randint(1, n) for _ in range(n)]

def show(numbers: list) -> None:
    for number in numbers:
        print(number, end=' ')
    print()

def bubble_sort(numbers: list) -> list:
    n = len(numbers)
    for j in range(0, n - 1):
        for i in range(0, n - 1 - j):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
    return numbers

def selection_sort(numbers: list) -> list:
    n = len(numbers)
    for j in range(0, n-1):
        p_min = j
        i = j + 1
        if i <= n:
            if numbers[i] < numbers[p_min]:
                p_min = i
        else:
            numbers[p_min], numbers[j] = numbers[j], numbers[p_min]
    return numbers

if __name__ == "__main__":
    numbers = rand_number(30)
    show(numbers)
    print("sortownie bombelkowe")
    print(bubble_sort(numbers))
    print("sortownie przez wybór")
    print(selection_sort(numbers))

