myDict={}
print("PRINT1\n",myDict)

myDict={
    "AAAAA": "AAAAA",
    "BBBBB": {},
    "CCCCC": {},
    "DDDDD": {}
}
myDict.pop("DDDDD")

print("PRINT2\n",myDict)
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
myDict.pop("DDDDD")
myDict.pop("DDDD")
print("PRINT3",myDict)
myDict={
    "AAAAA": "AAAAA",
    "BBBBB": {
        "CCCC": "CCCC",
        "DDDD": "DDDD"
    },
    "CCCCC": {
        "DDDD": "DDDD",
        "EEEE": {
            "FFF": "FFF"
        }
    },
    "DDDDD": {
        "EEEE": "EEEE",
        "FFFF": {
            "GGG": "GGG"
        },
        "GGGG": {
            "HHH": {}
        }
    }
}
myDict.pop("DDDDD")
print("PRINT4\n",myDict)
myDict={
    "AAAAA": "AAAAA",
    "BBBBB": {
        "CCCC": "CCCC",
        "DDDD": "DDDD"
    },
    "CCCCC": {
        "DDDD": "DDDD",
        "EEEE": {
            "FFF": "FFF"
        }
    },
    "DDDDD": {
        "EEEE": "EEEE",
        "FFFF": {
            "GGG": "GGG"
        },
        "GGGG": {
            "HHH": {
                "III": "III"
            }
        }
    }
}
myDict.pop("DDDDD")
print("PRINT5\n",myDict)
