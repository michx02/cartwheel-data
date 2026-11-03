import pandas as pd
from datetime import date,datetime
import random
import os

random.seed(32)

def generate_orders(some_date = date.today()):
    df = pd.read_csv("data/raw/olist/olist_orders_dataset.csv")

    sample_num = random.randint(50,200)
    sample = df.sample(n=sample_num, random_state=24,replace= False)

    #create new ORDER_id by adding date and time
    sample['order_id'] += '+' + f"{some_date}T{datetime.now().strftime('%H:%M:%S')}"

    #create a new customer 1/10th of the time
    sample['customer_id'] = sample['customer_id'].apply(
    lambda x: x + f"+{some_date}T{datetime.now().strftime('%H:%M:%S')}"
    if random.randint(0, 9) == 0
    else x
    )


    sample.to_csv(path_or_buf=f'data/raw/orders/{some_date}.csv', 
                  mode='a' if os.path.exists(f'data/raw/orders/{some_date}.csv') else 'w',
                   header=not os.path.exists(f'data/raw/orders/{some_date}.csv'), index= False)  


generate_orders()

