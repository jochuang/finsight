# FinSight

FinSight is a finance dashboard that provides personal finance trends at a glance. It builds on top of personal finance application like Mint and allows customizable charts and graphs that tailor to your needs.
This application provides a data pipeline that takes in all transaction data in a csv format, cleans and transforms the data, and displays data in a dashboard. The goal is to track transactions, visualize spending trends, and ultimately make more informed financial decisions.

<img src=/images/finsight_screenshot3.png" alt="screenshot">
![screenshot](/images/finsight_screenshot3.png)

### Table of Contents
   * [Getting Started](#getting-started)
      * [Set Up](#set-up)
      * [Run](#run)
   * [Usage](#usage)
   * [Framework](#framework)
   * [Documentation](#documentation)
      
## Getting Started <a name="getting-started"></a>
  
## Set Up <a name="set-up"></a>
<details>
  <summary><b>1. Clone the repo</b></summary>
  <pre><code>
  git clone https://github.com/jochuang/finsight.git
  </code></pre>
</details>

<details>
  <summary><b>2. Download finance data</b></summary>
  Download "transactions.csv" from <a href="https://mint.intuit.com">Mint.com</a> and save it to your project folder. You can also use the sample data ("transactions.csv") provided in this repo.
  
  ![export transactions.csv](/images/export_transactions.PNG)
</details>

<details>
  <summary><b>3. Upload data sources to Google Sheets</b></summary>
  Go to <a href="https://docs.google.com/spreadsheets">Google Sheets</a> > Click the <b><i>file icon</i></b> on the top-right corner (next to the grid icon and AZ icon) > Click <b><i>Upload</i></b> and drag csv file to the upload section > Upload csv file one at a time
  
  Repeat this process (4) times for each csv file. 
   
   Your Google Sheet Home should look something like this:  
   ![gsheets](images/gsheets_files.PNG)
</details>

<details>
  <summary><b>4. Connect data sources to Google Data Studio</b></summary>
  Go to <a href=https://datastudio.google.com>Google Data Studio</a> > Click <b><i>Create</i></b> on the top-left corner > Click <b><i>Data source</i></b> (It may ask you to set up the account if you haven't previously) > Click <b><i>Google Sheets</i></b> > Select the Spreadsheet that you just uploaded > Click <b><i>Connect</i></b> on the top-right corner  
  
  Repeat this process (4) times for each spreadsheet.  
  
  >Note: please make sure the name of the data sources are exactly identical as shown here. If it isn't, you can rename it  
  
  Your Data Studio data sources should look something like this:  
  ![gstudio](images/gstudio_files.PNG)  
  
</details>
 
<details>
  <summary><b>5. Make a copy of Data Studio Dashboard</b></summary>
  Use the provided dashboard <a href="https://datastudio.google.com/s/ntVQl5vcVHc"> link </a> > Click on the three-vertical-dot icon on the top-right corner > Click <b><i>Make a Copy</i></b> > Under New Data Source, select the (4) data sources in order as shown in picture below > Click <b><i>Copy Report</i></b><br></br>
  
  >Note: For Dashboard copy to function correctly, ensure the data sources are provided in order.  
  Google Data Studio is still in its infancy, and some of the functionality can be a bit finicky. You may have to play around with the configuration of the dashboard objects to get data to display correctly. See [Troubleshooting](#troubleshooting) section below for more information.
  
  The pop-up window for "Copy this Report" should look something like this:
  ![gstudio](images/gstudio_copy_report.PNG)  
</details>
  
<details>
  <summary><b>6. Set up data pipeline via API (automate csv file upload to Google Sheets)</b></summary>
  To interact with Google Sheets API, you will need to set up authentication on Google Cloud Platform. Since we want to automate the data upload pipeline, we will be accessing the spreadsheet on behalf of a bot.  
  For this, just follow the instructions for <a href="https://docs.gspread.org/en/latest/oauth2.html#enable-api-access-for-a-project">using a service account</a>. 
  
<!--   This <a href="https://medium.com/craftsmenltd/from-csv-to-google-sheet-using-python-ef097cb014f9">medium article</a> also provides step-by-step instructions for setting up authentication.   -->
  
  Once service account credential is created, it will automatically create a JSON file that looks like this:  
  <pre><code>
    {
    "type": "service_account",
    "project_id": "api-project-XXX",
    "private_key_id": "2cd … ba4",
    "private_key": "-----BEGIN PRIVATE KEY-----\nNrDyLw … jINQh/9\n-----END PRIVATE KEY-----\n",
    "client_email": "473000000000-yoursisdifferent@developer.gserviceaccount.com",
    "client_id": "473 … hd.apps.googleusercontent.com",
      ...}
  </code></pre>  
  
  Next steps:
  <ul>
    <li><b>This step is very important!</b> Go to <a href="https://docs.google.com/spreadsheets">Google Sheets</a>, open spreadsheet and share <b><i>Editor</i></b> permission with <code>client_email</code> (client_email can be found in the JSON file). Repeat this step for all (4) spreadsheets
    <li>Rename JSON file to <code>service_account.json</code> and store it in a desired path. For windows, it's recommended to store it in <code>%APPDATA%\gspread\service_account.json</code></li>
    <li>Update <code>finsight-compiler.py</code> to reference where the <code>service_account.json</code> is stored</li>
  </ul>
  <pre><code>
    credentials = ServiceAccountCredentials.from_json_keyfile_name('service_account.json',scope) # update JSON file path
  </code></pre>
  
  > Note: Remember to share spreadsheet Editor access with the client email, otherwise you will get a <code>gspread.exceptions.SpreadsheetNotFound</code> exception when executing the python file.
</details>

<details>
  <summary><b>7. (Optional) Define</b> <code>category_dict.py</code></summary>
  <br>
  <code>category_dict.py</code> defines a dictionary of key (subcategory) to value (category) pairs. You may want to modify this file if you have new subcategories or if you have a different categorization system. If you are utilizing the sample data provided, you do not need to modify this file. Example dictionary below:

  <pre><code>
  category_dict = {
    'Groceries':'Living Expense',
    'Transportation':'Living Expense',
    'Internet':'Monthly Bills',
    'Utilities':'Monthly Bills',
    'Rent':'Monthly Bills',
    'Investment - Source 1': 'Savings',
    'Investment - Source 2': 'Savings',
    'Paycheck - Source 1': 'Income',
    'Paycheck - Source 2': 'Income',
    'Restaurants':'Discretionary Spending',
    'Vacation': 'Occasional Expense'
}
  </code></pre>
</details>

## Run <a name="run"></a>
Download requirements  
 <pre><code>
 pip install -r requirements.txt
 </code></pre>
 Execute Python code
 <pre><code>
 python finsight-compiler.py
 </code></pre>
  
## Usage <a name="usage"></a>

  Use the drop-down menu located on the top of the dashboard, to filter desired date range, category, and sub-category to focus in on different views.
    
## Framework <a name="framework"></a>
  This budgeting framework is inspired by the zero-based budgeting system, which is a method to allocate all money earned to expenses, savings, and investment.  
  The goal is to achieve net zero when subtracting expenditures from income, so that every dollar is allocated and has a purpose.  
  I break down the main finance categories into 5 categories: Monthly Bills, living expense, discretionary spending, occasional spending, and savings.    

## Documentation <a name="documentation"></a>

### Troubleshooting <a name="troubleshooting"></a> 
  - If "no data" is displayed in an object, you can try refreshing the page to ensure connection loads. If after a few refreshes, the dashboard object still doesn't display correctly, you may have to reconfigure the object.
<!--   <details><summary>Example</summary>
  To configure "income vs. expense trend," ensure the correct data source is selected.  
  
  ![income vs expense trend](images/inv_trend.png)
  ![configuration](images/inv_config.png)
  </details>
   -->
<!-- ### Changelog
 -->




