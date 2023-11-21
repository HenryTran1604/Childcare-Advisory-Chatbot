from rule import Rule
from dao import DAO
class ForwardChaining:
    def __init__(self) -> None:
        dao = DAO()
        self.fc_rules = dao.find_all_forward_rules()

    def forward_chaining(self, facts):
        road = []

        # while goal not in facts: # khi mục tiêu chưa nằm trong facts tìm thấy
        while 1:
            rule_applied = False
            for rule in self.fc_rules:

                if rule.flag1: # nếu luạt đã được cm rồi
                    continue

                if rule.flag2: 
                    continue

                if rule.consequent in facts:# nếu vế phải đã được cm rồi
                    rule.flag2 = True
                    continue

                missing = rule.follows(facts) # tìm xem là có fact nào thiếu để kết luận luật đúng hay không 

                if missing is None:
                    rule_applied = True
                    rule.flag1 = True
                    facts.append(rule.consequent)
                    road.append("RU" + str(self.fc_rules.index(rule) + 1))
                    break

            if not rule_applied:
                return False, road, facts # ban đầu là []

        return True, road ,facts