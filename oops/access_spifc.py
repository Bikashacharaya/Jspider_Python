class demo:

    def __init__(self):
        self.name = "Bikash"
        self._add = "Bangalore"
        self.__phn = 9606223683

    def display(self):
        print(self.name, self._add, self.__phn)


m1 = demo()
m1.display()
print(m1.name)
print(m1._add)
print(m1.__phn)


# class myclass:
#     def __init__(self):
#         self.var1 = 100  # public attribute
#         self._var2 = 200  # protected attribute
#         self.__var3 = 300  # private attribute

#     def display(self):
#         print("Var 1 value->", self.var1)
#         print("Var 2 value->", self._var2)
#         print("Var 3 value->", self.__var3)


# m1 = myclass()
# m1.display()
# print(m1.var1)
# print(m1._var2)
# print(m1.__var3)
