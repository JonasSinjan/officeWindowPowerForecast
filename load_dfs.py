#functions to load in the two dataframes succintly and prep the data

import pandas as pd

def load_spotprices(zone='DK1'):
    """
    read the csv and return df with one zone selected (DK1 default)
    """
    spotPricesdf = pd.read_csv('./data/Elspotprices.csv',delimiter=';',decimal=',')

    spotPricesdf['HourDK'] = pd.to_datetime(spotPricesdf['HourDK'],format='%Y-%m-%d %H:%M:%S')
    spotPricesdf['HourUTC'] = pd.to_datetime(spotPricesdf['HourUTC'],format='%Y-%m-%d %H:%M:%S')

    DK1spotPricesdf = spotPricesdf[spotPricesdf['PriceArea']=='DK1']
    DK1spotPricesdf = DK1spotPricesdf.drop('PriceArea', axis=1, inplace=False)

    return DK1spotPricesdf

def load_openmeteo(lat='56.13N',lon='10.19E',elevation='27m'):
    """
    read the openmeteo csv, with input lat and lon and return df
    """
    openmeteodf=pd.read_csv(f'./data/open-meteo-{lat}{lon}{elevation}_all.csv',skiprows=3)
    openmeteodf['time'] = pd.to_datetime(openmeteodf['time'],format='%Y-%m-%dT%H:%M')

    return openmeteodf

def load_consumption(zone='DK1'):
    """
    read the csv and return df with one zone selected (DK1 default)
    """
    consumptiondf = pd.read_csv('./data/ConsumptionCoverageNationalDecl.csv',delimiter=';',decimal=',')

    consumptiondf['HourDK'] = pd.to_datetime(consumptiondf['HourDK'],format='%Y-%m-%d %H:%M:%S')
    consumptiondf['HourUTC'] = pd.to_datetime(consumptiondf['HourUTC'],format='%Y-%m-%d %H:%M:%S')

    Zonalconsumptiondf = consumptiondf[consumptiondf['ConnectedArea']==zone]
    Zonalconsumptiondf = Zonalconsumptiondf.drop('ConnectedArea', axis=1, inplace=False)
    Zonalconsumptiondf = Zonalconsumptiondf.drop('HourUTC', axis=1, inplace=False)

    return Zonalconsumptiondf

"""TODO (optional to make it more general later)
------------------
- check if both dfs hourly
- check what variables in open meteo (if it has temp, wind speed, sunshine duration, cloud cover)
- chcek if both cover the same timerange
- check if 'time' in same timezone
"""
