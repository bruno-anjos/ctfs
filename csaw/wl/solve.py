#!/usr/bin/python3

import zwsp_steg
import requests

resp = requests.get("http://web.chal.csaw.io:5018/ahsdiufghawuflkaekdhjfaldshjfvbalerhjwfvblasdnjfbldf/alm0st_2_3z")

decoded = zwsp_steg.decode(resp.text)

print(decoded)