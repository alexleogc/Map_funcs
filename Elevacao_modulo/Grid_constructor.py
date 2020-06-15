import numpy as np
import pandas as pd

#===================================== Grid UTM ====================================================#
def grid_utm(long_i,long_f,lat_i,lat_f,zone,letter,dx=None,dy=None,nx=None,ny=None):
    
    """
    Recebe longitude(s), latitude(s), zona(s), letra(s) e gera um grid de espaçamento regular
    
    Dados de entrada - Atributos da Função
    
    long_i - (int, list(int))
    long_f - (int, list(int))
    lat_i -  (int, list(int))
    lat_f -  (int, list(int))
    zone - Zona da coordenada UTM      (int,list(int))
    letter Letra da  coordenada UTM    (int,list(int))
    dx -     (int)
    dy -     (int)
    nx - número de células no eixo x - longitude - (int)
    ny - número de células no eixo x - latitude - (int)
    
    Saída
    
    retorna um DataFrame com a longitudade e latitude fornecidade para a criação do grid (DataFrame)
    """
    
    long_i, long_f, lat_i, lat_f = list(long_i), list(long_f), list(lat_i), list(lat_f)
    zone, letter = list(zone), list(letter)
    
    df = pd.DataFrame()
    
    for lg_i,lg_f,lt_i,lt_f,z,l in zip(long_i,long_f,lat_i,lat_f,zone,letter):
    
        X,Y = np.meshgrid(np.arange(lg_i,lg_f,dx),np.arange(lt_i,lt_f,dy))
        aux = pd.DataFrame({'Longitude':X.reshape(X.shape[0]*X.shape[1]), 'Latitude':Y.reshape(Y.shape[0]*Y.shape[1])})
        aux['Zone'] = z
        aux['Letter'] = l
    
        df = df.append(aux)
    return df

#================================== Função grid graus decimais ========================#    
def grid_decimal_degree(long_i,long_f,lat_i,lat_f,dx=None,dy=None,nx=None,ny=None):
    """
    Dados de entrada - Atributos da Função
    
    long_i - (float)
    long_f - (float)
    lat_i -  (float)
    lat_f -  (float)
    dx -     (float)
    dy -     (float)
    nx -
    ny -
    
    Saída
    
    retorna um DataFrame com a longitudade e latitude fornecidade para a criação do grid (DataFrame)
    """
    
    try: x = np.arange(long_i,long_f+dx,dx) ; y = np.arange(lat_i,lat_f,dy)
    except: x = np.linspace(long_i,long_f,nx) ; y = np.linspace(lat_i,lat_f,ny)
        
    X,Y = np.meshgrid(x,y)
    return pd.DataFrame({'Longitude':X.reshape(X.shape[0]*X.shape[1]), 'Latitude':Y.reshape(Y.shape[0]*Y.shape[1])})
