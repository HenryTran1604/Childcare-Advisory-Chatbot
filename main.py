from forward_chaining import ForwardChaining
from backward_chaining import BackwardChaining
from dao import DAO
from classification import classify
from helper import *

class Validation:
    def __init__(self) -> None:
        pass

    def validate_number(self, datatype, value):
        try:
            target_value = datatype(value)
            return target_value
        except:
            return None

    def validate_numberic_answer(self, datatype, answer):
        pass


class Main:
    def __init__(self) -> None:
        self.dao = DAO()
        self.facts = self.dao.find_all_facts()
        self.current_problems = []
        self.negative_problems = []
        self.age = 0
        self.weight = 0
        self.height = 0
        self.gender = None

    def greeting(self):
        pass

    def gender_question(self):
        chatbot_print(
            "Con của bạn là bé trai hay bé gái? (1 - bé trai, 0 - bé gái)"
        )
        self.gender = int(input())
        user_print(f'Con tôi là {"con trai" if self.gender == 1 else "con gái"}')

    def age_question(self):
        question = "Con bạn bao nhiêu tháng tuổi? (Nhập 1 số từ 1 đến 24)"
        chatbot_print(question)
        self.age = int(input())
        if 0 <= self.age < 1:
            period = "P1"
        elif 1 <= self.age < 2:
            period = "P2"
        elif 2 <= self.age < 4:
            period = "P3"
        elif 4 <= self.age < 6:
            period = "P4"
        elif 6 <= self.age < 7:
            period = "P5"
        elif 7 <= self.age < 9:
            period = "P6"
        elif 9 <= self.age < 12:
            period = "P7"
        else:
            period = "P8"
        user_print(f"Con tôi {self.age} tháng tuổi, [{self.facts[period]}]")

        self.current_problems.append(period)

    def height_weight_question(self):
        height_question = "Con của bạn có chiều cao là bao nhiêu cm?"
        chatbot_print(height_question)
        self.height = float(input())
        user_print(f"Con tôi cao {self.height} cm")
        weight_question = "Con của bạn có cân nặng là bao nhiêu (kg)?"
        chatbot_print(weight_question)
        self.weight = float(input())
        user_print(f"Con tôi nặng {self.weight} kg")
        self.current_problems.append(
            classify(self.gender, self.age, self.height, self.weight)
        )

    def __ask(self, question_keys):
        cnt = 0
        while cnt < len(question_keys):
            chatbot_print("Con của bạn có dấu hiệu nào trong các đặc điểm sau hay không?")
            for i, key in enumerate(question_keys):
                if key not in self.current_problems:
                    options_print(f"{i + 1}: [{key}] {self.facts[key]}")
            options_print("0. Con tôi không có triệu chứng nào ở trên")
            ans = int(input())
            if ans == 0:
                user_print(f'Con tôi không có dấu hiệu nào kể trên')
                break
            user_print(f"Con tôi có dấu hiệu: [{question_keys[ans - 1]}] {self.facts[question_keys[ans - 1]]}")

            self.current_problems.append(question_keys[ans - 1])
            cnt += 1
        for key in question_keys:
            if key not in self.current_problems:
                self.negative_problems.append(key)

    def health_question(self):
        chatbot_print("Chúng tôi muốn biết tình trạng về **SỨC KHỎE** hiện tại của con bạn")
        health_symptom_keys = ["SY2", "SY11", "SY43"]
        self.__ask(health_symptom_keys)

    def skin_question(self):
        chatbot_print("Chúng tôi muốn biết tình trạng về **DA** hiện tại của con bạn")
        skin_symptom_keys = ["SY5", "SY6", "SY41"]
        self.__ask(skin_symptom_keys)

    def sleep_question(self):
        chatbot_print("Chúng tôi muốn biết tình trạng về **GIẤC NGỦ** hiện tại của con bạn")
        sleep_symptom_keys = ["SY13", "SY14"]
        self.__ask(sleep_symptom_keys)

    def digest_question(self):
        chatbot_print("Chúng tôi muốn biết tình trạng về **TIÊU HÓA** hiện tại của con bạn")
        digest_symptom_keys = ["SY44", "SY16", "SY17", "SY18", "SY33"]
        self.__ask(digest_symptom_keys)

    def respiratory_question(self):
        chatbot_print("Chúng tôi muốn biết tình trạng về **TIÊU HÓA** hiện tại của con bạn")
        respiratory_symp_keys = ["SY19", "SY29"]
        self.__ask(respiratory_symp_keys)

    def vision_question(self):
        chatbot_print("Chúng tôi muốn biết tình trạng về **THỊ GIÁC** hiện tại của con bạn")
        vision_symp_keys = ["SY27", "SY28", "SY30", "SY15"]
        self.__ask(vision_symp_keys)

    def predict(self):
        self.greeting()
        self.gender_question()
        self.age_question()
        self.height_weight_question()
        self.health_question()
        self.skin_question()
        self.sleep_question()
        self.digest_question()
        self.respiratory_question()
        self.vision_question()
        fc = ForwardChaining()
        problems = fc.forward_chaining(self.current_problems)[2]
        fc.write('FC')
        others, predict_reasons = [], []
        status = ''
        for x in problems:
            if x[:2] == 'ST':
                status = x
            if x[:2] == 'RS':
                predict_reasons.append(x)
            else:
                others.append(x)
        chatbot_print(f'Chúng tôi đã có thông tin giới tính, chiều cao, cân nặng của con bạn. Theo đánh giá, con bạn đang trong tình trạng {self.facts[status]}')
        if len(predict_reasons):
            chatbot_print('Một cách chi tiết hơn, chúng tôi thấy con bạn có thể đang gặp các tình trạng sau:')
            for reason in predict_reasons:
                chatbot_print2(f'[{reason}] {self.facts[reason]}')
            self.current_problems = others
            return predict_reasons
    
    def confirm(self):
        predict_reasons = self.predict()
        bc = BackwardChaining()
        asked_symptoms = set()
        for reason in predict_reasons:
            result = bc.backward_chaining(self.current_problems, reason)
            if result:
                print(f'Chúng tôi đã có kết luận, con bạn đã bị {self.facts[symp]}')
                self.current_problems.append(reason)
                continue
            chatbot_print(f'Chúng tôi muốn xác nhận liệu con bạn có đang bị {self.facts[reason]} hay không.')
            chatbot_print2('Vui lòng trả lời có hoặc không những câu hỏi sau đây')
            remain_symps = list(self.dao.find_all_symtoms_by_reason(reason) - set(self.current_problems) - asked_symptoms - set(self.negative_problems))
            found = False
            while len(remain_symps) > 0:
                symp = remain_symps.pop()
                asked_symptoms.add(symp)
                chatbot_print(f'Con bạn có hiện tượng [{symp}] {self.facts[symp]} hay không?')
                ans = int(input())
                if ans == 1:
                    user_print('Có')
                    self.current_problems.append(symp)
                    result = bc.backward_chaining(self.current_problems, reason)
                    if result:
                        chatbot_print(f'Chúng tôi đã có kết luận, con bạn đã bị [{reason}] {self.facts[reason]}')
                        self.current_problems.append(reason)
                        found = True
                        break
                else:
                    user_print('Không')
            if not found:
                chatbot_print(f'Có vẻ con bạn không bị [{reason}] {self.facts[reason]}')
            chatbot_print('Bạn có muốn tiếp tục suy luận hay muốn nhận lời khuyên? (1 - tiếp tục, 0 - nhận lời khuyên)')
            tmp = int(input())
            if tmp == 0:
                self.give_advices()
                return
        self.give_advices()

    def confirm2(self):
        pass

    def give_advices(self):
        advices = []
        bc = BackwardChaining()
        print(self.current_problems)
        for i in range(1, 50):
            if bc.backward_chaining(self.current_problems, f'A{i}'):
                advices.append(f'A{i}')
        chatbot_print('Chúng tôi có lời tư vấn cho cách chăm sóc con của bạn như sau:')
        for advice in advices:
            chatbot_print(f'Đối với vấn đề {advice}')
            chatbot_print2(self.facts[advice])

    def run(self):
        self.predict()
        self.confirm()


main = Main()
main.confirm()
