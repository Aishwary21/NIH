import pandas as pd
import os
def save(data):
    df = pd.DataFrame(data)
    pd.set_option('display.width', 1000)
    if os.stat("NIH_DATA.csv").st_size == 0:
        df.to_csv("NIH_DATA.csv",mode="a+",index=False,header=True)
    else:
        df.to_csv("NIH_DATA.csv",mode="a+",index=False,header=False)
    