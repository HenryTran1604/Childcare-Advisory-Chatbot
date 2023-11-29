from dao import DAO
import numpy
class FuzzyPercent:
    def __init__(self) -> None:
        self.low = 0
        self.mid = 0
        self.high = 0
    def __str__(self):
        return f'-> {self.low} {self.mid} {self.high}'

# y = ax + b (h, 1), (k, 0)
def find_coeff(h, k):
    a = 1/(h - k)
    b = -k*a
    return a, b

def fuzzificate(gender, age, weight, height): # mờ hóa
    std = DAO().find_std_weight_height_by_age_and_gender(gender, age)
    sd1, sd2 = (std[3] - std[2])/2, (std[4] - std[3])/2
    p = [std[2], std[2] + sd1 / 2, std[3] + sd2 / 2, std[4]]
    print(p)
    weight_fuzzy = FuzzyPercent()
    
    if weight < p[0]:
        weight_fuzzy.low = 1
    elif weight <= p[1]:
        a_low, b_low = find_coeff(p[0], p[1])
        weight_fuzzy.low = a_low * weight + b_low
        a_mid, b_mid = find_coeff(p[1], p[0])
        weight_fuzzy.mid = a_mid * weight + b_mid
    elif weight <= p[2]:
        weight_fuzzy.mid = 1
    elif weight <= p[3]:
        a_mid, b_mid = find_coeff(p[2], std[3])
        weight_fuzzy.mid = a_mid * weight + b_mid
        a_high, b_high = find_coeff(p[3], p[2])
        weight_fuzzy.high = a_high * weight + b_high
    else:
        weight_fuzzy.high = 1

    sd3, sd4 = (std[6] - std[5])/2, (std[7] - std[6])/2
    q = [std[5], std[5] + sd3 / 2, std[6] + sd4 / 2, std[7]]
    height_fuzzy = FuzzyPercent()
    if height < q[0]:
        height_fuzzy.low = 1
    elif height <= q[1]:
        a_low, b_low = find_coeff(q[0], q[1])
        height_fuzzy.low = a_low * height + b_low
        a_mid, b_mid = find_coeff(q[1], q[0])
        height_fuzzy.mid = a_mid * height + b_mid
    elif height <= q[2]:
        height_fuzzy.mid = 1
    elif height <= q[3]:
        a_mid, b_mid = find_coeff(q[2], q[3])
        height_fuzzy.mid = a_mid * height + b_mid
        a_high, b_high = find_coeff(q[3], q[2])
        height_fuzzy.high = a_high * height + b_high
    else:
        height_fuzzy.high = 1
    # print(weight_fuzzy, height_fuzzy)
    return weight_fuzzy, height_fuzzy

def caculate(gender, age, weight, height):
    weight_fuzzy, height_fuzzy = fuzzificate(gender, age, weight, height)
    percents = []
    st1_percent = max(min(weight_fuzzy.low, height_fuzzy.mid), min(weight_fuzzy.low, height_fuzzy.high))
    st2_percent = min(weight_fuzzy.mid, height_fuzzy.low)
    st3_percent = min(weight_fuzzy.low, height_fuzzy.low)
    st4_percent = max(min(weight_fuzzy.mid, height_fuzzy.mid), min(weight_fuzzy.mid, weight_fuzzy.high))
    st5_percent = max(min(weight_fuzzy.high, height_fuzzy.low), min(weight_fuzzy.high, height_fuzzy.mid), min(weight_fuzzy.high, height_fuzzy.high))
    percents = [st1_percent, st2_percent, st3_percent, st4_percent, st5_percent]
    print(percents)
    return f'ST{numpy.argmax(percents) + 1}'
