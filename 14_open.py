#==== .wirte / 내용 쓰기 ====
score_file = open("score.txt", "w", encoding="utf8") 
#파일명, 쓰기모드"w", 한글사용시 utf8 지정
print("수학 : 0", file = score_file)
print("영어 : 50", file = score_file)
score_file.close()

score_file = open("score.txt", "a", encoding="utf8") # 추가모드 a
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100") #.write로 작성시 줄바꿈이 되지 않아 \n
score_file.close()

#==== .read(n) / 전체(n)내용 읽기 ====
score_file = open("score.txt", "r", encoding="utf8") # 읽기모두 r
print(score_file.read()) # 한번에 모든 내용일 읽어옴
score_file.close()
# 수학 : 0
# 영어 : 50
# 과학 : 80
# 코딩 : 100

score_file = open("score.txt", "r", encoding="utf8") # 읽기모두 r
print(score_file.read(4)) # n개(4)의 글자를 읽어서 문자열로 리턴
score_file.close()
# 수학 :

#==== .readline() / 한줄 읽기 ====
score_file = open("score.txt", "r", encoding="utf8") # 읽기모두 r
print(score_file.readline()) # (\n만날때까지의)한줄을 읽고 커서는 다음 줄로 이동
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
score_file.close()
# 수학 : 0

# 영어 : 50

# 과학 : 80

# 코딩 : 100

score_file = open("score.txt", "r", encoding="utf8") # 읽기모두 r
print(score_file.readline(), end = "")
print(score_file.readline(), end = "")
print(score_file.readline(), end = "")
print(score_file.readline(), end = "")
score_file.close()
# 수학 : 0
# 영어 : 50
# 과학 : 80
# 코딩 : 100

#==== 내용이 몇줄인지 모를 때 ====
score_file = open("score.txt", "r", encoding="utf8") # 읽기모두 r
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end="")
score_file.close()

#==== .readlines() / 리스트로 반환 ====
score_file = open("score.txt", "r", encoding="utf8") # 읽기모두 r
lines = score_file.readlines() # 파일 내용이 끝날 때 까지 문자를 읽어서 list로 리턴
for line in lines:
    print(line, end="")
score_file.close()
    
