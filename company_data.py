import clearbit
import company_list

clearbit.key = 'sk_99f74980bd4ba096c78f4327c965e4ba'

# read excel file containing subscriptions and save to dataframe (exclude null entries)
sub_list = company_list.company_list()

# iterate over sub list to find company data
for subscription in sub_list:
    try:
        domain = clearbit.NameToDomain.find(name=subscription)
        company_data = clearbit.Enrichment.find(domain=domain['domain'])
    except:
        print("error")

