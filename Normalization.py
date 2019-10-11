import pandas as pd
import numpy as np
import pandas as pd
import seaborn as sns

from prepocess import standardize_xlsx


def normalize_dataframe(name):
    df = standardize_xlsx(name)
    x= df.iloc[:,0:15]
    y= df.iloc[:,15]
    #use normalizing logic
    x = (x - x.mean()) / (x.max() - x.min())
    return x,y,df


# a,b,c = normalize_dataframe("Train Data")

