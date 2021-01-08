# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 10:47:48 2021

@author: Kiran Khanal
"""

import pandas as pd
import requests
import flipp_extracter
from PIL import Image
from io import BytesIO

# Information needed for data extraction
item_name = 'broccoli'
zip_code = 60565

#results list of dictionarys of query items
Output = flipp_extracter.search(item_name, zip_code)    

## dictionary of selected properties from the big dictionary of items
#selected_dic = {}
##print(Output[0]['item'])
#for i in range(len(Output)):
#    items_dict = Output[i]['item']
#    
#    print( items_dict)
    
#    for key in items_dict:
#        if i == 2:
#            print(key, items_dict[key])
#        if key == 'Current_price':
#            selected_dic[key] = items_dict[key]
#        if key == 'merchant':
#            selected_dic[key] = items_dict[key]
#        if key == 'description':
#            selected_dic[key] = items_dict[key]
#        if key =='percent_off':
#           selected_dic[key] = items_dict[key]
#        if key == 'image_url':
#            #response = requests.get(items_dict[key])
#            #img = Image.open(BytesIO(response.content))
#            #img.show() # img.show() open image with default image reader
#            selected_dic[key] = items_dict[key]
#            #print(sheller, weight)
#            #display(img)
            
#print(selected_dic)    
    
def select_df(list_dics_all):
    '''
    Results a datafram of selected items reading a list of 
    dictionaries of extracted items.
    '''
    #Reading data from Output dictionary
    selected_cols = ['brand', 'merchant', 'name', 'category', 'description', 
                                           'current_price', 'price_text', 'percent_off','image_url','cutout_image_url']
    df_all_items = pd.DataFrame(columns = selected_cols) # dataframe from selected items

    list_dic_selected_items =[]  # list of dictionaries with selected item desriptions only


    for i in range(len(Output)):
        items_dict = Output[i]['item']
        selected_dict = {}

        for key in items_dict:
            if key in selected_cols:
                selected_dict[key] = items_dict[key]                   
        list_dic_selected_items.append(selected_dict)   #update list with dictinaries for each group
    df_all_items = df_all_items.append(list_dic_selected_items, True)   # append list to dataframe 
    return df_all_items
df_sel = select_df(Output)
 
pd.set_option("display.max_columns",3)
#print(df_sel.head())