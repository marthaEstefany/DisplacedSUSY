 #!/usr/bin/env python

############################################################################################################
#########  LIST OF MINIAOD V2 DATASETS  ####################################################################
############################################################################################################

dataset_names = {
    #DY
    'DYJetsToLL_50'     : ['/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAOD-RECOSIMstep_94X_mc2017_realistic_v10-v1/MINIAODSIM', # 48M
                           '/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAOD-RECOSIMstep_94X_mc2017_realistic_v10_ext1-v1/MINIAODSIM'], # 49M
    'DYJetsToLL_10to50' : '/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v2/MINIAODSIM', # 39M

    #DYBBJets
    'DYBBJetsToLL' : '/DYBBJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAOD-PU2017_94X_mc2017_realistic_v11-v1/MINIAODSIM', # 3M

    #WJets
    #'WJetsToLNu' : #doesn't exist for 2017 MC yet

    #WW
    'WWToLNuLNu' : '/WWTo2L2Nu_NNPDF31_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM', #2M
    'WWToLNuQQ'  : '/WWToLNuQQ_NNPDF31_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAOD-PU2017_94X_mc2017_realistic_v11_ext1-v1/MINIAODSIM', #9M

    #WZ
    #'WZToLNu2QorQQ2L' : #doesn't exist for 2017 MC yet
    #'WZToLNuNuNu'     : #doesn't exist for 2017 MC yet
    'WZToLLLNu'       : '/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v2/MINIAODSIM',#11M

    #ZZ
    #'ZZToNuNuQQ' : #doesn't exist for 2017 MC yet
    #'ZZToLLQQ'   : #doesn't exist for 2017 MC yet
    'ZZToLLNuNu' : '/ZZTo2L2Nu_13TeV_powheg_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM', #8M
    'ZZToLLLL'   : ['/ZZTo4L_13TeV_powheg_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v2/MINIAODSIM', #7M
                    '/ZZTo4L_13TeV_powheg_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10_ext1-v1/MINIAODSIM' #96M
                    ],

    #VG
    #'WG' : #doesn't exist for 2017 MC yet
    #'ZG' : #doesn't exist for 2017 MC yet

    #SingleTop
    'SingleTop_s_channel'         : '/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM', #9M
    'SingleTop_t_channel_top'     : '/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM', # 6M
    'SingleTop_t_channel_antitop' : '/ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM', #4M
    'SingleTop_tbarW'             : ['/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10_ext1-v1/MINIAODSIM',#6M
                                     '/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM' #5M
                                     ],
    'SingleTop_tW'                : '/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM', #5M

    #TTJets
    #'TTJets_DiLept'             : 
    #'TTJets_SingleLeptFromT'    : 
    #'TTJets_SingleLeptFromTbar' : 

#    #QCD MuEnriched
    #'QCD_MuEnriched_15to20'    : 
    #'QCD_MuEnriched_20to30'    : 
    #'QCD_MuEnriched_30to50'    : 
    #'QCD_MuEnriched_50to80'    : 
    #'QCD_MuEnriched_80to120'   : 
    #'QCD_MuEnriched_120to170'  : 
    #'QCD_MuEnriched_170to300'  : 
    #'QCD_MuEnriched_300to470'  : 
    #'QCD_MuEnriched_470to600'  : 
    #'QCD_MuEnriched_600to800'  : 
    #'QCD_MuEnriched_800to1000' : 
    #'QCD_MuEnriched_1000toInf' : 

#    #QCD EMEnriched
    #'QCD_EMEnriched_20to30'   : 
    #'QCD_EMEnriched_30to50'   : 
    #'QCD_EMEnriched_50to80'   : 
    #'QCD_EMEnriched_80to120'  : 
    #'QCD_EMEnriched_120to170' : 
    #'QCD_EMEnriched_170to300' : 
    #'QCD_EMEnriched_300toInf' : 

#    #QCD bcToE
    #'QCD_bcToE_15to20'   : 
    #'QCD_bcToE_20to30'   : 
    #'QCD_bcToE_30to80'   : 
    #'QCD_bcToE_80to170'  : 
    #'QCD_bcToE_170to250' : 
    #'QCD_bcToE_250toInf' : 

    ############################################################################

    ############################################################################
    # MuonEG 2017, 17Nov2017 rereco
    'MuonEG_2017B' : '/MuonEG/Run2017B-17Nov2017-v1/MINIAOD',
    'MuonEG_2017C' : '/MuonEG/Run2017C-17Nov2017-v1/MINIAOD',
    'MuonEG_2017D' : '/MuonEG/Run2017D-17Nov2017-v1/MINIAOD',
    'MuonEG_2017E' : '/MuonEG/Run2017E-17Nov2017-v1/MINIAOD',
    'MuonEG_2017F' : '/MuonEG/Run2017F-17Nov2017-v1/MINIAOD',
    ############################################################################

    ############################################################################
    # DoubleMuon 2017, 17Nov2017 rereco
    'DoubleMu_2017B' : '/DoubleMuon/Run2017B-17Nov2017-v1/MINIAOD',
    'DoubleMu_2017C' : '/DoubleMuon/Run2017C-17Nov2017-v1/MINIAOD',
    'DoubleMu_2017D' : '/DoubleMuon/Run2017D-17Nov2017-v1/MINIAOD',
    'DoubleMu_2017E' : '/DoubleMuon/Run2017E-17Nov2017-v1/MINIAOD',
    'DoubleMu_2017F' : '/DoubleMuon/Run2017F-17Nov2017-v1/MINIAOD',
    ############################################################################

    ############################################################################
    # DoubleEG 2017, 17Nov2017 rereco
    'DoubleEG_2017B' : '/DoubleEG/Run2017B-17Nov2017-v1/MINIAOD',
    'DoubleEG_2017C' : '/DoubleEG/Run2017C-17Nov2017-v1/MINIAOD',
    'DoubleEG_2017D' : '/DoubleEG/Run2017D-17Nov2017-v1/MINIAOD',
    'DoubleEG_2017E' : '/DoubleEG/Run2017E-17Nov2017-v1/MINIAOD',
    'DoubleEG_2017F' : '/DoubleEG/Run2017F-17Nov2017-v1/MINIAOD',
    ############################################################################

    ############################################################################
    # MET 2017, 17Nov2017 rereco
    'MET_2017B' : '/MET/Run2017B-17Nov2017-v1/MINIAOD',
    'MET_2017C' : '/MET/Run2017C-17Nov2017-v1/MINIAOD',
    'MET_2017D' : '/MET/Run2017D-17Nov2017-v1/MINIAOD',
    'MET_2017E' : '/MET/Run2017E-17Nov2017-v1/MINIAOD',
    'MET_2017F' : '/MET/Run2017F-17Nov2017-v1/MINIAOD',
    ############################################################################

    ############################################################################
    # JetHT 2017, 17Nov2017 rereco
    'JetHT_2017B' : '/JetHT/Run2017B-17Nov2017-v1/MINIAOD',
    'JetHT_2017C' : '/JetHT/Run2017C-17Nov2017-v1/MINIAOD',
    'JetHT_2017D' : '/JetHT/Run2017D-17Nov2017-v1/MINIAOD',
    'JetHT_2017E' : '/JetHT/Run2017E-17Nov2017-v1/MINIAOD',
    'JetHT_2017F' : '/JetHT/Run2017F-17Nov2017-v1/MINIAOD',
    ############################################################################

}
