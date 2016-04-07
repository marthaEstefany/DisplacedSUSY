#!/usr/bin/env python

# to be run with submitToCondor.py -l protoBatchConfig.py

# import the definitions of all the datasets on the T3
from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.miniAODV2_76X_Samples import *

# specify which config file to pass to cmsRun
config_file = "QCDElectronControlRegion_cfg.py"

# choose luminosity used for MC normalization
intLumi = 2613 # for 13 TeV Silver Json, 2015D 

# create list of datasets to process
datasets = [
    #'DoubleEG_2015D',
    'SingleEle_2015D',
    #'SinglePhoton_2015D',
    #'DYJetsToLL_50',
    #'WJetsToLNu',
    #'Diboson',
    #'SingleTop',
    #'TTJets_Lept',
    #'QCD_EMEnriched',
    #'QCD_bcToE',
]
InputCondorArguments = {'hold': 'true'}
