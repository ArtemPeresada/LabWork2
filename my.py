# Введення масиву з клавіатури
input_array = []
n = int(input("Введіть розмірність масиву (N): "))
for _ in range(n):
    row = list(map(int, input("Введіть рядок чисел через пробіл: ").split()))
    input_array.append(row)

# Знаходження сум чисел у кожному рядку
sums = []
for row in input_array:
    row_sum = sum(row)
    sums.append(row_sum)

# Сортування масиву за сумами рядків
sorted_array = [x for _, x in sorted(zip(sums, input_array))]

# Виведення відсортованого масиву
print("Відсортований масив:")
for row in sorted_array:
    print(row)