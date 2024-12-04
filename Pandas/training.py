import pandas as pd

df = pd.read_csv('Данные_собес - Data.csv')
print(df)

#sex 1 girl 2 boy
#bin read_izd

print(df["sex"].unique())
print(df["sex"].dtypes)

df["sex"] = (df["sex"].replace('.', '2'))
print(df["sex"].unique())

print('new')

#df2 = (df["age"].replace('.', ))
#

#if type(df["age"]) == int:
    #a = df["age"].mean()
        #(df["age"].replace('.', a ))

df['age'] = df['age'].replace('.', df[df['age'] != '.'].age.astype(int).mean()).astype(int)
print(df["age"].unique())
#mean1 = (df["age"].mean())
#print(mean1)
#df["age"] = (df["sex"].replace('.', '2'))

#MIN_AGE = 12
#if df["age"].unique() > MIN_AGE

print(df["age"].min())
print(df["age"].max())


# time voted
print("all okay!: ")
print(df.drop_duplicates(subset=["resp_id"]))


