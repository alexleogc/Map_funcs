import request

def get_elevation_airmap(lat,long):
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