myDict={}
print("PRINT1\n",myDict)


myDict["AAAAA"]="AAAAA"
myDict["BBBBB"]={}
myDict["CCCCC"]={}
myDict["DDDDD"]={}


print("PRINT2\n",myDict)

myDict["AAAAA"]="AAAAA"
myDict["BBBBB"]={}
myDict["BBBBB"]["CCCC"] = "CCCC"
myDict["BBBBB"]["DDDD"]="DDDD"
myDict["CCCCC"]={}
myDict["CCCCC"]["DDDD"]="DDDD"
myDict["CCCCC"]["EEEE"]={}
myDict["DDDDD"]={}
myDict["DDDDD"]["EEEE"]="EEEE"
myDict["DDDDD"]["FFFF"]={}
myDict["DDDDD"]["GGGG"]={}

print("PRINT3\n",myDict)


myDict["AAAAA"]="AAAAA"
myDict["BBBBB"]={}
myDict["BBBBB"]["CCCC"] = "CCCC"
myDict["BBBBB"]["DDDD"]="DDDD"
myDict["CCCCC"]={}
myDict["CCCCC"]["DDDD"]="DDDD"
myDict["DDDDD"]={}
myDict["DDDDD"]["EEEE"]="EEEE"
myDict["DDDDD"]["FFFF"]={}
myDict["DDDDD"]["GGGG"]={}
myDict["GGGG"]={}
myDict["GGGG"]["HHH"]={}


print("PRINT4\n",myDict)


myDict["AAAAA"]="AAAAA"
myDict["BBBBB"]={}
myDict["BBBBB"]["CCCC"]="CCCC"
myDict["BBBBB"]["DDDD"]="DDDD"
myDict["CCCCC"]={}
myDict["CCCCC"]["DDDD"]="DDDD"
myDict["CCCCC"]["EEEE"]={}
myDict["CCCCC"]["EEEE"]["FFF"]="FFF"
myDict["DDDDD"]={}
myDict["DDDDD"]["EEEE"]="EEEE"
myDict["DDDDD"]["FFFF"]={}
myDict["DDDDD"]["FFFF"]["GGG"]="GGG"
myDict["GGGG"]={}
myDict["GGGG"]["HHH"]={}
myDict["GGGG"]["HHH"]["III"]="III"
print("PRINT5\n",myDict)




# CODE REMOVE "D" ALL SPACE 




myDict["BBBBB"]["CCCC"]="ZZZZ"
print( "PRINT():\n",myDict)
