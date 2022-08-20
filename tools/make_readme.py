#!/usr/bin/env python3

import os

_LOC = '../resources/markdown'
OUTPUT_MD = '../README.md'

list_md = [
    'toc',

    'introduction',
    'docker',


    'user_flow',
    'wireframe',
    'mockup',
    'sitemap',

    'uml_use_case_diagram',
    'database',
    'rest_api',
    'tests',


    


    

    'end_user_documentation',
    'legal',
    'references'
]

if os.path.exists(OUTPUT_MD):
    os.remove(OUTPUT_MD)


def make_readme():
    for i in list_md:
        os.system(f'cat {_LOC}/{i}.md >> {OUTPUT_MD}')


make_readme()
