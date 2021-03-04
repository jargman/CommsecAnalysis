


import pandas as pd
import numpy as np

#JARG CODE: IMPORT COMMSEX TRANSACTIONS FILE
jarg_trans = pd.read_csv('E:\PythonVirtEnv\ShareTradingEnv\Transactions_2274187_03012021_03022021.csv')
jarg_trans

def TransactionType(x):
    if (x[:1] == "S") :
        return 'SELL'
    elif (x[:1] == "B") :
        return 'BUY'
    elif (x[:6] == "Direct") :
        return "Transfer"
    elif (x[:3] == "Rej") :
        return "Rejected Transfer"
    else:
        return 'ERROR'


#make copy of import
jarg_trans_new=jarg_trans.copy()

#apply the above function to create new column
jarg_trans_new['SellBuy'] = jarg_trans_new['Details'].apply(TransactionType)

#view the top records
jarg_trans_new.head()

#------------------------------------------------------------

#this doesn't work
#jarg_trans_new['DollarAmt'] = np.where(jarg_trans_new.SellBuy == "SELL"),1,0

#try again
# def extractD():
#     if SellBuy == "BUY" or SellBuy == "SELL":
#         return jarg_trans_new['DollarAmt'] = jarg_trans_new['Details'].str.slice(1,10)
# extractD()
# pd.DataFrame(df.row.str.split(' ',2)

#closest working attempt: substr on 2nd-10th letter
jarg_trans_new['NmbrShrs'] = jarg_trans_new['Details'].str.slice(1,10)
#then keep only numbers
jarg_trans_new.NmbrShrs = jarg_trans_new.NmbrShrs.str.extract('(\d+)')

jarg_imp=jarg_trans_new.copy()
#jarg_imp.SellBuy == "SELL", 'DollarAmt' = jarg_trans_new.DollarAmt.str.extract('(\d+)')


#this works - if logic to create new single SELL/BUY variable
jarg_trans_new['SBCHK'] = np.where((jarg_trans_new['SellBuy']=="SELL") | (jarg_trans_new['SellBuy'] =="BUY"), 1, 0)

#this should work but doesn't :(
#jarg_trans_new['ASXCODE'] = np.where(jarg_trans_new['SBCHK'] >=1) ,jarg_trans_new['Details'].str.split(" ", expand=True)[2]

#this works to create variable to get ASX code - but no check for above logic
jarg_trans_new['ASXCODE'] = jarg_trans_new['Details'].str.split(" ", expand=True)[2]


#this doesn't work - trying to clean
#jarg_trans_new['ASXCODE'] = np.where(len(jarg_trans_new['ASXCODE'])>3) ,jarg_trans_new['ASXCODE'] = ''

def CleanASX(x):
    if len(x) == 3:
        return x
    elif len(x) >3:
        return ''
    elif len(x) <3:
        return ''

#apply the above function to create new column
jarg_trans_new['ASXCODE'] = jarg_trans_new['ASXCODE'].apply(CleanASX)



#get the rate paid/sold (following the @ sign)
jarg_trans_new['AtRate'] = jarg_trans_new['Details'].str.split(" ", expand=True)[4]

#cleaning up - keep only valid @ rates
def CleanAtRate(x):
    if len(x) >=8:
        return x
    else:
        return ''

#apply the above function to clean @ rates
jarg_trans_new['AtRate'] = jarg_trans_new['AtRate'].apply(CleanAtRate)

#create function to convert to INT or FLOAT
def num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)

jarg_trans_new['AtRate'] = jarg_trans_new['AtRate'].apply(num)

jarg_trans_new['DlrShrs'] = jarg_trans_new['AtRate'] * jarg_trans_new['NmbrShrs']

#neither of these work
jarg_trans_new['ASXCODE'] = np.where(jarg_trans_new['SBCHK']==1) ,jarg_trans_new.Details.str.split(' ', 1)








#jarg_trans_new['ASXCODE'] = np.where(jarg_trans_new['SBCHK']==1) ,jarg_trans_new.Details.split()[3]

#jarg_trans_new['ASXCODE'] = np.where(jarg_trans_new['SBCHK']==1) ,jarg_trans_new.Details.str.split(' ', 1)



#this works


firstlast['First_Name'] = firstlast['String'].str.split(" ", expand=True)[-1]

data.composers.str.split('\s+').str[-1]

jarg_trans_new['SBCHK'] = np.where(jarg_trans_new['SellBuy']=="BUY", 'yes', 'no')
# def ExtractDollar():
#     if SellBuy in ("SELL","BUY"):
#         jarg_trans_new[['First', 'Last']] = jarg_trans_new.Details.str.split(expand=True)
#
# ExtractDollar()
#
#         jarg_trans_new['DollarAmt'] = jarg_trans_new['Details'].astype(str).str.split().str[1]
# df.Name.str.split(expand=True))
# ExtractDollar()
# jarg_trans_new['DollarAmt'] = jarg_trans_new['Details'].apply(ExtractDollar)
#
# def DollarAmt(x):
#     if SellBuy in ("SELL","BUY"):
#         jarg_trans_new['DollarAmt'] = jarg_trans_new['Details'].astype(str).str.split().str[1]


# jarg_trans_new
#
# if jarg_trans[:1] == "S":
#     jarg_trans.Sell = 1
#
# jarg_trans_new.DollarAmt = int(jarg_trans_new.DollarAmt)
# else:
#     Body of else
# >>> x[:2]
# 'He'