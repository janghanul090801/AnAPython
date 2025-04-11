# a = "N"
# b = True
# c = 10
# d = 10.2

# mix = [a,b,c,d]

# print(mix)

# a = ['Math','Science','History']
# b = ['P.E','Music','Art']

# subject = a+b

# aa = a*2

# print(subject, aa)

# #index

# print(subject[-1])
# print(subject[-6])

# #슬라이싱
# # arr[start:stop:step]

# print(subject[1:3])

# print(subject[5:1:-1])

# print(subject[::3])

# print(subject[::-1])

# k = [1,2,3,4,5,6,7,8,9,10]
# #[1,4,7]
# print(k[:-2:3])

# def fjlak(a,b,c):
#     return a,b,c

# print(tuple(fjlak(3,2,1)))

# subway = ["prodo","tube","apichi"]

# print(subway)

# print(subway.index("prodo"))

# subway.append("raiun")
# print(subway)

# subway.insert(3, 'chunsik2')
# print(subway)

# subway.append("chunsik2")
# print(subway)

# print(subway.count("chunsik2"))

# subway.clear()
# print(subway)

# li = [9,4,8,3,7]
# li.sort()
# print(li)

# li.reverse()
# print(li)

# s1 = set([2,3,4,5,6,7,7,7])
# # s1 = {2,3,4,5,6,7,7,7,7}
# print(s1)

# s2 = set("ana")
# print(s2)

# A = {1,2,3,4,5,6,7}
# B = {4,5,6,7,8,9,10}

# # intersection, & : 교집합
# C = A & B
# # C = A.intersection(B)
# print(C)

# # union, |
# C = A | B
# # C = A.union(B)
# print(C)

# # difference, -
# C = B - A
# # C = B.difference(A)
# print(C)

# A.add(100)
# print(A)

# A.update([100,101,102,103])
# print(A)

# A.remove(103)
# print(A)

# A.discard(102)
# print(A)

# # A.remove(35235)  # Error

# A.discard(35252)
# print(A)

# A.clear()
# print(A)

# age = input("how old are you?")
# print("You ar",age,"years old.")

text = "Python"
print(len(text))

x = 3.14
print(type(x))

num_str = "10"
num = int(num_str)
print(num + 5)

f = float("3.14")
print(14+f)

s = str(123)
print(s + "456")

numbers = [1,2,3,4,5]
total = sum(numbers)
print(total)

print(max(numbers))
print(min(numbers))

unsorted = [5,3,8,1]
sorted_list = sorted(unsorted)
print(sorted_list) 