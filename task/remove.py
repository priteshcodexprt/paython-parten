

myDict={
    "AAAAA": "AAAAA",
    "BBBBB": {},
    "CCCCC": {},
    "DDDDD": {}
}
D=myDict.pop("DDDDD")
print("PRINT1\n",myDict)

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
print("PRINT2\n",myDict)
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

myDict.popitem()
print("PRINT3\n",myDict)
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
myDict.popitem()
print(myDict)
