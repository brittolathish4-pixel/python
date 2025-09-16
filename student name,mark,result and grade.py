name=input("enter your name")
rollno=int(input("enter your rollno"))
m1=int(input("enter your m1"))
m2=int(input("enter your m2"))
m3=int(input("enter your m3"))
m4=int(input("enter your m4"))
m5=int(input("enter your m5"))
total=m1+m2+m3+m4+m5
print("total=",total)
avg=total/5
if m1>40 and m2>40 and m3>40 and m4>40 and m5>40:
    result="pass"
    print("result is pass")
else:
    result="fail"
    print("result is fail")
if result=="pass":
    if avg>=90:
        print("grade A")
    elif avg>=80:
        print("grade B")
    elif avg>=70:
        print("grade C")
    elif avg>=60:
        print("grade D")
    else:
        print("grade E")
