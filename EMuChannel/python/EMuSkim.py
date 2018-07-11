import FWCore.ParameterSet.Config as cms
import copy
import string
from DisplacedSUSY.EMuChannel.CutDefinitions import *

##########################################################################
##### Set up the EMu Skim Selections for the displaced SUSY analysis #####
##########################################################################

EMuSkim = cms.PSet(
    name = cms.string("EMuSkim"),
    triggers = cms.vstring(), # TRIGGER
    cuts = cms.VPSet()
)
### at least one good electron
EMuSkim.cuts.append(electron_eta_cut)
EMuSkim.cuts.append(electron_pt_30_cut)
### at least one good muon
EMuSkim.cuts.append(muon_eta_cut)
EMuSkim.cuts.append(muon_pt_30_cut)
EMuSkim.cuts.append(muon_global_cut)
