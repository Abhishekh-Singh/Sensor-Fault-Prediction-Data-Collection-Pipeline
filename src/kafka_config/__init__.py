
import os



# API_KEY = os.getenv('API_KEY',None)
# ENDPOINT_SCHEMA_URL  = os.getenv('ENDPOINT_SCHEMA_URL',None)
# API_SECRET_KEY = os.getenv('API_SECRET_KEY',None)
# BOOTSTRAP_SERVER = os.getenv('BOOTSTRAP_SERVER',None)
# # SECURITY_PROTOCOL = os.getenv('SECURITY_PROTOCOL',None)
# # SSL_MACHENISM = os.getenv('SSL_MACHENISM',None)
# SCHEMA_REGISTRY_API_KEY = os.getenv('SCHEMA_REGISTRY_API_KEY',None)
# SCHEMA_REGISTRY_API_SECRET = os.getenv('SCHEMA_REGISTRY_API_SECRET',None)

SECURITY_PROTOCOL="SASL_SSL"
SSL_MACHENISM="PLAIN"

##Cloud

API_KEY = "ZPZGUHOYQIIHNYVH"
API_SECRET_KEY = " g5oezGAHSnaaEelhMnwL9Yy1+zhrPuwQGUhQO2W7GcHRtJsCbtA7BqseaZ1iouQc"
BOOTSTRAP_SERVER = "pkc-41p56.asia-south1.gcp.confluent.cloud:9092"
# SECURITY_PROTOCOL = os.getenv('SECURITY_PROTOCOL',None)
# SSL_MACHENISM = os.getenv('SSL_MACHENISM',None)



##Schema

ENDPOINT_SCHEMA_URL  =  "https://psrc-znpo0.ap-southeast-2.aws.confluent.cloud" 
SCHEMA_REGISTRY_API_KEY = "NIUDRKANG2XLIP2H"
SCHEMA_REGISTRY_API_SECRET = "ZgF5AjDmGSexM+0wO6SajqEYfFEcJ5EKrorAjjxYcK/0yey8rE4Kk+MBfgz0iVJn"






def sasl_conf():

    sasl_conf = {'sasl.mechanism': SSL_MACHENISM,
                 # Set to SASL_SSL to enable TLS support.
                #  'security.protocol': 'SASL_PLAINTEXT'}
                'bootstrap.servers':BOOTSTRAP_SERVER,
                'security.protocol': SECURITY_PROTOCOL,
                'sasl.username': API_KEY,
                'sasl.password': API_SECRET_KEY
                }
    # print(sasl_conf)
    return sasl_conf



def schema_config():
    return {'url':ENDPOINT_SCHEMA_URL,
    
    'basic.auth.user.info':f"{SCHEMA_REGISTRY_API_KEY}:{SCHEMA_REGISTRY_API_SECRET}"

    }

if __name__ == '__main__':
    sasl_conf()

