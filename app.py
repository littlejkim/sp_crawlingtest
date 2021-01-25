import clearbit
import pandas as pd

clearbit.key = ''

# read excel file containing subscriptions and save to dataframe (exclude null entries)
sub_list = pd.read_excel('./test.xlsx', engine='openpyxl')
f_sub_list = sub_list[sub_list['Name'].notna()]
final_sub_list = f_sub_list['Name'].values.tolist()


success = 0
# iterate over sub list to find company data
for subscription in final_sub_list:
    try:
        domain = clearbit.NameToDomain.find(name=subscription)
        company_data = clearbit.Enrichment.find(domain=domain['domain'])
        success += 1
    except:
        print("error")


print("Succeeded " + str(success) + " out of " + str(len(final_sub_list)))
        
