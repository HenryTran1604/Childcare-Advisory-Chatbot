class Rule:
    def __init__(self, id, antecedent, consequent) -> None:
        self.id = id
        self.antecedent = antecedent
        self.consequent = consequent
        self.is_fired = False

    def follows(self, facts):
        for fact in self.antecedent:
            if fact not in facts:
                return fact
        return None
    def __str__(self):
        return self.id + ': ' + ', '.join(self.antecedent) + ' -> ' + self.consequent