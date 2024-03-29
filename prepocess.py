import csv

import pandas as pd
from pandas import ExcelFile, ExcelWriter
from sklearn.metrics import classification_report, confusion_matrix



def standardize_xlsx(name):
    data = pd.read_excel('{}.xlsx'.format(name))

    #creating dictionaries for each non numerical attribute with their labels
    job_array = data.job.unique()
    job_array.sort()
    job_dict = {job_array[i]:i for i in range(len(job_array))}
    marital_array = data.marital.unique()
    marital_array.sort()
    marital_dict = {marital_array[i]:i for i in range(len(marital_array))}
    edu_array = data.education.unique()
    edu_array.sort()
    edu_dict = {edu_array[i]:i for i in range(len(edu_array))}
    connect_dict = {'no':0, 'yes':1}
    landline_dict= {'no':0, 'yes':1}
    smart_dict= {'no':0, 'yes':1}
    mon_array = data.last_month.unique()
    mon_array.sort()
    mon_dict= {mon_array[i]:i for i in range(len(mon_array))}
    pout_array = data.poutcome.unique()
    pout_array.sort()
    pout_dict = {pout_array[i]:i for i in range(len(pout_array))}

    #creating duration dictionary after scanning the heatmap
    duration_array = data.duration
    duration_dict = {duration_array[i]:duration_array[i]*2 for i in range(len(duration_array))}

    # campaign_array = data.campaign
    # campaign_dict = {campaign_array[i]:campaign_array[i]*1.3 for i in range(len(campaign_array))}

    #mapping each processed attribute in the dataset
    data.job=[job_dict[item] for item in data.job]
    data.marital=[marital_dict[item] for item in data.marital]
    data.education=[edu_dict[item] for item in data.education]
    data.connect=[connect_dict[item] for item in data.connect]
    data.landline=[landline_dict[item] for item in data.landline]
    data.smart=[smart_dict[item] for item in data.smart]
    data.last_month=[mon_dict[item] for item in data.last_month]
    data.poutcome=[pout_dict[item] for item in data.poutcome]
    data.duration=[duration_dict[item] for item in data.duration]
    
    # data.campaign=[campaign_dict[item] for item in data.campaign]
    return data

# standardize_xlsx(name)

