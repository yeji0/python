# 오류가 발생할 때 처리하는 방법을 정의

try:
    print("나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요: "))
    num2 = int(input("두 번째 숫자를 입력하세요: "))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")
# num1 6, num2 3, 6 / 3 = 2
# num1 6, num2 참, 에러! 잘못된 값을 입력하였습니다.
# num1 6, num2 0, 중간에 오류(ZeroDivisionError) 종료
except ZeroDivisionError as err:
    print(err)
# num1 6, num2 0, division by zero
except Exception as err: # 어떤 오류가 발생하던 오류 확인
    print(err)

try: 
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫번째 숫자를 입력하세요: ")))
    nums.append(int(input("두번째 숫자를 입력하세요: ")))
    # nums.append(int(nums[0] / nums[1])) # nums[2]를 누락한 에러발생시
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except: # 그냥 except: 만 사용하면 어떤 오류든 실행
    print("알 수 없는 에러가 발생하였습니다.")
    
#==== raise 오류를 발생시킬때 ====
try:
    print("한 자리 수 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요: "))
    num2 = int(input("두 번째 숫자를 입력하세요: "))
    if num1 >= 10 or num2 >= 10:
        raise ValueError
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
# 위, 아래 같은 결과    
try:
    print("한 자리 수 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요: "))
    num2 = int(input("두 번째 숫자를 입력하세요: "))
    if num1 >= 10 or num2 >= 10:
        raise
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
    
#==== 사용자가 원하는 오류명을 만듦(bignumerr) ====
class bignumerr(Exception):
    pass #아무것도 하지 않고 넘어간다.
try:
    print("한 자리 수 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요: "))
    num2 = int(input("두 번째 숫자를 입력하세요: "))
    if num1 >= 10 or num2 >= 10:
        raise bignumerr
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except bignumerr:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
    
#==== 심화 ====
# 에러(bignumerr)가 발생 했을 때 
# class(msg)에 문자열("입력값 : {0}, {1}".format(num1, num2))을 보내고
# class에서 가지고 있다가 처리될 때(except) err로 받아와 출력
class bignumerr(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg
    
try:
    print("한 자리 수 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요: "))
    num2 = int(input("두 번째 숫자를 입력하세요: "))
    if num1 >= 10 or num2 >= 10:
        raise bignumerr("입력값 : {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except bignumerr as err:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
    print(err)
# 잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.
# 입력값 : 10, 5

#==== finally - try가 정상실행 하던 오류가 있던 무조건 실행 ====
class bignumerr(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg
    
try:
    print("한 자리 수 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요: "))
    num2 = int(input("두 번째 숫자를 입력하세요: "))
    if num1 >= 10 or num2 >= 10:
        raise bignumerr("입력값 : {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except bignumerr as err:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
    print(err)
finally:
    print("감사합니다.")
# 잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.
# 입력값 : 10, 5
# 감사합니다.