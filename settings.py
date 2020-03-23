#!/usr/bin/python3
from imaplib import IMAP4_SSL
import ssl
from email.parser import HeaderParser
import requests
import time
from config import *
context = ssl.SSLContext(ssl.PROTOCOL_TLS)
headers = {'X-Gotify-Key': token}
pushed_email = []
