# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 03:34:57 2018

@author: karum
"""

# coding: utf-8
# 学生メソッドを作る

class Gakusei:
    def __init__(self, kokugo, sansu):
        self.kokugo = kokugo
        self.sansu  = sansu
    
    def sum(self):
        return self.kokugo + self.sansu

    # この下に、合計得点を戻り値として返すsumメソッドを記述する

yamada = Gakusei(70, 43)
print("合計は" + str(yamada.sum()) + "点です")