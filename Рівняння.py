import math
a = float(input("Введіть число a: "))
b = float(input("ведіть число b: "))
c = float(input("Введіть число c: "))
discriminant = b**2 - 4*a*c
print(f"Дискримінант D = {discriminant:.2f}")
if a == 0:
    print("Ну тоді це не квадратне рівняння,ти що в школі не вчився? зміни число!")
elif discriminant >= 0:
    x1 = (-b + math.sqrt(discriminant)) / (2 * a)
    x2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print(f"x1 = {x1:.2f}")
    print(f"x2 = {x2:.2f}")
else:
    print("Подумай краще і напиши число b трошки побільше")

