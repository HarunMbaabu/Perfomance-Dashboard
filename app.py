from pyforest import * 
import streamlit as st 

st.set_page_config(
            page_title = "Performance Dashboard",
            page_icon = ":bar_chart:",
            layout = "wide"
)


data = pd.read_excel(
    io = "Clean Performance Dashboard.xlsx",
    engine = "openpyxl"  
) 


st.sidebar.header("Select the countys for your Region:")  
county = st.sidebar.multiselect(
    "Select the County:",
    options=data["County"].unique(),
    default=data["County"].unique(),
)


data_selection  = data.query(
    "County == @county"
) 


st.title(":bar_chart: Performance Dashboard") 
st.markdown("""---""") 


# TOP KPI's
total_MTD_Month_Target = int(data_selection["CIP_Month Target "].sum())
total_MTD_Target = int(data_selection["CIP_MTD Target"].sum())
total_MTD_Actual = int(data_selection["CIP_MTD Actual"].sum())
total_MTD_performance = int((data_selection["CIP_MTD Performance"].mean(axis = 0)*100))

st.subheader("Cash Input and Mechanization") 
left_column, middle_column, right_column, total_column = st.columns(4)
with left_column:
    st.subheader("Month Target:")
    st.subheader(f"Ksh {total_MTD_Month_Target:,} /=")
   
with middle_column:
    st.subheader("MTD Target:")
    st.subheader(f"Ksh {total_MTD_Target:,} /=")  
    
with right_column:
    st.subheader("MTD Actual:")
    st.subheader(f"Ksh {total_MTD_Actual:,} /=")
    
with total_column:
    st.subheader("Average Perfm:")
    st.subheader(f"{total_MTD_performance:,} %")

st.markdown("""---""")


total_CR_Month_Target = int(data_selection["CR_MonthTarget"].sum())
total_CR_MTD_Target = int(data_selection["CR_MTD Target"].sum())
total_CR_MTD_Actual = int(data_selection["CR_MTD Actual"].sum())
total_MTD_performance = int((data_selection["CR_MTD Performance"].mean(axis = 0)*100))

st.subheader("Credit") 


left_column, middle_column, right_column, total_column = st.columns(4)
with left_column:
    st.subheader("Month Target::")
    st.subheader(f"Ksh {total_CR_Month_Target:,} /=")
   
with middle_column:
    st.subheader("MTD Target:")
    st.subheader(f"Ksh {total_CR_MTD_Target:,} /=")  
    
with right_column:
    st.subheader("MTD Actual:")
    st.subheader(f"Ksh {total_CR_MTD_Actual:,} /=")
    
with total_column:
    st.subheader("Average Perfm:")
    st.subheader(f" {total_MTD_performance:,} %") 
    
st.markdown("""---""")     


total_MKTA_Month_Target = int(data_selection["MKTA_MonthTarget"].sum())
total_MKTA_MTD_Target = int(data_selection["MKTA_MTD Target"].sum())
total_MKTA_MTD_Actual = int(data_selection["MKTA_MTD Actual"].sum())
total_MKTA_MTD_Performance = int((data_selection["MKTA_MTD Performance"].mean(axis = 0)*100))

st.subheader("Market Acess") 

left_column, middle_column, right_column, total_column = st.columns(4)
with left_column:
    st.subheader("Cash Inputs & M:")
    st.subheader(f"Ksh {total_MKTA_Month_Target:,} /=")
   
with middle_column:
    st.subheader("Credit:")
    st.subheader(f"Ksh {total_MKTA_MTD_Target:,} /=")
    
with right_column:
    st.subheader("MTD Actual:")
    st.subheader(f"Ksh {total_MKTA_MTD_Actual:,} /=")
    
with total_column:
    st.subheader("Average Perfm:")
    st.subheader(f"{total_MKTA_MTD_Performance:,} %") 
    
st.markdown("""---""")
  

total_farmers = int(data_selection["Total Farmers"].sum())
MTD_Farmers = int(data_selection["MTD Farmers"].sum())
total_MTD_Actual = int(data_selection["Total_MTD Actual"].sum())
total_MTD_Performance = int((data_selection["Total_MTD Performance"].mean(axis = 0)*100))

st.subheader("General Totals") 

left_column, middle_column, right_column, total_column = st.columns(4)
with left_column:
    st.subheader("Total Farmers:")
    st.subheader(f"Ksh {total_farmers:,} /=")
   
with middle_column:
    st.subheader("MTD Farmers:")
    st.subheader(f"Ksh {MTD_Farmers:,} /=")
    
    
with right_column:
    st.subheader("Total MTD Actual:")
    st.subheader(f"Ksh {total_MTD_Actual:,} /=")
    
with total_column:
    st.subheader("Total Avr Perfm:")
    st.subheader(f"{total_MTD_Performance:,} %") 
    
st.markdown("""---""") 

#Bar plots
fig_1 = px.bar(
    data["Total Farmers"],
    x="Total Farmers",
    y=data["CIP_MTD Target"],
    orientation="v",
    title="<b>Total Farmers vs Cash Inputs & Mechanization MTD Actual </b>",
    color_discrete_sequence=["#0083B8"] * len(data["CIP_MTD Target"]),
    template="plotly_white",
)

st.plotly_chart(fig_1)


fig_2 = px.bar(
    data["Total Farmers"],
    x="Total Farmers",
    y=data["MKTA_MTD Actual"],
    orientation="v",
    title="<b>Total Farmers vs Credit MTD Actual </b>",
    color_discrete_sequence=["#0083B8"] * len(data["MKTA_MTD Actual"]),
    template="plotly_white",
)

st.plotly_chart(fig_2)


fig_3 = px.bar(
    data["Total Farmers"],
    x="Total Farmers",
    y=data["MKTA_MTD Actual"],
    orientation="v",
    title="<b>Total Farmers vs Market MTD Actual</b>",
    color_discrete_sequence=["#0083B8"] * len(data["MKTA_MTD Actual"]),
    template="plotly_white",
)

st.plotly_chart(fig_3)


#Hiding the Menu && Footer  
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
