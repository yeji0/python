# 문제) 매주 1회 작성해야 하는 보고서가 있다.
# 보고서는 아래와 같은 형태로 출력되어야 한다.

# - X 주차 주간보고 -
# 부서:
# 이름:
# 업무 요약:

# 1주차부터 10주차까지의 보고서를 만드는 프로그램을 작성하시오.

# 파일명은 1주차.txt, 2주차.txt, ... 


for i in range(1, 11):
    with open(str(i) + "주차.txt","w",encoding="utf8") as report:
        report.write("- {} 주차 주간보고 -".format(i))
        report.write("\n부서:")
        report.write("\n이름:")
        report.write("\n업무 요약:")
    