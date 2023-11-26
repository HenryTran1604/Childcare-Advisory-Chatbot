from rule import Rule
from dao import DAO
class ForwardChaining:
    def __init__(self) -> None:
        dao = DAO()
        self.fc_rules = dao.find_all_forward_rules()
        self.log = ''

    def forward_chaining(self, facts):
        self.log_rules_facts(facts)
        self.log += '\nII. INFERENCE\n'
        road = []
        i, pos = 1, len(facts)
        while i:
            self.log += f'-----------ITERATION {i}------------\n'
            rule_applied = False
            for rule in self.fc_rules:
                self.log += str(rule)
                if rule.flag1: # nếu luạt đã được cm rồi
                    self.log += ' bỏ qua vì cờ flag1 đã được đánh dấu.\n'
                    continue

                if rule.flag2: 
                    self.log += ' bỏ qua vì cờ flag2 đã được đánh dấu.\n'
                    continue

                if rule.consequent in facts:# nếu vế phải đã được cm rồi
                    self.log += ' bỏ qua vì vế phải đã tồn tại trong facts, cập nhật flag2.\n'
                    rule.flag2 = True
                    continue

                missing = rule.follows(facts) # tìm xem là có fact nào thiếu để kết luận luật đúng hay không 

                if missing is None:
                    rule_applied = True
                    rule.flag1 = True
                    facts.append(rule.consequent)
                    road.append("RU" + str(self.fc_rules.index(rule) + 1))
                    self.log += f' áp dụng, cập nhật flag1. Facts {", ".join(facts[:pos])} => {", ".join(facts[pos:])}\n'
                    break
                else: # do vế trái thiếu mất fact
                    self.log += " không được áp dụng, vì thiếu fact: %s\n" % missing
            i += 1

            if not rule_applied:
                self.log_result(facts, road)
                return False, road, facts # ban đầu là []
        self.log_result(facts, road)
        return True, road ,facts
    
    def log_rules_facts(self, facts):
        self.log += 'I. RULE\n'
        for rule in self.fc_rules:
            self.log += f'\t{rule}\n'
        self.log += 'FACT:\n\t'
        for fact in facts:
            self.log += fact + ", "
    def log_result(self, facts, road):
        self.log += '----------------------------------------------------\n'
        self.log += f'Facts sau khi suy diễn: {", ".join(facts)}\n'
        self.log += f'Những luật được áp dụng: {", ".join(road)}\n'

    def write(self, file_name):
        with open(f'log\{file_name}.txt', encoding='utf8', mode='w') as f:
            f.writelines(self.log)