class Calc:
    @staticmethod
    def add(a, b):  # 스테틱메서드
        print(a + b)

    def mul(self, a, b):  # 인스턴스메서드
        print(a * b)


Calc.add(1, 1)

c = Calc()
c.mul(2, 5)



class StringUtils:
    @staticmethod
    def toCamelcase(text):
        words = iter(text.split("_"))
        return next(words) + "".join(i.title() for i in words)

    @staticmethod
    def toSnakecase(text):
        letters = ["_" + i.lower() if i.isupper() else i for i in text]
        return "".join(letters).lstrip("_")


StringUtils.toCamelcase("last_modified_date")
StringUtils.toSnakecase("lastModifiedDate")
