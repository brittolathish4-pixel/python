d={"eno":123 ,"ename":"abc"}
print(d)
print(d["eno"])
print(d.get("ensme"))
d["ename"]="xyz"
print(d)
d["age"]=19
print(d)
for key in d:
    print(key)
for value in d.values():
    print(key,":",value)
d.pop("eno")
print(d)
d.popitem()
print(d)
d.clear()
print(d)    
