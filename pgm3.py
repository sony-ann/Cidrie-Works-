def pair(nums, target):
    num_set = set()
    for i in num1:
        num = target - i
        if num in num_set:
            return(num, i)
        num_set.add(i)
    return None

num1 = range(1000001)
target = int(input("Enter the target sum: "))

result = pair(num1, target)

if result:
    print("Pair found", result)
else:
    print("No pair found")