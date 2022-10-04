# with를 이용하면 코드를 간단히 할 수 있고.
# with를 이용하면 close하지 않아도 된다.

import pickle
with open("profile.pickle","rb") as profile_file: #"profile.picke"파일을 열고 profile.file변수로 저장
    print(pickle.load(profile_file))
    
with open("study.txt","w",encoding="utf8") as file:
    file.write("파이썬을 열심히 공부해요")
    
with open("study.txt","r",encoding="utf8") as read:
    print(read.read()) # 파이썬을 열심히 공부해요