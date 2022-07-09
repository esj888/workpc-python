#    one  two
# a  1.0    1
# b  2.0    2
# c  3.0    3
# d  NaN    4

import pandas as pd

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']), 
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)

print(df)
print(df.loc['b'])
