from docx2python import docx2python
import pandas as pd 
import re
from make_dic import make_dictionary

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


def generate_doc(doc_body, doc_len):
        if doc_len == 1:
            
            for i in range(doc_len):
                # 일반 텍스트 글들 -> 전처리 필요함
                contents_lists = remove_blank(list(doc_body[i][0]))
                temp_list =[]
                last_list_value = contents_lists[-1]
                result_list = []
                # 사전(목차)에 있는 단어인지 비교 후 처리
                for content in contents_lists:
                    if content in index_dictionary:
                        if temp_list:
                            # 파이썬 list append 함수는 해당 list의 주소를 참조하는 것 이기 때문에 복사 후 넣어줘야함 개고생
                            temp_list2=temp_list[:]
                            result_list.append(temp_list2)
                        #print(temp_list)
                        temp_list.clear()
                        #print("---------------------------------")
                        temp_list.append(content)
                    elif content == last_list_value:
                        temp_list.append(content)
                        temp_list2=temp_list[:]
                        result_list.append(temp_list2)
                        #print(temp_list)
                        temp_list.clear()
                    else:
                        temp_list.append(content)
                return result_list
                    
                 
        else:
            print("This is TABLE, OK?")
            # 테이블 처리
            table_list=[]
            for i in range(doc_len):
                filed_list=[]
                for k in range(len(doc_body[i])):
                    filed_list.append(doc_body[i][k][0])
                table_list.append(filed_list)
            
            return table_list


if __name__ == "__main__":
    # 목차를 이용하여 사전 생성
    index_dictionary = make_dictionary()

    # 문서 로드 
    doc_result = docx2python(r"./doc_data/test.docx")

    for j in range(1,len(doc_result.body)):
        doc_body = doc_result.body[j]
        doc_len = len(doc_body)
        contents_part = generate_doc(doc_body, doc_len)
        for i, content in enumerate(contents_part):
            #print('ID = {0}0{1}'.format(str(j),str(i)))
            print(content)
    

                







