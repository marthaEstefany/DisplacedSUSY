#!/usr/bin/env python

# input info - be careful if running over preselection data while still blinded
input_file = "/uscms_data/d3/cardwell/condor/mumu_closureTests_07Dec2020/Background_2016.root"
#input_file = "/uscms_data/d3/cardwell/condor/mumu_closureTests_07Dec2020/Background_2017_2018.root"
#input_file = "/uscms_data/d3/cardwell/condor/mumu_closureTests_07Dec2020/DoubleMu_2016_postHIP.root"
#input_file = "/uscms_data/d3/cardwell/condor/mumu_closureTests_07Dec2020/DoubleMu_2017_2018.root"
#input_file = "/uscms_data/d3/cardwell/condor/MuMuPreselectionOneBJet_2018Analysis_21Jan2021/DoubleMu_2018.root"

input_hist = "PreselectionPlotter/Muon-beamspot Plots/muonAbsD0[0]_vs_muonAbsD0[1]_100000um_vs_muonPt[0]"
#input_hist = "PreselectionOneBJetPlotter/Muon-beamspot Plots/muonAbsD0[0]_vs_muonAbsD0[1]_100000um_vs_muonPt[0]"

# Is the sample data? This affects how the poisson uncertainty is calculated
data = False
# Was the histogram constructed with TH2(name,title,nbinsx,xbins,nbinsy,ybins)
variable_bins = True
# Specify fit function for extrapolation. Currently supported functions are pol0, pol1, and expo
fit_func = "pol1"

# uncertainty info
# mutliplicative correction to the most-prompt signal region estimate to account for correlation
prompt_sys = None # needed for closure tests
#prompt_sys = { # from elogs 1852 and 1854
    ## 2016 MC
    #'val'    : 2.03,
    #'err_hi' : 0.80,
    #'err_lo' : 0.80,
    ## 2017+18 MC
    #'val'    : 7.77,
    #'err_hi' : 3.68,
    #'err_lo' : 3.68,
    ## 2016 data
    #'val'    : 2.51,
    #'err_hi' : 0.87,
    #'err_lo' : 0.87,
    ## 2017+18 data
    #'val'    : 4.20,
    #'err_hi' : 1.51,
    #'err_lo' : 1.51,
#}
# multiplicative correction to more-displaced signal region estimates
# we generally set the central value to 1.00 and use the uncertainty as a systematic
displaced_sys = None # needed for closure tests
#displaced_sys = { # from elog 1860
    ## 2016
    #'val'    : 1.00, # should be 1.00 for most use cases
    #'err_hi' : 0.64,
    #'err_lo' : 0.64,
    ## 2017+18
    #'val'    : 1.00, # should be 1.00 for most use cases
    #'err_hi' : 1.40,
    #'err_lo' : 1.00,
#}

# output info
#output_file  = "mumu_bgMC_2016_signalRegion.root"
#output_file  = "mumu_bgMC_2017_2018_signalRegion.root"
output_file  = "mumu_bgMC_2016_promptRegion.root"
#output_file  = "mumu_bgMC_2017_2018_promptRegion.root"
#output_file  = "mumu_bgMC_2016_displacedLeading.root"
#output_file  = "mumu_bgMC_2017_2018_displacedSubleading.root"
#output_file  = "mumu_bgMC_2016_displacedLeading500um.root"
#output_file  = "mumu_bgMC_2017_2018_displacedSubleading500um.root"
#output_file  = "mumu_data_2016_signalRegion.root"
#output_file  = "mumu_data_2017_2018_signalRegion.root"
#output_file  = "mumu_data_2016_promptRegion.root"
#output_file  = "mumu_data_2017_2018_promptRegion.root"
#output_file  = "mumu_data_2016_displacedLeading.root"
#output_file  = "mumu_data_2017_2018_displacedSubleading.root"
#output_file  = "mumu_data_2016_displacedLeading500um.root"
#output_file  = "mumu_data_2017_2018_displacedSubleading500um.root"
#output_file  = "mumu_data_oneBJet_2018_signalRegion.root"

# region definitions
# set last bin to -1 on any axis to include overflow along that axis
# bin edges must line up with bin edges in input histograms
# be careful not to accidently unblind if running over preselection data

# actual signal regions (don't unblind!)
#bins_x = [0, 100, 500, 100000]
#bins_y = [0, 100, 500, 100000]
#bins_z = [0, -1]

# prompt-sub mu/prompt-lead mu region
bins_x = [20, 50, 100]
bins_y = [20, 50, 100]
bins_z = [0, -1]

# displaced-leading-mu/prompt-subleading-mu region, 100 um to 500 um
#bins_x = [20, 100, 500]
#bins_y = [20, 30, 40, 50, 60, 70, 80, 90, 100]
#bins_z = [0, -1]

# displaced-leading-mu/prompt-subleading-mu region, 500 um to 10 cm
#bins_x = [20, 100, 500, 100000]
#bins_y = [20, 30, 100]
#bins_z = [0, -1]

# prompt-leading-mu/displaced-subleading-mu region, 100 um to 500 um
#bins_x = [20, 30, 40, 50, 60, 70, 80, 90, 100]
#bins_y = [20, 100, 500]
#bins_z = [0, -1]

# prompt-leading-mu/displaced-subleading-mu region, 500 um to 10 cm
#bins_x = [20, 30, 100]
#bins_y = [20, 100, 500, 100000]
#bins_z = [0, -1]
