# multi-level

class A:
    def Ainfo(self):
        print("A")

class B(A):
    def Binfo(self):
        print("B")
        A().Ainfo()

class C(B):
    def Cinfo(self):
        print("C")
        B().Binfo()
        
Cobj=C()
Cobj.Cinfo()
