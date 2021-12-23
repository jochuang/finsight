import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import category_dict

# 1- Load CSV

# Load transactions csv downloaded from Mint as Pandas dataframe
df_org = pd.read_csv("transactions.csv",encoding='ISO-8859-1')

# 2- Clean Dataframe

# Drop columns that are not needed
df = df_org.drop(columns=['Original Description','Transaction Type','Account Name','Labels','Notes'])

# Drop data whose categories are "Hide from Budgets & Trends"
df = df[df['Category'] != 'Hide from Budgets & Trends']
# print(len(df['Category'].unique()))

# Convert 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Rename columns
df = df.rename(columns={'Date':'date', 'Description':'description', 'Amount':'amount', 'Category':'category'})
df_new = df.rename(columns={'category':'sub-category'})

# Add Main Category as a column of df_new
cat_list = []
for cat in df_new['sub-category'].tolist():
    cat_list.append(category_dict.category_dict[cat])        
df_new['category']=cat_list

# Re-arrange column sequence of dataframe
df_new = df_new[['date', 'category','sub-category','description','amount']]

# 3- Slicing Dataframe
df_income = df_new[df_new.category == 'Income'].copy()
df_expenses = df_new[df_new.category != 'Income'].copy()

# 4- Create Summary Dataframes through groupby and merge

# Create (2) new dataframes for monthly summary comparison of income vs expenses
grouped_income = df_income.groupby(df['date'].dt.strftime('%b-%Y'))['amount'].sum().sort_values()
grouped_income = df_income.groupby(pd.Grouper(key='date', freq='M'))['amount'].sum()
grouped_expenses = df_expenses.groupby(pd.Grouper(key='date', freq='M'))['amount'].sum()

# Merge grouped_income and grouped_expenses (new df = income_expenses)
income_expenses = pd.merge(grouped_income, grouped_expenses, on='date', suffixes = ['_income','_expenses'])
income_expenses['amount_expenses'] = income_expenses['amount_expenses']*(-1)
income_expenses['net_income'] = income_expenses['amount_income'] - abs(income_expenses['amount_expenses'])

# Convert income_expenses from wide format to long format
income_expenses = income_expenses.reset_index()
long_income_expenses = pd.melt(income_expenses, id_vars = ['date'], value_vars = ['amount_income', 'amount_expenses'], var_name = 'type',value_name = 'amount')
long_income_expenses['amount'] = abs(long_income_expenses['amount'])

# To convert datatype from date to string because Google Sheet does not recognize date type 
df_income['date']=df_income.loc[:,'date'].astype(str)
df_expenses['date']=df_expenses.loc[:,'date'].astype(str)
income_expenses['date']=income_expenses.loc[:,'date'].astype(str)
long_income_expenses['date']=long_income_expenses.loc[:,'date'].astype(str)

print("Data cleaning completed...")

# 5- Uploading Pandas to Google Sheets

# Initialize a connection
print("Connecting to Google Sheets...")

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('service_account.json',scope) # Update JSON file path
gc = gspread.authorize(credentials)

print("Connection established!")

# Interact with a sheet
sh = gc.open("income_transaction")
worksheet = sh.get_worksheet(0)
worksheet.update([df_income.columns.values.tolist()] + df_income.values.tolist())

sh = gc.open("expenses_transaction")
worksheet = sh.get_worksheet(0)
worksheet.update([df_expenses.columns.values.tolist()] + df_expenses.values.tolist())

sh = gc.open("ive_bar_graph")
worksheet = sh.get_worksheet(0)
worksheet.update([income_expenses.columns.values.tolist()] + income_expenses.values.tolist())

sh = gc.open("ive_pie_chart")
worksheet = sh.get_worksheet(0)
worksheet.update([long_income_expenses.columns.values.tolist()] + long_income_expenses.values.tolist())

print("Data successfully updated to Google Sheets :)")

## 6- (Option) Saving dataframes to csv in local project folder
df_income.to_csv('income_transaction.csv',index=False)
df_expenses.to_csv('expenses_transaction.csv', index=False)
income_expenses.to_csv('ive_bar_graph.csv',index=False)
long_income_expenses.to_csv('ive_pie_chart.csv', index=False)