from .base import *

SECRET_KEY = env('DJANGO_SECRET_KEY', default = 'wk(s2!l3vt4=w+68z=9q+#22&$ntbmk9y3h*rj#^qno_e1wx_6')

DEBUG = env.bool('DJANGO_DEBUG', default=True)