import streamlit as st

import pandas as pd

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(page_title="KD 3198 Stats Dashboard",layout="wide")


@st.cache_data
def get_data_from_excel():
    df = pd.read_csv( "18Jan_3199.csv"
    )
    return df 


# st.markdown("<p style='color: yellow; font-family: Tahoma, Verdana, sans-serif; font-weight: bold; margin-left: 10px;'>Kingdom 3198 Data & Stats Tracking</p>", unsafe_allow_html=True)

df = get_data_from_excel()
print(df.columns)


df["T4-Kills"] = df["T4-Kills"].str.replace('.', '',regex=True).astype('int64')  
df["T5-Kills"] = df["T5-Kills"].str.replace('.', '',regex=True).astype('int64')
df["Kill Points"] = df["Kill Points"].str.replace('.', '',regex=True).astype('int64')
df["Governor ID"] = df["Governor ID"].astype(str).str.replace('.', '',regex=True)
df["Power"] = df["Power"].str.replace('.', '',regex=True).astype('int64')

pd.options.display.large_repr = 'truncate'

total_t4Kills =  df["T4-Kills"].sum()
total_t5Kills =  df["T5-Kills"].sum()
total_kills =  total_t4Kills+total_t5Kills
total_deads =  df["T4-Kills"].sum()
total_t4Kills1 =  df["T4-Kills"].sum()*2
total_t5Kills1=  df["T5-Kills"].sum()*2
total_t4Kills2 =  df["T4-Kills"].sum()*3
total_t5Kills2 =  df["T5-Kills"].sum()*3
total_t4Kills3 =  df["T4-Kills"].sum()*4
total_t5Kills3 =  df["T5-Kills"].sum()*4
data = {'T4 Kills': [total_t4Kills,total_t4Kills1,total_t4Kills2,total_t4Kills3],
        'T5 Kills':[total_t5Kills,total_t5Kills1,total_t5Kills2,total_t5Kills3]}

new_df = pd.DataFrame(data)
# Sort DataFrame
df = df.sort_values(by=["Kill Points"], ascending=False)

df.index = range(1, len(df) + 1)
df = df.rename_axis("Rank")



header_col1, header_col2, header_col3, header_col4 = st.columns(4)


def format_tick_label(x):
    if abs(x) >= 1e9:
        print(x)
        return f"{x / 1e9:.2f}B"
    elif abs(x) >= 1e6:
        return f"{x / 1e6:.2f}M"
    else:
        return str(x)



# Render title in the first column
title = header_col1.markdown("<p style='font-size :48px; color: yellow; margin-right:20px; font-family: Tahoma, Verdana, sans-serif; font-weight: bold; margin-left: 10px;'>Kingdom 3198</p>", unsafe_allow_html=True)

# Render select boxes in the remaining columns
kvk = header_col2.selectbox("Kvk", options=["All Kvk","KvK1", "KvK2", "KvK3"])
id_ = header_col3.selectbox("ID", options=["All ID"])
name = header_col4.selectbox("NAME", options=["All Names"])
sub_title = header_col1.markdown("<p style='font-size :32px; color: yellow; margin-right:20px; font-family: Tahoma, Verdana, sans-serif; font-weight: bold; margin-left: 10px;'>Data & Stats Tracking</p>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(spec=[0.25,0.25,0.5],gap="large")

with col1:
    st.markdown("<p style='font-size :20px; color: yellow; margin-right:20px; font-family: Tahoma, Verdana, sans-serif; font-weight: bold; margin-left: 10px;'>Performance Breakdown</p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size :16px; color: yellow; margin-right:20px; font-family: Tahoma, Verdana, sans-serif; font-weight: bold; margin-top:0;margin-bottom:5.5px ;margin-left: 10px;'>by Total Kills, T5 & T4 Kills, Dead Troops</p>", unsafe_allow_html=True)

    st.header("Totals")
    st.subheader("Total T4 Kills")
    st.info(f"{format_tick_label(total_t4Kills)}")

    st.subheader("Total T5 Kills")
    st.info(f"{format_tick_label(total_t5Kills)}")

with col2:
    st.markdown("<p style='font-size :20px; color: yellow; margin-right:20px; font-family: Tahoma, Verdana, sans-serif; font-weight: bold;visibility:hidden ;margin-left: 10px;'>Performance Breakdown</p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size :16px; color: yellow; margin-right:20px; font-family: Tahoma, Verdana, sans-serif; font-weight: bold;visibility:hidden; margin-top:0;margin-bottom:5.5px ;margin-left: 10px;'>by Total Kills, T5 & T4 Kills, Dead Troops</p>", unsafe_allow_html=True)

    st.header("Totals")
    st.subheader("Total Kill Points")
    st.info(f"{format_tick_label(total_kills)}")

    st.subheader("Total Deads")
    st.info(f"{format_tick_label(total_deads)}")

with col3:
    st.markdown("<p style='font-size :20px; color: yellow; margin-right:20px; font-family: Tahoma, Verdana, sans-serif; font-weight: bold;visibility:hidden ;margin-left: 10px;'>Performance Breakdown</p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size :16px; color: yellow; margin-right:20px; font-family: Tahoma, Verdana, sans-serif; font-weight: bold;visibility:hidden; margin-top:0;margin-bottom:5.5px ;margin-left: 10px;'>by Total Kills, T5 & T4 Kills, Dead Troops</p>", unsafe_allow_html=True)

    fig = px.scatter(new_df,x="T4 Kills", y="T5 Kills", size =[30]*4
                    )
    fig.update_layout(
    title="Pilot Scatter Plot",
    xaxis=dict(
        title='Total T4 Kills',
        tickfont=dict(size=12, color='yellow'),  # Customize tick font size and color
        gridcolor='black',  # Change grid color
        showline=True,  # Show x-axis line
        linewidth=2,  # Set x-axis line width
        linecolor='orange',  # Set x-axis line color
        # tickvals=x,  # Set tick values
        # ticktext=[format_tick_label(total_t4Kills)],  # Set custom tick labels

        
    ),
    yaxis=dict(
        title='Total T5 Kills',
        tickfont=dict(size=12, color='orange'),  # Customize tick font size and color
        gridcolor='black',  # Change grid color
        showline=True,  # Show y-axis line
        linewidth=2,  # Set y-axis line width
        linecolor='orange',
        # tickvals=[total_t5Kills],  # Set tick values

        # ticktext=[format_tick_label(total_t5Kills)],  # Set custom tick labels
# Set y-axis line color
    ),
    plot_bgcolor='black',  # Set plot background color
    font=dict(
        family="Arial",  # Set font family
        size=14,  # Set font size
        color="orange"  # Set font color
    ),


)



    # Show plot
    st.plotly_chart(fig,use_container_width=True)
col4,col5 = st.columns([0.5,0.5])
with col4:
    st.dataframe(df,use_container_width=True)

def format_tick_label(x):
    if abs(x) >= 1e9:
        print(x)
        return f"{x / 1e9:.2f}B"
    elif abs(x) >= 1e6:
        return f"{x / 1e6:.2f}M"
    else:
        return str(x)



# fig, ax = plt.subplots()
# # Create pie chart using Plotly
# fig = go.Figure(data=[go.Pie(labels=df['Governor ID'], values=df['Kill Points'], hoverinfo='label+percent', textinfo='none')])

# # Set layout options
# fig.update_layout(title="Kill Points Distribution")

# # Display the pie chart
# st.plotly_chart(fig)


st.markdown("""
            <style> .st-af {
                font-size:20px;
            }
            p, ol, ul, dl {
                font-size:22px; }
            </style>
            """,unsafe_allow_html=True)

# # Sample data
# data = {
#     "Name": ["John", "Alice", "Bob", "Emily", "John", "Alice", "Bob", "Emily"],
#     "KillPoints": [1000000000, 2000000000, 3000000000, 4000000000, 1500000000, 2500000000, 3500000000, 4500000000],
#     "Day": ["Monday", "Monday", "Monday", "Monday", "Tuesday", "Tuesday", "Tuesday", "Tuesday"]
# }

# # Create a DataFrame from the sample data
# df = pd.DataFrame(data)

# # Render the DataFrame
# st.dataframe(df)

# # Aggregate the kill points for each person across all days
# df_agg = df.groupby('Name')['KillPoints'].sum().reset_index()

# # Create a pie chart for the aggregated data
# fig = go.Figure(data=[go.Pie(labels=df_agg['Name'], values=df_agg['KillPoints'])])
# fig.update_layout(title="Total Kill Points Distribution")

# # Display the pie chart
# st.plotly_chart(fig)
