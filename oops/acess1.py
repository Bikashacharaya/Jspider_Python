class sample:

    def test(self):
        print("Test is running")
        self.__test2()

    def _test1(self):
        print("Test1 is running")
        self.__test2()

    def __test2(self):
        print("Test2 is running")


m1 = sample()
m1.test()
m1._test1()
