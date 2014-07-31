#!/usr/bin/env python
#sdataset='allSample'
sdataset='ToBeSet'
scondor_dir='modelTesting_check'

input_histograms = [
    { 'condor_dir' : scondor_dir,
      'dataset' : sdataset,
      'channel_numerator' : 'SignalGenMatching_KynCuts_CrossCuts_oneRecoMu',
      'channel_denominator' : 'SignalGenMatching_KynCuts_CrossCuts',
      'name' : 'secondaryMcparticleAbsD0Beamspot',
      'legend_entry' : 'Muon_cuts',
      'color': 1,
    },
]