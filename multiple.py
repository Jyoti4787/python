#multiple
class A:
    def Ainfo(self):
        print("A")

class B:
    def Binfo(self):
        print("B")
class C(A,B):
    def Cinfo(self):
        A().Ainfo()
        print("C")
        B().Binfo()
Cobj=C()
Cobj.Cinfo()