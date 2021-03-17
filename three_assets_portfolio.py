import math

"""共分散と平均投資収益率"""


class KandH:
    def __init__(self, ht1, ht2, ht3, b1, b2, b3, kbab, kbbc, kbca):
        self.ht1 = ht1
        self.ht2 = ht2
        self.ht3 = ht3
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.kbab = kbab
        self.kbbc = kbbc
        self.kbca = kbca

    def hyousa_a(self):
        return math.sqrt(self.b1)

    def hyousa_b(self):
        return math.sqrt(self.b2)

    def hyousa_c(self):
        return math.sqrt(self.b3)

    def kb_ab(self):
        return self.kbab

    def kb_bc(self):
        return self.kbbc

    def kb_ca(self):
        return self.kbca

    def ht1(self):
        return self.ht1

    def ht2(self):
        return self.ht2

    def ht3(self):
        return self.ht3


# 共分散と平均投資収益率
kandh = KandH(
    148,  # 平均投資収益率１
    7,  # 平均投資収益率２
    43,  # 平均投資収益率３
    6.13,  # 分散１
    1.16,  # 分散２
    1.69,  # 分散３
    -0.58,  # 分散１２
    -0.33,  # 分散２３
    -1.47,  # 分散３１
)


# 相関係数
soukan_ab = kandh.kb_ab() / kandh.hyousa_a() / kandh.hyousa_b()
soukan_bc = kandh.kb_bc() / kandh.hyousa_b() / kandh.hyousa_c()
soukan_ca = kandh.kb_ca() / kandh.hyousa_c() / kandh.hyousa_a()


print("aの標準偏差", kandh.hyousa_a())
print("bの標準偏差", kandh.hyousa_b())
print("cの標準偏差", kandh.hyousa_c())

print("abの相関係数は", soukan_ab)
print("bcの相関係数は", soukan_bc)
print("caの相関係数は", soukan_ca)
