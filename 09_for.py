#==== 반복문 ====
# for 변수 in range(5):
#     실행명령문
# #순차적으로 커질때는 range(5): 0~4까지

# for 변수 in [100, 200, 300, 400, 500]:
#     실행명령문
# #리스트 값을 변수에 한번씩 넣으면서 실행

# 변수1 = ["진연", "범수", "민수"]
# for 변수2 in 변수1
#     실행명령문
# #변수1의 값 하나씩 변수2에 넣으면서 실행


#==== 숫자 ====
for waiting in range(1, 6): # range(시작, 끝(미포함), 간격)
    print("대기번호 : {}".format(waiting))
# 대기번호 : 1
# 대기번호 : 2
# 대기번호 : 3
# 대기번호 : 4
# 대기번호 : 5

#리스트
for waiting_l in [100, 200, 300, 400, 500]: 
    print("대기번호 : %s" % waiting_l)
# 대기번호 : 100
# 대기번호 : 200
# 대기번호 : 300
# 대기번호 : 400
# 대기번호 : 500

#튜플
# 내용 변경이나 추가를 할 수 없음. 단 속도가 리스트보다 빠름. 변경되지 않는 목록에 사용.
for waiting_t in (10, 20, 30, 40, 50): 
    print(f"대기번호 : {waiting_t}")
# 대기번호 : 10
# 대기번호 : 20
# 대기번호 : 30
# 대기번호 : 40
# 대기번호 : 50

#딕셔너리
scores = {"수학":0, "영어":50, "코딩":100, "기술가정":100}
for subject, score in scores.items(): # in scores(딕셔너리명만 작성한 경우)는 X
    print(subject, score)
# 수학 0
# 영어 50
# 코딩 100
# 기술가정 100

scores = {"수학":0, "영어":50, "코딩":100, "기술가정":100}
for subject, score in scores.items(): # in scores(딕셔너리명만 작성한 경우)는 X
    print(subject.ljust(8), str(score).rjust(4), sep=":")
     #.ljust(8) 8칸확보하여 왼쪽정렬, .rjust(4) 4칸 확보하여 오른쪽 정렬
# 수학      :   0
# 영어      :  50
# 코딩      : 100
# 기술가정    : 100 빈칸 2칸과 2글자 사이의 차이로 정렬이 안됨.


#==== 문자열 ====
cafe = ["김진연", "김범수", "김민수"]
for customer in cafe:
    print("{}님, 음료가 준비되었습니다.".format(customer))
# 김진연님, 음료가 준비되었습니다.
# 김범수님, 음료가 준비되었습니다.
# 김민수님, 음료가 준비되었습니다.

#==== 한줄for ====
# 번호가 1, 2, 3, 4 / 앞에 100 을 추가하자.
students = [1, 2, 3, 4]
print(students) # [1, 2, 3, 4]
students = [i+100 for i in students] 
# students에 있는 값을 하나씩 불러와 i에 넣고, i에 100을 더한 값을 리스트에 넣는다.
print(students) # [101, 102, 103, 104]

# 학생 이름을 길이로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [len(i) for i in students]
print(students) # [8, 4, 10]

# 학생 이름을 대문자로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students) # ['IRON MAN', 'THOR', 'I AM GROOT']