from dao import DAO
import numpy
class FuzzyRate: # object fuzzy chứa giá trị của 3 hàm thành viên
    def __init__(self) -> None:
        self.low = 0
        self.mid = 0
        self.high = 0
    def __str__(self):
        return f'-> {self.low} {self.mid} {self.high}'

# y = ax + b (h, 1), (k, 0)
def find_coeff(h, k): # tính hệ số cho các hàm thành viên
    a = 1/(h - k)
    b = -k*a
    return a, b

def fuzzificate(gender, age, weight, height): # mờ hóa
    std = DAO().find_std_weight_height_by_age_and_gender(gender, age) # lấy ra chiều cao cân nặng chuẩn theo giới tính và tháng tuổi
    sd1, sd2 = (std[3] - std[2])/2, (std[4] - std[3])/2 # tính phương của 2 khoảng
    w = [std[2], std[2] + sd1 / 2, std[3] + sd2 / 2, std[4]] # 4 giá trị w1, w2, w3, w4
    #print(w)
    weight_fuzzy = FuzzyRate()
    
    if weight < w[0]: # nếu cân nặng dưới -2sd => low = 1
        weight_fuzzy.low = 1
    elif weight <= w[1]: # nếu cân nặng nằm trong khoảng từ -2sd đến -1.5sd => tính giá trị low và mid
        a_low, b_low = find_coeff(w[0], w[1]) # tính hệ số đường thẳng low
        weight_fuzzy.low = a_low * weight + b_low # tính tỷ lệ
        a_mid, b_mid = find_coeff(w[1], w[0]) # tính hệ số đường thằng mid
        weight_fuzzy.mid = a_mid * weight + b_mid # tính tỷ lệ
    elif weight <= w[2]: # nếu cân nặng nằm trong khoảng từ -1.5sd đến 1.5sd => mid = 1
        weight_fuzzy.mid = 1
    elif weight <= w[3]: # nếu cân nặng nằm trong khoảng từ 1.5sd đến 2sd => tính giá trị high và mid
        a_mid, b_mid = find_coeff(w[2], std[3]) # tính hệ số đường thẳng mid
        weight_fuzzy.mid = a_mid * weight + b_mid  # tính tỷ lệ
        a_high, b_high = find_coeff(w[3], w[2]) # tính hệ số đường thẳng high
        weight_fuzzy.high = a_high * weight + b_high # tính tỷ lệ
    else:
        weight_fuzzy.high = 1 # nếu cân nặng lớn hơn 2sd => high = 1

    sd3, sd4 = (std[6] - std[5])/2, (std[7] - std[6])/2
    h = [std[5], std[5] + sd3 / 2, std[6] + sd4 / 2, std[7]]
    height_fuzzy = FuzzyRate()
    if height < h[0]:  # nếu chiều cao dưới -2sd => low = 1
        height_fuzzy.low = 1
    elif height <= h[1]: # nếu chiều cao nằm trong khoảng từ -2sd đến -1.5sd => tính giá trị low và mid
        a_low, b_low = find_coeff(h[0], h[1]) # tính hệ số đường thẳng low
        height_fuzzy.low = a_low * height + b_low # tính tỷ lệ
        a_mid, b_mid = find_coeff(h[1], h[0]) # tính hệ số đường thằng mid
        height_fuzzy.mid = a_mid * height + b_mid # tính tỷ lệ
    elif height <= h[2]: # nếu chiều cao nằm trong khoảng từ -1.5sd đến 1.5sd => mid = 1
        height_fuzzy.mid = 1
    elif height <= h[3]: # nếu chiều cao nằm trong khoảng từ 1.5sd đến 2sd => tính giá trị high và mid
        a_mid, b_mid = find_coeff(h[2], h[3]) # tính hệ số đường thẳng mid
        height_fuzzy.mid = a_mid * height + b_mid # tính tỷ lệ
        a_high, b_high = find_coeff(h[3], h[2]) # tính hệ số đường thẳng high
        height_fuzzy.high = a_high * height + b_high # tính tỷ lệ
    else:
        height_fuzzy.high = 1 # nếu chiều cao lớn hơn 2sd => high = 1
    # print(weight_fuzzy, height_fuzzy)
    return weight_fuzzy, height_fuzzy

def caculate(gender, age, weight, height):
    log = ''
    weight_fuzzy, height_fuzzy = fuzzificate(gender, age, weight, height)
    rates = []
    # luật fuzzy
    st1_rate = max(min(weight_fuzzy.low, height_fuzzy.mid), min(weight_fuzzy.low, height_fuzzy.high)) 
    st2_rate = min(weight_fuzzy.mid, height_fuzzy.low)
    st3_rate = min(weight_fuzzy.low, height_fuzzy.low)
    st4_rate = max(min(weight_fuzzy.mid, height_fuzzy.mid), min(weight_fuzzy.mid, height_fuzzy.high))
    st5_rate = max(min(weight_fuzzy.high, height_fuzzy.low), min(weight_fuzzy.high, height_fuzzy.mid), min(weight_fuzzy.high, height_fuzzy.high))
    rates = [st1_rate, st2_rate, st3_rate, st4_rate, st5_rate]

    log += f'Giới tính, tháng tuổi, cân nặng, chiều cao: {gender, age, weight, height}\n'
    log += f'Giá trị hàm thanh viên weight: (low, mid, height) = ({weight_fuzzy})\n'
    log += f'Giá trị hàm thanh viên height: (low, mid, height) = ({height_fuzzy})\n'
    log += f'Tỷ lệ của [ST1, ST2, ST3, ST4, ST5] = {rates}\n'
    # print(rates)
    fuzzy_file = open('log/fuzzy.txt', 'w', encoding='utf8')
    fuzzy_file.writelines(log)
    return f'ST{numpy.argmax(rates) + 1}'
