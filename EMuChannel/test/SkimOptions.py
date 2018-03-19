#!/usr/bin/env python
import os
from DisplacedSUSY.StandardAnalysis.Options import *

# specify which config file to pass to cmsRun
config_file = "Skim_cfg.py"

# create list of datasets to process
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    datasets = [
        'MuonEG_2016',
        ]
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    datasets = [
        'MuonEG_2017'
        ]
