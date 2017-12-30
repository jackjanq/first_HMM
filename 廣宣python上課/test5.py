import pandas as pd
import pandas_datareader.data as web
import datetime
start=datetime.datetime(2017,12,1)
end==datetime.datetime(2017,12,10)
df=web.DataReader('2330.tw','yahoo',star,end)
# write to excel file
write=pd.ExcelWriter('./file/2330.xlsx')
df.to_excel(write,'2330')
workbook=writer.book
worksheet=write.sheets['2330']