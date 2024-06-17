import pandas as pd
df = pd.read_csv('../Reviews.csv')


df_1 = df.iloc[:170536,:]


df_1.to_csv('reveiws1.csv', sep=',',index=False)