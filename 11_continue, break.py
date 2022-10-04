#==== (반복문에서 사용)continue 와 break ====
# continue 다음 반복으로 넘긴다.
# break 반복문을 종료한다.

transfer = [2, 5] #전학 간 학생의 번호
for student in range(1, 11): # 1~10번
    if student in transfer:
        continue
    print("{}번 학생, 왔나요?".format(student))
# 1번 학생, 왔나요?
# 3번 학생, 왔나요?
# 4번 학생, 왔나요?
# 6번 학생, 왔나요?
# 7번 학생, 왔나요?
# 8번 학생, 왔나요?
# 9번 학생, 왔나요?
# 10번 학생, 왔나요?    

transfer = [2, 5] #전학 간 학생의 번호
absent = [7] # 결석한 학생의 번호
for student in range(1, 11): # 1~10번
    if student in transfer:
        continue
    elif student in absent:
        print("%d번 학생이 없어요?"%student)
        break
    print("{}번 학생, 왔나요?".format(student))
# 1번 학생, 왔나요?
# 3번 학생, 왔나요?
# 4번 학생, 왔나요?
# 6번 학생, 왔나요?
# 7번 학생이 없어요?