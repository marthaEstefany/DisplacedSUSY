#!/usr/bin/env python

from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.processingUtilities import *

config_file = "qcdPreselectionAnalyzer_cfg.py"

intLumi = 19754.  # 

datasets = [

####################
### data samples ###
####################

#    'MuEG_22Jan2013',
        


##########################
### background samples ###
##########################



#    'Wjets',

#    'Diboson',
    #    'WW',
    #    'WZ',
    #    'ZZ',

#    'DY',
    #    'DYToEE_20',
    #    'DYToMuMu_20',
    #    'DYToTauTau_20',

#    'SingleTop',

#    'TTbar',
    #    'TTbar_Had',
    #    'TTbar_SemiLep',
    ##    'TTbar_Lep',

    #    'Background',   


    'QCD_ElectronEnriched',
    'QCD_MuEnriched',

]


