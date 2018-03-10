#!/usr/bin/env python

# import the definitions of all the datasets on the T3
from OSUT3Analysis.Configuration.configurationOptions import *
from DisplacedSUSY.Configuration.cmsswVersion import *
if (cmssw_version()[0]>8 and cmssw_version()[1]>-1):
    from DisplacedSUSY.Configuration.miniAODV2_94X_Samples import *
else:
    from DisplacedSUSY.Configuration.miniAODV2_80X_Samples import *


# specify which config file to pass to cmsRun
config_file = "MCRegions_cfg.py"

# choose luminosity used for MC normalization
intLumi = 27660 # from 2016BCDEFG Prompt reco golden json

systematics_file = "DisplacedSUSY.Configuration.systematicsDefinitions"
external_systematics_directory = "DisplacedSUSY/Configuration/data/"

# create list of datasets to process
datasets = [

    ### DY
    'DYJetsToLL_50',

    ### TTbar
    'TTJets_DiLept',

    ### QCD (mu-enriched is bigger)
    'QCD_MuEnriched',
]

InputCondorArguments = {}
