from datetime import datetime
from datetime import date

date_ex = "2022-11-09 11:36:38"

def convert_windows_date(date_str : str):
    date_obj = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
    day : int = date_obj.weekday()
    hour : int = int(date_obj.strftime("%H"))

    return day,hour


