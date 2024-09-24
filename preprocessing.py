import re
import pandas as pd
from datetime import datetime

def preprocess(text):
  text.split("\n")
  pattern="\d{1,2}/\d{1,2}/\d{1,2},\s\d{1,2}:\d{2}\u202f\w{2}\s-"
  messages=re.split(pattern,text)[1:]
  date=re.findall(pattern,text)
  df=pd.DataFrame({"Date":date,"messages":messages})
  df['Date']=pd.to_datetime(df['Date'],format='%m/%d/%y, %I:%M %p -'  )
  df['month']=df['Date'].dt.month_name()
  df['year']=df['Date'].dt.year
  df['day']=df['Date'].dt.day
  df['Day']=df['Date'].dt.day_name()

  D=[]
  for i in df['Date']:
    st=str(i)
    st=st.split()
    D.append(st[1])
  
  df['Time']=D
  obj=datetime.strptime(df['Time'][0],'%H:%M:%S')    
  time=[]
  for i in range (len(df['Time'])):
    
    obj=datetime.strptime(df['Time'][i],'%H:%M:%S')
    time_12=obj.strftime("%I:%M %p")
    time.append(time_12)
   
  df['Time']=time 
  
  
  user=[]
  messages=[]
  for i in df['messages']:
    entry=re.split('([\w\W]+?):\s',i)
    
    if entry[1:]:
        user.append(entry[1])
        messages.append(entry[2])
    else:
        user.append('Group Notification')
        messages.append(entry[0])
  years=[]
  for i in range(len(df['year'])):
        years.append(str(df['year'][i]))
  df['year']=years  
   
  df['names']=user
  df['messages']=messages
  final_df=df[['day','month','year','Day','Time','names','messages']] 
  return final_df