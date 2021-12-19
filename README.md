# FinSight
Project Overview:\
FinSight is a finance dashboard that provides personal finance trends at a glance. It builds on top of personal finance app like Mint and allows more flexibility to customize charts and graphs that tailors to your needs.
This program provides a data pipeline that takes in all transaction data in a csv format, cleans and transforms the data, and displays data in a dashboard for visualization. The goal is to better track transactions and visualize spending trends, which will lead to more informed financial decisions.

Getting Started

  - Prerequisite:\
    Download "transactions.csv" from Mint.com and save it your project folder
    
    ![export transactions.csv](/images/export_transactions.PNG)
  
  - Installation / Set up\
  1. Upload 4 data sources to Google Sheets:\
  Go to Google Sheets Home > Click the file icon on the top-right corner > Click the Upload tab and drag csv file to the upload section > Upload all (4) csv files
<!--   ![click file icon](images/gsheets_open_file_picker.PNG)\ -->
<!--   ![upload file](images/gsheets_upload_file.png)\ -->
  Your Google Sheet Home should look something like this:\
  ![gsheets](images/gsheets_files.PNG)
  
 2. Connect Data Sources to Google Data Studio:\
  Go to Goolge Data Studio > Click create on the top-left corner > Click Google Sheets > Select the Spreadsheet that you just uploaded > Hit Connect\
  Do this (4) times for each of the spreadsheet
  Your Data Studio Data Srouces should look something like this:\
  (Note: please make sure the name of the data sources are exactly identical as shown here. If it isn't, you can rename it)\
  ![gstudio](images/gstudio_files.PNG)
  
  3. Make a Copy of the Data Studio Dashboard
  Use the provided dashborad link > Click on the three-vertical-dot icon on the top-right corner > Click "Make a Copy" > Under New 
  Data Source > Select the (4) Data Sources that were connected > Click "Copy Report
  ![gstudio](images/gstudio_copy_report.PNG)
  
  (Note: Google Data Studio is still in its infancy, and some of the functionality can be a bit finicky. You may have to play around with the dashboard objects to get the configuration to work)
  
  4. Set up data pipeline via API (automate csv file upload to Goole Sheets)
  Using python library gspread. Documentation:
  
 
    Set up Google Data Studio pipeline
    Sign into Google Sheet and open 4 spreadsheets
    Define category_dict, which is a dictionary of key (subcategory) to value (category) pairs
<!--   </details>   -->
  
  - Usage:\
    Run ```python finsight-compiler.py```\
    How to read a sample report?
    
  - Method:
    This budgeting framework is inspired by the zero-based budgeting system, which is a method to allocate all money earned to expenses, savings, and investment.\
    The goal is to achieve net zero when subtracting expenditures from income, so that every dollar is allocated and has a purpose.
    I break down the main finance categories into 5 cateogries: Monthly Bills, living expense, discretionary spending, occasional spending, and savings    

Documentation
  - Changelog
  - Known bugs





