import time
#import json,yaml,re
#import re

#start_time = time.monotonic()
#print(time.monotonic()-start_time)

#first task
f = open("Wednesday.json",'r',encoding="utf-8")

def jsonToYaml(file):
    text = file.read()
    file.close()
    text = text.replace('"',"")\
           .replace("\t","  ").replace("{\n  ","",1)
    startOfArray,endOfArray = text.index("["),text.index("]")
    text = text[:startOfArray].replace(",","")\
           +text[startOfArray:endOfArray+1].replace("[","").replace("{\n","- ")\
           .replace("}","")\
           .replace("       "," ").replace(",\n","\n")\
           +text[endOfArray:]
    text = text.replace("]","").replace("\n{\n  ","").replace("    ","  ").\
           replace("{","").replace("}","").replace("\n  \n","\n").\
           replace("\n  \n","\n").replace("\n\n","\n").replace("\n  \n ","")
    result = open("Wednesday.yaml","w")
    result.write(text)
    result.close()
    
jsonToYaml(f)
#print(time.monotonic()-start_time)

#second task
f = open("Wednesday.json",'r',encoding='utf-8')
result = open("WednesdayWithLibs.yaml",'w')
result.write(yaml.dump(json.load(f),allow_unicode=True))
f.close()
result.close()
#print(time.monotonic()-start_time)

#third task
f = open("Wednesday.json",'r',encoding='utf-8')
text = f.read()
f.close()
res = re.sub(r'\"',"",text)
res = re.sub(r'\t',"  ",res)
res = re.sub(r"{\n  ","",res,1)
res = re.sub(r'[\[\]]',"",res)
res = re.sub(r'[{}]',"",res)
res = re.sub(r"\n    ,\n    \n","\n    - ",res)
res = re.sub(r",\n","\n",res)
res = re.sub(r"\n    \n     ","\n    -",res)
res = re.sub(r"\n  \n      ","-",res)
res = re.sub(r'       '," ",res)
res = re.sub(r'-     \n      ',"- ",res)
res = re.sub(r'\n  \n    ',"\n  ",res)
res = re.sub(r'\n    ',"\n  ",res)
res = re.sub(r'\n  \n  \n  \n  \n',"",res)
res = re.sub(r'\n\n','\n',res)
res = res[:-1]
result = open("WednesdayWithRegex.yaml","w")
result.write(res)
result.close()
#print(time.monotonic()-start_time)
