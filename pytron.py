#! /usr/bin/python2.7
#-*- coding: utf-8 -*-
import random

class pytron():
    quotes_list = []
    def __init__(self):
        global quotes_list
        file = open("quotes", "r")
        quotes_list = file.read()
        quotes_list = quotes_list.split(";;")

    def get_quote(self, number):
        #note: this only works if you end your quotes file with ;; !
        if number <= (len(quotes_list)-2):
            print quotes_list[number]
        else:
            raise IndexError
        print quotes_list[number]

    def random_quote(self):
        rand_number = random.randrange(0, len(quotes_list))
        print quotes_list[rand_number]
