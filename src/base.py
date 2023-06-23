import pandas as pd
import streamlit as st


class Base:
    def __init__(self):
        self.df = None
        self.csv_file = r'C:\Users\patty\OneDrive\Desktop\capstone_II\water_potability.csv'
        self.get_data()
        self.clean_data()
    
    def return_string(self):
        return self.csv_file
    
    def get_data(self):
        self.df = pd.read_csv(self.csv_file)
        return self.df
    
    def clean_data(self):
        

        self.df.fillna(1, inplace = True)
        
        self.df['ph'] = round(self.df['ph'], 2)
        self.df['Hardness'] = round(self.df['Hardness'],2)
        self.df['Solids'] = round(self.df['Solids'], 2)
        self.df['Chloramines'] = round(self.df['Chloramines'], 2)
        self.df['Sulfate'] = round(self.df['Sulfate'], 2)
        self.df['Conductivity'] = round(self.df['Conductivity'], 2)
        self.df['Organic_carbon'] = round(self.df['Organic_carbon'], 2)
        self.df['Trihalomethanes'] = round(self.df['Trihalomethanes'], 2)
        self.df['Turbidity'] = round(self.df['Turbidity'], 2)

        self.df.rename(columns={
            'Hardness': 'hardness',
            'Solids':'solids',
            'Chloramines': 'chloramines',
            'Sulfate': 'sulfate',
            'Conductivity': 'conductivity',
            'Organic_carbon': 'organic_carbon',
            'Trihalomethanes': 'trihalomethanes',
            'Turbidity': 'turbidity',
            'Potability':'potability',

        }, inplace=True)
        


if __name__ == '__main__':
    c = Base()
    print(c.return_string())
    print(c.df)
    c.df.to_csv('water_potability_cleaned.csv')