# 출처: https://rfriend.tistory.com/790 [R, Python 분석과 프로그래밍의 친구 (by R Friend):티스토리]
from PyPDF2 import PdfReader
import pandas as pd
import re

## initiate PdfReader
pdf_path = r"D:\airflow\pdf\book.pdf"
reader = PdfReader(pdf_path)

print(len(reader.pages))
# 4



## extract text from a pdf file
text_all = []

for page in reader.pages:
    text = page.extract_text()
    text = text.replace('-',' ')
    text = text.replace('—',' ')
    text_all.append(text)
    


# 문자열을 공백 및 개행 기준으로 분할
words = [re.sub(r'[^a-zA-Z]', '', word).lower() for text in text_all for word in text.split()]

# 데이터프레임 생성
df = pd.DataFrame(sorted(words), columns=["Word"])
# df = df.replace('—','')
df = df.drop_duplicates()

df.to_csv(r"D:\airflow\pdf\output_file.csv", index=False, encoding="utf-8")

# 결과 출력
# import ace_tools as tools
# tools.display_dataframe_to_user(name="Words DataFrame", dataframe=df)
