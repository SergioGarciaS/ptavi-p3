#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):

    def __init__ (self):
        self.root_layout = {"width": "", "height": "","background_color" : ""};
        self.region = {"id": "","top": "", "bottom" : "","left":"","right":""};
        self.img = {"src":"","region": "","begin" : "", "dur" : ""};
        self.audio = {"src":"","begin" : "", "dur" : ""};
        self.textstream = {"src":"","region": ""};
    
    def startElement(self,name,attrs):
        if name == 'root_layout':
            #Captura la etiqueta y guarda los atributos si los hubiese.
        if name == 'region':
            #Captura la etiqueta y guarda los atributos si los hubiese.
        if name == 'img':
            #Captura la etiqueta y guarda los atributos si los hubiese.
        if name == 'audio':
            #Captura la etiqueta y guarda los atributos si los hubiese.
        if name == 'textstream':
            #Captura la etiqueta y guarda los atributos si los hubiese.
   
if __name__ == "__main__":
    """
    Programa principal
    """
    parser = make_parser()
    cHandler = ChistesHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('chistes2.xml'))
