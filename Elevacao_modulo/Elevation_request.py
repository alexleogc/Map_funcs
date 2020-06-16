import requests

def get_elevation_airmap(long,lat):
    """
    
    Documentação da API: https://developers.airmap.com/docs/elevation-api
    
    Entrada
    
    long - Longitude em graus decimais (float)
    lat - Latitude em graus decimais (float)
    
    
    Saída - Elevação (float)
    """
    js = requests.get('https://api.airmap.com/elevation/v1/ele/?points='+str(lat)+','+str(long)).json()
    if js['status'] == 'success':
        return js['data']
    else:
        return -99999 #retorna -99999 em caso de erro

def grid_elevation_airmap(df,long='Longitude',lat='Latitude'):
    """
    Recebe um DataFrame com um grid e retorna a elevação
    """
    long, lat, size = df[long].to_numpy(), df[lat].to_numpy(), df.size
    return [get_elevation_airmap(long[i],lat[i])[0] for i in range(size)]


def get_elevation_google(lat,lon,key):
    """
    Função que requisita a elevação a partir da API do google
    
    Entrada 
    
    lat - Latitude em graus decimais (float)
    lon - Longitude em graus decimais (float)
    key - Chave da API (str)
    
    Saída
    
    A saída é um dicionário contendo informações sobre o status / dado de elevação (dic)
    """
    html = 'https://maps.googleapis.com/maps/api/elevation/json?locations='
    html_full = html+str(lat)+','+str(lon)+'&key='+key
    return requests.get(html_full).json()