import mysql.connector
from rule import Rule
class DAO:
    def __init__(self) -> None:
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="kbs"
        )
        self.cursor = self.db.cursor()
        
    def find_all_facts(self):
        stm = "SELECT * FROM fact"
        self.cursor.execute(stm)
        facts = self.cursor.fetchall()
        d_facts = dict()
        for fact in facts:
            d_facts[fact[0]] = fact[1]
        return d_facts
    
    def find_all_by_id_containing(self, key):
        stm = f"SELECT * FROM fact WHERE id_fact LIKE '{key}%'"
        self.cursor.execute(stm)
        facts = self.cursor.fetchall()
        return facts
    
    def find_all_forward_rules(self):
        stm = f'SELECT rule.id_rule, id_antecedent_fact, id_consequent_fact FROM rule, inference WHERE rule.type = 0 AND rule.id_rule = inference.id_rule'
        self.cursor.execute(stm)
        result = self.cursor.fetchall()
        forward_rules = [Rule(x[0], [x[1]], x[2]) for x in result]
        return forward_rules
    
    def find_all_backward_rules(self):
        stm = f'SELECT rule.id_rule, id_antecedent_fact, id_consequent_fact FROM rule, inference WHERE rule.type = 1 AND rule.id_rule = inference.id_rule'
        self.cursor.execute(stm)
        result = self.cursor.fetchall()
        d = {}
        for x in result:
            key = (x[0], x[2])
            if key not in d:
                d[key] = [x[1]]
            else:
                d[key].append(x[1])

        backward_rules = [Rule(x[0], d[x], x[1]) for x in d]
        return backward_rules
