import random

def rand_number(n: int) -> list:
    return [random.randint(1, n) for _ in range(n)]

def show(numbers: list) -> None:
    for number in numbers:
        print(number, end=' ')
    print()

#sortownie bombelkowe
def bubble_sort(numbers: list) -> list:
    n = len(numbers)
    for j in range(0, n - 1):
        for i in range(0, n - 1 - j):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
    return numbers

# sortowanie przez wybór
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

#sortowanie przez wstawianie
def insertion_sort(numbers: list) -> list:
    n = len(numbers)
    for j in range(n - 2, -1, -1):
        x = numbers[j]
        i = j + 1
        while i < n and x > numbers[i]:
            numbers[i-1] = numbers[i]
            i = i + 1
        numbers[i-1] = x
    return numbers



if __name__ == "__main__":
    numbers = rand_number(30)
    show(numbers)
    print("sortownie bombelkowe")
    show(bubble_sort(numbers))
    print("sortownie przez wybór")
    show(selection_sort(numbers))
    print("sortownie przez wstawianie")
    show(insertion_sort(numbers))

