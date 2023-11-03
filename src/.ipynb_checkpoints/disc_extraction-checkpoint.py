import pandas as pd

smi = pd.read_csv("rawdata/smiles.csv")
txt = pd.read_csv("rawdata/txtdata4.csv")

data = pd.merge(smi,txt)

print(data)

disc_phase = {"D","Dh","Dhd","Dho","Dr","Dt"}

for i in range(len(txt["phases"])):
    if "D" in str(data["phases"][i]):
        print(i,data["phases"][i])