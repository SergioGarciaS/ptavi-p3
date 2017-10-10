#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):

    def __init__ (self):
    
        self.root_layout = {"width": "", "height": "","background_color" : ""}
        self.region = {"id": "","top": "", "bottom" : "","left":"","right":""}
        self.img = {"src":"","region": "","begin" : "", "dur" : ""}
        self.audio = {"src":"","begin" : "", "dur" : ""}
        self.textstream = {"src":"","region": ""}
    
    def startElement(self,name,attrs):
        atributos = name.keys()
        if name == 'root_layout':
            for i in atributos:
                self.root_layout[i] = attrs.get('i', "")
        if name == 'region':
            for i in atributos:
                self.region[i] = attrs.get('i', "")
        if name == 'img':
            for i in atributos:
                self.img[i] = attrs.get('i', "")
        if name == 'audio':
            for i in atributos:
                self.audio[i] = attrs.get('i', "")
        if name == 'textstream':
            for i in atributos:
                self.textstream[i] = attrs.get('i', "")
   
if __name__ == "__main__":
    """
    Programa principal
    """
    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
