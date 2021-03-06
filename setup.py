from setuptools import setup

import os

# Put here required packages
packages = ['Django<=1.6', 'GDAL', 'Pillow', 'Pygments', 'South', 'argparse', 'diff-match-patch', 'dj-database-url', 'dj-static', 'django-appconf', 'django-filebrowser', 'django-geoposition', 'django-grappelli', 'django-leaflet', 'django-toolbelt', 'djangorestframework', 'docutils', 'geopy', 'gunicorn', 'psycopg2', 'pystache', 'requests', 'six', 'static', 'tablib', 'virtualenv', 'wsgiref',]

if 'REDISCLOUD_URL' in os.environ and 'REDISCLOUD_PORT' in os.environ and 'REDISCLOUD_PASSWORD' in os.environ:
     packages.append('django-redis-cache')
     packages.append('hiredis')

setup(name='rest_server',
      version='1.0',
      description='RESTful server for archiving data uploaded by the Field Observation Server',
      author='Terry C. Wong',
      author_email='tw1123@mail.sfsu.edu',
      url='https://github.com/KungFuLucky7/rest_server_cloud',
      install_requires=packages,
)