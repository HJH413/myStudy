import pandas as pd

sample_1 = pd.read_excel('./study/2_Data_Analysis_basic/files/sample_1.xlsx', header=1, skipfooter=2, usecols='A:C')

# read_excel 엑셀 파일불러오는 함수
# header 컬럼명의 row를 찾기
# skipfooter 마지막 row에서 생략하고 불러올 수
# usecols 불러올 column 범위

# head 처음 부터 n번째 row 까지 제공
print(sample_1.head(3))
print('*' * 50)

# tail 마지막 부터 n번째  row 까지 제공
print(sample_1.tail(3))
print('*' * 50)

# 데이터 확인시 처음과 마지막을 불러오자

# info 데이터의 요약 정보를 제공
print(sample_1.info())
print('*' * 50)

# 데이터의 기초통계량 살피기
# describe() 함수는 숫자 형 변수에 대한 여러 가지 통계량을 출력하는 함수
# 위에서부터 데이터의 개수, 평균값, 표준편차, 최솟값, 1사분위수, 2사분위수(중위수), 3사분위수, 최댓값
print(sample_1.describe())
print('*' * 50)

# 데이터 선택 - 칼럼 기준
print(sample_1)
print('*' * 50)

# 보고싶은 컬럼을 선택할때에는 ['']이용하며 컬럼 명 입력
print(sample_1['입국객수'])
print('*' * 50)

# 보고싶은 여러 컬럼을 선택할때에는 [['','']]이용하며 컬럼 명 입력
# 여려개의 컬럼을 볼 때에는 리스트를 이용하여 본다

print(sample_1[['국적코드', '입국객수']])
print('*' * 50)

# 컬럼 생성하기
# 기존에 존재하지 않던 컬럼에 값을 부여하면 새로운 컬럼을 생성할 수 있음
sample_1['기준년월'] = '2019-11'
print(sample_1)
print('*' * 50)

# 데이터 선택 - 로우 기준
sex = (sample_1['성별'] == '남성')
print(sex)
print('*' * 50)

# boolean으로 ture인 컬럼명으로 데이터를 불러옴
print(sample_1[sex])
print('*' * 50)

# 수식을 이용하여 해당되는 컬럼의 데이터를 불러올 수 있다
customerCount = (sample_1['입국객수'] >= 150000)
print(sample_1[customerCount])
print('*' * 50)

print(sample_1[sex & customerCount])
print('*' * 50)

# \ 를 이용하여 코드의 가독성을 올릴 수 있다.
nationCode = (sample_1['국적코드'] == 'A01') \
             | (sample_1['국적코드'] == 'A18')

print(sample_1[nationCode])
print('*' * 50)

# isin() 함수 안에 찾고 싶은 값들을 리스트 형태로 넣으면 국적코드에서 리스트 안의 값에 해당될 경우 True 값을 반환합니다.
nationList = sample_1['국적코드'].isin(['A01', 'A18'])
print(sample_1[nationList])
print('*' * 50)

# False 호출 하기
print(sample_1[nationList == False])
print('*' * 50)
