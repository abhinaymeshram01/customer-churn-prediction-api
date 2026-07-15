import pandas as pd


def tenure_group(tenure):
    if tenure <=12:
        return 'New'
    elif tenure<=24:
        return 'Developing'
    elif tenure<=48:
        return 'Estabilished'
    else:
        return 'loyal'

def create_feature(df):

    df['tenure_group']=df['tenure'].apply(tenure_group)
    
    df['ChargePerMonth'] = (df['TotalCharges'] / (df['tenure'] + 1)).round(2)

    service_cols = ['PhoneService', 'MultipleLines', 'OnlineSecurity',
                'OnlineBackup', 'DeviceProtection', 'TechSupport',
                'StreamingTV', 'StreamingMovies']
    
    df['service_count'] = df[service_cols].apply(
        lambda row:sum(1 for val in row if val =='Yes'), axis=1
    )
    
    df['HasPremiumServices'] = (
        (df['OnlineSecurity'] == 'Yes') |
        (df['TechSupport'] == 'Yes') |
        (df['DeviceProtection'] == 'Yes')
    ).astype(int)

    median_charge = 70.35

    df['IsHighValue'] = (df['MonthlyCharges'] > median_charge).astype(int)

    return df