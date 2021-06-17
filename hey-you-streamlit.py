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
  

Data Limitations
- Structure of the data is per hour, per day and not per transaction

  
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
    
    At the day of week level, the metrics are:
    """   

    dow_summary = pd.DataFrame.from_dict({
        'Day of Week': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',
       'Sunday'],
       'customers': [555906.0, 581544.0, 604730.0, 605350.0, 525182.0, 286384.0, 241604.0], 
       'orders': [564142.0, 590508.0, 614612.0, 615342.0, 534720.0, 292402.0, 246774.0],
       'order_per_customer': [1.0148154544113572, 1.0154141389129627, 1.0163411770542226, 
       1.0165061534649376, 1.01816132312227, 1.021013743784569, 1.021398652340193],
       'amount_per_order': [6.842192781250104, 6.789480582820217, 6.891127768413241, 
       7.004108902041465, 7.682790843806101, 10.076126975875667, 10.649719014158707]
       }) 
    dow_summary

    """At the hourly level, the metrics are:"""

    hour_summary = pd.DataFrame.from_dict({'Hour of day': [ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
            17, 18, 19, 20, 21, 22, 23],
            'customers': [4.0, 2.0, 6.0, 2.0, 12.0, 14582.0, 224750.0, 635220.0, 927164.0, 583956.0, 363232.0, 207140.0, 
            156904.0, 132200.0, 93600.0, 42760.0, 8652.0, 3820.0, 3212.0, 2372.0, 886.0, 178.0, 38.0, 8.0],
            'orders': [4.0, 2.0, 6.0, 2.0, 12.0, 14654.0, 227490.0, 644870.0, 941822.0, 595374.0, 370352.0, 211064.0, 159894.0,
            134488.0, 95428.0, 43574.0, 8802.0, 3878.0, 3260.0, 2402.0, 898.0, 178.0, 38.0, 8.0],
            'order_per_customer': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0049375942943355, 1.0121913236929923, 1.015191587166651, 
            1.0158095008002899, 1.0195528430224194, 1.0196017971984848, 1.0189437095684077, 1.0190562382093509, 1.0173071104387292,
            1.0195299145299146, 1.0190364826941067, 1.0173370319001387, 1.0151832460732984, 1.0149439601494397, 1.0126475548060707, 
            1.0135440180586908, 1.0, 1.0, 1.0],
            'amount_per_order': [25.0, 100.0, 36.666666666666664, 50.0, 8.0, 7.126492425276375, 7.039530792562313, 6.972432025059304, 
            6.7566209538532815, 7.4463139807918965, 7.854607022508305, 8.893474680665577, 10.941265463369483, 8.932071114151453, 
            6.764872364505179, 6.186674163491988, 8.558582140422633, 24.077194430118624, 41.3845337423313, 40.98659450457953, 
            38.46897550111359, 41.17561797752809, 30.414736842105263, 30.625]
            })
    hour_summary

    """
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
    model earns from more customers) or slow down (if business model earns from amount of order) the bottomline.
    
    ### Next Steps:
    - The joint plot shows that the analysis could be wrong when plotted against day of week. The segments described could be affected
    by the weekly seasonality. Thus, a better way to describe customer profile and segments could be to analyze distinct customer data and behavior.
    """

if option == '3. Describe the impact of the AI system':

    """
    # Impact of the AI System
    
    The AI system was deployed after the first week March 2021.
    
    --------------------------
    ### Before vs After AI Deployment


    Year to date aggregation metrics are:
    """
    metrics_ai = pd.DataFrame.from_dict({"metric":['order_per_customer', 'amount_per_order', 'promo_per_customer',  
    'order_per_vendor', 'amount_per_vendor', 'promo_per_vendor'],
       "Before AI": [1.0170220852836773, 7.5646278091047, 0.021160261601127734, 3.5300247954901876, 26.703323734794207, 0.07344604331793328],
       "Deployed AI": [1.0169105716065427, 7.482367307944383, 0.02086072938215021, 3.773068802191322, 28.23148665614122, 0.07740008750071332]})
    metrics_ai['pct_change'] = round(((metrics_ai['Deployed AI']/metrics_ai['Before AI']) - 1)*100, 2)
    metrics_ai['pct_change'] = metrics_ai['pct_change'].astype(str) + "%"
    metrics_ai
    """
    

    ### Daily Metrics

    On a daily level, the metrics before AI was deployed are:"""

    pre_ai_metrics = pd.DataFrame.from_dict({'Day of week': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',
       'Sunday'],
       'order_per_customer': [1.014903129657228, 1.015493835619466, 1.0163808063619362, 1.016583852233893, 1.0180987353684507, 1.021139577208456, 1.0211124197827115],
       'order_per_vendor': [3.519619177150629, 3.696283185840708, 3.6736648194385237, 3.6915112295393984, 3.4131498918540926, 3.165523826056766, 3.1872530493042435],
       'amount_per_vendor': [24.362704692281515, 25.25175591311342, 25.398268984836477, 25.90773521126761, 26.35081459075311, 31.97025952608279, 33.763852259062],
       'promo_per_customer': [0.020486900933406542, 0.024489543318642556, 0.024097349754856535, 0.026123236262238714, 0.023948929647290524, 0.004601241308507163, 0.006879698834303829],
       'amount_per_order': [6.921971800370965, 6.831661602618791, 6.913605413985019, 7.018192171258869, 7.720380125596773, 10.099516314779265, 10.593401821807788],
       'promo_per_vendor': [0.07104726283577015, 0.08913917940466613, 0.08709883685524633, 0.09486105824133993, 0.08028817225285001, 0.014263808118508232, 0.021473973544064592]
       })
    pre_ai_metrics = pre_ai_metrics[['Day of week', 'order_per_customer', 'amount_per_order', 'promo_per_customer',  
    'order_per_vendor', 'amount_per_vendor', 'promo_per_vendor']]
    pre_ai_metrics

    """On a daily level, the metrics after AI was deployed are:"""

    post_ai_metrics = pd.DataFrame.from_dict({'Day of week': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',
       'Sunday'],
       'order_per_customer': [1.0145736727548027, 1.0151348504329776, 1.0161963265746001, 1.0162174793581555, 1.0183899085819574, 1.020639720365079, 1.0222667334334836],
       'amount_per_customer': [6.718623612594464, 6.742129258128985, 6.919234061552205, 7.064506620969001, 7.684306923676565, 10.213104003107041, 11.061257219162064],
       'promo_per_customer': [0.020616744852573376, 0.025126640125168465, 0.025110464489707943, 0.0247546346782988, 0.023332860888668414, 0.006879906788359641, 0.006876982139876481],
       'amount_per_order': [6.622115074553279, 6.641609491835807, 6.808954018634958, 6.951766491392132, 7.545545040186494, 10.006571172297559, 10.820323950101221],
       'order_per_vendor': [3.8316654753395283, 4.003298918687763, 3.9659316229045243, 3.9388321961234225, 3.628685057761505, 3.360522469857508, 3.330650424189689],
       'amount_per_vendor': [25.373729704891247, 26.58834809701267, 27.003846061407224, 27.381841676227292, 27.380406539991164, 33.627307270734335, 36.03871655427449],
       'promo_per_vendor': [0.07786173797610538, 0.09908974280652452, 0.09799915880550382, 0.09594831229998188, 0.083138690739221, 0.0226525392765802, 0.022405916902327606]
       })
    post_ai_metrics = post_ai_metrics[['Day of week', 'order_per_customer', 'amount_per_order', 'promo_per_customer',  
    'order_per_vendor', 'amount_per_vendor', 'promo_per_vendor']]
    post_ai_metrics

    
    """
    Key notes:
    - Number of customers increased versus the previous month but the ratio of customers to orders remained. 
    - It is also important to note that due to the aggregation of the data, distinct customers were not taken into account.
    So, customer to order ratio is calculated at an hourly level, i.e., customers order once per hour.
    - Amount per vendor improved versus previous month."""
    st.image('overall_graphs/customers_monthly.png')

    """
    ### Customer Segmentation Post-AI  
    - Promos have no effect on the amount per customer after the deployment.
    - There are four distinct customer segments after the deployment.
    """
    a3, b3 = st.beta_columns(2)
    a3.subheader('Before AI: Promos vs Amount of Customers')
    a3.image('overall_graphs/pre_ai_amtcust_promo.png', use_column_width = True)
    a3.image('overall_graphs/joint_pre_ai_amtcust_promo.png', use_column_width = True)
    b3.subheader('After AI: Promos vs Amount of Customers')
    b3.image('overall_graphs/post_ai_amtcust_promo.png', use_column_width = True)
    b3.image('overall_graphs/joint_post_ai_amtcust_promo.png', use_column_width = True)

    a4, b4 = st.beta_columns(2)
    a4.subheader('Before AI: Promos vs Volume of Customers')
    a4.image('overall_graphs/pre_ai_cust_promo.png', use_column_width = True)
    a4.image('overall_graphs/joint_pre_ai_cust_promo.png', use_column_width = True)
    b4.subheader('After AI: Promos vs Volume of Customers')
    b4.image('overall_graphs/post_ai_cust_promo.png', use_column_width = True)
    b4.image('overall_graphs/joint_post_ai_cust_promo.png', use_column_width = True)

    
    