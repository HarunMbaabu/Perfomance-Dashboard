import streamlit as st
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


st.set_page_config(
            page_title = "Performance Dashboard",
            page_icon = ":bar_chart:",
            layout = "wide"
)


# Define a more complex function:


def column_check(x):
    if 'unnamed' in x.lower():
        return False
    if 'priority' in x.lower():
        return False
    if 'order' in x.lower():
        return True
    return True


# data section
data = pd.read_excel('Performance_Dashboard.xlsx',
                     header=1, usecols=column_check)
data = data.dropna()
# programstart
CashInput = data.groupby('Region')[
    'Region', 'Season to Date Actual', 'MTD Target', 'MTD Actual'].sum().reset_index()
Credit = data.groupby('Region')['MonthTarget',
                                'MTD Target', 'MTD Actual'].sum().reset_index()
GeneralTotals = data.groupby(
    'Region')['Total Farmers', 'MTD Farmers', 'MTD Actual'].sum().reset_index()
# end of data grouping
# st.write(data.head())
opt = ["Cash Input and Mechanization",
       "Credit", "General Totals"]
selected_reg = st.sidebar.selectbox('select data to display', opt)
# lets work =on the data and make sure it is on the right format
if (selected_reg == "Cash Input and Mechanization"):
    reg = CashInput['Region'].unique()
    region = st.sidebar.multiselect('select Region', reg)
    st.header("KPI'S  DASHBORD (METRIC)")
    for x in region:
        datareg = CashInput[CashInput['Region'] == x]
        # region=datareg['Region']
        seaborn2date = datareg['Season to Date Actual']
        MTDTarget = datareg['MTD Target']
        MTDActual = datareg['MTD Actual']
        totals = (seaborn2date+MTDActual+MTDTarget)
        # visualization section
        st.success('Total Sales for the {}'.format(x))
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Season to Date Actual", int(seaborn2date), "1.2 °F")
        col2.metric("MTD Target", int(MTDTarget), "-8%")
        col3.metric("MTD Actual", int(MTDActual), "4%")
        col4.metric("TOTALS", int(totals), "4%")
        # st.write(datareg.sum())
elif(selected_reg == "Credit"):
    reg = Credit['Region'].unique()
    region = st.sidebar.multiselect('select Region', reg)
    st.header("KPI'S  DASHBORD SECTION")
    for x in region:
        datareg = Credit[Credit['Region'] == x]
        # region=datareg['Region']
        seaborn2date = datareg['MonthTarget']
        MTDTarget = datareg['MTD Target']
        MTDActual = datareg['MTD Actual']
        totals = (seaborn2date+MTDActual+MTDTarget)
        # visualization section
        st.success('Total Sales for the {}'.format(x))
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("MonthTarget", int(seaborn2date), "1.2 °F")
        col2.metric("MTD Target", int(MTDTarget), "-8%")
        col3.metric("MTD Actual", int(MTDActual), "4%")
        col4.metric("TOTALS", int(totals), "4%")


else:
    reg = GeneralTotals['Region'].unique()
    region = st.sidebar.multiselect('select Region', reg)
    st.header("KPI'S  DASHBORD SECTION")
    for x in region:
        datareg = GeneralTotals[GeneralTotals['Region'] == x]
        # region=datareg['Region']
        seaborn2date = datareg['Total Farmers']
        MTDTarget = datareg['MTD Farmers']
        MTDActual = datareg['MTD Actual']
        totals = (seaborn2date+MTDActual+MTDTarget)
        # visualization section
        st.success('Total Sales for the {}'.format(x))
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("MonthTarget", int(seaborn2date), "1.2 °F")
        col2.metric("MTD Target", int(MTDTarget), "-8%")
        col3.metric("MTD Actual", int(MTDActual), "4%")
        col4.metric("TOTALS", int(totals), "4%")
        # st.line_chart(datareg)
            
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)            
