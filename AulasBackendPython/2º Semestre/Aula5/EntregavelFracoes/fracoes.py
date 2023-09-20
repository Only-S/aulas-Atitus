class Fracao:
    def __init__(self, num: int, den: int):
        if den == 0:
            raise ValueError("O denominador não pode ser zero.")
        divisor_comum = self.mdc(num, den)
        self._num = num // divisor_comum
        self._den = den // divisor_comum

    @property
    def num(self):
        return self._num

    @num.setter
    def num(self, valor):
        self._num = valor

    @property
    def den(self):
        return self._den

    @den.setter
    def den(self, valor):
        self._den = valor


    def mdc(self, a: int, b: int) -> int:
        while b != 0:
            r = a % b
            a = b
            b = r
        return a

    def __add__(self, outraFracao):
        novo_num = self._num * outraFracao.den + self._den * outraFracao.num
        novo_den = self._den * outraFracao.den
        if novo_den != 1:
            return f"{novo_num}/{novo_den}"
        else:
            return f"{novo_num}"
        # return f"{(self._num * outraFracao.den + self._den * outraFracao.num) / (self._den * outraFracao.den):.2f}"
    def __sub__(self, outraFracao):
        novo_num = self._num * outraFracao.den - self._den * outraFracao.num
        novo_den = self._den * outraFracao.den
        if novo_den != 1:
            return f"{novo_num}/{novo_den}"
        else:
            return f"{novo_num}"
        # return f"{(self._num * outraFracao.den - self._den * outraFracao.num) / (self._den * outraFracao.den):.2f}"

    def __mul__(self, outraFracao):
        novo_num = self._num * outraFracao.num
        novo_den = self._den * outraFracao.den
        if novo_den != 1:
            return f"{novo_num}/{novo_den}"
        else:
            return f"{novo_num}"
        # return f"{(self._num * outraFracao.num) / (self._den * outraFracao.den):.2f}"
    def __truediv__(self, outraFracao):
        novo_num = self._num * outraFracao.den
        novo_den = self._den * outraFracao.num
        if novo_den != 1:
            return f"{novo_num}/{novo_den}"
        else:
            return f"{novo_num}"
        # return f"{(self._num * outraFracao.den) / (self._den * outraFracao.num):.2f}"

    def __lt__(self, outraFracao):
        return self._num * outraFracao.den < self._den * outraFracao.num

    def __eq__(self, outraFracao):
        return self._num == outraFracao.num and self._den == outraFracao.den

    def __le__(self, outraFracao):
        return self.__eq__(outraFracao) or self.__lt__(outraFracao)

    def __str__(self):
        if self._den != 1:
            return f"{self._num}/{self._den}"
        else:
            return f"{self._num}"

    def __float__(self):
        return self._num / self._den

    def __int__(self):
        return self._num // self._den


f1 = Fracao(16, 9)
f2 = Fracao(3, 4)
f3 = Fracao(5, 25)
f4 = Fracao(16, 4)
f5 = Fracao(5, 4)

print(f1)
print(f2)
print(f3)
print(f4)
print(f5)

print("F1 + F2 =", f1 + f2)
print("F2 - F3 =", f2 - f3)
print("F3 * F4 =", f3 * f4)
print("F4 / F5 =", f4 / f5)

print("16/2 + 16/2 =", Fracao(16, 2) + Fracao(16, 2))

print("F2 == F3 =", f2 == f3)
print("F3 > F3 =", f3 > f3)
print("F4 == 4/1 =", f4 == Fracao(4, 1))

print(f1, float(f1), int(f1))
print(f2, float(f2), int(f2))
print(f3, float(f3), int(f3))
print(f4, float(f4), int(f4))
print(f5, float(f5), int(f5))
