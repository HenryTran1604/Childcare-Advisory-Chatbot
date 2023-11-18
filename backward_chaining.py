from rule import Rule
from dao import DAO
class BackwardChaining:
    def __init__(self):
        dao = DAO()
        self.bc_rules = dao.find_all_backward_rules()

    def do_backward_chaining(self, facts, goal, indent=""):# trả về giá trị true false caajp0 nhật cho result
            ls=0 # Biến điều kiện, nếu ls==0 thì không có luật nào phù hợp với goal và fact thì trả về false
            for rule in self.rules:
                # ls=0
                dk=1 #Biến điều kiện để dừng vòng lặp khi có triệu chứng không thuộc fact ban đầu
                
                if rule.consequent == goal:
                    for i in range(len(rule.antecedent)):
                        fact_guess=str(rule.antecedent[i])
                        if fact_guess not in facts:
                            dk=0
                            break

                            # dk=1
                    self.road="R" + str(self.rules.index(rule) + 1)
                    
                    if dk == 1: #Kiểm tra nếu đúng hết các triệu chứng thì dừng vòng lặp
                        ls=1 #Kiểm tra xem có fact nào có trong tập luật ban đầu không
                        break 
            if ls==0: #Nếu không có luật nào trả lời đùng theo fact thì dừng
                return False
            else:
                return True