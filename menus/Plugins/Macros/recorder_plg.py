# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 23:24:43 2016

@author: yxl
"""

from core.engines import Free
from ui.macroseditor import MacrosEditor
from core.managers import TextLogManager
import IPy, wx

class Recorder(Free):
    title = 'Macros Recorder'
    
    def run(self, para = None):
        if TextLogManager.get('Recorder')==None:
            f = lambda : MacrosEditor('Recorder').Show()
            wx.CallAfter(f)
            
class Edite(Free):
    title = 'Macros Editor'
    
    def run(self, para = None):
        f = lambda : MacrosEditor(TextLogManager.name('Macros Editor')).Show()
        wx.CallAfter(f)
        
class Run(Free):
    title = 'Run Macros'
    para = {'path':''}
    
    def show(self):
        filt = 'Macros files (*.mc)|*.mc'
        return IPy.getpath('open..', filt, self.para)
        
    def run(self, para = None):
        f = open(para['path'])
        lines = f.readlines()
        f.close()
        IPy.run_macros(lines)

plgs = [Recorder, Edite, Run]