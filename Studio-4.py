import pandas as pd
file_path = "C:/Users/rache/Documents/ENGR103/energy_use_terrawatthours.csv"

worldpower = pd.read_csv(file_path)
print(worldpower)

energy = ["Bioenergy", "Clean", "Coal", "Fossil", "Gas", "Hydro", "Nuclear",
          "Other Fossil", "Renewables", "Solar", "Wind"]

year = worldpower.loc[:, "year"]
source = worldpower.loc[:, "variable"]
energy_gen = worldpower.loc[:, "generation_twh"]

for x in range(len(year)):
    if year[x] == 2000:
        print("Energy from", source[x], "accounts for",
              energy_gen[x], "twh of world power in year 2000.")

for x in range(len(year)):
    if year[x] == 2020:
        print("Energy from", source[x], "accounts for",
              energy_gen[x], "twh of world power in year 2020.")

for x in range(len(source)):
    if source[x] == "Clean":
        print("Energy from", source[x], "accounts for",
              energy_gen[x], "twh of world power in year", year[x],".")

for x in range(len(source)):
    if source[x] == "Fossil":
        print("Energy from", source[x], "accounts for",
              energy_gen[x], "twh of world power in year", year[x],".")

for x in range(len(source)):
    if source[x] == "Clean":
        Clean_power = energy_gen[x]
    if source[x] == "Coal":
        Coal_power = energy_gen[x]
    if Clean_power > Coal_power:
        print("In year", year[x], "world Clean energy production was greater"
              "than world Coal energy production.")

