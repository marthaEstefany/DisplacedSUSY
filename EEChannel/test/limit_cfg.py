#!/usr/bin/env python
from DisplacedSUSY.Configuration.limitOptions import *

blinded = True # sets observed events equal to bg estimate

# full run 2 background estimates are loaded from a json that also defines the signal regions
background = {
    'name' : 'bg_estimate',
    'dir'  : 'EEPreselection_FullAnalysis_3Dhists_30July2019',
    'file' : 'standard_background_estimate.json',
}

# fixme: populate fields with full run2 unblinded results when we're ready to unblind
data = {
    'name' : '',
    'dir'  : '',
    'file' : '',
    'hist' : '',
}

# fixme: temporary fudge factor to scale 2018 signal yield to Run II signal yield
lumi_factor = 117.6/59.7

processes = ['stopToLB']
masses = [m for m in range(200, 1801, 100)]
#lifetimes = [10**e for e in range(-1, 4)]
lifetimes = [b*10**e for e in range(-1, 3) for b in range(1, 10)] + [1000]
signal_points = ["{}{}_{}mm".format(p, m, l) for p in processes for m in masses for l in lifetimes]

# a separate datacard will be produced for each signal point
if arguments.era == "2016":
    signal = {
        'name' : '', # will be automatically generated for each signal point
        'dir'  : 'EEPreselection_2018Analysis_Signal_15Aug2019',
        'file' : '', # will be automatically generated for each signal point
        'hist' : 'PreselectionPlotter/Electron-beamspot Plots/electronAbsD0[0]_vs_electronAbsD0[1]_2000um_vs_electronPt[0]',
    }
elif arguments.era == "2017":
    signal = {
        'name' : '', # will be automatically generated for each signal point
        'dir'  : 'EEPreselection_2018Analysis_Signal_15Aug2019',
        'file' : '', # will be automatically generated for each signal point
        'hist' : 'PreselectionPlotter/Electron-beamspot Plots/electronAbsD0[0]_vs_electronAbsD0[1]_2000um_vs_electronPt[0]',
    }
elif arguments.era == "2018":
    signal = {
        'name' : '', # will be automatically generated for each signal point
        'dir'  : 'EEPreselection_2018Analysis_Signal_15Aug2019',
        'file' : '', # will be automatically generated for each signal point
        'hist' : 'PreselectionPlotter/Electron-beamspot Plots/electronAbsD0[0]_vs_electronAbsD0[1]_2000um_vs_electronPt[0]',
    }
