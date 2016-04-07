import FWCore.ParameterSet.Config as cms
from OSUT3Analysis.Configuration.processingUtilities import *
import math
import os

################################################################################
##### Set up the 'process' object ##############################################
################################################################################

process = cms.Process ('OSUAnalysis')

# how often to print a log message
process.load ('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 100
process.source = cms.Source ('PoolSource',
  fileNames = cms.untracked.vstring (
    #'root://cms-xrd-global.cern.ch//store/mc/RunIIFall15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12_ext1-v1/00000/18C19294-83BC-E511-9850-002590C192A8.root',
    'file:/data/users/bing/condor/QCDElectronSkim76XWithPatCand/SingleEle_2015D/QCDElectronSkim/skim_2.root'
   )
)


#set_input(process, "/data/users/bing/condor/EMuSkim13TeV/TTJets_DiLept_MiniAOD/EMuSKim13TeV/")

# output histogram file name when running interactively
process.TFileService = cms.Service ('TFileService',
    fileName = cms.string ('hist.root')
)

# number of events to process when running interactively
process.maxEvents = cms.untracked.PSet (
    input = cms.untracked.int32 (-1)
)

################################################################################
##### Set up the 'collections' map #############################################
################################################################################

# this PSet specifies which collections to get from the input files
miniAOD_collections = cms.PSet (
  electrons       =  cms.InputTag  ('objectSelector0','originalFormat','OSUAnalysisQCDElectronSkim1459725264'),
  genjets         =  cms.InputTag  ('slimmedGenJets',                 ''),
  jets            =  cms.InputTag  ('objectSelector1','originalFormat','OSUAnalysisQCDElectronSkim1459725264'),
  bjets           =  cms.InputTag  ('objectSelector1','originalFormat','OSUAnalysisQCDElectronSkim1459725264'),
  generatorweights=  cms.InputTag  ('generator', ''), 
  mcparticles     =  cms.InputTag  ('packedGenParticles',             ''),
  mets            =  cms.InputTag  ('slimmedMETs',                    ''),
  muons           =  cms.InputTag  ('slimmedMuons',                   ''),
  photons         =  cms.InputTag  ('slimmedPhotons',                 ''),
  primaryvertexs  =  cms.InputTag  ('offlineSlimmedPrimaryVertices',  ''),
  pileupinfos     =  cms.InputTag  ('slimmedAddPileupInfo',  ''),
  beamspots       =  cms.InputTag  ('offlineBeamSpot',                ''),
  superclusters   =  cms.InputTag  ('reducedEgamma',                  'reducedSuperClusters'),
  taus            =  cms.InputTag  ('slimmedTaus',                    ''),
  triggers        =  cms.InputTag  ('TriggerResults',                 '',  'HLT'),
  trigobjs        =  cms.InputTag  ('selectedPatTrigger',             ''),
)

collections = miniAOD_collections

################################################################################
##### Set up any user-defined variable producers ###############################
################################################################################


variableProducers = []
variableProducers.append('PUScalingFactorProducer')

weights = cms.VPSet (
    cms.PSet (
        inputCollections = cms.vstring("eventvariables"),
        inputVariable = cms.string("puScalingFactor")
    ),
    #cms.PSet (
    #    inputCollections = cms.vstring("eventvariables"),
    #    inputVariable = cms.string("electronScalingFactor")
    #),
)

scalingfactorproducers = []
#ObjectScalingFactorProducer = {}
#ObjectScalingFactorProducer['name'] = 'ObjectScalingFactorProducer'
#ObjectScalingFactorProducer['muonFile'] = cms.string(os.environ['CMSSW_BASE'] + '/src/OSUT3Analysis/AnaTools/data/muonSF.root')
#ObjectScalingFactorProducer['electronFile'] = cms.string(os.environ['CMSSW_BASE'] + '/src/OSUT3Analysis/AnaTools/data/electronSF.root')
#ObjectScalingFactorProducer['muonWp'] = cms.string('NUM_TightIDandIPCut_DEN_genTracks_PAR_pt_spliteta_bin1/abseta_vs_pt')
#ObjectScalingFactorProducer['electronWp'] = cms.string('GlobalSF')
#ObjectScalingFactorProducer['doEleSF'] = cms.bool(True)
#ObjectScalingFactorProducer['doMuSF'] = cms.bool(False)

#scalingfactorproducers.append(ObjectScalingFactorProducer)
################################################################################
##### Import the channels to be run ############################################
################################################################################

from DisplacedSUSY.BackgroundStudies.QCDControlRegions import *

eventSelections = []
eventSelections.append(QCDElectronNoIsoDisplacedControlRegion)
eventSelections.append(QCDElectronDisplacedControlRegion)
eventSelections.append(QCDElectronIsoControlRegion)

################################################################################
##### Import the histograms to be plotted ######################################
################################################################################

from OSUT3Analysis.Configuration.histogramDefinitions import *
from DisplacedSUSY.Configuration.histogramDefinitions import ElectronD0Histograms
from DisplacedSUSY.StandardAnalysis.HistogramsDefinitions import eventHistograms

histograms = cms.VPSet()
histograms.append(ElectronHistograms)
histograms.append(ElectronIPHistograms)
histograms.append(ElectronD0Histograms)
histograms.append(MetHistograms)
histograms.append(JetHistograms)
histograms.append(BjetHistograms)
histograms.append(JetBjetHistograms)
histograms.append(ElectronJetHistograms)
histograms.append(ElectronMetHistograms)
histograms.append(ElectronBjetHistograms)
histograms.append(eventHistograms)

################################################################################
##### Attach the channels and histograms to the process ########################
################################################################################

add_channels (process, eventSelections, histograms, weights, scalingfactorproducers, collections, variableProducers, False)

process.PUScalingFactorProducer.dataset = cms.string("QCD_EMEnriched_170to300")
process.PUScalingFactorProducer.target = cms.string("MuonEG_2015D")
process.PUScalingFactorProducer.PU = cms.string(os.environ['CMSSW_BASE'] + '/src/DisplacedSUSY/StandardAnalysis/data/pu.root')
process.PUScalingFactorProducer.type = cms.string("data")

#outfile = open('dumpedConfig.py','w'); print >> outfile,process.dumpPython(); outfile.close()
