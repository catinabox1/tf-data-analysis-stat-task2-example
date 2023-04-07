import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 417796486 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
alpha = 1 - p
n = len(x)
left = (-x.mean() - 1 / 2) / (14**2 / 2)
right = (-np.log(alpha) / n -x.mean() - 1 / 2) / (14**2 / 2)
return left, \
right
