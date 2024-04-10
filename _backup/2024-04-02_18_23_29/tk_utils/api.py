""" tk_utils API

         
"""

import csv
import dataclasses as dc
import datetime as dt
import io
import pathlib
import requests
import shutil
import textwrap
import zipfile

import pandas as pd

# Toolkit must be available

try: 
    import toolkit_config as tk_cfg
except ModuleNotFoundError:
    msg = '''Could not import the `toolkit_config` module

Please make sure this module is located directly under `toolkityiping`

    toolkityiping/                <- PyCharm project folder
    | ...
    |__ toolkit_config.py
'''
    raise ModuleNotFoundError(msg)






