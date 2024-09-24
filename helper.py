from urlextract import URLExtract
import numpy as np
from wordcloud import WordCloud
from collections import Counter
import pandas as pd
import nltk
from nltk.corpus import stopwords
import emoji
nltk.download ("stopwords")
extractor = URLExtract()



def stats(option,final_df,select_month,select_year):
  if option!="For ALL" and select_month=="All" and select_year=="All" :
     df=final_df[final_df['names']==option]
    
     num_messages=df['messages'].count()
     
     final=final_df[final_df['names']!='Group Notification']
     final=final[final['messages']!='<Media omitted>\n']
     filter_df=final[final['names']==option]
     words=[]
     for i in filter_df['messages']:
       words.extend(i.split())
       
     media_l=df[df['messages']=='<Media omitted>\n'].shape[0]  
     
     urls=[]
     for i in df['messages']:
        urls.extend(extractor.find_urls(i))
        
  
  elif option!="For ALL" and select_month!="All" and select_year=="All" :
     df=final_df[(final_df['names'] == option) & (final_df['month'] == select_month)]
    
     num_messages=df['messages'].count()
     
     final=final_df[final_df['names']!='Group Notification']
     final=final[final['messages']!='<Media omitted>\n']
     filter_df=final[(final['names']==option) & (final['month'] == select_month)]
     words=[]
     for i in filter_df['messages']:
       words.extend(i.split())
       
     media_l=df[df['messages']=='<Media omitted>\n'].shape[0]  
     
     urls=[]
     for i in df['messages']:
        urls.extend(extractor.find_urls(i))      
     
  
  
  
  elif option!="For ALL" and select_month!="All" and select_year!="All" :
     df=final_df[(final_df['names'] == option) & (final_df['month'] == select_month) & (final_df['year'] == select_year)]
    
     num_messages=df['messages'].count()
     
     final=final_df[final_df['names']!='Group Notification']
     final=final[final['messages']!='<Media omitted>\n']
     filter_df=final[(final['names']==option) & (final['month'] == select_month) & (final['year']==select_year)]
     words=[]
     for i in filter_df['messages']:
       words.extend(i.split())
       
     media_l=df[df['messages']=='<Media omitted>\n'].shape[0]  
     
     urls=[]
     for i in df['messages']:
        urls.extend(extractor.find_urls(i))    
  
  
  elif option=="For ALL" and select_month!="All" and select_year!="All" :
     df=final_df[(final_df['month'] == select_month) & (final_df['year'] == select_year)]
    
     num_messages=df['messages'].count()
     
     final=final_df[final_df['names']!='Group Notification']
     final=final[final['messages']!='<Media omitted>\n']
     filter_df=final[(final['month'] == select_month) & (final['year']==select_year)]
     words=[]
     for i in filter_df['messages']:
       words.extend(i.split())
       
     media_l=df[df['messages']=='<Media omitted>\n'].shape[0]  
     
     urls=[]
     for i in df['messages']:
        urls.extend(extractor.find_urls(i)) 
  
  
  elif option=="For ALL" and select_month=="All" and select_year!="All" :
     df=final_df[(final_df['year'] == select_year)]
    
     num_messages=df['messages'].count()
     
     final=final_df[final_df['names']!='Group Notification']
     final=final[final['messages']!='<Media omitted>\n']
     filter_df=final[(final['year']==select_year)]
     words=[]
     for i in filter_df['messages']:
       words.extend(i.split())
       
     media_l=df[df['messages']=='<Media omitted>\n'].shape[0]  
     
     urls=[]
     for i in df['messages']:
        urls.extend(extractor.find_urls(i)) 
  
  
  
  elif option!="For ALL" and select_month=="All" and select_year!="All" :
     df=final_df[(final_df['names'] == option) & (final_df['year'] == select_year)]
    
     num_messages=df['messages'].count()
     
     final=final_df[final_df['names']!='Group Notification']
     final=final[final['messages']!='<Media omitted>\n']
     filter_df=final[(final['names']==option) &  (final['year']==select_year)]
     words=[]
     for i in filter_df['messages']:
       words.extend(i.split())
       
     media_l=df[df['messages']=='<Media omitted>\n'].shape[0]  
     
     urls=[]
     for i in df['messages']:
        urls.extend(extractor.find_urls(i))
  
  
  
  elif option=="For ALL" and select_month!="All" and select_year=="All" :
     df=final_df[(final_df['month'] == select_month)]
    
     num_messages=df['messages'].count()
     
     final=final_df[final_df['names']!='Group Notification']
     final=final[final['messages']!='<Media omitted>\n']
     filter_df=final[(final['month'] == select_month)]
     words=[]
     for i in filter_df['messages']:
       words.extend(i.split())
       
     media_l=df[df['messages']=='<Media omitted>\n'].shape[0]  
     
     urls=[]
     for i in df['messages']:
        urls.extend(extractor.find_urls(i))
  
  
  
  else:
    df=final_df
    num_messages=final_df.shape[0]  
    
    final=final_df[final_df['names']!='Group Notification']
    final=final[final['messages']!='<Media omitted>\n']
    
    words=[]
    for i in final['messages']:
      words.extend(i.split())
      
    media_l=final_df[final_df['messages']=='<Media omitted>\n'].shape[0]
    
    
    urls=[]
    for i in final['messages']:
      urls.extend(extractor.find_urls(i))  

    
  return df,num_messages,len(words),media_l ,len(urls)


def top_users(df):
  
    x=df['names'].value_counts().head(5) 
    df_user=round((df['names'].value_counts()/df['messages'].shape[0])*100,2).reset_index().rename(columns={"count":"Percentage",'names':"Users"})
    
    return x,df_user
  
def unique(final_df):
  months_list=final_df['month'].unique()
  year_list=final_df['year'].unique()
  months_list.sort()
  months_list=np.insert(months_list,0,"All")

  year_list.sort()
  year_list=np.insert(year_list,0,"All")

  return months_list,year_list   

def top_day_months(df):
  top_days=df['Day'].value_counts().head(5) 
  top_months=df['month'].value_counts().head(5) 
  
  
  return top_days,top_months

def wordcloud(df):
  final=df[df['names']!='Group Notification']
  final=final[final['messages']!='<Media omitted>\n']
  wc=WordCloud(width=500,height=500,min_font_size=10,background_color='white')
  df_wc=wc.generate(final['messages'].str.cat(sep=" "))
  
  words=[]
  for i in final['messages']:
    words.extend(i.split())
    
  stop_words = set(stopwords.words('english'))
  filtered_text=[]

  filtered_sentence = [word for word in words if word.lower() not in stop_words]
  filtered_text = ' '.join(filtered_sentence)
  words=filtered_text.split() 
  
  stopword=open("stop_hinglish.txt",'r')
  stop_word=stopword.read()
  f_word=[]
  for i in words:
    if i not in stop_word:
        f_word.append(i)  
            
  c=Counter(f_word)
  common_words=pd.DataFrame(c.most_common(5),columns={"words":0,"freq":1})
  return df_wc,common_words


def emojis(df):
  emojis=[]
  for i in df['messages']:
         emojis.extend(c for c in i if c in emoji.EMOJI_DATA)
         
  em=pd.DataFrame(Counter(emojis).most_common(len(Counter(emojis))))
  emojis=em.rename(columns={0:"emojis",1:"freq"})
  
  return emojis