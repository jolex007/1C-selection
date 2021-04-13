import pandas as pd
import argparse
import numpy as np


class CoursesNeed():

    class CoursesToChoose():
        def __init__(self, string):
            self.choose = np.array(list(map(int, string.split('/'))))
            pass

        def __len__(self):
            return len(self.choose)

        def __iter__(self):
            return iter(self.choose)
        
        def is_one(self):
            return len(self.choose) == 1
        
        def get_elem(self):
            if self.is_one():
                return self.choose[0]
            else:
                return self.choose
        
        pass

    def __init__(self, string):
        if string == 'nan':
            self.courses = np.array([])
        else:
            self.courses = list(map(lambda x: self.CoursesToChoose(x), string.split(', ')))
    
    def __iter__(self):
        return iter(self.courses)
    
    def __len__(self):
        return len(self.courses)
    
    pass
        
    

def parse_timetable(table_path):
    """
    Parse table with timetable

    :input:
        table_path
    :output:
        table
    """

    table = pd.read_csv(table_path)
    table.rename(columns={'Номер' : 'index',
                          'Название' : 'name',
                          'Формат' : 'format',
                          'Уровень' : 'level',
                          'Зависимости' : 'dependencies'},
                 inplace=True
    )
    table.set_index('index', inplace=True)

    table['dependencies'] = table['dependencies'].astype(str).apply(lambda elem: CoursesNeed(elem))
    
    return table