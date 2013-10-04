import FWCore.ParameterSet.Config as cms
import copy

###########################################################
##### Set up the event selections (channels) #####
###########################################################

##### List of valid input collections #####
# jets, muons, electrons, taus, photons, mets,
# events, tracks, primaryvertexs,
# genjets, mcparticles,
# bxlumis, superclusters



# abs(genMatchedPdgGrandmotherId) = 1000006 covers the stop->Bl matching
# abs(genMatchedPdgGrandmotherId) = 24 covers the stop->Tnu matching

SignalGenMatching = cms.PSet(
    name = cms.string("SignalGenMatching"),
    cuts = cms.VPSet (
      #at least one electron
      cms.PSet (
        inputCollection = cms.string("mcparticles"),
        cutString = cms.string("abs(genMatchedPdgGrandmotherId) = 1000006 | abs(genMatchedPdgGrandmotherId) = 24 & abs(id) = 11"),
        numberRequired = cms.string(">= 1")
      ),
      #at least one muon
      cms.PSet (
        inputCollection = cms.string("secondary mcparticles"),
        cutString = cms.string("abs(genMatchedPdgGrandmotherId) = 1000006 | abs(genMatchedPdgGrandmotherId) = 24 & abs(id) = 13"),
        numberRequired = cms.string(">= 1")
      ),
    )
)

from DisplacedSUSY.StandardAnalysis.Preselection import * 

#################################################################

# PRESELECTION WITH LEPTON d0 > 200 um

Signal_Selection_200um = cms.PSet(
        name = cms.string("Signal_Selection_200um"),
            triggers = copy.deepcopy(Preselection.triggers),
            cuts = cms.VPSet ()
        )
Signal_Selection_200um.cuts.extend(copy.deepcopy(Preselection.cuts))

electron_d0_cut = cms.PSet (
        inputCollection = cms.string("electrons"),
            cutString = cms.string("abs(correctedD0) > 0.02"),
            numberRequired = cms.string("== 1")
        )
Signal_Selection_200um.cuts.append(electron_d0_cut)

muon_d0_cut = cms.PSet (
        inputCollection = cms.string("muons"),
            cutString = cms.string("abs(correctedD0) > 0.02"),
            numberRequired = cms.string("== 1")
        )
Signal_Selection_200um.cuts.append(muon_d0_cut)

#################################################################

# PRESELECTION WITH LEPTON d0 > 500 um

Signal_Selection_500um = cms.PSet(
        name = cms.string("Signal_Selection_500um"),
            triggers = copy.deepcopy(Preselection.triggers),
            cuts = cms.VPSet ()
        )
Signal_Selection_500um.cuts.extend(copy.deepcopy(Preselection.cuts))

electron_d0_cut = cms.PSet (
        inputCollection = cms.string("electrons"),
            cutString = cms.string("abs(correctedD0) > 0.05"),
            numberRequired = cms.string("== 1")
        )
Signal_Selection_500um.cuts.append(electron_d0_cut)

muon_d0_cut = cms.PSet (
        inputCollection = cms.string("muons"),
            cutString = cms.string("abs(correctedD0) > 0.05"),
            numberRequired = cms.string("== 1")
        )
Signal_Selection_500um.cuts.append(muon_d0_cut)

#################################################################

# PRESELECTION WITH LEPTON d0 > 1000 um

Signal_Selection_1000um = cms.PSet(
        name = cms.string("Signal_Selection_1000um"),
            triggers = copy.deepcopy(Preselection.triggers),
            cuts = cms.VPSet ()
        )
Signal_Selection_1000um.cuts.extend(copy.deepcopy(Preselection.cuts))

electron_d0_cut = cms.PSet (
        inputCollection = cms.string("electrons"),
            cutString = cms.string("abs(correctedD0) > 0.1"),
            numberRequired = cms.string("== 1")
        )
Signal_Selection_1000um.cuts.append(electron_d0_cut)

muon_d0_cut = cms.PSet (
        inputCollection = cms.string("muons"),
            cutString = cms.string("abs(correctedD0) > 0.1"),
            numberRequired = cms.string("== 1")
        )
Signal_Selection_1000um.cuts.append(muon_d0_cut)
