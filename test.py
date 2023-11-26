import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# mờ hóa
BMI = ctrl.Antecedent(np.arange(0, 40, 1), 'BMI')
BFP = ctrl.Antecedent(np.arange(0, 30, 1), 'BFP')
PHARSE = ctrl.Antecedent(np.arange(0, 8, 1), 'PHARSE')
CARBOHYDRATE = ctrl.Consequent(np.arange(0, 60, 1), 'CARBOHYDRATE')
PROTEIN = ctrl.Consequent(np.arange(0, 50, 1), 'PROTEIN')

BMI['Gầy'] = fuzz.trapmf(BMI.universe, [0, 0, 16, 18.5])
BMI['Bình thường'] = fuzz.trapmf(BMI.universe, [16, 18.5, 25, 30])
BMI['Béo'] = fuzz.trapmf(BMI.universe, [25, 30, 40, 40])

BFP['Thấp'] = fuzz.trapmf(BFP.universe, [0, 0, 4, 8])
BFP['Bình thường'] = fuzz.trapmf(BFP.universe, [4, 8, 15, 20])
BFP['Cao'] = fuzz.trapmf(BFP.universe, [15, 20, 30, 30])

PHARSE['Pharse 0'] = fuzz.trapmf(PHARSE.universe, [0, 0, 0, 2])
PHARSE['Pharse 1'] = fuzz.trapmf(PHARSE.universe, [0, 2, 4, 6])
PHARSE['Pharse 2'] = fuzz.trapmf(PHARSE.universe, [4, 6, 8, 8])

CARBOHYDRATE['Thấp'] = fuzz.trapmf(CARBOHYDRATE.universe, [0, 0, 20, 30])
CARBOHYDRATE['Bình thường'] = fuzz.trapmf(CARBOHYDRATE.universe, [20, 30, 40, 50])
CARBOHYDRATE['Cao'] = fuzz.trapmf(CARBOHYDRATE.universe, [40, 50, 60, 60])

PROTEIN['Thấp'] = fuzz.trapmf(PROTEIN.universe, [0, 0, 15, 20])
PROTEIN['Bình thường'] = fuzz.trapmf(PROTEIN.universe, [15, 20, 30, 40])
PROTEIN['Cao'] = fuzz.trapmf(PROTEIN.universe, [30, 40, 50, 50])

BMI.view()
# BFP.view()
# PHARSE.view()
# CARBOHYDRATE.view()
# PROTEIN.view()

# add rule
rule1 = ctrl.Rule(BMI['Gầy'] & BFP['Thấp'] & PHARSE['Pharse 0'], CARBOHYDRATE['Cao'])
rule1a = ctrl.Rule(BMI['Gầy'] & BFP['Thấp'] & PHARSE['Pharse 0'], PROTEIN['Bình thường'])

rule2 = ctrl.Rule(BMI['Gầy'] & BFP['Bình thường'] & PHARSE['Pharse 0'], CARBOHYDRATE['Cao'])
rule2a = ctrl.Rule(BMI['Gầy'] & BFP['Bình thường'] & PHARSE['Pharse 0'], PROTEIN['Bình thường'])

rule3 = ctrl.Rule(BMI['Bình thường'] & BFP['Thấp'] & PHARSE['Pharse 0'], CARBOHYDRATE['Bình thường'])
rule3a = ctrl.Rule(BMI['Bình thường'] & BFP['Thấp'] & PHARSE['Pharse 0'], PROTEIN['Cao'])

rule4 = ctrl.Rule(BMI['Bình thường'] & BFP['Bình thường'] & PHARSE['Pharse 0'], CARBOHYDRATE['Bình thường'])
rule4a = ctrl.Rule(BMI['Bình thường'] & BFP['Bình thường'] & PHARSE['Pharse 0'], PROTEIN['Bình thường'])

rule5 = ctrl.Rule(BMI['Bình thường'] & BFP['Cao'] & PHARSE['Pharse 0'], CARBOHYDRATE['Thấp'])
rule5a = ctrl.Rule(BMI['Bình thường'] & BFP['Cao'] & PHARSE['Pharse 0'], PROTEIN['Bình thường'])

rule6 = ctrl.Rule(BMI['Béo'] & BFP['Bình thường'] & PHARSE['Pharse 0'], CARBOHYDRATE['Thấp'])
rule6a = ctrl.Rule(BMI['Béo'] & BFP['Bình thường'] & PHARSE['Pharse 0'], PROTEIN['Cao'])

rule7 = ctrl.Rule(BMI['Béo'] & BFP['Cao'] & PHARSE['Pharse 0'], CARBOHYDRATE['Thấp'])
rule7a = ctrl.Rule(BMI['Béo'] & BFP['Cao'] & PHARSE['Pharse 0'], PROTEIN['Cao'])

rule8 = ctrl.Rule(BMI['Gầy'] & BFP['Thấp'] & PHARSE['Pharse 1'], CARBOHYDRATE['Cao'])
rule8a = ctrl.Rule(BMI['Gầy'] & BFP['Thấp'] & PHARSE['Pharse 1'], PROTEIN['Bình thường'])

rule9 = ctrl.Rule(BMI['Gầy'] & BFP['Bình thường'] & PHARSE['Pharse 1'], CARBOHYDRATE['Cao'])
rule9a = ctrl.Rule(BMI['Gầy'] & BFP['Bình thường'] & PHARSE['Pharse 1'], PROTEIN['Bình thường'])

rule10 = ctrl.Rule(BMI['Bình thường'] & BFP['Thấp'] & PHARSE['Pharse 1'], CARBOHYDRATE['Bình thường'])
rule10a = ctrl.Rule(BMI['Bình thường'] & BFP['Thấp'] & PHARSE['Pharse 1'], PROTEIN['Bình thường'])

rule11 = ctrl.Rule(BMI['Bình thường'] & BFP['Bình thường'] & PHARSE['Pharse 1'], CARBOHYDRATE['Bình thường'])
rule11a = ctrl.Rule(BMI['Bình thường'] & BFP['Bình thường'] & PHARSE['Pharse 1'], PROTEIN['Bình thường'])

rule12 = ctrl.Rule(BMI['Bình thường'] & BFP['Cao'] & PHARSE['Pharse 1'], CARBOHYDRATE['Bình thường'])
rule12a = ctrl.Rule(BMI['Bình thường'] & BFP['Cao'] & PHARSE['Pharse 1'], PROTEIN['Cao'])

rule13 = ctrl.Rule(BMI['Béo'] & BFP['Bình thường'] & PHARSE['Pharse 1'], CARBOHYDRATE['Bình thường'])
rule13a = ctrl.Rule(BMI['Béo'] & BFP['Bình thường'] & PHARSE['Pharse 1'], PROTEIN['Cao'])

rule14 = ctrl.Rule(BMI['Béo'] & BFP['Cao'] & PHARSE['Pharse 1'], CARBOHYDRATE['Thấp'])
rule14a = ctrl.Rule(BMI['Béo'] & BFP['Cao'] & PHARSE['Pharse 1'], PROTEIN['Cao'])

rule15 = ctrl.Rule(BMI['Gầy'] & BFP['Thấp'] & PHARSE['Pharse 2'], CARBOHYDRATE['Cao'])
rule15a = ctrl.Rule(BMI['Gầy'] & BFP['Thấp'] & PHARSE['Pharse 2'], PROTEIN['Bình thường'])

rule16 = ctrl.Rule(BMI['Gầy'] & BFP['Bình thường'] & PHARSE['Pharse 2'], CARBOHYDRATE['Cao'])
rule16a = ctrl.Rule(BMI['Gầy'] & BFP['Bình thường'] & PHARSE['Pharse 2'], PROTEIN['Bình thường'])

rule17 = ctrl.Rule(BMI['Bình thường'] & BFP['Thấp'] & PHARSE['Pharse 2'], CARBOHYDRATE['Bình thường'])
rule17a = ctrl.Rule(BMI['Bình thường'] & BFP['Thấp'] & PHARSE['Pharse 2'], PROTEIN['Bình thường'])

rule18 = ctrl.Rule(BMI['Bình thường'] & BFP['Bình thường'] & PHARSE['Pharse 2'], CARBOHYDRATE['Bình thường'])
rule18a = ctrl.Rule(BMI['Bình thường'] & BFP['Bình thường'] & PHARSE['Pharse 2'], PROTEIN['Bình thường'])

rule19 = ctrl.Rule(BMI['Bình thường'] & BFP['Cao'] & PHARSE['Pharse 2'], CARBOHYDRATE['Bình thường'])
rule19a = ctrl.Rule(BMI['Bình thường'] & BFP['Cao'] & PHARSE['Pharse 2'], PROTEIN['Cao'])

rule20 = ctrl.Rule(BMI['Béo'] & BFP['Bình thường'] & PHARSE['Pharse 2'], CARBOHYDRATE['Bình thường'])
rule20a = ctrl.Rule(BMI['Béo'] & BFP['Bình thường'] & PHARSE['Pharse 2'], PROTEIN['Cao'])

rule21 = ctrl.Rule(BMI['Béo'] & BFP['Cao'] & PHARSE['Pharse 2'], CARBOHYDRATE['Thấp'])
rule21a = ctrl.Rule(BMI['Béo'] & BFP['Cao'] & PHARSE['Pharse 2'], PROTEIN['Cao'])


# rule1.view()
# rule2.view()

carbohydrate_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10,
                                        rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19, rule20,
                                        rule21])

protein_ctrl = ctrl.ControlSystem([rule1a, rule2a, rule3a, rule4a, rule5a, rule6a, rule7a, rule8a, rule9a, rule10a,
                                   rule11a, rule12a, rule13a, rule14a, rule15a, rule16a, rule17a, rule18a, rule19a,
                                   rule20a, rule21a])

final_result = ctrl.ControlSystemSimulation(carbohydrate_ctrl)
final_result2 = ctrl.ControlSystemSimulation(protein_ctrl)

final_result.input['BMI'] = 22.5
final_result.input['BFP'] = 15.6
final_result.input['PHARSE'] = 3

final_result2.input['BMI'] = 22.5
final_result2.input['BFP'] = 15.6
final_result2.input['PHARSE'] = 3

final_result.compute()
final_result2.compute()

print(final_result2.output['PROTEIN'])
print(final_result.output['CARBOHYDRATE'])
CARBOHYDRATE.view(sim=final_result)
PROTEIN.view(sim=final_result2)

plt.show()