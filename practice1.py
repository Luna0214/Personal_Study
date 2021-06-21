# station = ("사당", "신도림", "인천공항")

# print(station[0] + "행 열차가 들어오고 있습니다")
# print(station[1] + "행 열차가 들어오고 있습니다")
# print(station[2] + "행 열차가 들어오고 있습니다")


# from random import *
# study = randint(4, 28)

# print("오프라인 스터디 모임 날짜는 매월 " + str(study) +"일로 선정되었습니다.")

# --------------------------------------------------------------------------------------

# url = "http://google.com"
# address = url.replace("http://", "")
# webtitle = address[ :address.index(".")]

# password = webtitle[:3] + str(len(webtitle)) + str(webtitle.count("e")) + "!"

# print("{0} 의 비밀번호는 {1} 입니다".format(url, password))

# --------------------------------------------------------------------------------------

# from random import *

# applicant = range(1, 21)
# applicant = list(applicant)

# shuffle(applicant)

# winners = sample(applicant, 4)

# print(" -- 당첨자 발표 --")
# print("치킨 당첨자 : {0}".format(winners[0]))
# print("당첨자 발표 : {0}".format(winners[1:]))
# print(" -- 축하합니다 --")

# --------------------------------------------------------------------------------------

# from random import *

# total = 0

# for i in range(1, 51):
#     time = randrange(5, 51)
#     if 5 <= time <= 15:
#         print("[O] {0}번째 고객: 소요시간: {1}".format(i, time))
#         total +=1
#     else:
#         print("[ ] {0}번째 고객: 소요시간: {1}".format(i, time))

# print("총 탑승인원: {0}".format(total))

# --------------------------------------------------------------------------------------   

# gender = input("성별?")
# height = int(input("키?"))

# def std_weight(height, gender):
#     if gender == "남자":
#         return height * height * 22
#     else:
#         return height * height * 21


# weight = round(std_weight(height / 100, gender), 2)

# print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))

# -------------------------------------------------------------------------------------- 
#내 정답
# n = 1
# while n in range(1, 51):
#     with open(str(n) + "주차파일.txt", "w", encoding="utf8") as report_file:
#         report_file.write("-" + str(n) + " 주차 주간보고 -")
#         report_file.write("\n부서 :")
#         report_file.write("\n이름 :")
#         report_file.write("\n업무 요약 :")
#     n = n + 1

#해설자 정답
# for i in range(1, 51):
#     with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
#         report_file.write("- {0} 주차 주간보고 -".format(i))
#         report_file.write("\n부서  :")
#         report_file.write("\n이름  :")
#         report_file.write("\n업무 요약:  :")

# -------------------------------------------------------------------------------------- 

# class House:
#     def __init__(self, location, building_type, deal_type, price, completion_year):
#         self.location = location
#         self.building_type = building_type
#         self.deal_type = deal_type
#         self.price = price
#         self.completion_year = completion_year      
#     def show_detail(self):
#         print(self.location, self.building_type, self.deal_type, self.price, self.completion_year)

# houses = []

# house1 = House("강남", "아파트", "매매", "10억", "2010년")
# house2 = House("마포", "오피스텔", "전세", "5억", "2007년")
# house3 = House("송파", "빌라", "월세", "500/50", "2000년")

# houses.append(house1)
# houses.append(house2)
# houses.append(house3)

# print("총 {0}개의 매물이 있습니다.".format(len(houses)))
# for House in houses:
#     House.show_detail()


# 총 3개의 매물이 있습니다.
# House("강남", "아파트", "매매", "10억", "2010년")
# House("마포", "오피스텔", "전세", "5억", "2007년")
# House("송파", "빌라", "월세", "500/50", "2000년")

# -------------------------------------------------------------------------------------- 

# chicken = 10
# waiting = 1
# class SoldOutError(Exception):
#     pass
    
# while(True):
#     try:
#         print("[남은 치킨 : {0}]".format(chicken))
#         order = int(input("치킨 몇 마리 주문하시겠습니까?"))
#         if order > chicken:
#             print("재료가 부족합니다.")
#         elif order <= 0:
#             raise ValueError
#         else:
#             print("[대기번호{0}] {1} 마리 주문이 완료되었습니다.".format(waiting, order))
#             waiting += 1
#             chicken -= order
#         if chicken == 0: raise SoldOutError
#     except ValueError:
#         print("잘못된 값을 입력하셨습니다.")
#     except SoldOutError:
#         print("재료가 소진되어 더 이상 주문을 받지 않습니다.")
#         break

# -------------------------------------------------------------------------------------- 
#모듈만들기
# import byme
# byme.sign()