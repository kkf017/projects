import csv
import json
import pickle
import numpy
from datetime import datetime

from typing import List, Tuple, Dict, Union



def format_date(x: int)-> str:
    """
            function to get the format of day or hour
            input: 
               x : hour, or date
            output: 
                formated hour
        
    """
    if len(str(x)) == 1: #int(math.log10(x))+1 == 1:
        return '0'+str(x)
    return str(x)



def get_date():
    """
            function to get the actual date and return it
                        - with format -
            input: 
               None
            output: 
                a string containing the date - with format year-month-day_hour-minute-sec
        
    """
    date = datetime.now()
    #date_format = str(date.year)+'-'+ str(date.month)+'-'+str(date.day)+'_'+ str(date.hour)+'-'+ str(date.minute)+'-'+str(date.second)
    
    day = [format_date(y) for y in [date.year, date.month, date.day]]
    hour = [format_date(y) for y in [date.hour, date.minute, date.second]]
    return '-'.join(day) + '_'+ '-'.join(hour)







def write_pickle(filename:str, y) -> None:
    """
        function to write pickle file.
        input: 
            filename - name of the file to create
        output: 
            None
    
    """
    pickle_file = open(filename, "wb")
    pickle.dump(y, pickle_file)
    pickle_file.close()
    
    
    
def read_pickle(filename:str) -> None:
    """
        function to read pickle file.
        input: 
            filename - name of the file to read
        output: 
            None
    
    """
    pickle_file = open(filename, "rb")
    y = pickle.load(pickle_file)
    pickle_file.close()
    return y



def read_json(filename:str) -> Dict[str, Union[str, int]]:
    """
        function to read .json file.
        input: 
            filename - name of the file to read
        output: 
            None
    
    """
    with open(filename, "r") as f:
        return json.load(f)



def create_file(filename:str, x:List[str])->None:
    """
        function to create a .csv file.
        input: 
            filename - name of the file to create
            rows - name of the columns
        output: 
            None
    
    """
    with open(filename , 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(x)
        
        

def write_file(filename:str, x:List[str])->None:
    """
        function to write on a .csv file.
        input: 
            filename - name of the file to write
            x - data to write
        output: 
            None
    
    """
    with open(filename , 'a', encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerow(x)
            
            

def read_file_windows(filename: str) -> List[List[str]]:
    """
        function to read a .csv file.
        input: 
            filename - name of the file 
        output: 
            data contained in .csv file
    
    """
    data = []
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            data.append(row)
    data = data[1:]
    data = [x for x in data if x != []]
    return data


def read_file(filename: str) -> List[List[str]]:
    """
        function to read a .csv file.
        input: 
            filename - name of the file 
        output: 
            data contained in .csv file
    
    """
    data = []
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            data.append(row)
    data = data[1:]
    return data
