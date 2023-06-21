import pandas as pd
schmet=pd.read_excel(r"C:\Users\HP\Documents\Trainee\Salam_assignments\salam_assignments\assign_13\schoolmets_names.xlsx")
#print(schmet)
import pandas as pd
collmet=pd.read_excel(r"C:\Users\HP\Documents\Trainee\Salam_assignments\salam_assignments\assign_13\collegemets_names.xls.xlsx")
#print(collmet)
print(schmet.groupby("Quality")["FriendName"].count())
print(collmet.groupby("Quality")["FriendName"].count())

import pandas as pd
boy1=pd.read_excel(r"C:\Users\HP\Documents\Trainee\Salam_assignments\salam_assignments\assign_11\boysname.xls")
print(boy1.groupby("Quality")["boysFriendName"].count())
import pandas as pd
girl2=pd.read_excel(r"C:\Users\HP\Documents\Trainee\Salam_assignments\salam_assignments\assign_11\girlsname.xls")
print(girl2.groupby("Quality")["GirlsFriendName"].count())

import pandas as pd
fatherside=pd.read_excel(r"C:\Users\HP\Documents\Trainee\Salam_assignments\salam_assignments\assign_11\fatherfamily_members.xls")
print(fatherside.groupby("Relation")["FamilyMemberName"].count())
import pandas as pd
motherside=pd.read_excel(r"C:\Users\HP\Documents\Trainee\Salam_assignments\salam_assignments\assign_11\montherfamily_members.xls")
print(motherside.groupby("Relation")["FamilyMemberName"].count())


import pandas as pd
dal=pd.read_excel(r"C:\Users\HP\Documents\Trainee\Salam_assignments\salam_assignments\assign_11\dal_items.xlsx")
print(dal.groupby("Taste")["VegFoodName"].count())
import pandas as pd
vegitable=pd.read_excel(r"C:\Users\HP\Documents\Trainee\Salam_assignments\salam_assignments\assign_11\vegitable_items.xlsx")
print(vegitable.groupby("Taste")["VegFoodName"].count())

import pandas as pd
soup=pd.read_excel(r"C:\Users\HP\Documents\Trainee\Salam_assignments\salam_assignments\assign_11\soups_items.xlsx")
print(soup.groupby("Taste")["soups"].count())
fry=pd.read_excel(r"C:\Users\HP\Documents\Trainee\Salam_assignments\salam_assignments\assign_11\fry_items.xlsx")
print(fry.groupby("Taste")["fry"].count())

import pandas as pd
chicken=pd.read_excel(r"C:\Users\HP\Documents\Trainee\Salam_assignments\salam_assignments\assign_11\chicken_items.xlsx")
print(chicken.groupby("Taste")["NonVegFoodName"].count())
mutton=pd.read_excel(r"C:\Users\HP\Documents\Trainee\Salam_assignments\salam_assignments\assign_11\mutton_items.xlsx")
print(mutton.groupby("Taste")["NonVegFoodName"].count())

import pandas as pd
winter=pd.read_excel(r"C:\Users\HP\Documents\Trainee\Salam_assignments\salam_assignments\assign_11\winterseason_names.xlsx")
print(winter.groupby("Season")["MonthName"].count())
summer=pd.read_excel(r"C:\Users\HP\Documents\Trainee\Salam_assignments\salam_assignments\assign_11\summerseason_names.xlsx")
print(summer.groupby("Season")["MonthName"].sum())
rainy=pd.read_excel(r"C:\Users\HP\Documents\Trainee\Salam_assignments\salam_assignments\assign_11\rainyseason_names.xlsx")
print(rainy.groupby("Season")["MonthName"].sum())


import pandas as pd
red=pd.read_excel(r"C:\Users\HP\Documents\Trainee\Salam_assignments\salam_assignments\assign_11\redflowers_names.xlsx")
print(red.groupby("colour")["FlowerName"].count())
white=pd.read_excel(r"C:\Users\HP\Documents\Trainee\Salam_assignments\salam_assignments\assign_11\whiteflowers_names.xlsx")
print(white.groupby("colour")["FlowerName"].count())
pink=pd.read_excel(r"C:\Users\HP\Documents\Trainee\Salam_assignments\salam_assignments\assign_11\pinkflower_names.xlsx")
print(pink.groupby("colour")["FlowerName"].count())
yellow=pd.read_excel(r"C:\Users\HP\Documents\Trainee\Salam_assignments\salam_assignments\assign_11\yellowflower_names.xlsx")
print(yellow.groupby("colour")["FlowerName"].count())



