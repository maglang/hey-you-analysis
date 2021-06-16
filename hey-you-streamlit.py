from numpy.lib.shape_base import column_stack
import streamlit as st
import pandas as pd
import numpy as np
import os

st.sidebar.title("EDA on Hey You Data")

option = st.sidebar.selectbox('Objectives', (
    '1. Describe customer behavior over time', 
    '2. Describe customer profile', 
    '3. Describe the impact of the AI system'))

st.sidebar.write(
"""
## About Hey You

## Value proposition:  
### "Make time for what matters"


### Services:
- Order ahead
- Dine in
- Delivery
- Pay through wallet

### Target Market
- App users  
  
App users are able to order ahead (and save on time),
dine in restaurants and pay through the app, 
and get food delivered to them.   

- Restaurant owners (B2B? not sure about the business model)  
  
Restaurant owners can get their processes streamlined through 
Hey You in terms of getting customers, placing orders to the kitchen, 
getting paid for the orders, setting up the logistics of the delivery, 
and marketing through promos and the website blog.
  
  
  
GitHub: maglang/hey-you-analysis
""")

if option == '1. Describe customer behavior over time':
    st.title('Customer Behavior over Time')

    """
    
    ### Orders by Month, by Day of Week, and by Hour
    Since order per customer does not vary, we can look into either order volume or number of customers 
    for an analysis of seasonality:
    - Customers usually order in the *morning*, with the peak of orders at 8 am.
    - The volume of orders is highest during the *mid-week*, on Wednesdays and Thursdays.
    
    """
    st.image('overall_graphs/orders_hour_group.png', width = 400)
    """- Compared to weekdays, *weekends receive at least or less than half* of the usual weekday volume of orders. This 
    could be due to a lower number of vendors on the weekends or a smaller number of promos."""
    orders_dow = pd.DataFrame.from_dict({'day of week': ['Monday', 'Tuesday', 'Wednesday',  
    'Thursday',    'Friday',  'Saturday',    'Sunday'],
    'orders':[564142., 590508., 614612., 615342., 534720., 292402., 246774.]})
    orders_dow

    a, b = st.beta_columns(2)
    a.subheader('Vendors Summary')
    a.image('overall_graphs/vendors_hour_group.png', use_column_width=True)
    b.subheader('Promo Count Summary')
    b.image('overall_graphs/promo_count_hour_group.png', use_column_width=True)
    """
      

    ### Order Amount per Customer
    - Order amount is higher during the *evenings*, the non-peak hours of the day, and during the 
    *weekends*, the non-peak hours of the week.

    """
    a1, b1 = st.beta_columns(2)
    amt_cust_dow = pd.DataFrame.from_dict({'day of week': ['Monday', 'Tuesday', 'Wednesday',  
    'Thursday',    'Friday',  'Saturday',    'Sunday'],
    'Average Amount per Customer':[13.63267048, 13.52306506, 15.49959235, 14.305424  , 17.02005855,
       19.48134653, 18.20314631]})
    a1.dataframe(amt_cust_dow)
    b1.image('overall_graphs/amount_per_customer_hour_group.png', use_column_width=True)

if option == '2. Describe customer profile':
    """
    # Customer Profile
      
      

    Majority of App users use iPhones:
    """

    device_use = pd.DataFrame.from_dict(
        {"Device":["iPhone", "Android", "GCF", "X11", "Windows", "Macintosh", "Tablet"], 
        "Device Users":[1016674.0, 188930.0, 60298.0, 9858.0, 7702.0, 3664.0, 1970.0], 
        "Device Users %": ['78.8672%', '14.6560%', '4.6775%', '0.7647%', '0.7647%', '0.28425', '0.1528%']}
    ).set_index('Device')
    device_use

    """
      
      

    On a daily average, there are around:
    - 22521 customers
    - 22903 orders
    - 1 order per customer
    - 8.11 AUD spent per order 
      
     

    
    We can speculate the customer segments by looking at the promo targeting:
    - One segment has a higher than average amount (higher purchasing power) and avails of less promos
    - Most of the customers belong to the second segment; 
    this has a lower than average amount, but at the average number of promos
    - The third segment has a very low average amount, but at the highest number of promos
    """
    a2, b2 = st.beta_columns(2)
    a2.subheader('Promos vs Amount per Customer')
    a2.image('overall_graphs/promo_amt_cust.png', use_column_width = True)
    a2.image('overall_graphs/joint_promo_amt_cust.png', use_column_width = True)
    b2.subheader('Promos vs Volume of Customers')
    b2.image('overall_graphs/promo_cust.png', use_column_width = True)
    b2.image('overall_graphs/joint_promo_cust.png', use_column_width = True)

    """
    - These graphs also show that promos have an inverse effect on the average amount per customer. More customers are ordering
    but customers with a basket that is below the average amount. Depending on the business model, this could increase (if business 
    model earns from more customers) or slow down (if business model earns from amount of order) the bottomline."""

if option == '3. Describe the impact of the AI system':

    """
    # Impact of the AI System
    
    The AI system was deployed after the first week March 2021.
    
    --------------------------
    
    """
    metrics_ai = pd.DataFrame.from_dict({"metric":['order_per_customer', 'order_per_vendor', 'amount_per_vendor',
       'promo_per_customer', 'amount_per_order', 'promo_per_vendor'],
       "Before AI": [1.0178, 3.456, 2.776, 1.796, 8.13475337e+00, 6.31723500e-0],
       "Deployed AI": [1.01494831e+00, 2.53224147e+00, 2.85912964e+01, 2.10129504e-02,
        1.47108910e+01, 4.88852414e-02]})
    metrics_ai
