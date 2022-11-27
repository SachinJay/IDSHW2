from datetime import datetime
from datetime import date

date_ex = "2022-11-09 11:36:38"

def convert_windows_date(date_str : str):
    """
    Params
    -------
    date_str : str
        the time generated attribute
    
    Returns
    --------
    day,hour : tuple[int, int]
        the day and hour of the time generated
    """
    date_obj = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
    day : int = date_obj.weekday()
    hour : int = int(date_obj.strftime("%H"))

    return day,hour

def convert_omniyyah_date_time(date_str : str):
    """
    Time generated in Omniyyah's files are in a different format somehow

    Params
    -------
    date_str : str
        the time generated attribute
    
    Returns
    --------
    day,hour : tuple[int, int]
        the day and hour of the time generated
    """
    date_obj = datetime.strptime(date_str, '%m/%d/%Y %H:%M')
    day : int = date_obj.weekday()
    hour : int = int(date_obj.strftime("%H"))

    return day,hour

