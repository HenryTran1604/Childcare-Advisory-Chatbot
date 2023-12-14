from helper import *
import re
def symptoms_response(max, exist):
    while True:
        response = input()
        s = re.split('\s+|,+|\.', response)
        ans, is_valid = [], True
        for x in s:
            try:
                x = int(x)
                if x < 0 or x > max:
                    is_valid = False
                    break
                if x not in exist:
                    ans.append(x)
            except:
                is_valid = False
        if is_valid:
            break
        else:
            user_print(response)
            chatbot_print('Câu trả lời vừa rồi không hợp lệ, vui lòng nhập lại!')
    return ans

def yes_no_response():
    while True:
        response = input()
        if response.lower() in ['1', 'yes', 'có']:
            return True
        elif response.lower() in ['0', 'no', 'không']:
            return False
        else:
            user_print(response)
            chatbot_print('Câu trả lời vừa rồi không hợp lệ, vui lòng trả lời có hoặc không!')

def gender_response():
    gender, age  = None, None
    while True:
        response = input()
        check = 0
        if 'trai' in response or 'nam' in response:
            gender = 1
            check = 1
        elif 'gái' in response or 'nữ' in response:
            gender = 0
            check = 1
        s = response.split()
        for x in s:
            if x.isnumeric():
                age = int(x)
                check += 1
        if check < 2 or age < 0 or age > 24:
            user_print(response)
            chatbot_print('Vui lòng chọn giới tính (nam/nữ) và tháng tuổi trong khoảng [0, 24]')
        else:
            user_print(response)
            break
    return gender, age


def height_weight_response():
    while True:
        response = input()
        height, weight = 0, 0
        s, cnt = response.split(), 0
        for x in s:
            try:
                x = float(x)
                if height == 0:
                    cnt += 1
                    height = float(x)
                else:
                    cnt += 1
                    weight = float(x)
            except:
                pass
        if height <= 0 or height > 120 or weight <= 0 or weight > 34 or cnt != 2:
            user_print(response)
            chatbot_print('Vui lòng nhập lại chiều cao và cân nặng!')
        else:
            user_print(f"Con tôi cao {height} cm và có cân nặng {weight} kg")
            break
    return height, weight
