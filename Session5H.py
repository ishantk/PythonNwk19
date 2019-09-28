# Passing Multi Value
def squareOfNumbers(numbers):
    print("** numbers is:", numbers, "and HashCode is:", hex(id(numbers)))

    for i in range(0, len(numbers)):
        numbers[i] = numbers[i] * numbers[i]

    print("** numbers now is:",numbers, "and HashCode is:",hex(id(numbers)))


nums = [1, 3, 5, 7, 9]
print(">> nums is:", nums, "and HashCode is:", hex(id(nums)))
print(">> nums[0] is:", nums[0], "and HashCode is:", hex(id(nums[0])))
print(">> nums[1] is:", nums[1], "and HashCode is:", hex(id(nums[1])))

squareOfNumbers(nums)

print(">> nums now is:", nums, "and HashCode is:", hex(id(nums)))

print(">> nums[0] is:", nums[0], "and HashCode is:", hex(id(nums[0])))
print(">> nums[1] is:", nums[1], "and HashCode is:", hex(id(nums[1])))


