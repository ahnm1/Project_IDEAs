import pandas as pd
from pyscbwrapper import SCB

class SCBRaw:
    def __init__(self):
        '''
        Call on "save_raw(data:dict, filename:str)"
        to save raw data to json
        '''
        pass

    def save_raw(self, data:dict, filename:str):
        with open(filename, 'w') as outfile:
            outfile.write(f'{data}')

    # Save Harmonized
    def raw_to_harmonized(self, raw_file:str, harmonized_file:str):
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
                    out_file.write(f"{raw_dict['data'][i]['values'][j]}")

                    if j < len(raw_dict['data'][i]['values'])-1:
                        out_file.write(',')

            # comments
            out_file.write(f"\ncomments,{raw_dict['comments']}")
            
            # metadata
            for i in raw_dict['metadata'][0]:
                out_file.write(f"\n{i},{raw_dict['metadata'][0][i]}")

            # url
            out_file.write(f"\nurl,{scb.get_url()}")

    def harmonized_to_clean(self, harmonized_file, clean_file):
        df = pd.read_csv(harmonized_file, index_col=False, engine = 'python', skipfooter=6)
        df.to_csv(f"{clean_file}", index = False)
        # print(df.columns[1])
    
if __name__ =='__main__':
    scb  = SCB('sv', 'HE', 'HE0110', 'HE0110G', 'TabVX4bDispInkN')
    # print(scb.info())
    
    data = scb.get_data()
    
    title = scb.info()['title'].split(',')[0].replace(' ', '_')
    raw   = f'raw_{title}.json'
    harm  = f'harmonized_{title}.csv'
    clean = f'clean_{title}.csv'

    raw_file   = 'raw/' + raw
    harm_file  = 'harmonized/' + harm
    clean_file = 'clean/' + clean

    # print(raw_file)
    # print(harm_file)
    # print(clean_file)

    handler = SCBRaw()
    handler.save_raw(data, raw_file)
    handler.raw_to_harmonized(raw_file, harm_file)
    handler.harmonized_to_clean(harm_file, clean_file)
    
