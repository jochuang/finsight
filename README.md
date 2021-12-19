# FinSight

FinSight is a finance dashboard that provides personal finance trends at a glance. It builds on top of personal finance app like Mint and allows customizable charts and graphs that tailors to your needs.
This program provides a data pipeline that takes in all transaction data in a csv format, cleans and transforms the data, and displays data in a dashboard for visualization. The goal is to better track transactions and visualize spending trends, which will lead to more informed financial decisions.

### Table of Contents
   * [Getting Started](#getting-started)
      * [Prerequisite](#prerequisite)
      * [Set Up](#set-up)
      * [Run](#run)
   * [Usage](#usage)
   * [Framework](framework)
   * [Documentation](#documentation)
      


## Getting Started <a name="getting-started"></a>

## Prerequisite <a name="prerequisite"></a>
   <pre><code>
   pip install pandas
   pip install gspread
   pip install oauth2client.service_account
   </code></pre>
   
  Download "transactions.csv" from [Mint.com](https://mint.intuit.com/) and save it to your project folder
  ![export transactions.csv](/images/export_transactions.PNG)
    
## Set Up <a name="set-up"></a>
<details>
  <summary><b>1. Upload data sources to Google Sheets</b></summary>
   Go to Google Sheets Home > Click the file icon on the top-right corner > Click the Upload tab and drag csv file to the upload section > Upload all (4) csv files  
   
   Your Google Sheet Home should look something like this:  
   ![gsheets](images/gsheets_files.PNG)
</details>

<details>
  <summary><b>2. Connect Data Sources to Google Data Studio</b></summary>
  Go to Goolge Data Studio > Click create on the top-left corner > Click Google Sheets > Select the Spreadsheet that you just uploaded > Hit Connect  
  Do this (4) times for each of the spreadsheet.
  
  Your Data Studio Data sources should look something like this:  
  ![gstudio](images/gstudio_files.PNG)  
  (Note: please make sure the name of the data sources are exactly identical as shown here. If it isn't, you can rename it)
</details>
 
<details>
  <summary><b>3. Make a Copy of Data Studio Dashboard</b></summary>
  Use the provided dashborad link > Click on the three-vertical-dot icon on the top-right corner > Click "Make a Copy" > Under New 
  Data Source > Select the (4) Data Sources that were connected > Click "Copy Report"  
  
  The pop-up window for "Copy this Report" should look somehting like this:
  ![gstudio](images/gstudio_copy_report.PNG)  
  (Note: Google Data Studio is still in its infancy, and some of the functionality can be a bit finicky. You may have to play around with the dashboard objects to get the configuration to work)
</details>
  
<details>
  <summary><b>4. Set up data pipeline via API (automate csv file upload to Goole Sheets)</b></summary>
  To interact with Google Sheets API, you will need to set up authentication on Goolge Cloud Platform. Since we want to automate the data upload pipeline, we will be accesssing the spreadsheet on behalf of a bot.  
  For this, just follow the instructions for <a href="https://docs.gspread.org/en/latest/oauth2.html#enable-api-access-for-a-project">using a service account</a>. This <a href="https://medium.com/craftsmenltd/from-csv-to-google-sheet-using-python-ef097cb014f9">medium article</a> also provids step-by-step instructions for setting up authentication.  
  
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

  Keep in mind:  
  <ul>
    <li>Share spreadsheet access with the client email (from the credentials.json file) with edit permission</li>
    <li>Rename JSON file to <code>service_account.json</code> and store it in the desired path. For windows, it's recommended to store it in <code>%APPDATA%\gspread\service_account.json</code>.  
    <li>Update <code>finsight-compiler.py</code> to reference where the <code>service_account.json</code> is stored</li>
  </ul>
  <pre><code>
    credentials = ServiceAccountCredentials.from_json_keyfile_name('service_account.json',scope) # update JSON file path
  </code></pre>
</details>

<details>
  <summary><b>5. Define</b> <code>category_dict.py</code></summary>
Define category_dict, which is a dictionary of key (subcategory) to value (category) pairs
</details>

## Run <a name="run"></a>
  Run ```python finsight-compiler.py```  
  
## Usage <a name="usage"></a>

  How to read a sample report?
    
## Framework <a name="framework"></a>
  This budgeting framework is inspired by the zero-based budgeting system, which is a method to allocate all money earned to expenses, savings, and investment.  
  The goal is to achieve net zero when subtracting expenditures from income, so that every dollar is allocated and has a purpose.  
  I break down the main finance categories into 5 cateogries: Monthly Bills, living expense, discretionary spending, occasional spending, and savings.    

## Documentation <a name="documentation"></a>

  - Troubleshooting
  - Changelog





