#==== 조건문(분기) ====
# if 조건:
#     실행 명령문
# elif 조건:
#     실행 명령문
# elif 조건:
#     실행 명령문
# else:
#     실행 명령문

#==== 문자열 ====
weather = "비"    
if weather == "비":
    print("우산을 챙기세요")
    
weather = "미세먼지"    
if weather == "비":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
    
weather = "맑음"    
if weather == "비":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("즐거운 하루 되세요.")
    
weather = input("오늘 날씨는 어때요?")
if weather == "비" or weather == "눈":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("즐거운 하루 되세요.")
    
#==== 숫자 ====
temp = int(input("오늘의 기온은 몇도인가요? "))
if 30 <= temp: # temp >= 30
    print("너무 더워요. 나가지 마세요")
elif 10 <= temp and temp < 30: 
    print("나들이 하기 좋은 날씨입니다.")
elif 0 <= temp < 10:
    print("외투를 챙기세요")
else:
    print("너무 추워요. 나가지 마세요.")
    
