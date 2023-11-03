import pandas as pd

smi = pd.read_csv("rawdata/smiles.csv", index_col=0)
txt = pd.read_csv("rawdata/txtdata4.csv", index_col=0)

data = pd.merge(smi,txt)
# print(data.columns)

disc_phase = {"D","Dh","Dhd","Dho","Dr","Dt"}

disc_data = data.query('phases.astype("str").str.contains("D")')
print(disc_data)
disc_data.to_csv("data/disc_data.csv")


# for i in range(len(txt["phases"])):
#     if "D" in str(data["phases"][i]):
#         print(i,data["phases"][i])