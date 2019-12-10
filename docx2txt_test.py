import docx2txt
import pandas as pd 

text = docx2txt.process(r"./doc_data/iGate Introduction-6차_20121211 v1.0.0.docx")

contents = []
for line in text.splitlines():
    #This will ignore empty/blank lines. 
    if line != '':
        # replace \t
        line = line.replace("\t","")
        #Append to list
        contents.append(line)
      
# t = []
# for content in contents:
#     if "\t" in content:
#         t.append(content)

print(contents)

print(len(text))
text = text[1:100]
print(text)