from dao import DAO
import numpy
class FuzzyRate:
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
    w = [std[2], std[2] + sd1 / 2, std[3] + sd2 / 2, std[4]]
    print(w)
    weight_fuzzy = FuzzyRate()
    
    if weight < w[0]:
        weight_fuzzy.low = 1
    elif weight <= w[1]:
        a_low, b_low = find_coeff(w[0], w[1])
        weight_fuzzy.low = a_low * weight + b_low
        a_mid, b_mid = find_coeff(w[1], w[0])
        weight_fuzzy.mid = a_mid * weight + b_mid
    elif weight <= w[2]:
        weight_fuzzy.mid = 1
    elif weight <= w[3]:
        a_mid, b_mid = find_coeff(w[2], std[3])
        weight_fuzzy.mid = a_mid * weight + b_mid
        a_high, b_high = find_coeff(w[3], w[2])
        weight_fuzzy.high = a_high * weight + b_high
    else:
        weight_fuzzy.high = 1

    sd3, sd4 = (std[6] - std[5])/2, (std[7] - std[6])/2
    h = [std[5], std[5] + sd3 / 2, std[6] + sd4 / 2, std[7]]
    height_fuzzy = FuzzyRate()
    if height < h[0]:
        height_fuzzy.low = 1
    elif height <= h[1]:
        a_low, b_low = find_coeff(h[0], h[1])
        height_fuzzy.low = a_low * height + b_low
        a_mid, b_mid = find_coeff(h[1], h[0])
        height_fuzzy.mid = a_mid * height + b_mid
    elif height <= h[2]:
        height_fuzzy.mid = 1
    elif height <= h[3]:
        a_mid, b_mid = find_coeff(h[2], h[3])
        height_fuzzy.mid = a_mid * height + b_mid
        a_high, b_high = find_coeff(h[3], h[2])
        height_fuzzy.high = a_high * height + b_high
    else:
        height_fuzzy.high = 1
    # print(weight_fuzzy, height_fuzzy)
    return weight_fuzzy, height_fuzzy

def caculate(gender, age, weight, height):
    log = ''
    weight_fuzzy, height_fuzzy = fuzzificate(gender, age, weight, height)
    log += f'Giới tính, tháng tuổi, cân nặng, chiều cao: {gender, age, weight, height}\n'
    log += f'Giá trị hàm thanh viên weight: (low, mid, height) = ({weight_fuzzy})\n'
    log += f'Giá trị hàm thanh viên height: (low, mid, height) = ({height_fuzzy})\n'
    rates = []
    st1_rate = max(min(weight_fuzzy.low, height_fuzzy.mid), min(weight_fuzzy.low, height_fuzzy.high))
    st2_rate = min(weight_fuzzy.mid, height_fuzzy.low)
    st3_rate = min(weight_fuzzy.low, height_fuzzy.low)
    st4_rate = max(min(weight_fuzzy.mid, height_fuzzy.mid), min(weight_fuzzy.mid, height_fuzzy.high))
    st5_rate = max(min(weight_fuzzy.high, height_fuzzy.low), min(weight_fuzzy.high, height_fuzzy.mid), min(weight_fuzzy.high, height_fuzzy.high))
    rates = [st1_rate, st2_rate, st3_rate, st4_rate, st5_rate]
    log += f'Tỷ lệ của [ST1, ST2, ST3, ST4, ST5] = {rates}\n'
    # print(rates)
    fuzzy_file = open('log/fuzzy.txt', 'w', encoding='utf8')
    fuzzy_file.writelines(log)
    return f'ST{numpy.argmax(rates) + 1}'
