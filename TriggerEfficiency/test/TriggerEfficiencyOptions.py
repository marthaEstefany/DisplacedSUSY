#!/usr/bin/env python

# to be run with submitToCondor.py -l protoBatchConfig.py

# import the definitions of all the datasets on the T3
from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.miniAODV2_76X_Samples import *

# specify which config file to pass to cmsRun
config_file = "TriggerEfficiency_cfg.py"

# choose luminosity used for MC normalization
intLumi = -1 # from 8 TeV MuEG dataset

# create list of datasets to process
datasets = [
    #'TTJets_DiLept',
    #'TTJets_Lept',
    #'MET_2015D',
    #'MuonEG_2015D'
    #'DisplacedSUSYSignal',
    'stop200_1mm',
    'stop200_10mm',
    'stop200_100mm',
    'stop200_1000mm',
    'stop500_1mm',
    'stop500_10mm',
    'stop500_100mm',
    'stop500_1000mm',
    'stop800_1mm',
    'stop800_10mm',
    'stop800_100mm',
    'stop800_1000mm',
]

InputCondorArguments = {'hold':'true','request_memory':'2048MB'}
