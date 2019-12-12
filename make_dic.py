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

def inverse_dic(text_array):
    dic = dict(zip(range(len(text_array)), text_array))
    inv_dic = {v: k for k, v in dic.items()}
    return inv_dic

def make_dictionary():
    doc_result = docx2python(r"./doc_data/contents_list.docx")
    doc_body_for_dic = doc_result.body[0][0][0]
    first = remove_blank_and_reg(doc_body_for_dic)
    second = reduce_num(first)

    # 목차를 이용하여 사전 생성
    list_dic = inverse_dic(second)
    print(list_dic)
    return list_dic