# # myDict={}
# # print("PRINT1\n",myDict)


# # myDict["AAAAA"]="AAAAA"
# # myDict["BBBBB"]={}
# # myDict["CCCCC"]={}
# # myDict["DDDDD"]={}


# # print("PRINT2\n",myDict)

# # myDict["AAAAA"]="AAAAA"
# # myDict["BBBBB"]={}
# # myDict["BBBBB"]["CCCC"] = "CCCC"
# # myDict["BBBBB"]["DDDD"]="DDDD"
# # myDict["CCCCC"]={}
# # myDict["CCCCC"]["DDDD"]="DDDD"
# # myDict["CCCCC"]["EEEE"]={}
# # myDict["DDDDD"]={}
# # myDict["DDDDD"]["EEEE"]="EEEE"
# # myDict["DDDDD"]["FFFF"]={}
# # myDict["DDDDD"]["GGGG"]={}

# # print("PRINT3\n",myDict)


# # myDict["AAAAA"]="AAAAA"
# # myDict["BBBBB"]={}
# # myDict["BBBBB"]["CCCC"] = "CCCC"
# # myDict["BBBBB"]["DDDD"]="DDDD"
# # myDict["CCCCC"]={}
# # myDict["CCCCC"]["DDDD"]="DDDD"
# # myDict["DDDDD"]={}
# # myDict["DDDDD"]["EEEE"]="EEEE"
# # myDict["DDDDD"]["FFFF"]={}
# # myDict["DDDDD"]["GGGG"]={}
# # myDict["GGGG"]={}
# # myDict["GGGG"]["HHH"]={}


# # print("PRINT4\n",myDict)


# # myDict["AAAAA"]="AAAAA"
# # myDict["BBBBB"]={}
# # myDict["BBBBB"]["CCCC"]="CCCC"
# # myDict["BBBBB"]["DDDD"]="DDDD"
# # myDict["CCCCC"]={}
# # myDict["CCCCC"]["DDDD"]="DDDD"
# # myDict["CCCCC"]["EEEE"]={}
# # myDict["CCCCC"]["EEEE"]["FFF"]="FFF"
# # myDict["DDDDD"]={}
# # myDict["DDDDD"]["EEEE"]="EEEE"
# # myDict["DDDDD"]["FFFF"]={}
# # myDict["DDDDD"]["FFFF"]["GGG"]="GGG"
# # myDict["GGGG"]={}
# # myDict["GGGG"]["HHH"]={}
# # myDict["GGGG"]["HHH"]["III"]="III"
# # print("PRINT5\n",myDict)




# CODE REMOVE "D" ALL SPACE 



# myDict={
#     "AAAAA": "AAAAA",
#     "BBBBB": {},
#     "CCCCC": {},
#     "DDDDD": {}
# }
# D=myDict.pop("DDDDD")
# print("PRINT1\n",myDict)

# myDict={
#     "AAAAA": "AAAAA",
#     "BBBBB": {
#         "CCCC": "CCCC",
#         "DDDD": "DDDD"
#     },
#     "CCCCC": {
#         "DDDD": "DDDD",
#         "EEEE": {}
#     },
#     "DDDDD": {
#         "EEEE": "EEEE",
#         "FFFF": {},
#         "GGGG": {}
#     }
# }

# myDict.popitem()
# print("PRINT2\n",myDict)
# myDict={
#     "AAAAA": "AAAAA",
#     "BBBBB": {
#         "CCCC": "CCCC",
#         "DDDD": "DDDD"
#     },
#     "CCCCC": {
#         "DDDD": "DDDD",
#         "EEEE": {
#             "FFF": "FFF"
#         }
#     },
#     "DDDDD": {
#         "EEEE": "EEEE",
#         "FFFF": {
#             "GGG": "GGG"
#         },
#         "GGGG": {
#             "HHH": {}
#         }
#     }
# }

# myDict.popitem()
# print("PRINT3\n",myDict)
# myDict={
#     "AAAAA": "AAAAA",
#     "BBBBB": {
#         "CCCC": "CCCC",
#         "DDDD": "DDDD"
#     },
#     "CCCCC": {
#         "DDDD": "DDDD",
#         "EEEE": {
#             "FFF": "FFF"
#         }
#     },
#     "DDDDD": {
#         "EEEE": "EEEE",
#         "FFFF": {
#             "GGG": "GGG"
#         },
#         "GGGG": {
#             "HHH": {
#                 "III": "III"
#             }
#         }
#     }
# }

# myDict.popitem()
# print("PRINT4\n",myDict)

# myDict["CCCCC"]="CCCCC"
# myDict.update["ZZZZZ"]="ZZZZZ"

# print(myDict)

# myDict={
#     "AAAAA": "AAAAA",
#     "BBBBB": {},
#     "CCCCC": {},
#     "DDDDD": {}
# }

myDict={
    "AAAAA": "AAAAA",
    "BBBBB": {
        "CCCC": "CCCC",
        "DDDD": "DDDD"
    },
    "CCCCC": {
        "DDDD": "DDDD",
        "EEEE": {}
    },
    "DDDDD": {
        "EEEE": "EEEE",
        "FFFF": {},
        "GGGG": {}
    }
}

myDict.update
print(myDict)