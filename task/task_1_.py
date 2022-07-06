#print1



myDict={}
print(myDict)
#print2
myDict2 = {
    "AAAAA": "AAAAA",
    "BBBBB": {},
    "CCCCC": {},
    "DDDDD": {}
}
print("PRINT2\n",myDict2)
#print3
myDict3 = {
    "AAAAA": "AAAAA",
    "BBBBB": {
    "CCCC":"CCCC",
    "DDDD":"DDDD"
    }
}
print("PRINT3\n",myDict3)
#PRINT4
myDict4={
    "AAAAA": "AAAAA",
    "BBBBB": {
        "CCCC": "CCCC",
        "DDDD": "DDDD"
    },
    "CCCC":{
        "DDDD":"DDDD",
        "EEEE":{
            "FFF":"FFF"
        }
    },
    "DDDDD":{
        "EEEE":"EEEE",
        "FFFF":{
            "GGG":"GGG"
        },
        "GGGG":{
            "HHH":{}
        }
    }
}
print("PRINT4\n",myDict4)
#PRINT5
myDict5={
    "AAAAA":"AAAAA",
    "BBBBB":{
        "CCCC":"CCCC",
        "DDDD":"DDDD",
    },
    "CCCC":{
        "DDDD":"DDDD",
        "EEEE":{
            "FFF":"FFF"
        }
    },
    "DDDDD":{
        "EEEE":"EEEE",
        "FFFF":{
            "GGG":"GGG"
        },
        "GGGG":{
            "HHH":{
                "III":{}
            }
        }
    }
}
print("PRINT5\n",myDict5)