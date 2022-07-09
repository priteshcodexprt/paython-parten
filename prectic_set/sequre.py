dic = {}

print("PRINT1\n",dic)


dic["AAAAA"] = "AAAAA"
dic["BBBBB"]= "{}"
dic["CCCCC"] = "{}"
dic["DDDDD"]="{}"

print("PRINT2\n",dic)

dic["AAAAA"]="AAAAA"
dic["BBBBB"]={}
dic["CCCC"]="CCCC"
dic["DDDD"]="DDDD"

print(dic)