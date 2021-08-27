import pyupbit
import numpy as np


access = "pvL1StUtbeKUGFdbdQzZdDqe8bOwpJmdTxzygPfs"
secret = "OxbvrFYnmZg1Ecj2xuz9vnfRx50AZQwxJ740gfG8"


upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balances())
print(upbit.get_balance("KRW"))         # 보유 현금 조회
