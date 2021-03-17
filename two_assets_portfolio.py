import math
import two_synario_and_portforio


class AssetsPort2:
    """synario_and_portfolio.py　の値をみること"""
    def __init__(self, w1, pr1, w2, pr2, b1, b2, kb):  # (組み入れ比率１、平均収益率１、組み入れ比率２、平均収益率２、分散１、２、共分散)
        self.w1 = w1
        self.pr1 = pr1
        self.w2 = w2
        self.pr2 = pr2
        self.b1 = b1
        self.b2 = b2
        self.kb = kb

    def assets_p_pr(self):
        """２資産ポートフォリオの平均収益率"""
        return self.w1 * self.pr1 + self.w2 * self.pr2

    def bunsan_assets_2(self):
        """２資産ポートフォリオの収益率の分散"""
        return (self.w1**2 * self.b1) + (self.w2**2 * self.b2) + (2 * self.w1 * self.w2 * self.kb)

    def perr1(self):
        return self.pr1

    def perr2(self):
        return self.pr2

    def bunsan1(self):
        return self.b1

    def bunsan2(self):
        return self.b2

    def kyobunsan(self):
        return self.kb


assets2 = AssetsPort2(
    0.5,  # 組み入れ比率１
    14.606741573033707,  # 平均収益率１
    0.5,  # 組み入れ比率２
    28.395061728395063,  # 平均収益率２
    3.366578293986452,  # 分散１
    96.69257735101355,  # 分散２
    -17.755583298654468   # 共分散
)

hyosa_assets_2 = math.sqrt(assets2.bunsan_assets_2())


# 比率
hiritsu1 = (assets2.bunsan2() - assets2.kyobunsan()) / (assets2.bunsan1() + assets2.bunsan2() - 2 * assets2.kyobunsan())
hiritsu2 = (assets2.bunsan1() - assets2.kyobunsan()) / (assets2.bunsan1() + assets2.bunsan2() - 2 * assets2.kyobunsan())

# 標準偏差(この比率を使った)
hyousa_hiritsu1_2 = (hiritsu1**2 * assets2.bunsan1()) + (hiritsu2**2 * assets2.bunsan2())\
                    + (2 * hiritsu1 * hiritsu2 * assets2.kyobunsan())

# この比率を使った平均投資収益率
heikin_ratio = hiritsu1 * assets2.perr1() + hiritsu2 * assets2.perr2()

print("２資産ポートフォリオの分散は", assets2.bunsan_assets_2())
print("２資産ポートフォリオの標準偏差(リスク)は", hyosa_assets_2, "\n")

print("比率１は", hiritsu1)
print("比率２は", hiritsu2, "\n")

print("この比率１と２を使った標準偏差は", hyousa_hiritsu1_2)

print("この比率を使った平均投資収益率は", heikin_ratio)







