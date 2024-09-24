import streamlit as st
import preprocessing
import helper
import matplotlib.pyplot as plt





st.sidebar.title("Whatsapp Message Analyzer")

file=st.sidebar.file_uploader("Drop your File Here")



if file is not None:
  bytes_data=file.getvalue()
  data=bytes_data.decode("utf-8")

  final_df=preprocessing.preprocess(data)
  
  
  #user list
  months_list,year_list=helper.unique(final_df)
  user=final_df['names'].unique().tolist()
  user.remove("Group Notification")
  user.sort()
  user.insert(0,"For ALL")
  
  
  option=st.sidebar.selectbox("Users",user)
  select_month=st.sidebar.selectbox("Months",months_list)
  select_year=st.sidebar.selectbox("Year",year_list)

  
  #for stats
  df,total_m,length_words,media,url=helper.stats(option,final_df,select_month,select_year)
  st.dataframe(df)
#   st.snow()
  
  col1, col2, col3 ,col4= st.columns(4)

  with col1:
     st.header("Total Messages")
     st.subheader(total_m)

  with col2:
     st.header("Total Words")
     st.subheader(length_words)

  with col3:
     st.header("Shared Media")
     st.subheader(media)
  
  with col4:
     st.header("Shared URL")
     st.subheader(url)
     
     
     
  #top 5 user plot
  x,df_user=helper.top_users(df)
  
  col1,col2  =st.columns(2) 
  fig,ax=plt.subplots()
  
  
  with col1:
     st.subheader("Top 5 Users")
     plt.xticks(rotation='vertical')
     ax.bar(x.index,x.values)
     st.pyplot(fig)
     
  with col2 :
     st.subheader("User Contribution")
     st.dataframe(df_user)
     
     
     
  #top busy days and months
   
  top_days,top_months=helper.top_day_months(df) 
 
  fig_days, ax_days = plt.subplots(figsize=(6, 4))
  fig_months, ax_months = plt.subplots(figsize=(6, 4))


  ax_days.bar(top_days.index, top_days.values)
  ax_days.set_xticklabels(top_days.index, rotation='vertical')
#   ax_days.set_title("Top 5 busy days")


  ax_months.bar(top_months.index, top_months.values)
  ax_months.set_xticklabels(top_months.index, rotation='vertical')
#   ax_months.set_title("Top 5 busy months")


  col1, col2 = st.columns(2)

  with col1:
    st.subheader("Top 5 busy days")
    st.pyplot(fig_days)

  with col2:
    st.subheader("Top 5 busy months")
    st.pyplot(fig_months)
     
     
#wordcloud
  df_wc,common_words=helper.wordcloud(df)

  fig,ax=plt.subplots()

  ax.imshow(df_wc)
  st.pyplot(fig)
  
   
  col1,col2=st.columns(2)
  
  with col1:
    st.dataframe(common_words)
  
  
#emoji
  with col2:
   emojis=helper.emojis(df)
   st.dataframe(emojis)
       
     
     
     