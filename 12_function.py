def open_account():
    print("새로운 계좌가 생성되었습니다.")
    
open_account()
# 새로운 계좌가 생성되었습니다.


#==== 전달값과 반환값 ====

def deposit(balance, money): #전달값
    print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance + money))
    return balance + money #반환값

def withdraw(balance, money): # 출금
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 %d원 입니다."%(balance-money))
        return balance - money
    else:
        print(f"잔액이 부족합니다. 잔액은 {balance}원 입니다.")
        return balance
def withdraw_night(balance, money):
    commission = 100 # 수수료 100원
    if balance >= money+ 100:
        print("출금이 완료되었습니다. 수수료 %d원 잔액은 %d원 입니다."%(commission, balance-money-commission))
        return commission, balance - money - commission
    else:
        print(f"수수료를 포함한 인출금이 부족합니다. 잔액은 {balance}원 입니다.")
        return commission, balance
    
    
balance = 0
balance = deposit(balance, 1000) # 입금이 완료되었습니다. 잔액은 1000원 입니다.  
print(balance) # 1000
balance = withdraw(balance, 2000) # 잔액이 부족합니다. 잔액은 1000원 입니다.
print(balance) # 1000
balance = withdraw(balance, 500) # 출금이 완료되었습니다. 잔액은 500원 입니다.
print(balance) # 500
commission, balance = withdraw_night(balance, 200) # 출금이 완료되었습니다. 수수료 100원 잔액은 200원 입니다. 
print(balance) # 200
commission, balance = withdraw_night(balance, 200) # 수수료를 포함한 인출금이 부족합니다. 잔액은 200원 입니다. 
print(balance) # 200
    
#==== 기본값 ====
def profile(name, age, main_lang):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}".format(name, age, main_lang))
profile("유재석", 20, "파이썬") # 이름 : 유재석   나이 : 20       주 사용 언어: 파이썬
profile("김태호", 25, "자바") # 이름 : 김태호   나이 : 25       주 사용 언어: 자바

#같은 학교 같은 학년 같은 반 같은 수업. 이름만 다르고 나이와 배우는 언어는 같다.
#이럴때 기본값 사용.

def profile(name, age=18, main_lang="파이썬"):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}"\
        .format(name, age, main_lang)) # \ 엔터는 코드 두줄을 한줄로 인식
profile("유재석") # 이름 : 유재석   나이 : 17       주 사용 언어: 파이썬
profile("김태호") # 이름 : 김태호   나이 : 17       주 사용 언어: 파이썬

#==== 키워드값 ====
def profile(name, age, main_lang):
    print(name, age, main_lang)
    
profile(name="유재석", main_lang="파이썬", age=20) # 유재석 20 파이썬
profile(main_lang="자바", age=25, name="김태호") # 김태호 25 자바

#==== 가변인자 ====
def profile(name, age, lang1, lang2, lang3, lang4):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    print(lang1, lang2, lang3, lang4) 
profile("유재석", 20, "파이썬", "자바", "C", "html") 
# 이름 : 유재석   나이 : 20        파이썬 자바 C html
profile("김태호", 25, "CSS", "html", "", "")
# 이름 : 김태호   나이 : 25        CSS html

# 다른 사람을 추가 할 때 마다 lang4를 채우기 위해 빈칸("") 넣어주기 불편.
# 혹은 언어를 추가하고 싶어지면 함수의 lang5를 추가해주어야 함.
# 그래서 가변인자(*)를 사용.

def profile(name, age, *language):
    print(f"이름 : {name}\t나이 : {age}\t", end=" ")
    for lang in language:
        print(lang, end=" ")
    print() # 앞사람과 뒷사람 줄 띄우기 위해
        
profile("유재석", 20, "파이썬", "자바", "C", "html", "C++") 
# 이름 : 유재석   나이 : 20        파이썬 자바 C html C++
profile("김태호", 25, "CSS", "html")
# 이름 : 김태호   나이 : 25        CSS html

#==== 지역변수, 전역변수 ====
# 지역변수 : 함수 내에서만 사용. 함수가 호출될 때 생성, 함수가 끝날 때 소멸
# 전역변수 : 프로그램 내 모든 곳에서 사용

gun = 10 # 전체 총기 수량
def checkpoint(soldiers): # 근무자를 제외한 총기 수량 확인
    gun = gun - soldiers
    print("[총기보관함 내] 총기 수량: %d"%(gun))

print("전체 총기 수량: {}".format(gun)) # 전체 총기 수량: 10
checkpoint(2) # 근무자2명
#(오류)UnboundLocalError: local variable 'gun' referenced before assignment
# gun = 10의 gun과 checkpoint 함수내 gun(지역변수)은 다름. 
# 함수 내 gun이 초기화 되지 않고 사용되어 오류 발생
# -----------------------------

gun = 10 # 전체 총기 수량
def checkpoint(soldiers): # 근무자를 제외한 총기 수량 확인
    gun = 20
    gun = gun - soldiers
    print("[총기보관함 내] 총기 수량: %d"%(gun))

print("전체 총기 수량: {}".format(gun)) # 전체 총기 수량: 10
checkpoint(2) # [총기보관함 내] 총기 수량: 18
print("함수 후 gun: {}".format(gun)) # 함수 후 gun: 10


gun = 10 # 전체 총기 수량
def checkpoint(soldiers): # 근무자를 제외한 총기 수량 확인
    global gun # 전역변수 gun(gun=10)을 사용하겠다.
    gun = gun - soldiers
    print("[총기보관함 내] 총기 수량: %d"%(gun))

print("전체 총기 수량: {}".format(gun)) # 전체 총기 수량: 10
checkpoint(2) # [총기보관함 내] 총기 수량: 8
print("함수 후 gun: {}".format(gun)) # 함수 후 gun: 8

#전역변수를 많이 사용하면 코드관리가 어려워짐
#가급적 함수의 전달값으로 파라미터로 던져서 게산하고 반환값을 받아서 사용
gun = 10 # 전체 총기 수량
def checkpoint_retun(gun, soldiers):
    gun = gun-soldiers
    print("[총기함 내] 총기 수량: {}".format(gun))
    return gun
print("전체 총기 수량: {}".format(gun)) # 전체 총기 수량: 10
gun = checkpoint_retun(gun, 2) # [총기함 내] 총기 수량: 8
print("함수 후 gun: {}".format(gun)) # 함수 후 gun: 8

    