#!/bin/python3

import os
import sys

from hashlib import sha256 as SHA


class block:

    def __init__(self,*data):
        self.uid = data[0]
        self.previous = data[1]
        self.next = data[2]
        self.alternatives = data[2:-2]
        self.cat = data[-2]
        self.data = data[-1]

    def packet( self ) -> tuple:
        return zip(self.uid,self.previous,self.next,self.alternatives,self.cat,self.data)

    def gen_hash( self , alg = sha1 ):
        uid = self.uid
        self.hash = alg(bytes(self.uid,encoding = "UTF-8"))

class Network:

    def __MOVE__( self, des ):
        if des >0:
            exist = self.cursor.next != None
        else :
            exist = self.cursor.previous != None

        while (des!=0 or exist):
            if des<=1:
                self.cursor = self.cursor.next
                des -=1
                exist = not (self.cursor.next==None)
            else:
                self.cursor = self.cursor.previous
                des +=1
                exist = not (self.cursor.previous==None)

    def __ADD__(self,data):
        for i in data:
            if self.cursor == None:
                self.cursor = block(self.collections,None,None,None,None,i)
            else:
                self.cursor.next = block(self.collections,self.cursor,None,None,None,i)
                self.cursor = self.cursor.next

    def __init__(self,*datas):
        self.collections = 0
        self.cursor = None

    def movl( self ):
        self.__MOVE__( 1 )

    def movr( self ):
        self.__MOVE__( -1 )

