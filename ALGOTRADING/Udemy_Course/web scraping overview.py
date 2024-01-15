import requests
from bs4 import BeautifulSoup
import pandas as pd 

tickers  = ["AAPL","FB","CSCO","INFY.NS","3988.HK"]

income_statement_dict = {}
balance_sheet_dict = {}
cashflow_st_dict = {}

for ticker in tickers:
    # scraping the income statement 
    url = "https://finance.yahoo.com/quote/{}/financials?p={}".format(ticker,ticker)
    income_statement = {}
    table_title = {}

    headers = {"User-Agent" : "Opera/104.0.4944.85"}
    page = requests.get(url, headers=headers)
    page_content = page.content
    soup = BeautifulSoup(page_content,"html.parser")
    tabl = soup.find_all("div",{"class" :"M(0) Whs(n) BdEnd Bdc($seperatorColor) D(itb)" })
    for t in tabl:
        heading = t.find_all("div", {"class" : "D(tbr) C($primaryColor)"})
        for top_row in heading:
            table_title[top_row.get_text(separator = "|").split("|")[0]] = top_row.get_text(separator = "|").split("|")[1:]
        rows = t.find_all("div", {"class" : "D(tbr) fi-row Bgc($hoverBgColor):h"})
        for row in rows : 
            income_statement[row.get_text(separator = "|").split("|")[0]] = row.get_text(separator = "|").split("|")[1:]

    temp =  pd.DataFrame(income_statement).T
    temp.columns = table_title["Breakdown"]
    income_statement_dict[ticker] = temp

    # scrape balance sheet 

    url = "https://finance.yahoo.com/quote/{}/balance-sheet?p={}".format(ticker,ticker)
    balance_seet = {}
    table_title = {}

    headers = {"User-Agent" : "Opera/104.0.4944.85"}
    page = requests.get(url, headers=headers)
    page_content = page.content
    soup = BeautifulSoup(page_content,"html.parser")
    tabl = soup.find_all("div",{"class" :"M(0) Whs(n) BdEnd Bdc($seperatorColor) D(itb)" })
    for t in tabl:
        heading = t.find_all("div", {"class" : "D(tbr) C($primaryColor)"})
        for top_row in heading:
            table_title[top_row.get_text(separator = "|").split("|")[0]] = top_row.get_text(separator = "|").split("|")[1:]
        rows = t.find_all("div", {"class" : "D(tbr) fi-row Bgc($hoverBgColor):h"})
        for row in rows : 
            balance_seet[row.get_text(separator = "|").split("|")[0]] = row.get_text(separator = "|").split("|")[1:]

    temp =  pd.DataFrame(balance_seet).T
    temp.columns = table_title["Breakdown"]
    balance_sheet_dict[ticker] = temp

# scrape the cash flow 
    url = "https://finance.yahoo.com/quote/{}/cash-flow?p={}".format(ticker,ticker)
    cash_flow = {}
    table_title = {}

    headers = {"User-Agent" : "Opera/104.0.4944.85"}
    page = requests.get(url, headers=headers)
    page_content = page.content
    soup = BeautifulSoup(page_content,"html.parser")
    tabl = soup.find_all("div",{"class" :"M(0) Whs(n) BdEnd Bdc($seperatorColor) D(itb)" })
    for t in tabl:
        heading = t.find_all("div", {"class" : "D(tbr) C($primaryColor)"})
        for top_row in heading:
            table_title[top_row.get_text(separator = "|").split("|")[0]] = top_row.get_text(separator = "|").split("|")[1:]
        rows = t.find_all("div", {"class" : "D(tbr) fi-row Bgc($hoverBgColor):h"})
        for row in rows : 
            cash_flow[row.get_text(separator = "|").split("|")[0]] = row.get_text(separator = "|").split("|")[1:]

    temp =  pd.DataFrame(cash_flow).T
    temp.columns = table_title["Breakdown"]
    cashflow_st_dict[ticker] = temp

#converting to numeric values 
for ticker in tickers : 
   for col in income_statement_dict[ticker].columns:
       income_statement_dict[ticker][col] = income_statement_dict[ticker][col].str.replace(',|- ','')
       income_statement_dict[ticker][col] = pd.to_numeric(income_statement_dict[ticker][col], errors= 'coerce')
       cashflow_st_dict[ticker][col] = cashflow_st_dict[ticker][col].str.replace(',|- ','')
       cashflow_st_dict[ticker][col] = pd.to_numeric(cashflow_st_dict[ticker][col], errors='coerce')
       if  col != "ttm" :
            balance_sheet_dict[ticker][col] = balance_sheet_dict[ticker][col].str.replace(',|- ','')
            balance_sheet_dict[ticker][col] = pd.to_numeric(balance_sheet_dict[ticker][col],errors='coerce')


print(cashflow_st_dict)