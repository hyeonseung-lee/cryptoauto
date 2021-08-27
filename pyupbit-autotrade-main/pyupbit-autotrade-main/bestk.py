import pyupbit
import numpy as np


def get_ror(k=0.5):
    df = pyupbit.get_ohlcv("KRW-DOT", count=7)      # 최근 7일 동안의 데이터로 테스트
    df['range'] = (df['high'] - df['low']) * k
    df['target'] = df['open'] + df['range'].shift(1)

    # fee = 0.00
    df['ror'] = np.where(df['high'] > df['target'],     # 수수료를 제외한 계산
                         df['close'] / df['target'],
                         1)

    ror = df['ror'].cumprod()[-2]
    return ror


for k in np.arange(0.1, 1.0, 0.1):
    ror = get_ror(k)
    print("%.2f %f" % (k, ror))
