from docx2python import docx2python
import pandas as pd 
import re

def remove_blank_and_reg(text_array):
    texts = []
    for line in text_array:
        #This will ignore empty/blank lines. 
        if line != '':
            # replace \t
            line = line.replace("\t","")
            remove_sign = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\<\>`\'…》]', '', line)
            #Append to list
            texts.append(remove_sign)
    return texts

def reduce_num(text_array):
    texts =[]
    for line in text_array:
        i = filter(str.isdigit, line)
        if i is not None:
            remove_digit = re.sub('[[\d\]+]', '', line)
            texts.append(remove_digit)
    return texts

def make_dic(text_array):
    dic = dict(zip(range(len(text_array)), text_array))
    inv_dic = {v: k for k, v in dic.items()}
    return inv_dic

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
    doc_body_for_dic = doc_result.body[0][0][2]
    #print(doc_body_for_dic)
    first = remove_blank_and_reg(doc_body_for_dic)
    second = reduce_num(first)

    # 목차를 이용하여 사전 생성
    list_dic = make_dic(second)
    print(list_dic)

    for j in range(1,len(doc_result.body)):
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
                # clear_doc = filter(None, doc_body[i][0])
                pre_text = remove_blank(list(doc_body[i][0]))

                # 사전(목차)에 있는 단어인지 비교 후 처리
                temp_list =[]
                last_list_value = pre_text[-1]
                for subject in pre_text:
                    if subject in list_dic:
                        print(temp_list)
                        temp_list.clear()
                        print("---------------------------------")
                        temp_list.append(subject)
                    elif subject in last_list_value:
                        temp_list.append(subject)
                        print(temp_list)
                        temp_list.clear()
                    else:
                        temp_list.append(subject)
                    
            elif doc2_len == 2 :
                # 일반적으로 표 형태 2x2
                    print(doc_body[i])

                
                

            elif doc2_len > 2:
                print(doc_body[i])
                # 2x2를 벗어나는 표 형태
            else:
                pass                







