for num in range(100000):
    original_number = num
    result = 0
    num_digits = len(str(num))  # Count the number of digits in num

    # Calculate the sum of digits raised to the power of num_digits
    while num != 0:
        digit = num % 10  # Extract the last digit
        result += digit ** num_digits
        num //= 10  # Remove the last digit

    # If the sum is equal to the original number, print it
    if original_number == result:
        print(original_number)
