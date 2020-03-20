# импортируем numpy и pandas
import numpy as np
import pandas as pd

# импортируем datetime
import datetime
from datetime import datetime, date

# задаем некоторые настройки pandas, регулирующие
# формат вывода
pd.set_option('display.notebook_repr_html', False)
pd.set_option('display.max_columns', 8)
pd.set_option('display.max_rows', 10)
pd.set_option('display.width', 80)

# импортируем matplotlib для построения графиков
import matplotlib.pyplot as plt
