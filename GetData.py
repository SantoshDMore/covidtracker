import pandas as pd
import requests

csse_confirmed_url = "https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_csse_confirmed_global.csv"
csse_recovered_url = "https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_csse_recovered_global.csv"
csse_fatalities_url = "https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"
vacination_url = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv"

def owid_all():
    data_url = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv"
    df = pd.read_csv(data_url)
    df.fillna(0,inplace=True)
    df['date'] = df['date'].astype('datetime64[D]')
    df['population'] = df['population'].astype(int)
    df['total_vaccinations_per_hundred'] = df['total_vaccinations_per_hundred'].astype(int)
    df.sort_values(by='date')
    print(df.columns.values)
    return df

def quandle_imf():
    quandle_imf_contry_codes_url = "/assets/Quandle_IMF_Country_Codes.csv"
    df_cc = pd.read_csv(quandle_imf_contry_codes_url)