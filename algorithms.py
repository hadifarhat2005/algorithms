def  factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
    
    
    
print(factorial(5))

# finding a maximum number in a list
numbers = [3, 7, 9, 5]
def find_max(list):
    max_val = list[0]
    for x in list:
        if x > max_val:
            max_val = x
    return max_val

print(find_max(numbers))        