import pandas as pd


data = pd.read_csv('pulsar_stars_new.csv')

# Все строки, где  TARGET(TG) = 0 и MIP пренадлежит  [104.1953125, 104.5859375]
zeros = data.query("""TG == 0 and 104.1953125 <= MIP <= 104.5859375""")

# И все строки, где TARGET(TG) = 1 и MIP пренадлежит [5.8125, 14.1484375]
ones = data.query("""TG == 1 and 5.8125 <= MIP <= 14.1484375""")

# Укажите число строк в полученной выборке:
rows = zeros.shape[0] + ones.shape[0]

# Определите выборочное среднее для столбца MIP:
# Введите ответ с точностью до трех знаков.
mip_mean = round(pd.concat([zeros, ones], ignore_index=True)['MIP'].mean(), 3)
