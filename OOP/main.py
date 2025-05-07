# class Hello:
#     def hello_world(self):
#         print("Hello, World!")

# a = Hello()
# a.hello_world()

# class Star:
#     def star_pyramid(self, num : int) -> None: 
#         for i in range(1,num+1):
#             print("*"*i)

# star = Star()
# star.star_pyramid(10)

# class Member:
#     def __init__(self, name : str):
#         self.name = name

#     def member_me(self):
#         print(f"My name is {self.name}")

# member = Member("hanul")
# member.member_me()

# class MyInfo:
#     def __init__(self, name : str, age : int, address : str):
#         self.name = name
#         self.age = age
#         self.address = address

#     def __str__(self) -> str:
#         return f"저의 이름은 {self.name}이고, 나이는 {self.age}살, 사는곳은 {self.address}입니다."

# a = MyInfo("hanul",17,"seoul")
# print(a)

# Bread 클래스 생성 -> name, price, stock 총 3개의 매개변수 생성 -> 
# -> stock 개수가 0개이면 "재고가 없습니다." 출력, 아니면 "구매해주셔서 감사합니다." 출력
class Bread:
    def __init__(self, name : str, stock : int):
        self.name = name
        self.stock = stock

    def __str__(self) -> str:
        if self.stock <= 0:
            return f"재고가 없습니다."
        else :
            self.stock -= 1
            return f"구매해주셔서 감사합니다."
        
    def __add__(self, stock):
        print(f"{self.name}을 {stock}개 만들었습니다.")
        self.stock += stock
        return self
    
class Bun(Bread):
    def __init__(self, name, stock, inside):
        super().__init__(name, stock)
        self.inside = inside

    def __add__(self, stock):
        print("만들기 실패!")
        
stock = int(input("stock: "))
bread = Bread("빵ㅋㅋㅋ", stock)
bread += 2
print(bread)
print()

bun = Bun("빵ㅋㅋ", stock, "농ㅋㅋㅋ")
bun + 2
for i in range(5):
    print(bun)