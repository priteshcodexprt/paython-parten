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
myDict["BBBBB"]["CCCC"]="ZZZZ"
print( "PRINT1:\n",myDict)
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


myDict["BBBBB"]["CCCC"]="ZZZZ"
print( "PRINT2:\n",myDict)


{
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
myDict["BBBBB"]["CCCC"]="ZZZZ"
print( "PRINT2:\n",myDict)