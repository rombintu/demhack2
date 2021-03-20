import psycopg2 
import json

from config_get_data import *

# columns [list] - столбцы таблицы
# table_name [string] - соответственно таблица 
# return [json]

def get_data(columns, table_name, where=0):
    columns_str = ",".join(columns)

    db = psycopg2.connect(dbname=db_name, user=db_user, password=db_pass, host=db_host) # коннектимся в бд
    sql = db.cursor() # создаем курсор
    
    if(where):
      script = f"""SELECT {columns_str} FROM {table_name} WHERE {where}""" # пишем скрипт
    else:
      script = f"""SELECT {columns_str} FROM {table_name}""" # пишем скрипт

    try:
        data = []
        sql.execute(script) # выполняем скрипт
        data_not_dict = sql.fetchall()

        for el in data_not_dict:
            d = dict(zip(columns, (el[x] for x in range(len(columns))))) # тут происходит магия
            data.append(d) # добавляем в массив
    except Exception as e:
        data = {"Error": e}
    
    db.close()

    return json.dumps(data)
