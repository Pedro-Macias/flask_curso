
import os

# creando el config , creamos varios entornos , de produccion .... etc

# medicnate clases creamos las configuraciones
class Config(object):
    SECRET_KEY ='mi_clave_secreta'

# creamos la clase de desarrollo , hereda de la principal
class DevelopmetConfig(Config):
    DEBUG = True