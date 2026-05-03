import pandas as pd
import numpy as np

def generate_synthetic_traffic_data(start_date='2023-01-01', num_days=365):
    start = pd.to_datetime(start_date)
    timestamps = pd.date_range(start=start, periods=num_days * 24, freq='1h')
    traffic_data = []
    np.random.seed(42)
    for ts in timestamps:
        hour = ts.hour
        day_of_week = ts.dayofweek
        baseline = 500
        if 7 <= hour < 9:
            daily_component = 400
        elif 17 <= hour < 19:
            daily_component = 350
        elif 10 <= hour < 16:
            daily_component = 200
        elif 19 <= hour < 23:
            daily_component = 150
        elif 23 <= hour or hour < 6:
            daily_component = 50
        else:
            daily_component = 100
        weekly_multiplier = 0.7 if day_of_week >= 5 else 1.0
        noise = np.random.normal(0, 40)
        traffic_volume = max(0, baseline + daily_component * weekly_multiplier + noise)
        traffic_data.append(traffic_volume)
    df = pd.DataFrame({'datetime': timestamps, 'traffic_volume': traffic_data})
    return df

df = generate_synthetic_traffic_data()
df.to_csv('traffic_dataset.csv', index=False)
print(f'Dataset saved: {len(df)} records')
print(df.head())
