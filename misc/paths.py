#%%
import os 
import pandas as pd 
data_folder = os.path.abspath("../Data")

calories_path = os.path.join(data_folder, "calories.xlsx")


pd.read_excel(calories_path)


#%%