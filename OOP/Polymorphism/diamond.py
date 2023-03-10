import charset_normalizer.md

from other.datetime import b


class A:
    def method(self):
        print("This method belongs to class A")


class B(A):
    def method(self):
        print("This method belongs to class B")
    pass

class C(A):
        def method(self):
            print("This method belongs to class B")
        pass

class D(C, B):
    pass

d = D()
a = A()

d.method()
a.method()


charset_normalizer.md.mess_ratio()
