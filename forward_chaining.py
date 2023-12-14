class ForwardChaining:
    def __init__(self) -> None:
        self.log = ''

    def forward_chaining(self, facts, fc_rules):
        self.log_rules_facts(facts, fc_rules)
        self.log += '\nII. INFERENCE\n'
        road = []
        i, pos = 1, len(facts)
        while i:
            self.log += f'-----------ITERATION {i}------------\n'
            rule_applied = False
            for rule in fc_rules:
                self.log += str(rule)
                if rule.is_fired: # nếu luạt đã được chứng minh rồi
                    self.log += ' bỏ qua vì cờ is_fired đã được đánh dấu.\n'
                    continue

                if rule.consequent in facts:# nếu vế phải đã nằm trong facts
                    self.log += ' bỏ qua vì vế phải đã tồn tại trong facts.\n'
                    continue

                missing = rule.follows(facts) # tìm xem là có fact nào thiếu để kết luận luật đúng hay không 

                if missing is None:
                    rule_applied = True
                    rule.is_fired = True
                    facts.append(rule.consequent)
                    road.append(rule.id)
                    self.log += f' áp dụng, cập nhật is_fired. Facts {", ".join(facts[:pos])} => {", ".join(facts[pos:])}\n'
                    break
                else: # do vế trái thiếu mất fact
                    self.log += " không được áp dụng, vì thiếu fact: %s\n" % missing
            i += 1

            if not rule_applied:
                self.log_result(facts, road)
                return False, road, facts # ban đầu là []
        self.log_result(facts, road)
        return True, road ,facts
    
    def log_rules_facts(self, facts, fc_rules):
        self.log += 'I. RULE\n'
        for rule in fc_rules:
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
