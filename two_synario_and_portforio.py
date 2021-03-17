import math


class Synario:
    def __init__(self, kakuritsu, future_price, income, price):
        self.k = kakuritsu
        self.fp = future_price
        self.i = income
        self.p = price

    def capitalgain(self):
        """キャピタルゲイン"""
        return self.fp - self.p

    def reoi(self):
        """投資収益"""
        return self.fp - self.p + self.i

    def ratioinvest(self):
        """投資収益率(平均ではない)"""
        return (self.fp - self.p + self.i) / self.p * 100


# シナリオ(確率、将来の株価、配当、現在の株価、good, normal, bad, terrible)
a_g = Synario(30, 490, 10, 445)
a_n = Synario(40, 500, 10, 445)
a_b = Synario(30, 510, 10, 445)
# a_t = Synario(1, 1, 1, 1)

b_g = Synario(30, 930, 25, 675)
b_n = Synario(40, 830, 20, 675)
b_b = Synario(30, 780, 15, 675)
# b_t = Synario(1, 1, 1, 1)

# 平均投資収益率
per_ratio_a = (a_g.ratioinvest() + a_n.ratioinvest() + a_b.ratioinvest()) / 3
per_ratio_b = (b_g.ratioinvest() + b_n.ratioinvest() + b_b.ratioinvest()) / 3


# 標準偏差
sa_a1 = (a_g.ratioinvest() - per_ratio_a)
sa_a2 = (a_n.ratioinvest() - per_ratio_a)
sa_a3 = (a_b.ratioinvest() - per_ratio_a)
# sa_a4 = (a_t.ratioinvest() - per_ratio_a) * 100

sa_b1 = (b_g.ratioinvest() - per_ratio_b)
sa_b2 = (b_n.ratioinvest() - per_ratio_b)
sa_b3 = (b_b.ratioinvest() - per_ratio_b)
# sa_b4 = (b_t.ratioinvest() - per_ratio_a) * 100

# (#分散を噛ませる)
sa_a1_jou = sa_a1 ** 2
sa_a2_jou = sa_a2 ** 2
sa_a3_jou = sa_a3 ** 2
sa_b1_jou = sa_b1 ** 2
sa_b2_jou = sa_b2 ** 2
sa_b3_jou = sa_b3 ** 2

hyousa_a = math.sqrt((sa_a1_jou + sa_a2_jou + sa_a3_jou) / 3)
# hyousa_a = math.sqrt((sa_a1 * sa_a1 + sa_a2 * sa_a2 + sa_a3 * sa_a3 + sa_a4 * sa_a4) / 4)

hyousa_b = math.sqrt((sa_b1_jou + sa_b2_jou + sa_b3_jou) / 3)
# hyousa_b = math.sqrt((sa_b1 * sa_b1 + sa_b2 * sa_b2 + sa_b3 * sa_b3 + sa_b4 * sa_b4) / 4)

bunsan_a = (sa_a1_jou + sa_a2_jou + sa_a3_jou) / 3
bunsan_b = (sa_b1_jou + sa_b2_jou + sa_b3_jou) / 3


# 共分散
hssk_g = sa_a1 * sa_b1
hssk_n = sa_a2 * sa_b2
hssk_b = sa_a3 * sa_b3

kyobunsan_ab = (hssk_g + hssk_n + hssk_b) / 3


# 相関係数
sokankeisu = kyobunsan_ab / hyousa_a / hyousa_b


print("Aの好況 のキャピタルゲインは", a_g.capitalgain())
print("Aの普通　のキャピタルゲインは", a_n.capitalgain())
print("Aの不況　のキャピタルゲインは", a_b.capitalgain(), "\n")
# print("Aの大不況(あれば、ない時は無視)　のキャピタルゲインは", a_t.capitalgain(), "\n")
print("Bの好況 のキャピタルゲインは", b_g.capitalgain())
print("Bの普通　のキャピタルゲインは", b_n.capitalgain())
print("Bの不況　のキャピタルゲインは", b_b.capitalgain(), "\n")
# print("Bの大不況(あれば、ない時は無視)　のキャピタルゲインは", b_t.capitalgain(), "\n")


print("Aの好況 投資収益率は", a_g.ratioinvest(), "%")
print("Aの普通　投資収益率は", a_n.ratioinvest(), "%")
print("Aの不況　投資収益率", a_b.ratioinvest(), "%", "\n")
# print("Aの大不況(あれば。ない時は無視)　投資収益率", a_t.ratioinvest(), "\n")
print("Bの好況 投資収益率は", b_g.ratioinvest(), "%")
print("Bの普通　投資収益率は", b_n.ratioinvest(), "%")
print("Bの不況　投資収益率", b_b.ratioinvest(), "%", "\n")
# print("Bの大不況(あれば。ない時は無視)　投資収益率", b_t.ratioinvest(), "\n")

print("Aの平均投資収益率は", per_ratio_a, "%")
print("Bの平均投資収益率は", per_ratio_b, "%", "\n")

print("Aの標準偏差は", hyousa_a)
print("Bの標準偏差は", hyousa_b, "\n")

print("Aの分散", bunsan_a)
print("Bの分散", bunsan_b, "\n")

print("ABの共分散は", kyobunsan_ab, "\n")

print("相関係数は", sokankeisu, "\n")









