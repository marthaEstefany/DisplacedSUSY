import FWCore.ParameterSet.Config as cms
from OSUT3Analysis.Configuration.processingUtilities import *
import OSUT3Analysis.DBTools.osusub_cfg as osusub
from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.LifetimeWeightProducer_cff import *

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
    'root://cmsxrootd.fnal.gov//store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2/120000/02A210D6-F5C3-E611-B570-008CFA197BD4.root',
    #'root://cmsxrootd.fnal.gov//store/mc/RunIISpring16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14_ext1-v1/80000/4EF9F71C-0057-E611-A3FF-002590A831AA.root'
    #'root://cmsxrootd.fnal.gov//store/mc/RunIISpring16MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v4/00000/7AADCC01-EC2B-E611-886E-02163E013F02.root'
    #'root://cmsxrootd.fnal.gov//store/data/Run2016G/DoubleEG/MINIAOD/23Sep2016-v1/100000/0608426D-3F8E-E611-A52D-00237DF28460.root',
    #'file:condor/EE_Preselection_17_05_04/DYJetsToLL_50/Preselection/skim_0.root',
  )
)

# output histogram file name when running interactively
process.TFileService = cms.Service ('TFileService',
    fileName = cms.string ('hist.root')
)

# suppress gen-matching errors
process.load ('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.categories.append ("osu_GenMatchable")
process.MessageLogger.cerr.osu_GenMatchable = cms.untracked.PSet(
    limit = cms.untracked.int32 (0)
)

# number of events to process when running interactively
process.maxEvents = cms.untracked.PSet (
    input = cms.untracked.int32 (1000)
)

data_global_tag = '80X_dataRun2_2016SeptRepro_v3'
mc_global_tag = '80X_mcRun2_asymptotic_2016_miniAODv2_v1'

process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, mc_global_tag, '')
if osusub.batchMode and (osusub.datasetLabel in types) and (types[osusub.datasetLabel] == "data"):
    print "using global tag " + data_global_tag + "..."
    process.GlobalTag = GlobalTag(process.GlobalTag, data_global_tag, '')
else:
    print "using global tag " + mc_global_tag + "..."


################################################################################
##### Set up the 'collections' map #############################################
################################################################################

# this PSet specifies which collections to get from the input files
miniAOD_collections = cms.PSet (
  electrons                   =  cms.InputTag  ('slimmedElectrons',                  ''),
  genjets                     =  cms.InputTag  ('slimmedGenJets',                    ''),
  jets                        =  cms.InputTag  ('slimmedJets',                       ''),
  bjets                       =  cms.InputTag  ('slimmedJets',                       ''),
  generatorweights            =  cms.InputTag  ('generator',                         ''), 
  mcparticles                 =  cms.InputTag  ('packedGenParticles',                ''),
  hardInteractionMcparticles  =  cms.InputTag  ('prunedGenParticles',                ''),
  mets                        =  cms.InputTag  ('slimmedMETs',                       ''),
  muons                       =  cms.InputTag  ('slimmedMuons',                      ''),
  photons                     =  cms.InputTag  ('slimmedPhotons',                    ''),
  primaryvertexs              =  cms.InputTag  ('offlineSlimmedPrimaryVertices',     ''),
  pileupinfos                 =  cms.InputTag  ('slimmedAddPileupInfo',              ''),
  beamspots                   =  cms.InputTag  ('offlineBeamSpot',                   ''),
  superclusters               =  cms.InputTag  ('reducedEgamma', 'reducedSuperClusters'),
  taus                        =  cms.InputTag  ('slimmedTaus',                       ''),
  triggers                    =  cms.InputTag  ('TriggerResults',             '', 'HLT'),
  trigobjs                    =  cms.InputTag  ('selectedPatTrigger',                ''),
)

collections = miniAOD_collections

################################################################################
##### Set up any user-defined variable producers ###############################
################################################################################

variableProducers = []
variableProducers.append('DisplacedSUSYEventVariableProducer')
variableProducers.append('LifetimeWeightProducer')
variableProducers.append('PUScalingFactorProducer')


weights = cms.VPSet(
    cms.PSet (
        inputCollections = cms.vstring("eventvariables"),
        inputVariable = cms.string("lifetimeWeight")
    ),
    cms.PSet (
        inputCollections = cms.vstring("eventvariables"),
        inputVariable = cms.string("puScalingFactor")
    ),
    cms.PSet (
        inputCollections = cms.vstring("eventvariables"),
        inputVariable = cms.string("triggerScaleFactor")
    ),
    cms.PSet (
        inputCollections = cms.vstring("eventvariables"),
        inputVariable = cms.string("electronReco2016")
    ),
    cms.PSet (
        inputCollections = cms.vstring("eventvariables"),
        inputVariable = cms.string("electronID2016Tight")
    ),
)

scalingfactorproducers = []
ObjectScalingFactorProducer = {}

ObjectScalingFactorProducer['name'] = 'ObjectScalingFactorProducer'
ObjectScalingFactorProducer['electronFile'] = cms.string(os.environ['CMSSW_BASE'] + '/src/OSUT3Analysis/AnaTools/data/electronSFs.root')
ObjectScalingFactorProducer['trackFile'] = cms.string(os.environ['CMSSW_BASE'] + '/src/OSUT3Analysis/AnaTools/data/trackSFs.root')

ObjectScalingFactorProducer['scaleFactors'] = cms.VPSet(
    cms.PSet (
        inputCollection = cms.string("electrons"),
        sfType = cms.string("Reco"),
        version = cms.string("2016")
    ),
    cms.PSet (
        inputCollection = cms.string("electrons"),
        sfType = cms.string("ID"),
        version = cms.string("2016"),
        wp = cms.string("Tight")
    ),
)

scalingfactorproducers.append(ObjectScalingFactorProducer)

################################################################################
##### Import the channels to be run ############################################
################################################################################

from DisplacedSUSY.EEChannel.ZControlRegionSelection import *

eventSelections = [ZControlRegion]
#                   ZControlRegionPrompt,
#                   ZControlRegionDisplaced,
#                   ZControlRegionVeryDisplaced]

################################################################################
##### Import the histograms to be plotted ######################################
################################################################################

from OSUT3Analysis.Configuration.histogramDefinitions import ElectronHistograms, DiElectronHistograms
from DisplacedSUSY.Configuration.histogramDefinitions import ElectronD0Histograms, BeamspotHistograms
from OSUT3Analysis.Configuration.histogramDefinitions import JetHistograms, ElectronJetHistograms
from OSUT3Analysis.Configuration.histogramDefinitions import MetHistograms, ElectronMetHistograms
from DisplacedSUSY.Configuration.histogramDefinitions import eventHistograms

################################################################################
##### Attach the channels and histograms to the process ########################
################################################################################

histograms = cms.VPSet()
histograms.append(ElectronHistograms)
histograms.append(DiElectronHistograms)
histograms.append(ElectronD0Histograms)
histograms.append(BeamspotHistograms)
histograms.append(JetHistograms)
histograms.append(ElectronJetHistograms)
histograms.append(MetHistograms)
histograms.append(ElectronMetHistograms)
histograms.append(eventHistograms)

add_channels (process, eventSelections, histograms, weights, scalingfactorproducers, collections, variableProducers, False)

process.PUScalingFactorProducer.dataset = cms.string("TTJets_DiLept")
process.PUScalingFactorProducer.target = cms.string ("data2016_GH")
process.PUScalingFactorProducer.targetUp = cms.string ("data2016_GHUp")
process.PUScalingFactorProducer.targetDown = cms.string ("data2016_GHDown")
process.PUScalingFactorProducer.PU = cms.string(os.environ['CMSSW_BASE'] + '/src/DisplacedSUSY/StandardAnalysis/data/pu2016.root')
process.PUScalingFactorProducer.type = cms.string("bgMC")


process.DisplacedSUSYEventVariableProducer.type = cms.string("bgMC")
process.DisplacedSUSYEventVariableProducer.triggerPath = cms.string("HLT_MET200_v")
process.DisplacedSUSYEventVariableProducer.triggerScaleFactor = cms.double(0.9645)
