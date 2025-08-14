'''
Expense tracker 

'''
#imported libraries 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import os 
import streamlit as st 
#data file 
data_file='expenses.csv'
def add_expenses(amount,category,description=""):
    if not os.path.exists(data_file):
        df=pd.DataFrame(columns=["Date","Amount","Category","Description"])
        df.to_csv(data_file,index=False)
    #add expense
    new_expense=pd.DataFrame({"Date":[datetime.now().strftime("%Y-%m-%d")],
                              "Amount":[amount],
                              "Category":[category],
                              "Description":[description]})
    new_expense.to_csv(data_file,mode='a',header=False,index=False)
    
def load_expenses():
    if os.path.exists(data_file):
        return pd.read_csv(data_file,parse_dates=['Date'])
    return pd.DataFrame(columns=['Date','Amount','Category','Description'])
st.title("Expense Tracker")

#add new expense
amount=st.number_input("Amount",min_value=0.0,step=0.01)
category=st.text_input("Category")
description=st.text_input("Description")
if st.button("Add Expense"):
    add_expenses(amount,category,description)
    st.success(f"Asdded:{amount} in {category} ")
#view expenses 
df=load_expenses()
if not df.empty:
    st.subheader("all expenses")
    st.dataframe(df)
    st.subheader('spending per category')
    category_total=df.groupby("Category")["Amount"].sum()
    st.bar_chart(category_total)
    st.subheader("spending over time")
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    monthly_total=df.groupby(df['Date'].dt.to_period("M"))['Amount'].sum()
    monthly_total.index=monthly_total.index.astype(str)
    st.line_chart(monthly_total)    
    
  



  