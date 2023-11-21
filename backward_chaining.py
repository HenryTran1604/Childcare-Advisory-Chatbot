from rule import Rule
from dao import DAO
class BackwardChaining:
    def __init__(self):
        dao = DAO()
        self.bc_rules = dao.find_all_backward_rules()
#        print(*self.bc_rules, sep='\n')

    def backward_chaining(self, facts, goal):# trả về giá trị true false caajp0 nhật cho result
            is_satisfy = False # Biến điều kiện, nếu ls==0 thì không có luật nào phù hợp với goal và fact thì trả về false
            for rule in self.bc_rules:
                out_facts = False #Biến điều kiện để dừng vòng lặp khi có triệu chứng không thuộc fact ban đầu
                
                if rule.consequent == goal:
                    for i in range(len(rule.antecedent)):
                        fact_guess = rule.antecedent[i]
                        if fact_guess not in facts:
                            out_facts = True
                            break

                            # dk=1
                    self.road="R" + str(self.bc_rules.index(rule) + 1)
                    
                    if not out_facts: #Kiểm tra nếu đúng hết các triệu chứng thì dừng vòng lặp
                        is_satisfy = True #Kiểm tra xem có fact nào có trong tập luật ban đầu không
                        break 
            return is_satisfy
#BackwardChaining()