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
    gender= None
    while True:
        response = input().strip()
        if response == '1':
            user_print('Nam')
            gender = 1
            break
        elif response == '0':
            user_print('Nữ')
            gender = 0
            break
        else :
            user_print(response)
            chatbot_print('Vui lòng chọn giới tính (nam: 1, nữ:0)')
    return gender

def age_response():
    age= None
    while True:
        response = input().strip()
        try:
            age = int(response.strip())
            user_print(age)
            break
        except:
            user_print(response)
            chatbot_print('Vui lòng nhập lại tháng tuổi [0; 24]')
    return age


def numeric_response(error):
    num = 0.0
    while True:
        response = input().strip()
        try:
            num = float(response)
            user_print(response)
            break
        except:
            user_print(response)
            chatbot_print(error)
    return num
