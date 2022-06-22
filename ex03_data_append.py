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

# 데이터를 통합하기 위해서는 칼럼 순서가 동일해야 합니다.

sample_2 = pd.read_excel('./study/2_Data_Analysis_basic/files/sample_2.xlsx', header=1, skipfooter=2, usecols='A:C')
sample_2['기준년월'] = '2019-11'

sample_2_code = pd.merge(left=sample_2, right=code_master, how='left', left_on='국적코드', right_on='국적코드')

print(sample_2_code)
print('*' * 50)

print(sample_2_code)
print('*' * 50)

# FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
# 위 경고문은 append 기능이 미래에는 삭제가 될 것임으로 사용을 자제하고  concat기능을 사용하기를 권장한다.
# ignore_index 데이터를 합칠때에는 원래의 인덱스로 값으로 합쳐지므로 일반적으로 ignore_index = True를 이용하여 인자의를 지정하길 권장

# sample = sample_1_code.append(sample_2_code, ignore_index=True)
# print(sample)

# concat을 이용하여 두개의 데이터 프레임을 합치기
# 데이터 프레임은 1개가 들어가도 리스트 형식으로 넣어야 함
# axis = 0 은 행으로 데이터를 넣고(위아래 붙이기) axis = 1은 열로 데이터를 넣음(옆으로 붙이기)
concatTest = pd.concat([sample_1_code, sample_2_code], axis=0, ignore_index=True)
print(concatTest)

# to_excel 엑셀파일로 파일저장하기
# concatTest.to_excel('./sample.xlsx')
# index = False 로 자동 생성된 인덱스 번호 지우기
concatTest.to_excel('./sample_index_false.xlsx', index=False)
