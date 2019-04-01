#!/usr/bin/env python

samples = [
    'DYJetsToLL',
    'TTJets_Lept',
    'SingleTop',
    'Diboson',
    'QCD_EMEnriched',
]

# fit assumes composite samples have two components
composite_samples = {
    'Background' : ['NonQcdBackground', 'QCD_MuEnriched']
}

# specifify which channel will be used for each region of d = c * b / a
channels = {
    'a' : 'PromptLowPtControlRegion',
    'b' : 'DisplacedLowPtControlRegion',
    'c' : 'PromptHighPtControlRegion',
    'd' : 'DisplacedHighPtControlRegion',
}

input_hist = "Electron Plots/electronPt"
bin_edges = [0,65,70,75,80,85,90,95,100,150,200,250,500]
#bin_edges = [0,65,70,75,80,85,90,95,100,110,120,130,140,150,200,300,400,500]
component_model = "[0] + [1]/x" # |d0| resolution as a function of pT
composite_model = "[0] * ([1] + [2]/x) + (1 - [0]) * ([3] + [4]/x)"
fit_range = (65, 100)