# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'wnf84u@i@)_o#1h@)3i5d@*gu0^h@i0+^5ysopve9ddjknq#$_'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'movielens',
        'USER': 'Cameron',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
