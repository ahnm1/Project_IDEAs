import os
import pandas as pd

class AgeCategoryHandler:
    def __init__(self):
        pass

    def split(self, filepath) -> list:
        dfs = []
        df  = pd.read_csv(filepath)
        age_list = df['ålder'].unique()

        for age in age_list:
            # print(age)
            dfs.append(df[df['ålder'] == age].reset_index(drop = True))

        return dfs

    def summerize(self, df_list):
        # For each df in list
        for i in range(len(df_list)):   # 1

            # For each column in df
            for col in range(len(df_list[i].columns)):

                if i < len(df_list)-1:
                    ##################### 1 ###################
                    # df = pd.DataFrame([df_list[i][df_list[i].columns[col]] + df_list[i+1][df_list[i].columns[col]]])
                    df = pd.DataFrame([df_list[i][df_list[i].columns[col]], df_list[i+1][df_list[i].columns[col]]])
                    # print(1, df_list[i][df_list[i].columns[col]])
                    # print(2, df_list[i+1][df_list[i].columns[col]])
        print(df)
        pass

if __name__ == '__main__':
    CURR_DIR_PATH = os.path.dirname(os.path.realpath('__file__'))
    filepath = CURR_DIR_PATH + '/EkonomiSCB/Bostader/' + 'clean/' + 'clean_Disponibel_inkomst_för_hushåll_efter_region.csv'
    a = AgeCategoryHandler()
    dfs = a.split(filepath)

    print(dfs)
    
    # a.summerize(dfs)
