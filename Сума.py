user_input = input("Введіть 4-значне число: ")
total_sum = 0
for digit_char in user_input:
    total_sum += int(digit_char)
output_expression = " + ".join(user_input)
print(f"\n {output_expression} = {total_sum}")