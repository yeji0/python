# 프로그램상 사용하고 있는 데이터를 파일 형태로 저장
# 파일을 열어서 pickle을 이용해 데이터를 가져와 코드에서 쓸 수 있음.

#==== pickle.dump(정보, 파일) / 정보를 파일에 저장 ====
import pickle
profile_file = open("profile.pickle","wb") #pickle위해서는 바이너리 형태로 열어야 함.
profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
print(profile)  # {'이름': '박명수', '나이': 30, '취미': ['축구', '골프', '코딩']}
pickle.dump(profile, profile_file)   #  pickle을 이용해 데이터를 파일에 쓴다.
                                     # profile정보를 profile_file에 쓴다.
profile_file.close()

#==== pickle.load(파일) / 파일에 있는 정보를 불러오기 ====
import pickle
profile_file = open("profile.pickle","rb") 
data = pickle.load(profile_file)
print(data) # {'이름': '박명수', '나이': 30, '취미': ['축구', '골프', '코딩']}
profile_file.close()