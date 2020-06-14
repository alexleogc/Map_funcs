import numpy as np
import pandas as pd

def grid_utm(long_i,long_f,lat_i,lat_f,dx=None,dy=None,nx=None,ny=None):
    """
    ATENÇÃO: Habilitar a criação do grida para mais de uma zona
    
    Ideia: passar uma lista com os ranges de cada letter
    
    Dados de entrada - Atributos da Função
    
    long_i - (int)
    long_f - (int)
    lat_i -  (int)
    lat_f -  (int)
    dx -     (int)
    dy -     (int)
    nx - número de células no eixo x - longitude - (int)
    ny - número de células no eixo x - latitude - (int)
    
    Saída
    
    retorna um DataFrame com a longitudade e latitude fornecidade para a criação do grid (DataFrame)
    
    """
    try: x = np.arange(long_i,long_f+dx,dx) ; y = np.arange(lat_i,lat_f,dy)
    except: x = np.linspace(long_i,long_f,nx) ; y = np.linspace(lat_i,lat_f,ny)
        
    X,Y = np.meshgrid(x,y)
    
    return pd.DataFrame({'Long_utm':X.reshape(X.shape[0]*X.shape[1]), 'Lat_utm':Y.reshape(Y.shape[0]*Y.shape[1])})

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
    return pd.DataFrame({'Long_utm':X.reshape(X.shape[0]*X.shape[1]), 'Lat_utm':Y.reshape(Y.shape[0]*Y.shape[1])})
