import pyupbit
import numpy as np


def get_ror(k=0.5):
    df = pyupbit.get_ohlcv("KRW-BTC", count=7)
    df['range'] = (df['high'] - df['low']) * k
    df['target'] = df['open'] + df['range'].shift(1)

    fee = 0.0032
    df['ror'] = np.where(df['high'] > df['target'],
                         df['close'] / df['target'] - fee,
                         1)

    ror = df['ror'].cumprod()[-2]
    return ror


results = {}
for k in np.arange(0.1, 1.0, 0.1):
    ror = get_ror(k)
    results[round(k, 2)] = round(ror, 7)
    print("%.1f %f" % (k, ror))

max_ror = max(results.values())
k_of_max_ror = list(results.keys())[list(results.values()).index(max_ror)]
print(k_of_max_ror)
