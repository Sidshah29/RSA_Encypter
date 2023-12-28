# -----------------------------------------------------------------------
# FA 23 CMPSC 360 Extra Credit Assignment
# Base Conversion
# 
# Name: Siddharth Shah
# ID: 916270083
# 
# 
# -----------------------------------------------------------------------
def base_conversion(number: int, base: int) -> int:
    # Check if digits of the input number are less than the base
    if any(int(digit) >= base for digit in str(number)):
        return 'The input is wrong. Digits should be less than the base.'

    # Convert the number to base 10
    result = 0
    multiplier = 1

    while number > 0:
        digit = number % 10
        result += digit * multiplier
        multiplier *= base
        number //= 10

    return result

# Test cases
print(base_conversion(345, 7))  # Output: 180
print(base_conversion(239, 9))  # Output: 'The input is wrong. Digits should be less than the base.'
print(base_conversion(1011, 2))  # Output: 11
print(base_conversion(1234, 5))  # Output: 194
