#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
import json
from xml.sax import make_parser
from smallsmilhandler import SmallSMILHandler

class karaokelocal:
    def __init__(self,file):
        parser = make_parser()
        KHandler = SmallSMILHandler()
        parser.setContentHandler(KHandler)
        parser.parse(open(file))
        self.mytags = KHandler.get_tags()

if __name__ == "__main__":
    try:
        fich = karaokelocal(sys.argv[1])
    except IndexError:
        sys.exit("Usage: python3 karaoke.py file.smil")
