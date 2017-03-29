#!/usr/bin/env python

# import the definitions of all the datasets on the T3
from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.miniAODV2_80X_Samples import *

# specify which config file to pass to cmsRun
config_file = "EMuSkim_cfg.py"

systematics_file = "DisplacedSUSY.Configuration.systematicsDefinitions"
external_systematics_directory = "DisplacedSUSY/Configuration/data/"

# choose luminosity used for MC normalization
intLumi = 12900 # don't know yet...

# create list of datasets to process
datasets = [

    # DY
    'DYJetsToLL_50',

    # TTbar
    'TTJets_DiLept',

    # tW
#    'SingleTop_tbarW',

    # Diboson
#    'WWToLNuLNu',
#    'ZZToLLNuNu',
#    'ZG',

    # QCD (mu-enriched is bigger)
    'QCD_MuEnriched',

    # Data
    'MuonEG_2016_23Sep',
    
    

]

InputCondorArguments = {}