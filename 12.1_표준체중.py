# 문제) 키에 따른 적절한 체중을 구하는 프로그램을 작성하시오.
# (성별에 따른 표준체중 공식)
# 남자 : 키(m) X 키(m) X 22
# 여자 : 키(m) X 키(m) X 21

# 조건1: 표준 체중은 별도의 함수 내에서 계산
#       함수명: std_weight
#       전달값 : 키(height), 성별(gender)
# 조건2: 표준 체중은 소수점 둘째자리까지 표시

# (출력예시) 키 175cm 남자의 표준 체중은 67.38kg 입니다.

height = float(input("당신의 키를 입력해 주세요(cm): "))/100
gender = input("당신의 성별을 입력해 주세요(남, 여): ")
def std_weight(height, gender):
    if gender == "남":
        weight = height*height*22
        print("키 {0}cm 남자의 표준 체중은 {1}kg 입니다.".format(height*100, weight))
    if gender == "여":
        weight = height*height*21
        print("키 {0}cm 여자의 표준 체중은 {1}kg 입니다.".format(height*100, weight))
std_weight(height, gender) # 키 175.0cm 남자의 표준 체중은 67.375kg 입니다.

# -------------- 키는 정수로 체중은 소수점 2째자리 까지 표현하기 위해 --------------
height = float(input("당신의 키를 입력해 주세요(cm): "))/100
gender = input("당신의 성별을 입력해 주세요(남, 여): ")
def std_weight(height, gender):
    if gender == "남":
        weight = height*height*22
        print("키 {0}cm 남자의 표준 체중은 {1}kg 입니다.".format(int(height*100), round(weight,2)))
    if gender == "여":
        weight = height*height*21
        print("키 {0}cm 여자의 표준 체중은 {1}kg 입니다.".format(int(height*100), round(weight,2)))
std_weight(height, gender) # 키 175cm 남자의 표준 체중은 67.38kg 입니다.

# -------------- 또는 --------------
height = float(input("당신의 키를 입력해 주세요(cm): "))/100
gender = input("당신의 성별을 입력해 주세요(남자, 여자): ")
def std_weight(height, gender):
    if gender == "남자":
        weight = height*height*22      
        return weight
    else:
        weight = height*height*21
        return weight
weight = round(std_weight(height, gender), 2)
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(int(height*100), gender, weight))
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.

# -------------- 또는 --------------
height = int(input("당신의 키를 입력해 주세요(cm): "))
gender = input("당신의 성별을 입력해 주세요(남자, 여자): ")
def std_weight(height, gender):
    if gender == "남자":
        weight = height*height*22      
        return weight
    else:
        weight = height*height*21
        return weight
weight = round(std_weight(height/100, gender), 2)
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.