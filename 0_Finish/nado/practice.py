# customer ='토르'
# index = 5
# while index >=1:
#     print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요".format(customer,index))
#     index -=1
#     if index ==0:
#         print("커피는 폐기처분 되었습니다.")

# customer = '아이언맨'
# index =1
# while True:
#     print("{0}, 커피가 준비 되었습니다. 호출 {1}회".format(customer, index))
#     index += 1

# customer ='토르'
# person = 'Unknown'

# while person != customer:
#     print("{0}, 커피가 준비 되었습니다. ".format(customer))
#     person = input("이름이 어떻게 되세요?")
    

# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")
# print("대기번호 : 5")

# for waiting_no in range(1,6):
#     print("대기번호 : {0}".format(waiting_no))


# starbucks = ["아이언맨","토르","그루트"]
# for customer in starbucks:
#     print("%s, 커피가 준비 되었습니다." % customer)

# Random 함수

# from random import *
# from re import sub

# print(random())
# print(random()*10)
# print(int(random()*10))
# print(int(random()*10))
# print(int(random()*10))

# print(int(random()*45)+1)
# print(int(random()*45)+1)
# print(int(random()*45)+1)
# print(int(random()*45)+1)
# print(int(random()*45)+1)
# print(int(random()*45)+1)

# print(randrange(1,46))
# print(randrange(1,46))
# print(randrange(1,46))
# print(randrange(1,46))
# print(randrange(1,46))
# print(randrange(1,46))

# print(randint(1,45))

# a = str(randint(4,28))

# print("오프라인 스터디 모임 날짜는 매월 "+a+" 일 로 선정되었습니다.")

# sentence= '나는 소년입니다.'
# print(sentence)
# sentence2 = "파이썬은 쉬워요"
# print(sentence2)
# sentence3 = """나는 소년이고, 
# 파이썬은 쉬워요"""
# print(sentence3)

# jumin = "990120-1234567"
# print("성별: " + jumin[7])
# print("연: " +jumin[0:2])
# print("월: "+jumin[2:4])

# print("생년월일: " + jumin[:6])
# print("뒤 7자리: " + jumin[7:])
# print("뒤 7자리(뒤에서부터): " + jumin[-7:])

# python = "Python is amazing"
# print(python.lower())
# print(python.upper())
# print(python[0].isupper())
# print(len(python))
# print(python.replace("Python","Java"))

# index = python.index("n")
# print(index)
# index = python.index("n", index +1)
# print(index)

# print(python.find("Java"))
# print(python.index("Java"))

# print("나는 %d 살 입니다." % 20) # 정수
# print("나는 %s 을 좋아해요" % "파이썬") # str
# print("Apple 은 %c 로 시작해요" % "A") # 1개 charactor
# print("나는 %s색과 %s색을 좋아해요" % ("빨간","파란"))

# print("나는 {}살입니다.".format(20))
# print("나는 {}색과 {}색을 좋아해요".format("빨간","파란"))
# print("나는 {0}색과 {1}색을 좋아해요".format("빨간","파란"))
# print("나는 {1}색과 {0}색을 좋아해요".format("빨간","파란"))

# print("나는 {age}살이며, {color}색을 좋아해요".format(age=20, color="빨간"))
# age = 20
# color = "빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요")

# print("백문이 불여일견 \n백견이 불여일타") # \n 줄바꿈
# print("저는 '나도코딩' 입니다.")
# print('저는 "나도코딩" 입니다.')
# print("저는 \"나도코딩\" 입니다.") # \" \' 문장 내에서 " '로 사용 할 수 있음
# print("c:\\Users\\Sue")

# print("Red Apple\rPine") # \r 커서를 맨 앞으로 이동

# print("Redd\bApple") #\b 백스페이스(한 글자 삭제)

# print("Red\tApple") # \t 탭


# url = "http://naver.com"
# url = "http://youtube.net"

# print(address[7:])
# print(address[7:12])
# a = address[7:10]
# b = len(address[7:12])
# c = address.count('e')
# print(a+str(b)+str(c)+"!")

# my_str = url.replace("http://","")
# my_str = my_str[:my_str.index(".")]
# password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
# print("{0}의 비밀번호는 {1}입니다.".format(url, password))


# subway = [10,20,30]
# print(subway)

# subway = ["유재석","조세호","박명수"]
# print(subway)
# print(subway.index("조세호"))

# subway.append("하하")
# print(subway)

# subway.insert(1,"정형돈")
# print(subway)

# subway.pop()
# print(subway)

# subway.pop()
# subway.pop()
# subway.pop()
# print(subway)

# subway.append("유재석")
# subway.append("유재석")
# print(subway)

# print(subway.count("유재석"))


# 정렬도 가능
# num_list = [5,2,4,3,1]
# num_list.sort()
# print(num_list)

# 순서 뒤집기
# num_list.reverse()
# print(num_list)

# 모두 지우기
# num_list.clear()
# print(num_list)

# 다양한 자료형 사용 가능
# mix_list = ['조세호',20, True]
# print(mix_list)

# 리스트 확장
# num_list.extend(mix_list)
# print(num_list)

# 사전, Dictionary
# cabinet = {3:"유재석", 100:"김태호"}
# print(cabinet[3])
# print(cabinet[100])

# print(cabinet.get(3))
# print(cabinet[5]) #오류가 뜨고, 뒤 코드는 실행되지 않음
# print(cabinet.get(5)) # None 이라고 표기되고 뒤 코드가 실행 됨
# print(cabinet.get(5,"사용 가능")) # key 값이 없을 경우, 뒤에 표기된 문자열이 표기 됨
# print("hi")

# print(3 in cabinet)
# print(5 in cabinet)

# cabinet = {"A-3":"유재석", "B-100":"김태호"}
# print(cabinet["A-3"])

# cabinet["C-20"]="조세호" # 새 key 를 만들고 값을 넣음. 만약 key 가 존재한다면 값을 업데이트 함
# print(cabinet)

# cabinet["C-20"]="김종국"
# print(cabinet)

# del cabinet["A-3"] # key 삭제
# print(cabinet)

# print(cabinet.keys()) # key 들만 출력
# print(cabinet.values()) # 값들만 출력
# print(cabinet.items()) # key, 값 쌍으로 출력

# cabinet.clear() # 모든 값 삭제
# print(cabinet)

# 튜플, Tuple
# menu = ("돈가스", "치즈가스")
# print(menu[0])
# print(menu[1])

# menu.add("생선가스") # 값 추가 불가능

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)

# (name, age, hobby) = ("김종국", 20, "코딩")
# print(name, age, hobby)

# # 집합 , Set
# # 중복이 안 되고 순서가 없음
# my_set = {1,2,3,3,3}
# print(my_set)

# java = {"유재석","김태호","양세형"}
# python = set(["유재석","박명수"])

# # 교집합 (java 와 python을 모두 할 수 있는 사람)
# print(java & python)
# print(java.intersection(python))

# # 합집합 (java 나 python 중 하나라도 할 수 있는 사람)
# print(java|python)
# print(java.union(python))

# # 차집합 (java는 할 수 있지만 python은 할 줄 모르는 사람)
# print(java - python)
# print(java.difference(python))

# # python 할 줄 아는 사람이 늘어남
# python.add("김태호")
# print(python)

# # java를 잊었어요
# java.remove("김태호")
# print(java)

# # 자료구조의 변경
# # 커피숍
# menu = {"커피","우유","주스"}
# print(menu, type(menu))

# menu = list(menu)
# print(menu, type(menu))

# menu = tuple(menu)
# print(menu, type(menu))

# menu = set(menu)
# print(menu, type(menu))

# #내가 짠거.....실패

# from random import *

# id = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# chicken = randint(1,20)
# id.remove(chicken)
# shuffle(id)
# coffee= sample(id,3)

# print(chicken)
# print(coffee)

# print("""-- 당첨자 발표 --
# 치킨 당첨자: {0}
# 커피 당첨자: {1}
# -- 축하합니다 --""",format(chicken,coffee))


# # 정답

# from random import *
# users = range(1,21)
# users = list(users)
# shuffle(users)

# winners = sample(users,4)

# print("-- 당첨자 발표 --")
# print("치킨 당첨자: {0}".format(winners[0]))
# print("커피 당첨자: {0}".format(winners[1:]))
# print("-- 축하합니다 --")


# 분기
# weather = input("오늘 날씨는 어때요?")
# if weather=="비" or weather == "눈":
#     print("우산을 챙기세요") 
# elif weather =="미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요")

# temp = int(input("기온은 어때요?"))
# if 30 <= temp:
#     print("너무 더워요, 나가지 마세요")
# elif 10<= temp and temp <30:
#     print("괜찮은 날씨에요")
# elif 0 <= temp <10:
#     print("외투를 챙기세요")
# else:
#     print("너무 추워요, 나가지 마세요")

# 반복문, for

# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")
# print("대기번호 : 5")
# print("대기번호 : 6")

# for i in range(1,11):
#     print("대기번호: {0}".format(i))

# starbucks = ['Ironman','Thor','Grut']
# for customer in starbucks:
#     print("{0}, 커피가 준비되었습니다.".format(customer)) 

# # continue and break
# absent = [2,5] # 결석
# no_book = [7] # 책을 안 가져옴
# for student in range (1,11):
#     if student in absent:
#         continue # 해당 경우에는 skip 하고 다음 반복으로 넘어감
#     elif student in no_book:
#         print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
#         break # 해당 경우에는 반복문을 멈춤. 다음 문장을 실행하지 않음.
#     print("{0}, 책을 읽어봐".format(student))

# 한 줄 for 문
# # 출석번호가 1,2,3,4 앞에 100을 붙이기로 함
# students = [1,2,3,4,5]
# print(students)
# students = [i+100 for i in students]
# print(students)

# # 학생 이름을 길이로 변환
# students = ['Iron man','Thor','Groot']
# students = [len(i) for i in students]
# print(students)

# students = ['Iron man','Thor','Groot']
# students = [i.upper() for i in students]
# print(students)

# 퀴즈
# 당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오

# 조건1: 승객별 운행 소요 시간은 5분~50분 사이의 난수로 정해집니다.
# 조건2: 당신은 소요 시간 5분~15분 사이의 승객만 매칭해야 합니다.

# 출력문 예제
# [O] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# [O] 3번째 손님 (소요시간 : 5분)
# ...
# [ ] 50번째 손님 (소요시간 : 16분)

# from random import randrange

# total =0

# for customer in range(1,51):
#     t = randrange(5,51)
#     if t <=15 and t >=5:
#         print("[O] {0}번째 손님 (소요시간: {1}분)".format(customer, t))
#         total += 1 
#     else:
#         print("[ ] {0}번째 손님 (소요시간: {1}분)".format(customer, t))

# print("총 탑승 승객 : %s분" % total)


### 함수###
# def open_account():
#     print("새로운 계좌가 생성되었습니다.")

# open_account()

# def deposit(balance, money):
#     print("입금이 완료되었습니다. 잔액은 {} 원입니다.".format(balance + money))
#     return balance + money

# def withdraw(balance, money):
#     if balance >= money:
#         print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
#         return balance - money
#     else:
#         print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
#         return balance

# def withdraw_night(balance, money):
#     commission = 100
#     return commission, balance - money - commission


# balance = 0
# balance = deposit(balance,1000)
# # balance = withdraw(balance,500)
# commission, balance = withdraw_night(balance,500)
# print("수수료는 {0} 원이며, 잔액은 {1} 원입니다.".format(commission, balance))

# def profile(name,age,main_lang):
#     print("이름: {0} \t나이: {1} \t주 사용 언어: {2}"\
#         .format(name,age,main_lang))

# profile("유재석",20,"Python")
# profile("김태호",25,"Java")

# 같은 학교, 같은 학년, 같은 반 , 같은 수업

# def profile(name,age=17,main_lang="파이썬"):
#     print("이름: {0} \t나이: {1} \t주 사용 언어: {2}"\
#         .format(name,age,main_lang))

# profile("유재석")
# profile("김태호")

# # 키워드 값
# def profile(name,age,main_lang):
#     print(name,age,main_lang)

# profile(name="유재석", main_lang="파이썬",age=20)
# profile( main_lang="자바",name="김태호",age=25)

# 가변인자를 이용한 함수 호출
# def profile(name, age, lang1, lang2, lang3, lang4,lang5):
#     print("이름: {0}\t나이: {1}\t".format(name,age),end=" ")
#     print(lang1,lang2,lang3,lang4,lang5)

# def profile(name, age, *language):
#     print("이름: {0}\t나이: {1}\t".format(name,age),end=" ")
#     for lang in language:
#         print(lang, end =" ")
#     print()

# profile("유재석",20, "Python","Java","C","C#","C++","Javascript")
# profile("김태호",25, "Kotlin","Swift")

# 지역변수와 전역변수
# 지역변수: 함수 내에서만 사용 가능한 변수
# 전역변수: 프로그램 전체에서 사용 가능한 변수

# gun = 10 # 얘는 전역변수

# def checkpoint(soldiers):
#     # gun = 20  # 얘는 지역 변수
#     global  gun # 전역변수를 함수 내에서 사용하겠다는 뜻
#     gun = gun -soldiers
#     print("[함수 내] 남은 총: {0}".format(gun))

# def checkpoint_ret(gun, soldiers):
#     gun = gun - soldiers
#     print("[함수 내] 남은 총: {0}".format(gun))
#     return gun

# print("전체 총: {0}".format(gun))
# # checkpoint(2)
# gun = checkpoint_ret(gun,2)
# print("남은 총:{0}".format(gun))

# 퀴즈
# 표준 체중을 구하는 프로그램을 작성하시오

# 표준 체중: 각 개인의 키에 적당한 체중

# 성별에 따른 공식
# 남자 : 키(m) x 키(m)x22/10000
# 여자 : 키(m) x 키(m)x21/10000

# 조건1: 표준 체중은 별도의 함수 내에서 계산
#           *함수명: std_weight
#           *전달값: 키(height), 성별(gender)
# 조건2: 표준 체중은 소수점 둘째자리까지 표시

# (출력 예제)
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.

# def std_weight(height,gender):
#     if gender == "남자":
#         return height*height*22
#     else:
#         return height*height*21

# height = 160
# gender = "여자"
# weight = round(std_weight(height/100,gender),2)

# print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height,gender,weight))

# 표준 입출력
# print("Python"+"Java")
# print("Python","Java","Javascript", sep=" vs ")
# print("Python","Java","Javascript", sep=",", end="?")
# print("무엇이 더 재밌을까요?")

# import sys
# print("Python","Java",file=sys.stdout)
# print("Python","Java",file=sys.stderr)

# scores ={"수학":0,"영어":50,"코딩":100}
# for subject, score in scores.items():
#     # print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4), sep=":")
#     # ljust(number) number 수 만큼 공간을 확보하고, left로 정렬
#     # rjust(number) number 수 만큼 공간을 확보하고, right로 정렬

# 은행 대기 순번표
# 001,002,003...
# for num in range(1,21):
#     print("대기번호: "+str(num).zfill(3))
#     # zfill(number) number 자리 수 만큼 0을 채움

# 표준 입력
# answer = input("아무 값이나 입력하세요:")
# answer= 10
# print(type(answer))
# print("입력하신 값은 "+answer+"입니다")
# input으로 받으면 모두 str로 출력됨

# 빈 자리는 빈 공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
# print("{0: >10}".format(500))

# 양 수일때는 +로 표시, 음 수일때는 -로 표시
# print("{0: >+10}".format(-500))
# print("{0: >+10}".format(500))

# # 왼쪽 정렬하고, 빈칸은 _로 채움
# print("{0:_<10}".format(500))
# # 3자리 마다 콤마를 찍어주기
# print("{0:,}".format(100000000))
# # 3자리 마다 콤마를 찍어주기 with +/- 부호
# print("{0:+,}".format(100000000))
# # 3자리 마다 콤마 찍고, 부호 붙이고, 자릿수 확보
# # 빈 자리는 ^로 채우기
# print("{0:^<+30,}".format(1000000000))
# # 소수점 출력
# print("{0:f}".format(5/3))
# # 소수점 특정 자리수 까지만 출력
# print("{0:.2f}".format(5/3))

# 파일 입출력
# score_file = open("score.txt","w",encoding="utf-8") #파일 만들기, 기존 파일이 있다면 덮어쓰기, 자동 줄바꿈 적용
# print("수학:0", file=score_file)
# print("영어:50", file=score_file)
# score_file.close()

# score_file =open("score.txt", "a", encoding="utf-8") #기 존재하는 파일에 내용 추가 a = append
# score_file.write("과학:80")
# score_file.write("\n코딩:100")
# score_file.close()

# score_file = open("score.txt","r",encoding="utf-8")
# print(score_file.read()) #파일 내용 전체 읽어오기
# score_file.close()

# score_file = open("score.txt","r",encoding="utf-8")
# print(score_file.readline()) # 한 줄을 읽어오고 커서를 다음 줄로 이동
# print(score_file.readline(), end="")   # 한 줄을 읽어오고 줄 바꿈 안 함
# print(score_file.readline())
# print(score_file.readline())
# score_file.close()

# # 내용이 몇 줄인지 모를 때
# score_file = open("score.txt","r",encoding="utf-8")
# while True:
#     line = score_file.read()
#     if not line: # 읽어온 내용이 없을 때 , 프로그램 종료
#         break
#     print(line)
# score_file.close()

# score_file = open("score.txt","r",encoding="utf-8")
# lines = score_file.readlines() # list 형태로 저장
# for line in lines:
#     print(line, end="")
# score_file.close()

# pickle
# import pickle
# profile_file = open("profile.pickle","wb") # wb = write + 바이너리
# profile = {"이름":"박명수","나이":30,"취미":["축구","골프","코딩"]}
# print(profile_file)
# pickle.dump(profile, profile_file)
# profile_file.close()

# profile_file = open("profile.pickle","rb") # rb = read + 바이너리
# profile = pickle.load(profile_file)
# print(profile)
# profile_file.close()

# with
# import pickle
# with open("profile.pickle","rb") as profile_file:
#     print(pickle.load(profile_file))  # 별도로 close 해 주지 않아도 됨

# with open("study.txt","w",encoding="utf-8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어오")

# with open("study.txt","r",encoding="utf-8") as study_file: 
#     print(study_file.read())


# 퀴즈
# 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
# 보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

# - X 주차 주간보고 -
# 부서:
# 이름:
# 업무 요약:

# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오

# 조건: 파일명은 '1주차.txt', '2주차.txt', ...와 같이 만듭니다.

score_file = open("score.txt","w",encoding="utf-8")

# # 내가 만든 파일 (정상 작동 함 ㅡㅡ...)
# for week in range(1,51):
#     report_file = open("{0}주차.txt".format(week),"w", encoding="utf-8")
#     print("--{0}주차 주간보고--".format(week), file=report_file)
#     print("부서:".format(week), file=report_file)
#     print("이름:".format(week), file=report_file)
#     print("업무 요약:".format(week), file=report_file)
#     report_file.close() 

# # 정답
# for i in range(1,51):
#     with open(str(i)+"주차.txt","w",encoding="utf-8") as report_file:
#         report_file.write("-{0}주차 주간보고-".format(i))
#         report_file.write("\n부서:")
#         report_file.write("\n이름:")
#         report_file.write("\n업무 요약:")


# Class *****중요*****


# # 마린: 공격 유닛, 군인. 총을 쏠 수 있음
# name = "marine" # 유닛
# hp = 40 # 유닛의 체력
# damage = 5 # 유닛의 공격력

# print("{0} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp,damage))
# # 탱크: 공격 유닛, 탱크. 포를 쏠 수 있는데, 일반 모드 / 시즈 모드
# tank_name = "tank"
# tank_hp=150
# tank_damage =35
# print("{0} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp,tank_damage))

# # tank 1대 추가
# tank2_name = "tank"
# tank2_hp=150
# tank2_damage =35
# print("{0} 유닛이 생성되었습니다.".format(tank2_name))
# print("체력 {0}, 공격력 {1}\n".format(tank2_hp,tank2_damage))

# def attack(name, location, damage):
#     print("{0}:{1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(name,location, damage))

# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)
# attack(tank2_name, "1시", tank2_damage)

# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage =damage
#         print("{0} 유닛이 생성되었습니다.".format(self.name)) #self.name, self.hp, self.damage => 멤버 변수, class 밖에서도 사용 가능
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# # # marine1 = Unit ("마린", 40, 5)
# # # marine2 = Unit ("마린", 40, 5)
# # # tank = Unit ("탱크", 150, 35)


# # # 멤버 변수
# # # 레이스: 공중 유닛, 비행기. 클로킹 (상대방에서 보이지 않음)
# # wraith1 = Unit("레이스",80, 5)
# # print("유닛 이름: {0}, 공격력: {1}".format(wraith1.name, wraith1.damage))

# # # 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (빼앗음)
# # wraith2 = Unit("빼앗은 레이스",80,5)
# # wraith2.clocking = True

# # if wraith2.clocking == True:
# #     print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))

# class AttackUnit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage =damage

#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
#             .format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0}: 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <=0:
#             print("{0}: 파괴되었습니다.".format(self.name))

# # 파이어뱃: 공격 유닛, 화염방사기
# firebat1 = AttackUnit("파이어뱃",50,16)
# firebat1.attack("5시")
# #공격 2번 받음
# firebat1.damaged(25)
# firebat1.damaged(25)

# 상속
# 메딕 : 의무병



# class Unit:
#     def __init__(self, name, hp):
#         self.name = name
#         self.hp = hp

# class AttackUnit(Unit):
#     def __init__(self, name, hp, damage):
#         Unit.__init__(self,name, hp)
#         self.damage =damage

#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
#             .format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0}: 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <=0:
#             print("{0}: 파괴되었습니다.".format(self.name))

# # # 파이어뱃: 공격 유닛, 화염방사기
# # firebat1 = AttackUnit("파이어뱃",50,16)
# # firebat1.attack("5시")
# # #공격 2번 받음
# # firebat1.damaged(25)
# # firebat1.damaged(25)

# # 다중 상속

# # 드랍쉽: 공중 유닛, 수송기. 마린/파이어뱃/탱크 등을 수송. 공격 x

# # 날 수 있는 기능을 가진 클래스
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print("{0}:{1} 방향으로 날아갑니다. [속도 {2}]"\
#             .format(name, location, self.flying_speed))

# # 공중 공격 유닛 클래스
# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, damage)
#         Flyable.__init__(self, flying_speed)

# # 발키리: 공중 공격 유닛, 한 번에 14발 미사일을 발사. 
# valkyrie = FlyableAttackUnit("발키리",200,6,5)
# valkyrie.fly(valkyrie.name, "3시")



# # 예외 처리

# try:
#     print("나누기 전용 계산기입니다.")
#     nums = []
#     nums.append(int(input("첫 번째 숫자를 입력하세요: ")))
#     nums.append(int(input("두 번째 숫자를 입력하세요: ")))
#     # nums.append(int(nums[0]/nums[1]))
#     print("{0}/{1}={2}".format(nums[0], nums[1], nums[2]))
# except ValueError:
#     print("에러! 잘못된 값을 입력하였습니다.")
# except ZeroDivisionError as err:
#     print(err)
# except Exception as err:
#     print("알 수 없는 오류가 발생하였습니다.")
#     print(err)

# # 에러 발생시키기
# try: 
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요: "))
#     num2 = int(input("두 번째 숫자를 입력하세요: "))
#     if num1 >=10 or num2 >=10:
#         raise ValueError
#     print("{0}/{1}={2}".format(num1, num2, int(num1/num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요")

# # 사용자 정의 예외 처리

# class BigNumberError(Exception):
#     def __init__(self, msg):
#         self.msg = msg
#     def __str__(self):
#         return self.msg

# try: 
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요: "))
#     num2 = int(input("두 번째 숫자를 입력하세요: "))
#     if num1 >=10 or num2 >=10:
#         raise BigNumberError("입력값 : {0}, {1}".format(num1, num2)) 
#     print("{0}/{1}={2}".format(num1, num2, int(num1/num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요")
# except BigNumberError as err:
#     print("에러가 발생 하였습니다. 한 자리 숫자만 입력하세요")
#     print(err)
# finally:
#     print("계산기를 이용해 주셔서 감사합니다.")
# # finally

# import

# import travel.thailand #module 이나 package 만 가능, class 나 def는 불가능
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage #class , def 도 가능
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

#__all__

# from travel import *
# # trip_to = vietnam.VietnamPackage()
# # trip_to.detail()

# trip_to = thailand.ThailandPackage()
# trip_to.detail()

# import inspect
# import random
# print(inspect.getfile(random))
# print(inspect.getfile(thailand))

