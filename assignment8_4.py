import csv

# CSV 읽기 DictReader
with open("score.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f) # 헤드라인 키, 나머지 내용 값으로

    for row in reader:
        print(row)

# list(reader)
with open("score.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f) 

    data = list(reader)

print(data)

# 결측치 처리
blank = 0
missing = 0
nan_Val = 0

for d in data:
    if d["나이"] == "":
        blank += 1
    elif d["국어"] == "":
        blank += 1
    elif d["영어"] == "":
        blank += 1
    else:
        continue

for d in data:
    if d["나이"] == "결측":
        missing += 1
    elif d["국어"] == "결측":
        missing += 1
    elif d["영어"] == "결측":
        missing += 1
    else:
        continue

for d in data:
    if d["나이"] == "NaN":
        nan_Val += 1
    elif d["국어"] == "NaN":
        nan_Val += 1
    elif d["영어"] == "NaN":
        nan_Val += 1
    else:
        continue

print("빈 문자열 개수 : ", blank)
print("결측 개수 : ", missing)
print("NaN 개수 : ", nan_Val)

# 나이 값 type 알아보기
for d in data:
    if d["나이"] != "":
        print(d["나이"])
        print(type(d["나이"]))

# 빈칸 제외 다 int로 type 형변환
for d in data:
    if d["나이"] != "":
        d["나이"] = int(d["나이"])

# 빈칸 제외 int로 형변환 된거 확인
for d in data:
    if d["나이"] != "":
        print(d["나이"])
        print(type(d["나이"]))

# 평균 구하기 -> 결측치 평균으로 대치
age_total = 0
age_count = 0

for d in data:
    if d["나이"] != "":
        age_total = age_total + d["나이"]
        age_count = age_count +1
avg = int(round(age_total / age_count,1))

print(age_total, age_count)
print(f"avg {avg}")

for d in data:
    if d["나이"] == "":
        d["나이"] = avg

# 국어 결측치 처리
for d in data:
    if d["국어"] != "":
        print(d["국어"])
        print(type(d["국어"]))

# 국어는 빈칸과 "결측이 둘 다 있으므로 둘 다 제외 하고 형변환"
for d in data:
    if d["국어"] != "" and d["국어"] != "결측":
        d["국어"] = int(d["국어"])

# 빈칸 제외 int로 형변환 된거 확인
for d in data:
    if d["국어"] != "":
        print(d["국어"])
        print(type(d["국어"]))

kor_total = 0
kor_count = 0

for d in data:
    # if d["국어"] != "" and d["국어"] != "결측":
    #     total += d["국어"]
    #     count += 1
    if d["국어"] != "" and d["국어"] != "결측":
        if 0 <= d["국어"] and d["국어"] <= 100:
            kor_total += d["국어"]
            kor_count += 1
print(kor_total, kor_count)
avg_kor = int(round(kor_total / kor_count,1))
print(avg_kor)

for d in data:
    if d["국어"] == "" or d["국어"] == "결측":
        d["국어"] = avg_kor

# 영어 결측치 처리
for d in data:
    if d["영어"] != "":
        print(d["영어"])
        print(type(d["영어"]))

# 영어는 빈칸과 NaN이 모두 존재
for d in data:
    if d["영어"] != "" and d["영어"] != "NaN":
        d["영어"] = int(d["영어"])

# 빈칸 제외 int로 형변환 된거 확인
for d in data:
    if d["영어"] != "":
        print(d["영어"])
        print(type(d["영어"]))

eng_total = 0
eng_count = 0

for d in data:
    if d["영어"] != "" and d["영어"] != "NaN":
        if 0 <= d["영어"] and d["영어"] <= 100:
            eng_total += d["영어"]
            eng_count += 1
print(eng_total, kor_count)
avg_eng = int(round(eng_total / eng_count,1))
print(avg_eng)

for d in data:
    if d["영어"] == "" or d["영어"] == "NaN":
        d["영어"] = avg_eng

# 이상치 처리

# 나이 이상치 처리 평균
age_total = 0
age_count = 0
for d in data:
    age_Outlier = d["나이"]

    if age_Outlier > 100:
        print(d)
    
    if d["나이"] < 100:
        age_total += d["나이"]
        age_count += 1

print(age_total/age_count)
age_avg = int(round(age_total / age_count,0))

print(f"avg {age_avg}")

for d in data:
    if d["나이"] > 100:
        d["나이"] = age_avg

# 국어 이상치 처리 평균
kor_out_total = 0
kor_out_count = 0
for d in data:
    if d["국어"] < 0 or d["국어"] > 100:
        print(d)
    
    if d["국어"] > 0 and d["국어"] <= 100:
        kor_out_total += d["국어"]
        kor_out_count += 1

print(kor_out_total/kor_out_count)
kor_out_avg = int(round(kor_out_total / kor_out_count,0))

print(f"avg {kor_out_avg}")

for d in data:
    if d["국어"] > 100 or d["국어"] < 0:
        d["국어"] = kor_out_avg

# 영어 이상치 처리 평균
eng_out_total = 0
eng_out_count = 0
for d in data:
    if d["영어"] < 0 or d["영어"] > 100:
        print(d)
    
    if d["영어"] > 0 and d["영어"] <= 100:
        eng_out_total += d["영어"]
        eng_out_count += 1

print(eng_out_total/eng_out_count)
eng_out_avg = int(round(eng_out_total / eng_out_count,0))

print(f"avg {eng_out_avg}")

for d in data:
    if d["영어"] > 100 or d["영어"] < 0:
        d["영어"] = eng_out_avg

# 파생 속성 

# 총점 = (국어 + 영어)
for d in data:
    d["총점"] = d["국어"] + d["영어"]

# 평균
for d in data:
    d["평균"] = round(d["총점"] / 2,1)

# 특성 추출 

# 합격(평균 >= 60), 불합격(평균 < 60)
for d in data:
    if d["평균"] >= 60:
        d["합격 결과"] = "합격"
    elif d["평균"] < 60:
        d["합격 결과"] = "불합격"

for d in data: # 모든 행에 반복문으로 순위를 구함
    
    rank = 1
    
    for other_student in data: # 전체를 반복
        if other_student["총점"] > d["총점"]:
            rank += 1

    # 순위 = 나보다 높은 학생 수 + 1
    d["순위"] = rank

# 결과 score_result.csv 파일로 저장
with open("score_result.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.DictWriter(f, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)

print("score_result.csv 저장 완료!")
