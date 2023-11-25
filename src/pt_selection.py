import pandas as pd

old_data = pd.read_csv("data/disc_data.csv", index_col=0)

# print(old_data)

unused_data = ""
used_data = ""
uncategolized_data = ""

for idx, data in old_data.iterrows():
    unuse = False
    # exclude (the data without smiles) and (polymers)
    if "*" in str(data["smiles"]) or "" == str(data["smiles"]):
        unuse = True

    if unuse:
        if unused_data is "":
            unused_data = data.to_frame().T
        else:
            unused_data = pd.concat([unused_data,data.to_frame().T])
        continue
    
    # extract the data with "Cr NUM D NUM is"
    phase_detail = data["phases"].split()
    cr_end = -1
    d_begin = -1
    d_end = -1
    is_begin = -1
    temp_cr_d = -9999
    temp_d_is = -9999
    phase_state = 0
    phase_updated = ""
    if len(phase_detail)%2 == 0:
        unuse = True
    else:
        for i in range(len(phase_detail)//2+1):
            if phase_state == 0:
                if "Cr" in phase_detail[i*2]:
                    continue
                elif "D" in phase_detail[i*2]:
                    phase_state = 1
                    try:
                        float(phase_detail[i*2-1])
                    except ValueError:
                        unuse = True
                        break
                    else:
                        phase_updated += "Cr "+phase_detail[i*2-1]+" D"
                else:
                    unuse = True
                    break
            elif phase_state == 1:
                if "D" in phase_detail[i*2]:
                    continue
                elif "is" in phase_detail[i*2]:
                    phase_state = 2
                    try:
                        float(phase_detail[i*2-1])
                    except ValueError:
                        unuse = True
                        break                        
                    else:
                        phase_updated += " "+phase_detail[i*2-1]+" is"
                else:
                    unuse = True
                    break
            elif phase_state == 2:
                unuse = True
                break                                

    if unuse:
        if uncategolized_data is "":
            uncategolized_data = data.to_frame().T
        else:
            uncategolized_data = pd.concat([uncategolized_data,data.to_frame().T])
        continue        
    else:
        data["phases"] = phase_updated
        if used_data is "":
            used_data = data.to_frame().T
        else:
            used_data = pd.concat([used_data,data.to_frame().T])     

print(uncategolized_data)
print(used_data)
used_data.to_csv("data/used_data.csv")