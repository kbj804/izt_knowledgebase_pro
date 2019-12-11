from docx2python import docx2python
import pandas as pd 

# get separate components of the document

 
# get the text from Zen of Python
# doc_result[0]
# doc_result[1] 
# doc_result[2]

# doc_result.images.key()  # dict_keys(['image1.png'])
# 이미지 추출 #
# for key,val in doc_result.images.items():
#     f = open(key, "wb")
#     f.write(val)
#     f.close()

## get all text in a single string
## doc_result.text

## 속성 값
## doc_result.properties

# get the headers
## doc_result.header
 
# get the footers
## doc_result.footer

# html 로 추출 - 별로 의미 없음
##doc_html_result = docx2python(r"./doc_data/iGate Introduction-6차_20121211 v1.0.0.docx", html = True)

#print(doc_html_result.text)

"""df = pd.DataFrame(doc_result.body[1][1:]).\
    applymap(lambda val: val[0].strip("\t"))
df.columns = [val[0].strip("\t") for val in doc_result.body[1][0]]
print(df)"""

#print(df.columns)

#  빈 배열 없애기 
#doc_body10 = filter(None, doc_body[10][0][0])

#print(list(doc_body10))

#doc_body = doc_result.body[9]
#print("Doc Length: ", len(doc_body))

#print(doc_body[0][0])

def remove_blank(text_array):
    texts = []
    for line in text_array:
        #This will ignore empty/blank lines. 
        if line != '':
            # replace \t
            line = line.replace("\t","")
            #Append to list
            texts.append(line)
    return texts


if __name__ == "__main__":
    doc_result = docx2python(r"./doc_data/test.docx")

    for j in range(len(doc_result.body)):
        doc_body = doc_result.body[j]
        doc_len = len(doc_body)
        print("DOC ID : ", j)
        #print('ID = {0}00{1}'.format(str(j),str(i)))
        #print("DOC LENGTH : ", doc_len)
        for i in range(doc_len):
            doc2_len = len(doc_body[i])
            #print("DOC2 LENGTH : " ,doc2_len)
            if doc2_len == 1 & doc_len == 1:
                # 일반 텍스트 글들 -> 전처리 필요함
                clear_doc = filter(None, doc_body[i][0])
                print(remove_blank(list(clear_doc)))

            elif doc2_len == 2 :
                # 일반적으로 표 형태 2x2
                print(doc_body[i])

            elif doc2_len > 2:
                # 2x2를 벗어나는 표 형태
                print(doc_body[i])





