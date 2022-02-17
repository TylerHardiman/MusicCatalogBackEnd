SECRET_KEY = 'django-insecure-6oe8xf#7fi7uxxgy!ckpvfjv+!qml7q7tb13#yydc^0k18#ux2'

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'musiclibrary',
        'USER': 'root',
        'PASSWORD': 'BingBong',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}