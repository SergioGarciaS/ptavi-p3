#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
import json
from xml.sax import make_parser
from smallsmilhandler import SmallSMILHandler
import urllib


class karaokelocal(SmallSMILHandler):
    def __init__(self):
        """ Método para capturar de terminal y realizar parseo """
        try:
            fich = sys.argv[1]
        except IndexError:
            sys.exit("Usage: python3 karaoke.py file.smil")
        parser = make_parser()
        KHandler = SmallSMILHandler()
        parser.setContentHandler(KHandler)
        parser.parse(open(fich))
        self.mytags = KHandler.get_tags()

    def __str__(self):
        """ Método para crear la lista de etiquetas """
        self.final = ""
        for dic in self.mytags:
            frase = "\t"
            for element in dic:
                for atributo in dic[element]:
                    frase += atributo + " = '" + dic[element][atributo] + "'\t"
                self.final += element + frase + "\n"
        return self.final

    def do_json(self, name="local"):
        if name != "local":
            name = sys.argv[1].split(".")[0]

        self.name = name + ".json"
        with open(self.name, "w") as outfile:
            json.dump(self.mytags, outfile, sort_keys=True, indent=4)

    def do_local(self):
        for dic in self.mytags:
            for element in dic:
                for atributo in dic[element]:
                    if atributo == 'src':
                        atr = dic[element][atributo]  # Lo utilizo para acortar
                        if atr.startswith('http://'):
                            urllib.request.urlretrieve(atr, atr.split('/')[-1])
                            dic[element][atributo] = "./" + atr.split('/')[-1]


if __name__ == "__main__":

    K_Local = karaokelocal()
    print(K_Local)
    K_Local.do_json(sys.argv[1])
    K_Local.do_local()
    print(K_Local)
    K_Local.do_json()
