import pandas as pd

# Database의 join을 생각하면 될 것 같다.

sample_1 = pd.read_excel('./study/2_Data_Analysis_basic/files/sample_1.xlsx', header=1, skipfooter=2, usecols='A:C')
code_master = pd.read_excel('./study/2_Data_Analysis_basic/files/sample_codemaster.xlsx')

print(sample_1)
print('*' * 50)
print(code_master)
print('*' * 50)

sample_1['기준년월'] = '2019-11'

# 데이터 옆으로 통합하기
# left 왼쪽 테이블 정하기, right 오른쪽 테이블 정하기, how 어떤 테이블을 기준으로 결합하는가, left_on 왼쪽 테이블의 기준 칼럼 정하기, right_on 오른쪽 테이블의 기준 칼럼 정하기
# 기준 칼럼은 DB에서 foreign Key 인듯
sample_1_code = pd.merge(left=sample_1, right=code_master, how='left', left_on='국적코드', right_on='국적코드')
print(sample_1_code)
print('*' * 50)

# 공통으로 존재하는 값을 표현할때에는 how = 'inner' 을 사용한다.
# database의 inner join
sample_1_code_inner = pd.merge(left=sample_1, right=code_master, how='inner', left_on='국적코드', right_on='국적코드')
print(sample_1_code_inner)
print('*' * 50)