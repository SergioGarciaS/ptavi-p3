#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    def __init__(self):
        self.motherlist = []
        self.dic = {'root-layout': ["width", "height", "background-color"],
                    'region': ['id', 'top', 'bottom', 'left', 'right'],
                    'img': ['src', 'region', 'begin', 'dur'],
                    'audio': ['src', 'dur', 'begin'],
                    'textstream': ['src', 'region']}

    def startElement(self, name, attrs):
        newdic = {}  # Creación de un diccionario nuevo cada vez.
        if name in self.dic:
            for i in self.dic[name]:
                newdic[i] = attrs.get(i, "")
            self.motherlist.append({name: newdic})

    def get_tags(self):
        return self.motherlist

if __name__ == "__main__":
    """
    Programa principal
    """
    parser = make_parser()
    KJandler = SmallSMILHandler()
    parser.setContentHandler(KJandler)
    parser.parse(open('karaoke.smil'))
    print(KJandler.get_tags())
