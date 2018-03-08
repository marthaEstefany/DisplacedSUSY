import FWCore.ParameterSet.Config as cms
import copy
import string

from DisplacedSUSY.StandardAnalysis.CutDefinitions import *
from DisplacedSUSY.BackgroundStudies.CutDefinitions import *

##############################################################
##### EVENT SELECTIONS FOR OUR QCD B-BBAR CONTROL REGIONS ####
##############################################################

##############################################################
################  basic HF + muon selection   ################
##############################################################

QCDMuonControlRegion = cms.PSet(
    name = cms.string("QCDMuonControlRegion"),
    triggers = cms.vstring("HLT_Mu50_v", "HLT_TkMu50_v"),
    cuts = cms.VPSet ()
)
QCDMuonControlRegion.cuts.append(one_jet_eta_cut)
QCDMuonControlRegion.cuts.append(one_jet_pt_30_cut)
QCDMuonControlRegion.cuts.append(one_jet_id_cut)
QCDMuonControlRegion.cuts.append(extra_jet_veto)

QCDMuonControlRegion.cuts.append(bjet_eta_cut)
QCDMuonControlRegion.cuts.append(bjet_pt_30_cut)
QCDMuonControlRegion.cuts.append(bjet_id_cut)
QCDMuonControlRegion.cuts.append(bjet_csvm_cut)
QCDMuonControlRegion.cuts.append(extra_bjet_veto)

QCDMuonControlRegion.cuts.append(muon_eta_cut)
#QCDMuonControlRegion.cuts.append(muon_pt_40_cut)
# raise muon pt to be in plateau of single muon trig eff curve
QCDMuonControlRegion.cuts.append(muon_pt_55_cut)
QCDMuonControlRegion.cuts.append(muon_global_cut)
QCDMuonControlRegion.cuts.append(muon_id_cut)
QCDMuonControlRegion.cuts.append(extra_muon_veto)

QCDMuonControlRegion.cuts.append(jet_bjet_deltaPhi_cut)
QCDMuonControlRegion.cuts.append(muon_jet_deltaR_cut)

prompt_muon_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("10000*abs(d0) < 200"),
    numberRequired = cms.string(">= 1")
    )
displaced_muon_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("10000*abs(d0) > 200 & 10000*abs(d0) < 1000"),
    numberRequired = cms.string(">= 1")
    )
very_displaced_muon_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("10000*abs(d0) > 1000"),
    numberRequired = cms.string(">= 1")
    )

QCDMuonControlRegionPrompt = cms.PSet(
    name = cms.string("QCDMuonControlRegionPrompt"),
    triggers = cms.vstring(),
    cuts = copy.deepcopy(QCDMuonControlRegion.cuts)
)
QCDMuonControlRegionPrompt.cuts.append(prompt_muon_cut)

QCDMuonControlRegionDisplaced = cms.PSet(
    name = cms.string("QCDMuonControlRegionDisplaced"),
    triggers = cms.vstring(),
    cuts = copy.deepcopy(QCDMuonControlRegion.cuts)
)
QCDMuonControlRegionDisplaced.cuts.append(displaced_muon_cut)

QCDMuonControlRegionVeryDisplaced = cms.PSet(
    name = cms.string("QCDMuonControlRegionVeryDisplaced"),
    triggers = cms.vstring(),
    cuts = copy.deepcopy(QCDMuonControlRegion.cuts)
)
QCDMuonControlRegionVeryDisplaced.cuts.append(very_displaced_muon_cut)
