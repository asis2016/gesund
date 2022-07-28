#!/usr/bin/env python3

import os

_LOC = '../resources/drawio'
_OUT = '../resources/images'

list_drawio = [
    'erd.drawio',
    'sitemap.drawio',
    'user_flow.drawio',
]


def make_erd():
    """ Creates .svg from drawio file. """
    os.system('echo "[info] Making database-diagram.png ..."')
    os.system('sleep 1')

    for i in list_drawio:
        _output = i.split('.')[0]
        _input = i
        os.system(f'/snap/bin/drawio -x -f svg -o    {_OUT}/{_output}.svg    {_LOC}/{_input}')

    os.system('echo "\n[info] Done!"')


if __name__ == '__main__':
    make_erd()
