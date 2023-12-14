from forward_chaining import ForwardChaining
from backward_chaining import BackwardChaining
from dao import DAO
from fuzzy import caculate
from helper import *
from validation import *

class Main:
    def __init__(self) -> None:
        self.dao = DAO()
        self.facts = self.dao.find_all_facts()
        self.current_facts = [] # bộ nhớ hoạt động
        self.negative_facts = [] # những triệu chứng đã xuất hiện mà mình không chọn
        self.age = 0 # tháng tuổi
        self.weight = 0 # cân nặng 
        self.height = 0 # chiều cao
        self.gender = None # giới tính
        self.status = None # trạng thái dinh dưỡng
        fc_rules = self.dao.find_all_forward_rules() # tất cả luật tiến
        self.fc_rules_pr = fc_rules[:35] # luật tiến cho suy diễn vấn đề sức khỏe
        self.fc_rules_ad = fc_rules[35:] # luật tiến cho suy diễn lời khuyên
        self.bc_rules = self.dao.find_all_backward_rules() # luật lùi
    
    def fuzzy(self):
        self.status = caculate(self.gender, self.age, self.weight, self.height) # tính toán trạng thái dinh dưỡng
        self.current_facts.append(self.status)

    def consult_nutrition_module(self): # tư vấn dinh dưỡng
        self.current_facts.append('M1')
        self.fuzzy()
        self.give_advices()

    def issue_resolution_module(self): # giải quyết vấn dề sức khỏe
        self.confirm()

    def greeting(self):
        chatbot_print('Xin chào! Tôi là chatbot tư vấn dinh dưỡng và vận động cho trẻ từ 0 - 2 tuổi!')
        chatbot_print2('Bạn vui lòng trả lời những câu hỏi phía dưới để tôi có thể hỗ trợ!')
    
    def farewell(self):
        print()
        chatbot_print('Cảm ơn bạn đã sử dụng hệ thống. Hẹn gặp lại!')

    def gender_age_question(self): # câu hỏi về giới tính và tuổi
        chatbot_print("Giới tính con của bạn là gì? Cháu bao nhiêu tháng tuổi rồi?")
        # con tôi là con yyy. Cháu đã xx tháng tuổi rồi
        self.gender, self.age = gender_response()
        self.identify_period()

    def identify_period(self):
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
        self.current_facts.append(period)

    def height_weight_question(self): # câu hỏi về chiều cao cân nặng
        question = "Con của bạn có chiều cao (cm), cân nặng (kg) là bao nhiêu? (Vui lòng nhập đúng thứ tự và đơn vị)"
        # con tôi nặng xx kg và cao yy cm
        chatbot_print(question)
        self.height, self.weight = height_weight_response()
        

    def __ask(self, question_keys):
        ans = []
        while True:
            chatbot_print("Con của bạn có dấu hiệu nào trong các đặc điểm sau hay không?")
            for i, key in enumerate(question_keys):
                if key not in self.current_facts:
                    options_print(f"{i + 1}: [{key}] {self.facts[key]}")
            options_print("0. Con tôi không có triệu chứng nào ở trên")
            response = symptoms_response(max=len(question_keys), exist=ans)

            if len(response) == 1 and response[0] == 0:
                user_print(f'Con tôi không có dấu hiệu nào kể trên')
                break
            else:
                ans.extend(response)
                user_print(f"Con tôi có dấu hiệu: {ans}")
                for x in response:
                    if x != 0:
                        self.current_facts.append(question_keys[x - 1])
                if len(ans) == len(question_keys):
                    break
        for key in question_keys:
            if key not in self.current_facts:
                self.negative_facts.append(key)

    def health_question(self):
        chatbot_print("Chúng tôi muốn biết tình trạng về **SỨC KHỎE** hiện tại của con bạn")
        health_symptom_keys = ["SY2", "SY11"]
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
        digest_symptom_keys = ["SY16", "SY17", "SY18", "SY33"]
        self.__ask(digest_symptom_keys)

    def respiratory_question(self):
        chatbot_print("Chúng tôi muốn biết tình trạng về **HÔ HẤP** hiện tại của con bạn")
        respiratory_symp_keys = ["SY19", "SY29"]
        self.__ask(respiratory_symp_keys)

    def vision_question(self):
        chatbot_print("Chúng tôi muốn biết tình trạng về **THỊ GIÁC** hiện tại của con bạn")
        vision_symp_keys = ["SY27", "SY28", "SY30", "SY15"]
        self.__ask(vision_symp_keys)

    def predict(self): # dự đoán vấn đề trẻ đang gặp phải
        self.health_question()
        self.skin_question()
        self.sleep_question()
        self.digest_question()
        # self.respiratory_question()
        self.vision_question()
        fc = ForwardChaining()
        facts = fc.forward_chaining(self.current_facts, self.fc_rules_pr)[2]
        fc.write('FC')
        others, predict_problems = [], []
        status = ''
        for x in facts:
            if x[:2] == 'ST':
                status = x
            if x[:2] == 'PR':
                predict_problems.append(x)
            else:
                others.append(x)
        if len(predict_problems):
            chatbot_print('Theo đánh giá sơ bộ, chúng tôi thấy con bạn có thể đang gặp các tình trạng sau:')
            for problem in predict_problems:
                chatbot_print2(f'[{problem}] {self.facts[problem]}')
            self.current_facts = others
            return predict_problems
    
    def confirm(self): # thực hiện xác nhận lại các vấn đề đó
        predict_problems = self.predict()
        # print(self.negative_facts)
        bc = BackwardChaining()
        asked_symptoms = set() # những triệu chứng đã hỏi
        for i, problem in enumerate(predict_problems):
            result = bc.backward_chaining(self.current_facts, problem, self.bc_rules) 
            if result:
                print(f'Chúng tôi đã có kết luận, con bạn đã bị {self.facts[symp]}')
                self.current_facts.append(problem)
                continue
            chatbot_print(f'Chúng tôi muốn xác nhận liệu con bạn có đang bị {self.facts[problem]} hay không.')
            chatbot_print2('Vui lòng trả lời có hoặc không những câu hỏi sau đây')
            remain_symps = sorted(self.dao.find_all_symtoms_by_problem(problem) - set(self.current_facts) - asked_symptoms - set(self.negative_facts))
            found = False
            while len(remain_symps) > 0:
                symp = remain_symps.pop()
                asked_symptoms.add(symp)
                chatbot_print(f'Con bạn có hiện tượng [{symp}] {self.facts[symp]} hay không?')
                ans = yes_no_response()
                if ans:
                    user_print('Có')
                    self.current_facts.append(symp)
                    result = bc.backward_chaining(self.current_facts, problem, self.bc_rules)
                    bc.write('BC')
                    if result:
                        chatbot_print(f'Chúng tôi đã có kết luận, con bạn đã bị [{problem}] {self.facts[problem]}')
                        self.current_facts.append(problem)
                        found = True
                        break
                else:
                    user_print('Không')
                
            if not found:
                chatbot_print(f'Có vẻ con bạn không bị [{problem}] {self.facts[problem]}')
            if i < len(predict_problems) - 1:
                chatbot_print('Bạn có muốn tiếp tục suy luận hay muốn nhận lời khuyên? (1 - tiếp tục, 0 - nhận lời khuyên)')
                tmp = input()
                if tmp == '0':
                    user_print('Đưa cho tôi lời khuyên')
                    self.give_advices()
                    return
                else:
                    user_print('Tiếp tục')
        self.give_advices()


    def give_advices(self):
        fc = ForwardChaining()
        result = fc.forward_chaining(self.current_facts, self.fc_rules_ad)[2]
        fc.write('ADVICE')
        advices = sorted([x for x in result if x[0] == 'A'], key=lambda x : int(x[1:])) # lọc ra lời khuyên
        problems = sorted([x for x in result if x[:2] == 'PR']) # lọc ra vấn đề đã chắc chắn
        if self.status:
            chatbot_print(f'Chúng tôi đã có thông tin giới tính, chiều cao, cân nặng của con bạn. Theo đánh giá, con bạn đang trong tình trạng {self.facts[self.status]}')            
        if len(advices):
            if self.status == None:
                chatbot_print(f'Con bạn đang gặp các vấn đề: {", ".join(self.facts[problem] for problem in problems)}')
            chatbot_print('Chúng tôi có lời tư vấn cho cách chăm sóc con của bạn như sau:')
            for advice in advices:
                chatbot_print2(self.facts[advice])
        else:
            chatbot_print('Có vẻ con bạn đang không gặp các vấn đề mà hệ thống của chúng tôi có thể giải quyết.')

    def run(self):
        self.greeting()
        self.gender_age_question()
        chatbot_print('Bạn muốn nhận lời khuyên từ mục nào?')
        chatbot_print2('1. Tư vấn dinh dưỡng và vận động')
        chatbot_print2('2. Tư vấn về các vấn đề sức khỏe')
        ans = input()
        while True:
            if ans == '1':
                user_print('Tôi muốn tư vấn về dinh dưỡng và vận động')
                self.height_weight_question()
                self.consult_nutrition_module()
                break
            elif ans == '2':
                user_print('Tôi muốn tư vấn về các vấn đề sức khỏe')
                self.issue_resolution_module()
                break
            else:
                chatbot_print('Vui lòng nhập lại!')
        self.farewell()


main = Main()
main.run()
# main.confirm()
