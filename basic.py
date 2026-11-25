# for normal array
a = [1,2,3,4,5,6,7,7,8]
res = [num for num in a if num% 2 ==0]
print(res)

# for dict

res = {num: num**3 for num in range(1, 6)}
print(res)