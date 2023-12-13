import pandas as pd
df = pd.read_csv('data.csv', encoding='utf8')
df_boy = df[:25]
df_girl = df[25:]
def classify(gender, age, height, weight):
    if gender == 1:
        cmp = df_boy.iloc[age].values
    else:
        cmp = df_girl.iloc[age].values
    w_m2SD, h_m2SD, w_2SD = cmp[[1, 4, 6]]
    if height < h_m2SD and weight < w_m2SD:
        return 'ST3'
    elif height < h_m2SD:
        return 'ST2'
    elif weight < w_m2SD:
        return 'ST1'
    if weight > w_2SD:
        return 'ST4'
    return 'ST5'
print(classify(1, 6, 6.3, 71.9))
    