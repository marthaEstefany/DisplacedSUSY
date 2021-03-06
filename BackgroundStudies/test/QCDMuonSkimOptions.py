#!/usr/bin/env python

# import the definitions of all the datasets on the T3
from OSUT3Analysis.Configuration.configurationOptions import *
from DisplacedSUSY.Configuration.miniAODV2_80X_Samples import *

# specify which config file to pass to cmsRun
config_file = "QCDMuonSkim_cfg.py"

# choose luminosity used for MC normalization
intLumi = 16146.2 # only for 2016G, H

# create list of datasets to process
datasets = [
    'WJetsToLNu',
    'Diboson',
    'DYJetsToLL',
    'SingleTop',
    'TTJets_Lept',
    'QCD_MuEnriched',
    'SingleMu_2016',
]

InputCondorArguments = {'request_memory':'2048MB'}
secondaryCollections ={}
