import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

STRING = getenv("STRING")
STRING2 = getenv("STRING2")
STRING3 = getenv("STRING3")
STRING4 = getenv("STRING4")
STRING5 = getenv("STRING5")
STRING6 = getenv("STRING6")
STRING7 = getenv("STRING7")
STRING8 = getenv("STRING8")
STRING9 = getenv("STRING9")
STRING10 = getenv("STRING10")
STRING11 = getenv("STRING11")
STRING12 = getenv("STRING12")
STRING13 = getenv("STRING13")
STRING14 = getenv("STRING14")
STRING15 = getenv("STRING15")
STRING16 = getenv("STRING16")
STRING17 = getenv("STRING17")
STRING18 = getenv("STRING18")
STRING19 = getenv("STRING19")
STRING20 = getenv("STRING20")
STRING21 = getenv("STRING21")
STRING22 = getenv("STRING22")
STRING23 = getenv("STRING23")
STRING24 = getenv("STRING24")
STRING25 = getenv("STRING25")
STRING26 = getenv("STRING26")
STRING27 = getenv("STRING27")
STRING28 = getenv("STRING28")
STRING29 = getenv("STRING29")
STRING30 = getenv("STRING30")
STRING31 = getenv("STRING31")
API_ID = getenv("API_ID")
API_HASH = getenv("API_HASH")
BIO_MESSAGE = getenv("BIO")
SUDO = list(map(int, getenv("SUDO").split()))
