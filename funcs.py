import pandas as pd
import numpy as np


def InfoColumns(df):
    d = {"Column Name": [], "Type": [], "Null Values": []}
    for c in df.columns:
        col = pd.isnull(df[c])
        d["Column Name"].append(c)
        d["Type"].append(df[c].dtype)
        d["Null Values"].append(np.shape(df[col])[0])
    dd = pd.DataFrame(d)
    return dd
