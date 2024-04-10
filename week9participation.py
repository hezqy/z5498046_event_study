import pandas
help(pandas.merge)
df1 = pandas.DataFrame({'key': ['A', 'B', 'C', 'D'],
                    'value1': [1, 2, 3, 4]})
df2 = pandas.DataFrame({'key': ['B', 'C', 'D', 'E'],
                    'value2': [5, 6, 7, 8]})
aa = pandas.merge(df1, df2, on='key')
bb = merged = pandas.merge(df1, df2, on='key', how='outer')
print(aa)
print(bb)