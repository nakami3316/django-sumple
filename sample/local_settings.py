import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SECRET_KEY ='django-insecure-snk2uf8%*@6!v!(3un)g7qqiix-gdryxw=sn(ons!hr)(t0y(*'

#settings.pyからそのままコピー
DATABASES = {
 'default': {
 'ENGINE': 'django.db.backends.sqlite3',
 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
 }
}
DEBUG = True