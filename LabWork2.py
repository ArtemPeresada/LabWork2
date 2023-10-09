# Зчитуємо ціле число від користувача
user_input = input ("Введіть довільне ціле число: ")

# Перевіряємо, чи ввід є коректним цілим числом
if user_input.isdigit():
   
    for i in user_input:
        number = int(i)
        histogram_row = "#" * number
        print(histogram_row)
else:
    print("Некоректний ввід. Введіть ціле число.")