class BackwardChaining:
    def __init__(self):
        self.log = ''
        self.iter = 0
#        self.bc_rules = dao.find_all_backward_rules()
#        print(*self.bc_rules, sep='\n')

    def backward_chaining(self, facts, goal, bc_rules):
        self.iter = 1
        self.log_rules_facts(facts, goal, bc_rules)
        self.log += '\nII. INFERENCE\n'
        is_satisfy = False 
        for rule in bc_rules: # quét tất cả luật lùi
            out_facts = False # cờ out_fact: nếu mà out_facts = true tức là tồn tại 1 fact mà không ở trong bộ nhớ hoạt động (current_facts)
            if rule.consequent == goal: # luật có vế phải thỏa mãn
                self.log_step(goal, '', f'Tìm thấy luật: {rule.id}. Các goals phải chứng minh mới: {rule.antecedent}')
                for i in range(len(rule.antecedent)):
                    fact_guess = rule.antecedent[i] # từng phần tử của vế trái
                    if fact_guess not in facts: # Nếu phần tử này không thuộc bộ nhớ hoạt động
                        self.log_step(fact_guess, '-', f'không có trong fact hiện tại. Luật {rule.id} không được chấp nhận. Dừng lại\n')
                        out_facts = True # đánh dấu out_facts = true 
                        break
                    else:
                        self.log_step(fact_guess, '-', f'ghi nhận {fact_guess} vì có trong fact hiện tại')

                self.road = rule.id
                
                if not out_facts:  # out_fact = false tức là tất cả phần tử vế trái đều nằm trong bộ nhớ hoạt động (current_facts)
                    is_satisfy = True # đánh dấu đã có luật thỏa mãn
                    self.log_step(goal, '==>', 'Luật đã được chứng minh.')
                    break 
        if not is_satisfy:
            self.log_step(goal, '', 'Không có luật nào thỏa mãn')
        self.log_result(is_satisfy, goal)
                
        return is_satisfy
    def log_step(self, goal, indent, msg):
        self.iter += 1
        self.log += f'{str(self.iter).rjust(3, " ")}) {indent}Goal {goal} {msg}\n'
    def log_rules_facts(self, facts, goal, bc_rules):
        self.log += 'I. RULE\n'
        for rule in bc_rules:
            self.log += f'\t{rule}\n'
        self.log += 'FACT:\n\t'
        self.log += ', '.join(facts)
        self.log += '\nGOAL: ' + goal + '\n'

    def log_result(self, result, goal):
        self.log += '------------------------------------------------------\n'
        if result:
            self.log += f'{goal} được chứng minh\n'
            self.log += f'Luật được áp dụng: {self.road}\n'
        else:
            self.log += f'{goal} không được chứng minh\n'
        self.log += '------------------------------------------------------\n'

    def write(self, file_name):
        with open(f'log\{file_name}.txt', encoding='utf8', mode='w') as f:
            f.writelines(self.log)
        self.log = ''
#BackwardChaining()