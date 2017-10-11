#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):

    def __init__ (self):
        self.motherlist = []
        self.dic = { 'root_layout' : ["width", "height","background_color"], 
        'region' : ['id', 'top', 'bottom', 'left','right'], 
        'img': ['src', 'region','begin','dur'], 
        'audio': ['src','dur'], 'textstream' : ['src','region']}
    
    def startElement(self,name,attrs):

        if name == 'root_layout':
            for i in atributos:
                self.root_layout['i'] = attrs.get('i', "")
            self.motherlist.append(self.root_layout)
        if name == 'region':
            for i in atributos:
                self.region['i'] = attrs.get('i', "")
            self.motherlist.append(self.region)
        if name == 'img':
            for i in atributos:
                self.img['i'] = attrs.get('i', "")
            self.motherlist.append(self.img)
        if name == 'audio':
            for i in atributos:
                self.audio['i'] = attrs.get('i', "")
            self.motherlist.append(self.audio)
        if name == 'textstream':
            for i in atributos:
                self.textstream['i'] = attrs.get('i', "")
            self.motherlist.append(self.textstream)
            
    def get_tags(self):
        return self.mortherlist
               
        
   
if __name__ == "__main__":
    """
    Programa principal
    """
    parser = make_parser()
    KJandler = SmallSMILHandler()
    parser.setContentHandler(KJandler)
    parser.parse(open('karaoke.smil'))
    
    print(KJandler.get_tags())
