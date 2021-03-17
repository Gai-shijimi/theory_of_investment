import math


class ReturnOnInvestment:
    def __init__(self, p0, p1, n):
        self.p0 = p0  # 前期
        self.p1 = p1  # 当期
        self.n = n  # 期間月数

    def ratio_roi(self):  # 投資収益率
        r1 = (self.p1 / self.p0 - 1) * self.n * 100
        return r1


# 一つ目の会社
# 各月の投資収益率 (p0 前期, p1 当期, n 期間月数)
roi_1 = ReturnOnInvestment(5970, 6190, 12)
roi_2 = ReturnOnInvestment(6190, 5600, 12)
roi_3 = ReturnOnInvestment(5600, 6380, 12)
roi_4 = ReturnOnInvestment(6380, 7090, 12)
roi_5 = ReturnOnInvestment(7090, 6450, 12)
roi_6 = ReturnOnInvestment(6450, 7100, 12)
roi_7 = ReturnOnInvestment(7100, 7980, 12)
roi_8 = ReturnOnInvestment(7980, 7200, 12)
roi_9 = ReturnOnInvestment(7200, 8100, 12)
roi_10 = ReturnOnInvestment(8100, 10000, 12)
roi_11 = ReturnOnInvestment(10000, 12310, 12)
roi_12 = ReturnOnInvestment(12310, 20500, 12)


# 2つ目の会社
# 各月の投資収益率 (p0 前期, p1 当期, n 期間月数)
roi_2_1 = ReturnOnInvestment(3710, 4320, 12)
roi_2_2 = ReturnOnInvestment(4320, 4570, 12)
roi_2_3 = ReturnOnInvestment(4570, 5350, 12)
roi_2_4 = ReturnOnInvestment(5350, 5260, 12)
roi_2_5 = ReturnOnInvestment(5260, 4980, 12)
roi_2_6 = ReturnOnInvestment(4980, 5130, 12)
roi_2_7 = ReturnOnInvestment(5130, 4970, 12)
roi_2_8 = ReturnOnInvestment(4970, 4400, 12)
roi_2_9 = ReturnOnInvestment(4400, 4460, 12)
roi_2_10 = ReturnOnInvestment(4460, 4400, 12)
roi_2_11 = ReturnOnInvestment(4400, 4200, 12)
roi_2_12 = ReturnOnInvestment(4200, 3810, 12)


# 3つ目の会社
# 各月の投資収益率 (p0 前期, p1 当期, n 期間月数)
roi_3_1 = ReturnOnInvestment(10900, 10800, 12)
roi_3_2 = ReturnOnInvestment(10800, 10180, 12)
roi_3_3 = ReturnOnInvestment(10180, 10250, 12)
roi_3_4 = ReturnOnInvestment(10250, 11240, 12)
roi_3_5 = ReturnOnInvestment(11240, 14400, 12)
roi_3_6 = ReturnOnInvestment(14400, 16850, 12)
roi_3_7 = ReturnOnInvestment(16850, 16770, 12)
roi_3_8 = ReturnOnInvestment(16770, 18550, 12)
roi_3_9 = ReturnOnInvestment(18550, 16960, 12)
roi_3_10 = ReturnOnInvestment(16960, 16560, 12)
roi_3_11 = ReturnOnInvestment(16560, 16800, 12)
roi_3_12 = ReturnOnInvestment(16800, 15700, 12)


# 平均投資収益率
per_roi = (roi_1.ratio_roi() + roi_2.ratio_roi() + roi_3.ratio_roi() + roi_4.ratio_roi() +
           roi_5.ratio_roi() + roi_6.ratio_roi() + roi_7.ratio_roi() + roi_8.ratio_roi() +
           roi_9.ratio_roi() + roi_10.ratio_roi() + roi_11.ratio_roi() + roi_12.ratio_roi()) / 12

per_roi_2 = (roi_2_1.ratio_roi() + roi_2_2.ratio_roi() + roi_2_3.ratio_roi() + roi_2_4.ratio_roi() + roi_2_5.ratio_roi()
             + roi_2_6.ratio_roi() + roi_2_7.ratio_roi() + roi_2_8.ratio_roi() + roi_2_9.ratio_roi()
             + roi_2_10.ratio_roi() + roi_2_11.ratio_roi() + roi_2_12.ratio_roi()) / 12

per_roi_3 = (roi_3_1.ratio_roi() + roi_3_2.ratio_roi() + roi_3_3.ratio_roi() + roi_3_4.ratio_roi()
             + roi_3_5.ratio_roi() + roi_3_6.ratio_roi() + roi_3_7.ratio_roi() + roi_3_8.ratio_roi()
             + roi_3_9.ratio_roi() + roi_3_10.ratio_roi() + roi_3_11.ratio_roi() + roi_3_12.ratio_roi()) / 12


# 乖離1
sa1_1 = roi_1.ratio_roi() - per_roi
sa1_2 = roi_2.ratio_roi() - per_roi
sa1_3 = roi_3.ratio_roi() - per_roi
sa1_4 = roi_4.ratio_roi() - per_roi
sa1_5 = roi_5.ratio_roi() - per_roi
sa1_6 = roi_6.ratio_roi() - per_roi
sa1_7 = roi_7.ratio_roi() - per_roi
sa1_8 = roi_8.ratio_roi() - per_roi
sa1_9 = roi_9.ratio_roi() - per_roi
sa1_10 = roi_10.ratio_roi() - per_roi
sa1_11 = roi_11.ratio_roi() - per_roi
sa1_12 = roi_12.ratio_roi() - per_roi

k1_1 = sa1_1 * sa1_1
k1_2 = sa1_2 * sa1_2
k1_3 = sa1_3 * sa1_3
k1_4 = sa1_4 * sa1_4
k1_5 = sa1_5 * sa1_5
k1_6 = sa1_6 * sa1_6
k1_7 = sa1_7 * sa1_7
k1_8 = sa1_8 * sa1_8
k1_9 = sa1_9 * sa1_9
k1_10 = sa1_10 * sa1_10
k1_11 = sa1_11 * sa1_11
k1_12 = sa1_12 * sa1_12


# 乖離2
sa2_1 = roi_2_1.ratio_roi() - per_roi_2
sa2_2 = roi_2_2.ratio_roi() - per_roi_2
sa2_3 = roi_2_3.ratio_roi() - per_roi_2
sa2_4 = roi_2_4.ratio_roi() - per_roi_2
sa2_5 = roi_2_5.ratio_roi() - per_roi_2
sa2_6 = roi_2_6.ratio_roi() - per_roi_2
sa2_7 = roi_2_7.ratio_roi() - per_roi_2
sa2_8 = roi_2_8.ratio_roi() - per_roi_2
sa2_9 = roi_2_9.ratio_roi() - per_roi_2
sa2_10 = roi_2_10.ratio_roi() - per_roi_2
sa2_11 = roi_2_11.ratio_roi() - per_roi_2
sa2_12 = roi_2_12.ratio_roi() - per_roi_2

k2_1 = sa2_1 * sa2_1
k2_2 = sa2_2 * sa2_2
k2_3 = sa2_3 * sa2_3
k2_4 = sa2_4 * sa2_4
k2_5 = sa2_5 * sa2_5
k2_6 = sa2_6 * sa2_6
k2_7 = sa2_7 * sa2_7
k2_8 = sa2_8 * sa2_8
k2_9 = sa2_9 * sa2_9
k2_10 = sa2_10 * sa2_10
k2_11 = sa2_11 * sa2_11
k2_12 = sa2_12 * sa2_12


# 乖離3
sa3_1 = roi_3_1.ratio_roi() - per_roi_3
sa3_2 = roi_3_2.ratio_roi() - per_roi_3
sa3_3 = roi_3_3.ratio_roi() - per_roi_3
sa3_4 = roi_3_4.ratio_roi() - per_roi_3
sa3_5 = roi_3_5.ratio_roi() - per_roi_3
sa3_6 = roi_3_6.ratio_roi() - per_roi_3
sa3_7 = roi_3_7.ratio_roi() - per_roi_3
sa3_8 = roi_3_8.ratio_roi() - per_roi_3
sa3_9 = roi_3_9.ratio_roi() - per_roi_3
sa3_10 = roi_3_10.ratio_roi() - per_roi_3
sa3_11 = roi_3_11.ratio_roi() - per_roi_3
sa3_12 = roi_3_12.ratio_roi() - per_roi_3


k3_1 = sa3_1 * sa3_1
k3_2 = sa3_2 * sa3_2
k3_3 = sa3_3 * sa3_3
k3_4 = sa3_4 * sa3_4
k3_5 = sa3_5 * sa3_5
k3_6 = sa3_6 * sa3_6
k3_7 = sa3_7 * sa3_7
k3_8 = sa3_8 * sa3_8
k3_9 = sa3_9 * sa3_9
k3_10 = sa3_10 * sa3_10
k3_11 = sa3_11 * sa3_11
k3_12 = sa3_12 * sa3_12

# 分散
bunsan1 = (k1_1 + k1_2 + k1_3 + k1_4 + k1_5 + k1_6 + k1_7 + k1_8 + k1_9 + k1_10 + k1_11 + k1_12) / 11
bunsan2 = (k2_1 + k2_2 + k2_3 + k2_4 + k2_5 + k2_6 + k2_7 + k2_8 + k2_9 + k2_10 + k2_11 + k2_12) / 11
bunsan3 = (k3_1 + k3_2 + k3_3 + k3_4 + k3_5 + k3_6 + k3_7 + k3_8 + k3_9 + k3_10 + k3_11 + k3_12) / 11


# 標準偏差
hyoujunhensa1 = math.sqrt(bunsan1)
hyoujunhensa2 = math.sqrt(bunsan2)
hyoujunhensa3 = math.sqrt(bunsan3)

# 共分散ab
seki1_ab = sa1_1 * sa2_1
seki2_ab = sa1_2 * sa2_2
seki3_ab = sa1_3 * sa2_3
seki4_ab = sa1_4 * sa2_4
seki5_ab = sa1_5 * sa2_5
seki6_ab = sa1_6 * sa2_6
seki7_ab = sa1_7 * sa2_7
seki8_ab = sa1_8 * sa2_8
seki9_ab = sa1_9 * sa2_9
seki10_ab = sa1_10 * sa2_10
seki11_ab = sa1_11 * sa2_11
seki12_ab = sa1_12 * sa2_12

kyobunsan_ab = (seki1_ab + seki2_ab + seki3_ab + seki4_ab + seki5_ab + seki6_ab + seki7_ab + seki8_ab + seki9_ab +
                seki10_ab + seki11_ab + seki12_ab) / 11

# 共分散bc
seki1_bc = sa2_1 * sa3_1
seki2_bc = sa2_2 * sa3_2
seki3_bc = sa2_3 * sa3_3
seki4_bc = sa2_4 * sa3_4
seki5_bc = sa2_5 * sa3_5
seki6_bc = sa2_6 * sa3_6
seki7_bc = sa2_7 * sa3_7
seki8_bc = sa2_8 * sa3_8
seki9_bc = sa2_9 * sa3_9
seki10_bc = sa2_10 * sa3_10
seki11_bc = sa2_11 * sa3_11
seki12_bc = sa2_12 * sa3_12

kyobunsan_bc = (seki1_bc + seki2_bc + seki3_bc + seki4_bc + seki5_bc + seki6_bc + seki7_bc + seki8_bc + seki9_bc +
                seki10_bc + seki11_bc + seki12_bc) / 11


# 共分散ca
seki1_ca = sa3_1 * sa1_1
seki2_ca = sa3_2 * sa1_2
seki3_ca = sa3_3 * sa1_3
seki4_ca = sa3_4 * sa1_4
seki5_ca = sa3_5 * sa1_5
seki6_ca = sa3_6 * sa1_6
seki7_ca = sa3_7 * sa1_7
seki8_ca = sa3_8 * sa1_8
seki9_ca = sa3_9 * sa1_9
seki10_ca = sa3_10 * sa1_10
seki11_ca = sa3_11 * sa1_11
seki12_ca = sa3_12 * sa1_12

kyobunsan_ca = (seki1_ca + seki2_ca + seki3_ca + seki4_ca + seki5_ca + seki6_ca + seki7_ca + seki8_ca + seki9_ca +
                seki10_ca + seki11_ca + seki12_ca) / 11


# 相関係数
skks_ab = kyobunsan_ab / hyoujunhensa1 / hyoujunhensa2
skks_bc = kyobunsan_bc / hyoujunhensa2 / hyoujunhensa3
skks_ca = kyobunsan_ca / hyoujunhensa3 / hyoujunhensa1

print("1番目の投資収益率は", roi_1.ratio_roi())
print("2番目の投資収益率は", roi_2.ratio_roi())
print("3番目の投資収益率は", roi_3.ratio_roi())
print("4番目の投資収益率は", roi_4.ratio_roi())
print("5番目の投資収益率は", roi_5.ratio_roi())
print("6番目の投資収益率は", roi_6.ratio_roi())
print("7番目の投資収益率は", roi_7.ratio_roi())
print("8番目の投資収益率は", roi_8.ratio_roi())
print("9番目の投資収益率は", roi_9.ratio_roi())
print("10番目の投資収益率は", roi_10.ratio_roi())
print("11番目の投資収益率は", roi_11.ratio_roi())
print("12番目の投資収益率は", roi_12.ratio_roi(), "\n")

print("平均投資収益率は", per_roi, "\n")

print("aの分散は", bunsan1)
print("bの分散は", bunsan2)
print("cの分散は", bunsan3, "\n")

print("aの標準偏差は", hyoujunhensa1)
print("bの標準偏差は", hyoujunhensa2)
print("cの標準偏差は", hyoujunhensa3, "\n")

print("abの共分散は", kyobunsan_ab)
print("bcの共分散は", kyobunsan_bc)
print("caの共分散は", kyobunsan_ca, "\n")

print("abの相関係数は", skks_ab)
print("bcの相関係数は", skks_bc)
print("caの相関係数は", skks_ca)


"""ここに値を入れれば投資収益率を出せる"""
roi = ReturnOnInvestment(217, 212, 12)  # (前期、当期、期間月数)
print(roi.ratio_roi())
