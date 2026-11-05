import pandas as pd
from datetime import date, datetime, timedelta
import random
import os

def change_order_dates(sample,some_date):

    #change to datetime types
    sample['order_purchase_timestamp'] = pd.to_datetime(sample['order_purchase_timestamp'])
    sample['order_approved_at'] = pd.to_datetime(sample["order_approved_at"])
    sample['order_delivered_carrier_date'] = pd.to_datetime(sample["order_delivered_carrier_date"])
    sample['order_delivered_customer_date'] = pd.to_datetime(sample["order_delivered_customer_date"])
    sample['order_estimated_delivery_date'] = pd.to_datetime(sample["order_estimated_delivery_date"])

    #differences from 
    d1 = sample['order_approved_at'] - sample['order_purchase_timestamp']
    d2 = sample['order_delivered_carrier_date'] - sample['order_approved_at']
    d3 = sample['order_delivered_customer_date'] - sample['order_delivered_carrier_date']
    d4 = sample['order_estimated_delivery_date'] - sample['order_delivered_customer_date']

    #change the dates so some_date is purchase date
    sample['order_purchase_timestamp'] = sample['order_purchase_timestamp'].apply(lambda x: 
                                                                                    x.replace(year=some_date.year, month=some_date.month, day = some_date.day))
    
    sample['order_approved_at'] = sample['order_purchase_timestamp'] + d1
    sample['order_delivered_carrier_date'] = sample['order_purchase_timestamp'] + d2
    sample['order_delivered_customer_date'] = sample['order_purchase_timestamp'] + d3
    sample['order_estimated_delivery_date'] = sample['order_purchase_timestamp'] + d4

    return sample



def generate_orders(some_date = date.today()):
    df = pd.read_csv("data/raw/olist/olist_orders_dataset.csv")

    #setting seed value
    seed_val = some_date.year + some_date.month + some_date.day
    random.seed(seed_val)

    sample_num = random.randint(50,200)
    sample = df.sample(n=sample_num, random_state=24,replace= False)

    #create new ORDER_id by adding date and time
    sample['order_id'] += '+' + f"{some_date}T{datetime.now().strftime('%H:%M:%S')}"

    #create a new customer 1/10 chance
    sample['customer_id'] = sample['customer_id'].apply(
    lambda x: x + f"+{some_date}T{datetime.now().strftime('%H:%M:%S')}"
    if random.randint(0, 9) == 0
    else x
    )

    sample = change_order_dates(sample,some_date)


    sample.to_csv(path_or_buf=f'data/raw/orders/{some_date}.csv', 
                  mode='a' if os.path.exists(f'data/raw/orders/{some_date}.csv') else 'w',
                   header=not os.path.exists(f'data/raw/orders/{some_date}.csv'), index= False)  

                   

generate_orders()

