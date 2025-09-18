class stud:
    def __init__(self,a,b,c):
        self.sno=a
        self.sname=b
        self.sage=c
    def disp(self):
        print(self.sno)
        print(self.sname)
        print(self.sage)

x=int(input("enter sno:"))
y=(input("enter snmae:"))
z=int(input("enter sage:"))
ob=stud(x,y,z)
ob.disp()
