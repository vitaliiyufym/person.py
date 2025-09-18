import math

# Отримання вхідних даних від користувача
a = int(input("Введіть перше ціле число (a): "))
b = int(input("Введіть друге ціле число (b): "))

# 1. Сума
sum_ab = a + b
print(f"Сума: {sum_ab}")

# 2. Різниця
diff_ab = a - b
print(f"Різниця: {diff_ab}")

# 3. Добуток
prod_ab = a * b
print(f"Добуток: {prod_ab}")

# 4. Середнє арифметичне
avg_arith = (a + b) / 2
print(f"Середнє арифметичне: {avg_arith}")

# 5. Середнє геометричне
# Використовуємо функцію sqrt() з модуля math для кореня
if a * b >= 0:
    avg_geom = math.sqrt(a * b)
    print(f"Середнє геометричне: {avg_geom}")
else:
    print("Середнє геометричне не можна обчислити для від'ємного добутку.")

# 6. Відстань (абсолютне значення різниці)
dist_ab = abs(a - b)
print(f"Відстань: {dist_ab}")

# 7. Максимум
max_ab = max(a, b)
print(f"Максимум: {max_ab}")

# 8. Мінімум
min_ab = min(a, b)
print(f"Мінімум: {min_ab}")

# 9. Сума квадратів
sum_squares = a**2 + b**2
print(f"Сума квадратів: {sum_squares}")

# 10. Квадрат суми
square_sum = (a + b)**2
print(f"Квадрат суми: {square_sum}")

# 11. а в степені b
power_ab = a**b
print(f"а в степені b: {power_ab}")