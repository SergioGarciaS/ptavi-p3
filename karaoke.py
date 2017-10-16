#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
import json
from xml.sax import make_parser
from smallsmilhandler import SmallSMILHandler

class karaokelocal(SmallSMILHandler):
    def __init__(self):
        try:
            fich = sys.argv[1]
        except IndexError:
            sys.exit("Usage: python3 karaoke.py file.smil")
        parser = make_parser()
        KHandler = SmallSMILHandler()
        parser.setContentHandler(KHandler)
        parser.parse(open(fich))
        self.mytags = KHandler.get_tags()

    def format(self):
        jambor = ""
        for dic in self.mytags:
            #print(dic)
            frase = "\t"

            for element in dic:
                #print(element)
                for atributo in dic[element]:
                    #print(atributo, dic[element][atributo])
                    frase  += atributo + " = "+ dic[element][atributo] + "\t"
                jambor += element + frase + "\n"
        return jambor

if __name__ == "__main__":


    karaok = karaokelocal()
    print(karaok.format())
