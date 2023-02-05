from pprint import pprint
import os
import pandas as pd
from pyscbwrapper import SCB

class SCBHandler:
    def __init__(self):
        '''
        Saves raw data response from SCB to ".json".
        -
        Harmonizes raw ".json" file and adds URL on last row,
        saves as ".csv".
        -
        Cleans harmonized file and leaves only column names + values, 
        saves as ".csv". 
        '''
        pass

    def save_raw(self, data:dict, filename:str):
        ''' 
        data:
            Usually a json respone in Python dict format.
        filename:
            Does not check if path is valid
            Ex: ".../raw/raw_***.json "
        '''
        with open(filename, 'w') as outfile:
            outfile.write(f'{data}')

    # Save Harmonized
    def raw_to_harmonized(self, raw_file:str, harmonized_file:str, url:str):
        '''
        raw_file:
            Usually a "raw_***.json" file
        harmonized_file:
            Path + filename of new harmonized file.
            Ex: ".../harmonized/harmonized_***.csv "
        url:
            scb.get_url() does the job
        '''
        with open(raw_file, 'r') as in_file, open(harmonized_file, 'w') as out_file:
            raw_dict = eval(in_file.read())

            # columns
            for i in range(len(raw_dict['columns'])):
                out_file.write(
                    f"{raw_dict['columns'][i]['text'].replace(' ', '_').replace(',', '')}")

                if i < len(raw_dict['columns'])-1:
                    out_file.write(',')
                
            # data
            for i in range(len(raw_dict['data'])):
                out_file.write(f"\n{raw_dict['data'][i]['key'][0]},")

                for j in range(len(raw_dict['data'][i]['values'])):
                    out_file.write(f"{raw_dict['data'][i]['values'][j].replace('..','0.0')}")

                    if j < len(raw_dict['data'][i]['values'])-1:
                        out_file.write(',')

            # comments
            out_file.write(f"\ncomments,{raw_dict['comments']}")
            
            # metadata
            for i in raw_dict['metadata'][0]:
                out_file.write(f"\n{i},{raw_dict['metadata'][0][i]}")

            # url
            out_file.write(f"\nurl,{url}")

    def harmonized_to_clean(self, harmonized_file, clean_file):
        df = pd.read_csv(harmonized_file, index_col=False, engine = 'python', skipfooter=6)
        df.to_csv(f"{clean_file}", index = False)
        # print(df.columns[1])
    
if __name__ =='__main__':
    CURR_DIR_PATH = os.path.dirname(os.path.realpath('__file__'))
    filepath = CURR_DIR_PATH + '/EkonomiSCB/Bostader/'

    ## Poke here to find nice data
    scb  = SCB('sv', 'EN', 'EN0105', 'EN0105A', 'ElProdAr')#, 'BO', 'BO0406', 'BO0406G', 'BO0406TabAh')
    # pprint(scb.info())
    

    ## When ready, get data
    data = scb.get_data()
    pprint(data)
    data_url = scb.get_url()
    
    ## Where are we (path)
    # print(CURR_DIR_PATH)
    
    ## Get & set filename from the data title
    title = scb.info()['title'].split(',')[0].replace(' ', '_')
    raw   = f'raw_{title}.json'
    harm  = f'harmonized_{title}.csv'
    clean = f'clean_{title}.csv'


    ## Save on this path
    raw_file   = filepath + 'raw/' + raw
    harm_file  = filepath + 'harmonized/' + harm
    clean_file = filepath + 'clean/' + clean

    ## Is the path valid?
    # print(raw_file)
    # print(harm_file)
    # print(clean_file)
    
    ## Saving: raw, harmonized then clean
    handler = SCBHandler()

    handler.save_raw(data, raw_file)                         # 1
    handler.raw_to_harmonized(raw_file, harm_file, data_url) # 2
    handler.harmonized_to_clean(                             # 3
        harm_file, clean_file)
    
