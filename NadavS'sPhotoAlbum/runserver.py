"""
This script runs the NadavS_sPhotoAlbum application using a development server.
"""

from os import environ
from NadavS_sPhotoAlbum import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555

    app.config['SECRET_KEY'] = 'All You Need Is Love Ta ta ta ta ta'
    app.run(HOST, PORT)

