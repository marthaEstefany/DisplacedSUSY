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
    #'root://cmsxrootd.fnal.gov//store/mc/RunIISpring15DR74/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v3/10000/009D49A5-7314-E511-84EF-0025905A605E.root',
    'file:/data/users/bing/condor/EMuSkimJan14th/stop200_1mm/EMuSkimSelection/skim_1.root'
)
)


# output histogram file name when running interactively
process.TFileService = cms.Service ('TFileService',
    fileName = cms.string ('hist.root')
)

# number of events to process when running interactively
process.maxEvents = cms.untracked.PSet (
    input = cms.untracked.int32 (1000)
)

################################################################################
##### Set up the 'collections' map #############################################
################################################################################
miniAOD_collections = cms.PSet (
  electrons       =  cms.InputTag  ('slimmedElectrons',''),
  genjets         =  cms.InputTag  ('slimmedGenJets',                 ''),
  jets            =  cms.InputTag  ('slimmedJets',                    ''),
  bjets           =  cms.InputTag  ('slimmedJets',                    ''),
  generatorweights= cms.InputTag  ('generator', ''), 
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
variableProducers.append('DisplacedSUSYEventVariableProducer')

weights = cms.VPSet (
    cms.PSet (
        inputCollections = cms.vstring("eventvariables"),
        inputVariable = cms.string("puScalingFactor")
    ),
    cms.PSet (
        inputCollections = cms.vstring("eventvariables"),
        inputVariable = cms.string("triggerScalingFactor")
    ),
    cms.PSet (
        inputCollections = cms.vstring("eventvariables"),
        inputVariable = cms.string("electronScalingFactor")
    ),
    cms.PSet (
        inputCollections = cms.vstring("eventvariables"),
        inputVariable = cms.string("muonScalingFactor")
    ),
)

scalingfactorproducers = []
ObjectScalingFactorProducer = {}
ObjectScalingFactorProducer['name'] = 'ObjectScalingFactorProducer'
ObjectScalingFactorProducer['muonFile'] = cms.string(os.environ['CMSSW_BASE'] + '/src/OSUT3Analysis/AnaTools/data/muonSF.root')
ObjectScalingFactorProducer['electronFile'] = cms.string(os.environ['CMSSW_BASE'] + '/src/OSUT3Analysis/AnaTools/data/electronSF.root')
ObjectScalingFactorProducer['muonWp'] = cms.string('TightID;1')
ObjectScalingFactorProducer['electronWp'] = cms.string('GlobalSF')
ObjectScalingFactorProducer['doEleSF'] = cms.bool(True)
ObjectScalingFactorProducer['doMuSF'] = cms.bool(True)

scalingfactorproducers.append(ObjectScalingFactorProducer)
################################################################################
##### Import the channels to be run ############################################
################################################################################


from DisplacedSUSY.StandardAnalysis.SignalRegionSelection import *
eventSelections = []
eventSelections.append(SignalRegionSelectionNoIsoNoOSInclusiveDisplacedTrigger)
eventSelections.append(SignalRegionSelectionNoIsoInclusiveDisplacedTrigger)
eventSelections.append(SignalRegionSelectionNoOSInclusiveDisplacedTrigger)
eventSelections.append(SignalRegionSelectionInclusiveDisplacedTrigger)

################################################################################
##### Import the histograms to be plotted ######################################
################################################################################
from OSUT3Analysis.Configuration.histogramDefinitions import *
from DisplacedSUSY.Configuration.histogramDefinitions import ElectronD0Histograms,MuonD0Histograms,ElectronMuonD0Histograms
from DisplacedSUSY.StandardAnalysis.HistogramsDefinitions import eventHistograms
################################################################################
##### Attach the channels and histograms to the process ########################
################################################################################
histograms = cms.VPSet()
histograms.append(ElectronHistograms)
histograms.append(ElectronD0Histograms)
histograms.append(MuonHistograms)
histograms.append(MuonD0Histograms)
histograms.append(ElectronMuonD0Histograms)
histograms.append(ElectronMuonHistograms)
histograms.append(eventHistograms)

add_channels (process, eventSelections, histograms, weights, scalingfactorproducers, collections,variableProducers, False)

process.PUScalingFactorProducer.dataset = cms.string("MuonEG_2015D")
process.PUScalingFactorProducer.PU = cms.string(os.environ['CMSSW_BASE'] + '/src/DisplacedSUSY/StandardAnalysis/data/pu.root')
process.PUScalingFactorProducer.type = cms.string("bgMC")
#DisplacedSUSYEventVariableProducer can only run over skims.
process.DisplacedSUSYEventVariableProducer.type = cms.string("bgMC")
process.DisplacedSUSYEventVariableProducer.triggerPath = cms.string("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v")
process.DisplacedSUSYEventVariableProducer.triggerScalingFactor = cms.double(0.962)
#outfile = open('dumpedConfig.py','w'); print >> outfile,process.dumpPython(); outfile.close()
