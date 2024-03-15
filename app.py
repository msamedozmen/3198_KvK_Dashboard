import streamlit as st

import pandas as pd

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

import plotly.graph_objects as go
import plotly.express as px
merged_df = pd.read_excel("merged.xlsx")



st.set_page_config(page_title="KD 3198 Stats Dashboard",layout="wide")

def format_tick_label(x):
    if abs(x) >= 1e9:
        return f"{x / 1e9:.2f}B"
    elif abs(x) >= 1e6:
        return f"{x / 1e6:.2f}M"
    else:
        return str(x)



@st.cache_data
def get_data_from_excel(option):
    if option == "All Kvk":
        df = pd.read_excel("merged.xlsx")
    else:
        option = option.lower()
        df = pd.read_excel(f"{option}.xlsx")
    return df 


def get_df_from_name(name):

    if name != "All Names":
        show_df =  df_grouped.where(df_grouped["Governor Name"]==name).dropna()
        pie_df = merged_df.where(merged_df["Governor Name"]==name).dropna()
        
        return show_df,pie_df
    
def get_df_from_id(id):
    if id != "All ID":
        show_df =  df_grouped.where(df_grouped["Governor ID"].astype(str)==id).dropna()
        pie_df = merged_df.where(merged_df["Governor ID"].astype(str)==id).dropna()

    else:
        show_df = df_grouped
        pie_df = merged_df
    return show_df,pie_df

st.markdown("""
            <style> .st-af {
                font-size:20px;
            }
            p, ol, ul, dl {
                font-size:22px; }
            .st-emotion-cache-1avcm0n .ezrtsby2 {
                visibility:hidden;
            }
            </style>
            """,unsafe_allow_html=True)


pd.options.display.large_repr = 'truncate'




header_col1, header_col2, header_col3, header_col4 = st.columns(4)

kvk_list = ["All Kvk","KvK1", "KvK2", "KvK3"]

title = header_col1.markdown("<p style='font-size :48px; color: yellow; margin-right:20px; font-family: Tahoma, Verdana, sans-serif; font-weight: bold; margin-left: 10px;'>Kingdom 3198</p>", unsafe_allow_html=True)

kvk = header_col2.selectbox("Kvk", options=kvk_list)
df = get_data_from_excel(kvk)
try : 
    df=df.drop(columns=["Unnamed: 0"])
except:
    pass

df["Governor ID"] = df["Governor ID"].astype(str)

df_grouped = df.groupby(["Governor ID", "Governor Name"]).sum()

df_grouped.reset_index(inplace=True)

id_options = df_grouped["Governor ID"].tolist()
name_options = df_grouped["Governor Name"].tolist()

id_options.insert(0, "All ID")
name_options.sort()
name_options.insert(0, "All Names")

df_grouped = df_grouped.sort_values(by="Total Kill Points",ascending=False).reset_index()   

df_grouped=df_grouped.dropna()
df_grouped = df_grouped.drop(columns="index")

total_t4Kills = df_grouped["T4 Kills"].sum()
total_t5Kills = df_grouped["T5 Kills"].sum()
total_kills = df_grouped["T5-T4 Total Kills"].sum()
total_deads = df_grouped["Dead Gain"].sum()

table_df = merged_df.groupby(["KvK"],as_index=False).sum()
table_df = table_df.drop(columns=["Governor ID","T4 Kills","T5 Kills","Total Kill Points"])
id = header_col3.selectbox("ID", options=id_options,key="ID")
name = header_col4.selectbox("NAME", options=name_options,)
sub_title = header_col1.markdown("<p style='font-size :32px; color: yellow; margin-right:20px; font-family: Tahoma, Verdana, sans-serif; font-weight: bold; margin-left: 10px;'>Data & Stats Tracking</p>", unsafe_allow_html=True)



if name != "All Names":
    show_df,pie_df = get_df_from_name(name)
else:
    show_df,pie_df = get_df_from_id(id)


col1, col2, col3 = st.columns(spec=[0.25,0.25,0.5],gap="large")

with col1:
    st.markdown("<p style='font-size :20px; color: yellow; margin-right:20px; font-family: Tahoma, Verdana, sans-serif; font-weight: bold; margin-left: 10px;'>Performance Breakdown</p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size :16px; color: yellow; margin-right:20px; font-family: Tahoma, Verdana, sans-serif; font-weight: bold; margin-top:0;margin-bottom:5.5px ;margin-left: 10px;'>by Total Kills, T5 & T4 Kills, Dead Troops</p>", unsafe_allow_html=True)

    st.header("Seperated T4 - T5 Kills")
    st.subheader("Total T4 Kills")
    st.info(f"{format_tick_label(total_t4Kills)}")

    st.subheader("Total T5 Kills")
    st.info(f"{format_tick_label(total_t5Kills)}")

with col2:
    st.markdown("<p style='font-size :20px; color: yellow; margin-right:20px; font-family: Tahoma, Verdana, sans-serif; font-weight: bold;visibility:hidden ;margin-left: 10px;'>Performance Breakdown</p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size :16px; color: yellow; margin-right:20px; font-family: Tahoma, Verdana, sans-serif; font-weight: bold;visibility:hidden; margin-top:0;margin-bottom:5.5px ;margin-left: 10px;'>by Total Kills, T5 & T4 Kills, Dead Troops</p>", unsafe_allow_html=True)

    st.header("Total Kill - Dead")
    st.subheader("Total Kill Points")
    st.info(f"{format_tick_label(total_kills)}")

    st.subheader("Total Deads")
    st.info(f"{format_tick_label(total_deads)}")



with col3:
    st.markdown("<p style='font-size :20px; color: yellow; margin-right:20px; font-family: Tahoma, Verdana, sans-serif; font-weight: bold;visibility:hidden ;margin-left: 10px;'>Performance Breakdown</p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size :16px; color: yellow; margin-right:20px; font-family: Tahoma, Verdana, sans-serif; font-weight: bold;visibility:hidden; margin-top:0;margin-bottom:5.5px ;margin-left: 10px;'>by Total Kills, T5 & T4 Kills, Dead Troops</p>", unsafe_allow_html=True)
    fig = px.scatter(table_df, x="T5-T4 Total Kills", y="Dead Gain", color="KvK", 
                    title=" KvK Performance",
                    labels={"T5-T4 Total Kills": "Total Kills ", "Dead Gain": "Total Deads ", "KvK ": "KvK"},
                    template="plotly_dark")

    fig.update_traces(marker=dict(size=30, opacity=0.7))

    fig.update_layout(xaxis=dict(
                        title='Total Kills',
                        tickfont=dict(size=12, color='yellow'),  
                        gridcolor='black',  
                        showline=True,  
                        linewidth=2, 
                        linecolor='orange'), 
                    yaxis=dict(
                        title='Total Deads',
                        tickfont=dict(size=12, color='orange'),  
                        gridcolor='black',  
                        showline=True, 
                        linewidth=2, 
                        linecolor='orange'), 
                    plot_bgcolor='black', 
                    font=dict(family="Arial", size=14, color="orange"))  

    # Display the scatter plot
    st.plotly_chart(fig,use_container_width=True)
col4,col5,col6 = st.columns([0.6,0.3,0.3])
with col4:
    st.dataframe(show_df,use_container_width=True)

with col5:
    fig_t5_t4 = px.pie(pie_df, values='T5-T4 Total Kills', names='KvK', title='T5-T4 Kill Distribution on KvKs')
    fig_t5_t4.update_traces(marker=dict(colors=['#1f77b4', '#ff7f0e', '#2ca02c'], line=dict(color='#000000', width=2)))
    fig_t5_t4.update_layout(template='plotly_dark')

    st.plotly_chart(fig_t5_t4,use_container_width=True)
with col6:
    fig_dead = px.pie(pie_df, values='Dead Gain', names='KvK', title='Dead Distribution on KvKs')
    fig_dead.update_traces(marker=dict(colors=['#1f77b4', '#ff7f0e', '#2ca02c'], line=dict(color='#000000', width=2)))
    fig_dead.update_layout(template='plotly_dark')

    st.plotly_chart(fig_dead,use_container_width=True)

def format_tick_label(x):
    if abs(x) >= 1e9:
        return f"{x / 1e9:.2f}B"
    elif abs(x) >= 1e6:
        return f"{x / 1e6:.2f}M"
    else:
        return str(x)

