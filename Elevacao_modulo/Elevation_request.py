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

def get_elevation_from_grid(df,long='Longitude',lat='Latitude'):
    """
    Recebe um DataFrame com um grid e retorna a elevação
    """
    long, lat, size = df[long].to_numpy(), df[lat].to_numpy(), df.size
    return [get_elevation_airmap(long[i],lat[i])[0] for i in range(size)]