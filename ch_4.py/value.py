myDict ={
    "fast":" In a quick manner",
    "harry":"a coder",
    "marks":[1,2,3],
    "anotherdict":{"harry":"player"},
    1:2
}

print(list(myDict.keys()))
print(myDict.values())
print(myDict)
updateDict={
    "Lovish":"Friend",
    "Divya":"Friend",
    "shubham":"Friend"
}
myDict.update(updateDict)
print(myDict)