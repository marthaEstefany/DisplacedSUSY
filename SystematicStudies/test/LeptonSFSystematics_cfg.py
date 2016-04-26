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
      'file:/data/users/bing/condor/EMuSkim76XSignal/stop200_1000mm/EMuSkimSelection/skim_1.root',
#    'root://cms-xrd-global.cern.ch//store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2_ext1-v1/10000/0036F7A6-CC6D-E511-8B5B-002590D60150.root',
#  )
))
#set_input(process, "/data/users/bing/condor/EMuSkim76X/DYJetsToLL_50/EMuSkimSelection/")

# output histogram file name when running interactively
process.TFileService = cms.Service ('TFileService',
    fileName = cms.string ('hist.root')
)

# number of events to process when running interactively
process.maxEvents = cms.untracked.PSet (
    input = cms.untracked.int32 (10000)
)

################################################################################
##### Set up the 'collections' map #############################################
################################################################################

# this PSet specifies which collections to get from the input files
miniAOD_collections = cms.PSet (
  electrons       =  cms.InputTag  ('slimmedElectrons',''),
  genjets         =  cms.InputTag  ('slimmedGenJets',                 ''),
  jets            =  cms.InputTag  ('slimmedJets',                    ''),
  bjets           =  cms.InputTag  ('slimmedJets',                    ''),
  generatorweights=  cms.InputTag  ('generator', ''),
  mcparticles     =  cms.InputTag  ('packedGenParticles',             ''),
  mets            =  cms.InputTag  ('slimmedMETs',                    ''),
  muons           =  cms.InputTag  ('slimmedMuons',                   ''),
  hardInteractionMcparticles  =  cms.InputTag  ('prunedGenParticles',             ''),
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
variableProducers.append('DisplacedSUSYEventVariableProducer')
variableProducers.append('PUScalingFactorProducer')
variableProducers.append('LifetimeWeightProducer')

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
    cms.PSet (
        inputCollections = cms.vstring("eventvariables"),
        inputVariable = cms.string("lifetimeWeight")
    ),
)

################################################################################
##### Set up any user-defined scale factor producers ###########################
################################################################################

DefaultSFProducer = {}
DefaultSFProducer['name'] = 'ObjectScalingFactorProducer'
DefaultSFProducer['muonFile'] = cms.string(os.environ['CMSSW_BASE'] + '/src/OSUT3Analysis/AnaTools/data/muonSF.root')
DefaultSFProducer['electronFile'] = cms.string(os.environ['CMSSW_BASE'] + '/src/OSUT3Analysis/AnaTools/data/electronSF.root')
DefaultSFProducer['doEleSF'] = cms.bool(True)
DefaultSFProducer['doMuSF'] = cms.bool(True)
DefaultSFProducer['muonWp'] = cms.string('TightID')
DefaultSFProducer['electronWp'] = cms.string('TightID')

################################################################################

MuUpSFProducer = copy.deepcopy(DefaultSFProducer)
MuUpSFProducer['muonWp'] = cms.string('TightID_up')

MuDownSFProducer = copy.deepcopy(DefaultSFProducer)
MuDownSFProducer['muonWp'] = cms.string('TightID_down')

################################################################################

EleUpSFProducer = copy.deepcopy(DefaultSFProducer)
EleUpSFProducer['electronWp'] = cms.string('TightID_up')

EleDownSFProducer = copy.deepcopy(DefaultSFProducer)
EleDownSFProducer['electronWp'] = cms.string('TightID_down')

################################################################################
##### Import the channels to be run ############################################
################################################################################

from DisplacedSUSY.SystematicStudies.LeptonSFSelections import *

################################################################################

MuUp = copy.deepcopy(CentralValue)
MuUp.name = cms.string("MuUp")
MuDown = copy.deepcopy(CentralValue)
MuDown.name = cms.string("MuDown")
EleUp = copy.deepcopy(CentralValue)
EleUp.name = cms.string("EleUp")
EleDown = copy.deepcopy(CentralValue)
EleDown.name = cms.string("EleDown")

################################################################################

MuUp50um = copy.deepcopy(CentralValue50um)
MuUp50um.name = cms.string("MuUp50um")
MuDown50um = copy.deepcopy(CentralValue50um)
MuDown50um.name = cms.string("MuDown50um")
EleUp50um = copy.deepcopy(CentralValue50um)
EleUp50um.name = cms.string("EleUp50um")
EleDown50um = copy.deepcopy(CentralValue50um)
EleDown50um.name = cms.string("EleDown50um")

################################################################################

MuUp100um = copy.deepcopy(CentralValue100um)
MuUp100um.name = cms.string("MuUp100um")
MuDown100um = copy.deepcopy(CentralValue100um)
MuDown100um.name = cms.string("MuDown100um")
EleUp100um = copy.deepcopy(CentralValue100um)
EleUp100um.name = cms.string("EleUp100um")
EleDown100um = copy.deepcopy(CentralValue100um)
EleDown100um.name = cms.string("EleDown100um")

################################################################################
##### Attach the channels and histograms to the process ########################
################################################################################

histograms = cms.VPSet()
from DisplacedSUSY.StandardAnalysis.HistogramsDefinitions import eventHistograms

histograms.append(eventHistograms)

add_channels (process, [CentralValue], histograms, weights, [DefaultSFProducer], collections, variableProducers, False)
add_channels (process, [MuUp], histograms, weights, [MuUpSFProducer], collections, variableProducers, False)
add_channels (process, [MuDown], histograms, weights, [MuDownSFProducer], collections, variableProducers, False)
add_channels (process, [EleUp], histograms, weights, [EleUpSFProducer], collections, variableProducers, False)
add_channels (process, [EleDown], histograms, weights, [EleDownSFProducer], collections, variableProducers, False)

#add_channels (process, [CentralValue50um], histograms, weights, [DefaultSFProducer], collections, variableProducers, False)
#add_channels (process, [MuUp50um], histograms, weights, [MuUpSFProducer], collections, variableProducers, False)
#add_channels (process, [MuDown50um], histograms, weights, [MuDownSFProducer], collections, variableProducers, False)
#add_channels (process, [EleUp50um], histograms, weights, [EleUpSFProducer], collections, variableProducers, False)
#add_channels (process, [EleDown50um], histograms, weights, [EleDownSFProducer], collections, variableProducers, False)

#add_channels (process, [CentralValue100um], histograms, weights, [DefaultSFProducer], collections, variableProducers, False)
#add_channels (process, [MuUp100um], histograms, weights, [MuUpSFProducer], collections, variableProducers, False)
#add_channels (process, [MuDown100um], histograms, weights, [MuDownSFProducer], collections, variableProducers, False)
#add_channels (process, [EleUp100um], histograms, weights, [EleUpSFProducer], collections, variableProducers, False)
#add_channels (process, [EleDown100um], histograms, weights, [EleDownSFProducer], collections, variableProducers, False)


process.PUScalingFactorProducer.dataset = cms.string("TTJets_DiLept")
process.PUScalingFactorProducer.PU = cms.string(os.environ['CMSSW_BASE'] + '/src/DisplacedSUSY/StandardAnalysis/data/pu.root')
process.PUScalingFactorProducer.type = cms.string("bgMC")
process.PUScalingFactorProducer.target = cms.string("MuonEG_2015D")
#DisplacedSUSYEventVariableProducer can only run over skims.
process.DisplacedSUSYEventVariableProducer.type = cms.string("bgMC")
process.DisplacedSUSYEventVariableProducer.triggerPath = cms.string("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v")
process.DisplacedSUSYEventVariableProducer.triggerScalingFactor = cms.double(0.975)

#outfile = open('dumpedConfig.py','w'); print >> outfile,process.dumpPython(); outfile.close()
