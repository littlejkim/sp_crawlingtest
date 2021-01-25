import pandas as pd

filepath = "./test.xlsx"

def company_list():
    sub_list = pd.read_excel(filepath, engine='openpyxl')
    f_sub_list = sub_list[sub_list['Name'].notna()]
    final_sub_list = f_sub_list['Name'].values.tolist()
    return final_sub_list