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
        self.final = ""
    def __str__(self):
        #self.final = ""
        for dic in self.mytags:
            frase = "\t"
            for element in dic:
                for atributo in dic[element]:
                    frase  += atributo + " = "+ dic[element][atributo] + "\t"
                self.final += element + frase + "\n"
        return self.final

    def do_json(self, name="local"):
        if name == "local":
            name = sys.argv[1].split(".")[0]

        self.name = name + ".json"
        with open(self.name, "w") as outfile:
            json.dump(self.mytags, outfile, sort_keys=True, indent=4)


if __name__ == "__main__":


    karaok = karaokelocal()
    #print(karaok.__str__())
    karaok.do_json()




