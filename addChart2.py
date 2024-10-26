import streamlit as st
import pandas as pd
import numpy as np
# import plotly_express as px
# from plotly.subplots import make_subplots
import plotly.graph_objects as go

from random import randint,random
from datetime import datetime,timedelta
# print(datetime.now())
time_list=[str((datetime.now()+timedelta(minutes=x)).time()).split('.')[0] for x in range(60)]


st.set_page_config(layout='wide')

placeholder=st.empty()

# curr_time=date

# Initialize session state for storing chart data
if 'charts_data' not in st.session_state:
    st.session_state.charts_data = []
    
if 'count' not in st.session_state:
    # st.start=True
    st.count=0
else:
    st.count+=1
print(st.count)
# st.count=0
# count+=1
# Function to add new chart data
def add_chart():
    # new_data = pd.DataFrame(np.random.randn(10, 2), columns=["x", "y"])
    # time_list=[f'09:{x}:00' for x in range(15,59)]
    val_list=[randint(100,150) for _ in range(len(time_list))]
    straddle_df=pd.DataFrame([time_list,val_list]).transpose()
    straddle_df.columns=['Time','Straddle']
    straddle_df['Random Decimals']=[random() for _ in range(len(time_list))]
    straddle_df.index=straddle_df['Time']
    straddle_df.drop('Time',axis=1,inplace=True)
    # print(straddle_df)
    st.session_state.charts_data.append(straddle_df)
    # st.count+=1

# Button to add a new chart

# if st.button("Add Chart"):
#     add_chart()


with st.sidebar:
    indices=st.multiselect('Select Indices',['BANKNIFTY','NIFTY','MIDCPNIFTY','FINNIFTY','SENSEX'],[])

# Create columns based on the number of charts
button_list=[]
# num_charts = len(st.session_state.charts_data)
num_charts=len(indices)
# num_charts=10
# print(num_charts)
for _ in range(num_charts):
    add_chart()
while num_charts>0:
    # cols = st.columns(num_charts)
    # count=0

    # for i, data in enumerate(st.session_state.charts_data):
        # with cols[i]:
            # st.line_chart(data.set_index("x"))
            # st.button('Remove',key=f'{st.count}-{i}')
            # count+=1
    val_list=[randint(100,150) for _ in range(len(time_list))]
    straddle_df=pd.DataFrame([time_list,val_list]).transpose()
    straddle_df.columns=['Time','Straddle']
    straddle_df['Random Decimals']=[random() for _ in range(len(time_list))]
    straddle_df.index=straddle_df['Time']
    straddle_df.drop('Time',axis=1,inplace=True)
    straddle_df=straddle_df
    with placeholder.container():
        rows=(num_charts//2)+1
        cols=2
        grid=[st.columns(2) for _ in range(rows)]

        curr_chart=0
        # data=st.session_state.charts_data[curr_chart]
        for i in range(rows):
            for j in range(2):
                if curr_chart<num_charts:
                    # data=st.session_state.charts_data[curr_chart]['Straddle']

                    with grid[i][j]:
                        if j==0:
                            temp_col=st.columns([1,3])

                            with temp_col[0]:
                                st.dataframe(straddle_df)
                            with temp_col[1]:
                                # fig = make_subplots(specs=[[{"secondary_y": True}]])
                                fig = go.Figure()

                                fig.add_trace(
                                    go.Scatter( y=straddle_df['Straddle'], name='Primary Y Axis Data', mode='lines+markers')
                                )

                                # Add second line chart for y2 (Secondary Y Axis)
                                fig.add_trace(
                                    go.Scatter( y=straddle_df['Random Decimals'], name='Secondary Y Axis Data', mode='lines+markers', yaxis='y2')
                                )
                                fig.update_layout(
                                    title='Dual Axis Line Chart Example',
                                    xaxis_title='X Axis Title',
                                    yaxis=dict(title='Primary Y Axis Title'),
                                    yaxis2=dict(title='Secondary Y Axis Title', overlaying='y', side='right'),
                                )

                                st.plotly_chart(fig)

                        
                        else:
                            temp_col=st.columns([3,1])

                            with temp_col[1]:
                                st.dataframe(straddle_df)
                            with temp_col[0]:
                                
                                fig = go.Figure()

                                fig.add_trace(
                                    go.Scatter( y=straddle_df['Straddle'], name='Primary Y Axis Data', mode='lines+markers')
                                )

                                # Add second line chart for y2 (Secondary Y Axis)
                                fig.add_trace(
                                    go.Scatter( y=straddle_df['Random Decimals'], name='Secondary Y Axis Data', mode='lines+markers', yaxis='y2')
                                )
                                fig.update_layout(
                                    title='Dual Axis Line Chart Example',
                                    xaxis_title='X Axis Title',
                                    yaxis=dict(title='Primary Y Axis Title'),
                                    yaxis2=dict(title='Secondary Y Axis Title', overlaying='y', side='right'),
                                )

                                st.plotly_chart(fig)


                        curr_chart+=1


                        

