1# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 19:29:39 2019

@author: Sandra Milena
"""

import sass
import os

sass.compile(dirname=('sass', 'css'), output_style='compressed')
with open('css/styles.css') as styles_css:
     print(styles_css.read())
