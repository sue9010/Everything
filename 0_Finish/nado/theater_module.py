def price(people):
    print("{0} 명의 일반 가격은 {1}원 입니다."\
        .format(people, people*10000))

def price_morning(people):
    print("{0} 명의 조조 할인 가격은 {1}원 입니다."\
        .format(people, people*6000))

def price_soldier(people):
    print("{0} 명의 군인 할인 가격은 {1}원 입니다."\
        .format(people, people*4000))