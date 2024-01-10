
import openmeteo_requests
import pandas as pd
import requests_cache
from retry_requests import retry
from django.shortcuts import render



cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)


def hava(request):
    url = "https://api.open-meteo.com/v1/forecast"
    parametreler = {
		"latitude": 37.7282,
		"longitude": 28.6057,
		"daily": ["weather_code", "temperature_2m_max", "temperature_2m_min", "sunrise", "uv_index_max", "wind_speed_10m_max"],
    
		}
    responses_gde = openmeteo.weather_api(url, params=parametreler)
    response = responses_gde[0]
    print(f"Coordinates {response.Latitude()}°E {response.Longitude()}°N")
    print(f"Elevation {response.Elevation()} m asl")
    print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
    print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")
    gunluk = response.Daily()
    gunluk_hava_code = gunluk.Variables(0).ValuesAsNumpy()
    gunluk_max_sıc = gunluk.Variables(1).ValuesAsNumpy()
    gunluk_min_sıc = gunluk.Variables(2).ValuesAsNumpy()
    gunluk_gunes = gunluk.Variables(3).ValuesAsNumpy()
    gunluk_UV_index = gunluk.Variables(4).ValuesAsNumpy()
    gunluk_max_ruz_hizi = gunluk.Variables(5).ValuesAsNumpy()
    gunluk_data = {"Gun": pd.date_range(
	    start = pd.to_datetime(gunluk.Time(), unit = "s"),
	    end = pd.to_datetime(gunluk.TimeEnd(), unit = "s"),
	    freq = pd.Timedelta(seconds = gunluk.Interval()),
	    inclusive = "left"
    )}
    gunluk_data["kod"] = gunluk_hava_code
    gunluk_data["mak"] = gunluk_max_sıc
    gunluk_data["min"] = gunluk_min_sıc
    gunluk_data["gunes"] = gunluk_gunes
    gunluk_data["uv_index_max"] = gunluk_UV_index
    gunluk_data["hizi"] = gunluk_max_ruz_hizi
    gunluk_dataframe = pd.DataFrame(data = gunluk_data)

    df = gunluk_dataframe
                          #hava_durumu = df.to_html()
                          #return HttpResponse (hava_durumu)
    #json_records = df.reset_index().to_json(orient ='records') 
    #data = [] 
    #data = json.loads(json_records) 
    #context = {'d': data}
    #return render(request, 'hava.html', context) 
    #df1 = df.loc["1"]

    l = df.values.tolist()
    for i in l:
        ma = int(i[2])
        new_ma = int(ma)
        i[2] = new_ma
        mi = int(i[3])
        new_mi = int(mi)
        i[3] = new_mi 
        uv = int(i[5])
        new_uv = int(uv)
        i[5] = new_uv
        h = int(i[6])
        new_h = int(h)
        i[6] = new_h    
    for i in l:
        gun = i[0]
        gun_py = gun.to_pydatetime()
        gun_str = gun_py.strftime('%d/%m/%Y')
        i[0] = gun_str 

    df1 = pd.DataFrame(l, columns=['G', 'K', 'MA', 'MI', 'GNS','UV','H' ])
    #print(df1)


    return render(request, 'hava.html', {'d': df1}) 





	 
