items = {
    "사과" : {
        "type" : "과일",
        "description" : "apple is apple",
        "price" : 2000
    },
    "수박" : {
        "type" : "과일",
        "description" : "watermalone",
        "price" : 10000
    },
    "바나나" : {
        "type" : "과일",
        "description" : "banana",
        "price" : 3000
    },
    "청사과" : {
        "type" : "과일",
        "description" : "greenApple",
        "price" : 2000
    }
}


for i in items.keys():
    print(f"{i}({items[i]["type"]}): {items[i]["price"]}원")
    print(f"ㄴ {items[i]["description"]}")
    print()


'''
은교햄.가격() -> "특별가격"
은교햄.과() -> "콘텐츠디자인과"

은교햄.출력(임시 : 은교햄.가격());
>> 특별가격
'''