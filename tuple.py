tp = ("사과", "바나나", "딸기")

apple, banana, strawberry = tp
print(apple)
print(banana)
print(strawberry)

def two(a,b,c) :
    return a*b, b*c

ab, bc = two(1,2,3)

print(ab, bc)

try:
    a = 2/0
    tp[0] = "은교햄"
except TypeError:
    print("오류1")
except ZeroDivisionError:
    print("오류2")

try :
    tp[0] = "대황은교햄"
except TypeError as e:
    print(f"오류 내용: {e}")
finally:
    print("끘")