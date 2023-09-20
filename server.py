import os
from livereload import Server, shell


def rebuild():
    print('Site rebuilt')


server = Server()

server.watch('./shop/templates/shop/*.html', rebuild())
server.serve(root='.', default_filename='shop/templates/shop/base.html')