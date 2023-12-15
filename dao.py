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

    def find_all_rules(self, type):
        stm = f'SELECT rule.id_rule, id_antecedent_fact, id_consequent_fact FROM rule, inference WHERE rule.type = %s AND rule.id_rule = inference.id_rule'
        self.cursor.execute(stm, (type, ))
        result = self.cursor.fetchall()
        d = {}
        for x in result:
            key = (x[0], x[2])
            if key not in d:
                d[key] = [x[1]]
            else:
                d[key].append(x[1])

        rules = [Rule(x[0], d[x], x[1]) for x in d]
        return rules

    def find_all_forward_rules(self):
        return self.find_all_rules(0)

    def find_all_backward_rules(self):
        return self.find_all_rules(1)
    
    
    def find_all_symtoms_by_problem(self, problem_id):
        stm = 'SELECT DISTINCT id_antecedent_fact FROM inference WHERE id_consequent_fact=%s'
        self.cursor.execute(stm, (problem_id,))
        result = self.cursor.fetchall()
        return set(x[0] for x in result)
    
    def find_all_std_weight_height(self):
        stm = 'SELECT * FROM std_weight_height'
        self.cursor.execute(stm)
        result = self.cursor.fetchall()
        std_weight_heights = [[x for x in r] for r in result]
        return std_weight_heights
    
    def find_std_weight_height_by_age_and_gender(self, gender, age):
        stm = 'SELECT * FROM std_weight_height WHERE gender = %s AND age=%s'
        self.cursor.execute(stm, (gender, age))
        result = self.cursor.fetchone()
        return list(result)
    