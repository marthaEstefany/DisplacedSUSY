import FWCore.ParameterSet.Config as cms
import copy
import string
import os

import DisplacedSUSY.StandardAnalysis.objectDefinitions as objectDefs
from OSUT3Analysis.Configuration.cutUtilities import *

#WE USE ETA 2.4 OFTEN
absEta_2p4_cutstring = cms.string("abs(eta) < 2.4")

# syntax to access gen mother is different in different releases
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_7_6_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    gen_mother_string = "mother_"
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
    gen_mother_string = "motherRef"
else:
    gen_mother_string = "motherRef"
    print "CMSSW release not recognized; gen mother cuts might not work"

#########################################################################
# weight selections to determine if they contribute to negative
# weighted event

lifetimeWeight_negative = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("lifetimeWeight < 0"),
    numberRequired = cms.string(">= 1"),
)

puScalingFactor_negative = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("puScalingFactor < 0"),
    numberRequired = cms.string(">= 1"),
)

##########################################################################

# BEGIN GEN PARTICLE CUTS
#just for checking signal, not used in analysis event selection
exactly2_genEle_status1_uniqueMotherIsStop_cut = cms.PSet(
    inputCollection = cms.vstring("hardInteractionMcparticles"),
    cutString = cms.string("abs ( pdgId ) == 11 & status==1 & abs (uniqueMotherPdgId) == 1000006"),
    numberRequired = cms.string("== 2"),
    alias = cms.string("Exactly 2 status==1 gen electrons whose unique mother is a stop")
)

exactly2_genMu_status1_uniqueMotherIsStop_cut = cms.PSet(
    inputCollection = cms.vstring("hardInteractionMcparticles"),
    cutString = cms.string("abs ( pdgId ) == 13 & status==1 & abs (uniqueMotherPdgId) == 1000006"),
    numberRequired = cms.string("== 2"),
    alias = cms.string("Exactly 2 status==1 gen muons whose unique mother is a stop")
)

exactly2_genEleOrMu_status1_uniqueMotherIsStop_cut = cms.PSet(
    inputCollection = cms.vstring("hardInteractionMcparticles"),
    cutString = cms.string("(abs (pdgId) ==11 || abs ( pdgId ) == 13) & status==1 & abs (uniqueMotherPdgId) == 1000006"),
    numberRequired = cms.string("== 2"),
    alias = cms.string("Exactly 2 status==1 gen electrons or muons whose unique mother is a stop")
)

genEleMuChannel_cut = cms.PSet(
    inputCollection = cms.vstring("hardInteractionMcparticles","hardInteractionMcparticles"),
    cutString = cms.string("abs(hardInteractionMcparticle.pdgId)+abs(hardInteractionMcparticle.pdgId)==24"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Exactly 1 gen electron and 1 gen muon")
)

atLeastTwo_genLxy_lessThan50cm_cut = cms.PSet(
    inputCollection = cms.vstring("hardInteractionMcparticles"),
    cutString = cms.string("sqrt(vx*vx+vy*vy)<500."),
    numberRequired = cms.string(">= 2"),
    alias = cms.string("At least 2 hardInteractionMcparticles with vertex in xy plane < 50 cm")
)

atLeastTwo_genLxy_lessThan1cm_cut = cms.PSet(
    inputCollection = cms.vstring("hardInteractionMcparticles"),
    cutString = cms.string("sqrt(vx*vx+vy*vy)<10."),
    numberRequired = cms.string(">= 2"),
    alias = cms.string("At least 2 hardInteractionMcparticles with vertex in xy plane < 1 cm")
)

atLeastTwo_genEta_cut = cms.PSet(
    inputCollection = cms.vstring("hardInteractionMcparticles"),
    cutString = absEta_2p4_cutstring,
    numberRequired = cms.string(">= 2")
    )

atLeastZero_genEta_cut = cms.PSet(
    inputCollection = cms.vstring("hardInteractionMcparticles"),
    cutString = absEta_2p4_cutstring,
    numberRequired = cms.string(">= 0")
    )


atLeastTwo_genPt_40_cut = cms.PSet(
    inputCollection = cms.vstring("hardInteractionMcparticles"),
    cutString = cms.string("pt > 40"),
    numberRequired = cms.string(">= 2")
    )

atLeastTwo_genPt_50_cut = cms.PSet(
    inputCollection = cms.vstring("hardInteractionMcparticles"),
    cutString = cms.string("pt > 50"),
    numberRequired = cms.string(">= 2")
    )

atLeastTwo_genPt_65_cut = cms.PSet(
    inputCollection = cms.vstring("hardInteractionMcparticles"),
    cutString = cms.string("pt > 65"),
    numberRequired = cms.string(">= 2")
    )

atLeastTwo_genPt_75_cut = cms.PSet(
    inputCollection = cms.vstring("hardInteractionMcparticles"),
    cutString = cms.string("pt > 75"),
    numberRequired = cms.string(">= 2")
    )

exactly2_genMu_status1_uniqueMotherIsZ_cut = cms.PSet(
    inputCollection = cms.vstring("hardInteractionMcparticles"),
    cutString = cms.string("abs ( pdgId ) == 13 & status==1 & abs (uniqueMotherPdgId) == 23"),
    numberRequired = cms.string("== 2"),
    alias = cms.string("Exactly 2 status==1 gen muons whose unique mother is a Z")
)

genPhoton_status1_cut = cms.PSet(
    inputCollection = cms.vstring("hardInteractionMcparticles"),
    cutString = cms.string("abs ( pdgId ) == 22 & status==1"),
    numberRequired = cms.string(">= 0"),
    alias = cms.string(">= 0 status==1 gen photons")
)

##########################################################################
# DUMMY CUT FOR PRODUCING FLOW CHART

cutDummyMet = cms.PSet(
    inputCollection = cms.vstring("mets"),
    cutString = cms.string("noMuPt > -1"),
    numberRequired = cms.string(">= 1"),
)

cutDummyMuon = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string(">= 0"),
    alias = cms.string("No offline cuts")
)

cutDummyElectron = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string(">= 0"),
    alias = cms.string("No offline cuts")
)

cutDummyPhoton = cms.PSet(
    inputCollection = cms.vstring("photons"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string(">= 0"),
    alias = cms.string("No offline cuts")
)

cutDummy = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string(">= 0"),
    alias = cms.string("No offline cuts")
)
##########################################################################

# level1 prefiring check cuts:
# https://twiki.cern.ch/twiki/bin/view/CMS/ExoPreapprovalChecklist
zero_jet_pt_100_cut = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("pt > 100"),
    numberRequired = cms.string("== 0")
    )

zero_jet_eta_greaterThan2p25_cut = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("abs(eta) > 2.25"),
    numberRequired = cms.string("== 0")
    )

zero_jet_eta_lessThan3_cut = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("abs(eta) < 3.0"),
    numberRequired = cms.string("== 0")
    )
##########################################################################

# BEGIN JET CUTS

atLeastZero_jet_eta_cut = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("abs(eta) < 2.4"),
    numberRequired = cms.string(">= 0")
    )

atLeastZero_jet_pt_30_cut = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("pt > 30"),
    numberRequired = cms.string(">= 0")
    )

atLeastZero_jet_id_cut = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = objectDefs.jet_id_cutstring,
    numberRequired = cms.string(">= 0"),
    alias = objectDefs.jet_id_alias
    )


atLeastOne_jet_eta_cut = copy.deepcopy(atLeastZero_jet_eta_cut)
atLeastOne_jet_eta_cut.numberRequired = cms.string(">= 1")

atLeastOne_jet_pt_30_cut = copy.deepcopy(atLeastZero_jet_pt_30_cut)
atLeastOne_jet_pt_30_cut.numberRequired = cms.string(">= 1")

atLeastOne_jet_id_cut = copy.deepcopy(atLeastZero_jet_id_cut)
atLeastOne_jet_id_cut.numberRequired = cms.string(">= 1")
atLeastOne_jet_id_cut.alias = cms.string(">=1 jets with ID against leptons")


atLeastTwo_jet_eta_cut = copy.deepcopy(atLeastZero_jet_eta_cut)
atLeastTwo_jet_eta_cut.numberRequired = cms.string(">= 2")

atLeastTwo_jet_pt_30_cut = copy.deepcopy(atLeastZero_jet_pt_30_cut)
atLeastTwo_jet_pt_30_cut.numberRequired = cms.string(">= 2")

atLeastTwo_jet_id_cut = copy.deepcopy(atLeastZero_jet_id_cut)
atLeastTwo_jet_id_cut.numberRequired = cms.string(">= 2")
atLeastTwo_jet_id_cut.alias = cms.string(">=2 jets with ID against leptons")

atLeastTwo_jet_loose_id_cut = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = objectDefs.jet_loose_id_cutstring,
    numberRequired = cms.string(">= 2"),
    alias = objectDefs.jet_loose_id_alias
    )

atLeastTwo_jet_ttbar_paper_loose_id_cut = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = objectDefs.jet_ttbar_paper_loose_id_cutstring,
    numberRequired = cms.string(">= 2"),
    alias = objectDefs.jet_ttbar_paper_loose_id_alias
    )

atLeastTwo_jet_lepton_cleaning_cut = cms.PSet (
        inputCollection = cms.vstring("jets"),
        cutString = cms.string("matchedToLepton = 0"),
        numberRequired = cms.string(">= 2"),
        alias = cms.string('>=2 jets not matched to leptons')
    )

veto_2orMore_jets = cms.PSet (
        inputCollection = cms.vstring("jets"),
        cutString = cms.string("pt > -1"),
        numberRequired = cms.string("< 2"),
        alias = cms.string('< 2 jets')
    )

veto_3orMore_jets = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string("<= 2")
    )


#BEGIN B-JET CUTS
atLeastZero_bjet_eta_cut = copy.deepcopy(atLeastZero_jet_eta_cut)
atLeastZero_bjet_eta_cut.inputCollection = cms.vstring("bjets")

atLeastZero_bjet_pt_30_cut = copy.deepcopy(atLeastZero_jet_pt_30_cut)
atLeastZero_bjet_pt_30_cut.inputCollection = cms.vstring("bjets")

atLeastZero_bjet_id_cut = copy.deepcopy(atLeastZero_jet_id_cut)
atLeastZero_bjet_id_cut.inputCollection = cms.vstring("bjets")
atLeastZero_bjet_id_cut.alias = cms.string(">=0 b-jets with ID against leptons")

atLeastOne_bjet_eta_cut = copy.deepcopy(atLeastOne_jet_eta_cut)
atLeastOne_bjet_eta_cut.inputCollection = cms.vstring("bjets")

atLeastOne_bjet_pt_30_cut = copy.deepcopy(atLeastOne_jet_pt_30_cut)
atLeastOne_bjet_pt_30_cut.inputCollection = cms.vstring("bjets")

atLeastOne_bjet_id_cut = copy.deepcopy(atLeastOne_jet_id_cut)
atLeastOne_bjet_id_cut.inputCollection = cms.vstring("bjets")
atLeastOne_bjet_id_cut.alias = cms.string(">=1 b-jets with ID against leptons")

veto_3orMore_bjets = cms.PSet(
    inputCollection = cms.vstring("bjets"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string("<= 2")
    )

#BEGIN B-JET CombinedSecondaryVertexv2 CUTS
#FIXME: should be applied to "bjets" instead of "jets" ?
jet_btag_twp_cut = cms.PSet (
        inputCollection = cms.vstring("jets"),
        cutString = objectDefs.btag_tightCSVv2_cutstring,
        numberRequired = cms.string(">= 1"),
        alias = cms.string('>= 1 tight b tags (CSVv2)')
    )

jet_btag_mwp_cut = cms.PSet (
        inputCollection = cms.vstring("jets"),
        cutString = objectDefs.btag_mediumCSVv2_cutstring,
        numberRequired = cms.string(">= 1"),
        alias = cms.string('>= 1 medium b tags (CSVv2)')
    )

jet_btag_2_mwp_cut = copy.deepcopy(jet_btag_mwp_cut)
jet_btag_2_mwp_cut.numberRequired = cms.string(">= 2")
jet_btag_2_mwp_cut.alias = cms.string('>= 2 medium b tags (CSVv2)')

jet_btag_mwp_veto = copy.deepcopy(jet_btag_mwp_cut)
jet_btag_mwp_veto.numberRequired = cms.string("== 0")
jet_btag_mwp_veto.alias = cms.string('no medium b tags (CSVv2)')
jet_btag_mwp_veto.isVeto = cms.bool(True)

jet_btag_lwp_cut = cms.PSet (
        inputCollection = cms.vstring("jets"),
        cutString = objectDefs.btag_looseCSVv2_cutstring,
        numberRequired = cms.string(">= 1"),
        alias = cms.string('>= 1 loose b tags (CSVv2)')
    )

jet_btag_2_lwp_cut = copy.deepcopy(jet_btag_lwp_cut)
jet_btag_2_lwp_cut.numberRequired = cms.string(">= 2")
jet_btag_2_lwp_cut.alias = cms.string('>= 2 loose b tags (CSVv2)')

jet_btag_lwp_veto = copy.deepcopy(jet_btag_lwp_cut)
jet_btag_lwp_veto.numberRequired = cms.string("== 0")
jet_btag_lwp_veto.alias = cms.string('no loose b tags (CSVv2)')
jet_btag_lwp_veto.isVeto = cms.bool(True)


##########################################################################

# BEGIN ELECTRON CUTS

electron_eta_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("abs(electron.eta) < 2.4"),
    numberRequired = cms.string(">= 1")
    )

electron_gap_veto = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("isEBEEGap = 0"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">= 1 electrons not in ECAL crack")
    )

electron_pt_20_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("pt > 20"),
    numberRequired = cms.string(">= 1")
    )

electron_pt_25_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("pt > 25"),
    numberRequired = cms.string(">= 1")
    )

electron_pt_25_dummy_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("pt > 25"),
    numberRequired = cms.string(">= 0")
    )

electron_pt_30_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("pt > 30"),
    numberRequired = cms.string(">= 1")
    )

electron_pt_42_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("pt > 42"),
    numberRequired = cms.string(">= 1")
    )

electron_pt_50_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("pt > 50"),
    numberRequired = cms.string(">= 1")
    )

electron_pt_65_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("pt > 65"),
    numberRequired = cms.string(">= 1")
    )

electron_pt_75_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("pt > 75"),
    numberRequired = cms.string(">= 1")
    )

electron_pt_100_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("pt > 100"),
    numberRequired = cms.string(">= 1")
    )

electron_pt_100_veto = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("pt > 100"),
    numberRequired = cms.string("== 0"),
    isVeto = cms.bool(True),
    alias = cms.string("electron pT > 100 GeV veto")
    )

electron_id_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("passesVID_tightID"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 electrons with versioned tight ID") #versioned tight ID normally includes tight isolation, but we remove it in customize.py so we can use the inverted isolation at times
    )

electron_iso_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = objectDefs.electron_iso_cutstring,
    numberRequired = cms.string(">= 1"),
    alias = objectDefs.electron_iso_alias
    )

electron_antiiso_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = objectDefs.electron_antiiso_cutstring,
    numberRequired = cms.string(">= 1"),
    alias = objectDefs.electron_antiiso_alias
    )

electron_loose_iso_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = objectDefs.electron_loose_iso_cutstring,
    numberRequired = cms.string(">= 1"),
    alias = objectDefs.electron_loose_iso_alias
    )

electron_id_impact_parameter_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = objectDefs.electron_id_impact_parameter_cutstring,
    numberRequired = cms.string(">= 1"),
    alias = objectDefs.electron_id_impact_parameter_alias
    )

# electron d0 < 10 microns
electron_d0_lessThan10_cut = cms.PSet(
    inputCollection = cms.vstring("electrons","beamspots"),
    cutString = cms.string("10000*abs("+electronSmearedD0WRTBeamspot+") < 10"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">= 1 electrons with |d_0| < 10 mum")
    )

# electron 10 < d0 < 20 microns
electron_d0_10to20_cut = cms.PSet(
    inputCollection = cms.vstring("electrons","beamspots"),
    cutString = cms.string("10000*abs("+electronSmearedD0WRTBeamspot+") > 10 & 10000*abs("+electronSmearedD0WRTBeamspot+") < 20"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 electrons with 10 < |d_0| < 20 mum")
    )

# electron d0 < 20 microns
electron_d0_lessThan20_cut = cms.PSet(
    inputCollection = cms.vstring("electrons","beamspots"),
    cutString = cms.string("10000*abs("+electronSmearedD0WRTBeamspot+") < 20"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 electrons with |d_0| < 20 mum")
    )

# electron d0 > 20 microns
electron_d0_greaterThan20_cut = cms.PSet(
    inputCollection = cms.vstring("electrons","beamspots"),
    cutString = cms.string("10000*abs("+electronSmearedD0WRTBeamspot+") > 20"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 electrons with |d_0| > 20 mum")
    )

# electron d0 < 40 microns
electron_d0_lessThan40_cut = cms.PSet(
    inputCollection = cms.vstring("electrons","beamspots"),
    cutString = cms.string("10000*abs("+electronSmearedD0WRTBeamspot+") < 40"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">= 1 electrons with |d_0| < 40 mum")
    )

# electron d0 < 50 microns
electron_d0_lessThan50_cut = cms.PSet(
    inputCollection = cms.vstring("electrons","beamspots"),
    cutString = cms.string("10000*abs("+electronSmearedD0WRTBeamspot+") < 50"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">= 1 electrons with |d_0| < 50 mum")
    )

# electron d0 > 50 microns
electron_d0_greaterThan50_cut = cms.PSet(
    inputCollection = cms.vstring("electrons","beamspots"),
    cutString = cms.string("10000*abs("+electronSmearedD0WRTBeamspot+") > 50"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 electrons with |d_0| > 50 mum")
    )

# electron 50 < d0 < 100 microns
electron_d0_50to100_cut = cms.PSet(
    inputCollection = cms.vstring("electrons","beamspots"),
    cutString = cms.string("10000*abs("+electronSmearedD0WRTBeamspot+") > 50 & 10000*abs("+electronSmearedD0WRTBeamspot+") < 100"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 electrons with 50 < |d_0| < 100 mum")
    )

# electron d0 < 100 microns
electron_d0_lessThan100_cut = cms.PSet(
    inputCollection = cms.vstring("electrons","beamspots"),
    cutString = cms.string("10000*abs("+electronSmearedD0WRTBeamspot+") < 100"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">= 1 electrons with |d_0| < 100 mum")
    )

# electron d0 > 100 microns
electron_d0_greaterThan100_cut = cms.PSet(
    inputCollection = cms.vstring("electrons","beamspots"),
    cutString = cms.string("10000*abs("+electronSmearedD0WRTBeamspot+") > 100"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 electrons with |d_0| > 100 mum")
    )

# electron 100 < d0 < 200 microns
electron_d0_100to200_cut = cms.PSet(
    inputCollection = cms.vstring("electrons","beamspots"),
    cutString = cms.string("10000*abs("+electronSmearedD0WRTBeamspot+") > 100 & 10000*abs("+electronSmearedD0WRTBeamspot+") < 200"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 electrons with 100 < |d_0| < 200 mum")
    )

# electron 100 < d0 < 500 microns
electron_d0_100to500_cut = cms.PSet(
    inputCollection = cms.vstring("electrons","beamspots"),
    cutString = cms.string("10000*abs("+electronSmearedD0WRTBeamspot+") > 100 & 10000*abs("+electronSmearedD0WRTBeamspot+") < 500"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 electrons with 100 < |d_0| < 500 mum")
    )

electron_d0_lessThan200_cut = cms.PSet(
    inputCollection = cms.vstring("electrons","beamspots"),
    cutString = cms.string("10000*abs("+electronSmearedD0WRTBeamspot+") < 200"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 electrons with |d_0| < 200 mum")
    )

electron_d0_greaterThan100_cut = cms.PSet(
    inputCollection = cms.vstring("electrons","beamspots"),
    cutString = cms.string("10000*abs("+electronSmearedD0WRTBeamspot+") > 100"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 electrons with |d_0| > 100 mum")
    )

electron_d0_greaterThan200_cut = cms.PSet(
    inputCollection = cms.vstring("electrons","beamspots"),
    cutString = cms.string("10000*abs("+electronSmearedD0WRTBeamspot+") > 200"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 electrons with |d_0| > 200 mum")
    )

# electron 500 < d0 < 1000 microns
electron_d0_500to1000_cut = cms.PSet(
    inputCollection = cms.vstring("electrons","beamspots"),
    cutString = cms.string("10000*abs("+electronSmearedD0WRTBeamspot+") > 500 & 10000*abs("+electronSmearedD0WRTBeamspot+") < 1000"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 electrons with 500 < |d_0| < 1000 mum")
    )

electron_mt_cut = cms.PSet (
    inputCollection = cms.vstring("electrons","mets"),
    cutString = cms.string("transMass(electron, met) < 50"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("electron m_{T} < 50 GeV")
    )

electron_num_exactly_1_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("exactly 1 electron")
    )

#####################
#BEGIN GEN ELECTRON CUTS

electron_gen_motherIsW_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("abs(genMatchedParticle.noFlags.{}.pdgId) == 24".format(gen_mother_string)),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 electrons from W (electron matched to gen particle whose mother has PDG ID of 24)")
)

##########################################################################

# BEGIN MUON CUTS

muon_eta_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("abs(muon.eta) < 2.4"),
    numberRequired = cms.string(">= 1")
    )

muon_eta_lessThan1_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("abs(eta) < 1.0"),
    numberRequired = cms.string(">= 1")
    )

muon_eta_greaterThan1_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("abs(eta) >= 1.0"),
    numberRequired = cms.string(">= 1")
    )

#####################################
muon_pt_15_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("pt > 15"),
    numberRequired = cms.string(">= 1")
    )

muon_pt_15_veto = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("pt > 15"),
    numberRequired = cms.string("== 0"),
    isVeto = cms.bool(True),
    alias = cms.string("muon pT > 15 GeV veto")
    )

muon_pt_20_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("pt > 20"),
    numberRequired = cms.string(">= 1")
    )

muon_pt_25_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("pt > 25"),
    numberRequired = cms.string(">= 1")
    )

muon_pt_25_dummy_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("pt > 25"),
    numberRequired = cms.string(">= 0")
    )

muon_pt_30_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("pt > 30"),
    numberRequired = cms.string(">= 1")
    )

muon_pt_35_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("pt > 35"),
    numberRequired = cms.string(">= 1")
    )

muon_pt_40_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("pt > 40"),
    numberRequired = cms.string(">= 1")
    )

muon_pt_50_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("pt > 50"),
    numberRequired = cms.string(">= 1")
    )

muon_pt_55_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("pt > 55"),
    numberRequired = cms.string(">= 1")
    )

muon_pt_70_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("pt > 70"),
    numberRequired = cms.string(">= 1")
    )

muon_pt_100_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("pt > 100"),
    numberRequired = cms.string(">= 1")
    )

muon_pt_100_veto = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("pt > 100"),
    numberRequired = cms.string("== 0"),
    isVeto = cms.bool(True),
    alias = cms.string("muon pT > 100 GeV veto")
    )

muon_pt_150_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("pt > 150"),
    numberRequired = cms.string(">= 1")
    )

muon_global_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = objectDefs.muon_global_cutstring,
    numberRequired = cms.string(">= 1"),
    alias = objectDefs.muon_global_alias
    )

muon_id_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = objectDefs.muon_id_cutstring,
    numberRequired = cms.string(">= 1"),
    alias = objectDefs.muon_id_alias
    )

muon_softID_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("isSoftMuonWRTVtx > 0"),
    numberRequired = cms.string(">= 1"),
    )

muon_softID_dummy = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("isSoftMuonWRTVtx > 0"),
    numberRequired = cms.string(">= 0"),
    )

muon_tightID_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("isTightMuonWRTVtx > 0"),
    numberRequired = cms.string(">= 1"),
    )

muon_tightID_dummy = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("istightMuonWRTVtx > 0"),
    numberRequired = cms.string(">= 0"),
    )

muon_id_impact_parameter_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = objectDefs.muon_id_impact_parameter_cutstring,
    numberRequired = cms.string(">= 1"),
    alias = objectDefs.muon_id_impact_parameter_alias
    )

muon_iso_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = objectDefs.muon_iso_cutstring,
    numberRequired = cms.string(">= 1"),
    alias = objectDefs.muon_iso_alias
    )

muon_antiiso_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = objectDefs.muon_antiiso_cutstring,
    numberRequired = cms.string(">= 1"),
    alias = objectDefs.muon_antiiso_alias
    )

muon_pfBetaIsoCorr_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = objectDefs.muon_pfBetaIsoCorr_cutstring,
    numberRequired = cms.string(">= 1"),
    alias = objectDefs.muon_pfBetaIsoCorr_alias
)

# muon d0 < 10 microns
muon_d0_lessThan10_cut = cms.PSet(
    inputCollection = cms.vstring("muons","beamspots"),
    cutString = cms.string("10000*abs("+muonSmearedD0WRTBeamspot+") < 10"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 muons with |d_0| < 10 mum")
    )

# muon 10 < d0 < 20 microns
muon_d0_10to20_cut = cms.PSet(
    inputCollection = cms.vstring("muons","beamspots"),
    cutString = cms.string("10000*abs("+muonSmearedD0WRTBeamspot+") > 10 & 10000*abs("+muonSmearedD0WRTBeamspot+") < 20"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 muons with 10 < |d_0| < 20 mum")
    )

# muon d0 < 40 microns
muon_d0_lessThan40_cut = cms.PSet(
    inputCollection = cms.vstring("muons","beamspots"),
    cutString = cms.string("10000*abs("+muonSmearedD0WRTBeamspot+") < 40"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 muons with |d_0| < 40 mum")
    )

# muon d0 > 40 microns
muon_d0_greaterThan40_cut = cms.PSet(
    inputCollection = cms.vstring("muons","beamspots"),
    cutString = cms.string("10000*abs("+muonSmearedD0WRTBeamspot+") > 40"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 muons with |d_0| > 40 mum")
    )

# muon d0 < 50 microns
muon_d0_lessThan50_cut = cms.PSet(
    inputCollection = cms.vstring("muons","beamspots"),
    cutString = cms.string("10000*abs("+muonSmearedD0WRTBeamspot+") < 50"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 muons with |d_0| < 50 mum")
    )

# muon d0 > 50 microns
muon_d0_greaterThan50_cut = cms.PSet(
    inputCollection = cms.vstring("muons","beamspots"),
    cutString = cms.string("10000*abs("+muonSmearedD0WRTBeamspot+") > 50"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 muons with |d_0| > 50 mum")
    )

# muon 50 < d0 < 100 microns
muon_d0_50to100_cut = cms.PSet(
    inputCollection = cms.vstring("muons","beamspots"),
    cutString = cms.string("10000*abs("+muonSmearedD0WRTBeamspot+") > 50 & 10000*abs("+muonSmearedD0WRTBeamspot+") < 100"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 muons with 50 < |d_0| < 100 mum")
    )

# muon d0 < 100 microns
muon_d0_lessThan100_cut = cms.PSet(
    inputCollection = cms.vstring("muons","beamspots"),
    cutString = cms.string("10000*abs("+muonSmearedD0WRTBeamspot+") < 100"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 muons with |d_0| < 100 mum")
    )

# muon d0 > 100 microns
muon_d0_greaterThan100_cut = cms.PSet(
    inputCollection = cms.vstring("muons","beamspots"),
    cutString = cms.string("10000*abs("+muonSmearedD0WRTBeamspot+") > 100"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 muons with |d_0| > 100 mum")
    )

# exactly one muon w/ d0 > 100 microns
muon_d0_greaterThan100_exactly1_cut = cms.PSet(
    inputCollection = cms.vstring("muons","beamspots"),
    cutString = cms.string("10000*abs("+muonSmearedD0WRTBeamspot+") > 100"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("==1 muons with |d_0| > 100 mum")
    )

# muon 100 < d0 < 200 microns
muon_d0_100to200_cut = cms.PSet(
    inputCollection = cms.vstring("muons","beamspots"),
    cutString = cms.string("10000*abs("+muonSmearedD0WRTBeamspot+") > 100 & 10000*abs("+muonSmearedD0WRTBeamspot+") < 200"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 muons with 100 < |d_0| < 200 mum")
    )

# muon 100 < d0 < 500 microns
muon_d0_100to500_cut = cms.PSet(
    inputCollection = cms.vstring("muons","beamspots"),
    cutString = cms.string("10000*abs("+muonSmearedD0WRTBeamspot+") > 100 & 10000*abs("+muonSmearedD0WRTBeamspot+") < 500"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 muons with 100 < |d_0| < 500 mum")
    )

muon_d0_lessThan200_cut = cms.PSet(
    inputCollection = cms.vstring("muons","beamspots"),
    cutString = cms.string("10000*abs("+muonSmearedD0WRTBeamspot+") < 200"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 muons with |d_0| < 200 mum")
    )

muon_d0_greaterThan200_cut = cms.PSet(
    inputCollection = cms.vstring("muons","beamspots"),
    cutString = cms.string("10000*abs("+muonSmearedD0WRTBeamspot+") > 200"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 muons with |d_0| > 200 mum")
    )

# muon d0 < 300 microns
muon_d0_lessThan300_cut = cms.PSet(
    inputCollection = cms.vstring("muons","beamspots"),
    cutString = cms.string("10000*abs("+muonSmearedD0WRTBeamspot+") < 300"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 muons with |d_0| < 300 mum")
    )

# muon d0 > 300 microns
muon_d0_greaterThan300_cut = cms.PSet(
    inputCollection = cms.vstring("muons","beamspots"),
    cutString = cms.string("10000*abs("+muonSmearedD0WRTBeamspot+") > 300"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 muons with |d_0| > 300 mum")
    )

# muon 500 < d0 < 1000 microns
muon_d0_500to1000_cut = cms.PSet(
    inputCollection = cms.vstring("muons","beamspots"),
    cutString = cms.string("10000*abs("+muonSmearedD0WRTBeamspot+") > 500 & 10000*abs("+muonSmearedD0WRTBeamspot+") < 1000"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 muons with 500 < |d_0| < 1000 mum")
    )

muon_d0_lessThan2000_cut = cms.PSet(
    inputCollection = cms.vstring("muons","beamspots"),
    cutString = cms.string("abs("+muonSmearedD0WRTBeamspot+") < 0.2"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 muons with |d_0| < 0.2 cm")
    )

muon_d0Sig_greaterThan6_cut = cms.PSet(
    inputCollection = cms.vstring("muons","beamspots"),
    cutString = cms.string(""+muonD0WRTBeamspotSig+" > 6"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 muons with d0 significance > 6")
    )

muon_dZ_lessThan5000_cut = cms.PSet(
    inputCollection = cms.vstring("muons","primaryvertices"),
    cutString = cms.string("abs("+muonDZWRTBeamspot+") < 0.5"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 muons with dZ < 0.5 cm")
    )

muon_mt_cut = cms.PSet (
    inputCollection = cms.vstring("muons","mets"),
    cutString = cms.string("transMass(muon, met) < 50"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("muon m_{T} < 50 GeV")
    )

muon_num_exactly_1_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("exactly 1 muon")
    )

#####################
#BEGIN GEN MUON CUTS

muon_gen_motherIsW_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("abs(genMatchedParticle.noFlags.{}.pdgId) == 24".format(gen_mother_string)),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 muons from W (muon matched to gen particle whose mother has PDG ID of 24)")
)

muon_gen_motherIsTau_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("abs(genMatchedParticle.noFlags.{}.pdgId) == 15".format(gen_mother_string)),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 muons from Tau (muon matched to gen particle whose mother has PDG ID of 15)")
)

##########################################################################

# BEGIN ELECTRON-MUON CUTS

emu_mass_20_cut = cms.PSet (
    inputCollection = cms.vstring("electrons", "muons"),
    cutString = cms.string("invMass(electron,muon) > 20"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 electron-muon pair with invariant mass > 20 GeV")
    )

emu_mass_lessThan100_cut = cms.PSet (
    inputCollection = cms.vstring("electrons", "muons"),
    cutString = cms.string("invMass(electron,muon) < 100"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 electron-muon pair with invariant mass < 100GeV")
    )

emu_opposite_charge_cut = cms.PSet (
    inputCollection = cms.vstring("electrons", "muons"),
    cutString = cms.string("electron.charge * muon.charge < 0"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 oppositely-charged e-mu pair")
    )

emu_samesign_cut = cms.PSet (
    inputCollection = cms.vstring("electrons", "muons"),
    cutString = cms.string("electron.charge * muon.charge > 0"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 like-charged e-mu pair")
)

emu_pt_25_20_cut = cms.PSet (
    inputCollection = cms.vstring("electrons", "muons"),
    cutString = cms.string("(electron.pt > 25 & muon.pt > 20) | (electron.pt > 20 & muon.pt > 25)"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Leading lepton 25 pT, sub-leading 20 pT")
    )

emu_pt_greaterThan50_cut = cms.PSet (
    inputCollection = cms.vstring("electrons", "muons"),
    cutString = cms.string("pT(electron,muon) > 50"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("pT(e,mu) > 50")
    )

emu_deltaR_cut = cms.PSet (
    inputCollection = cms.vstring("electrons", "muons"),
    cutString = cms.string("deltaR(electron,muon) > 0.5"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 well separated e-mu pair (#DeltaR > 0.5)")
    )

emu_correlated_d0_cut = cms.PSet (
    inputCollection = cms.vstring("electrons", "muons","beamspots"),
    cutString = cms.string("abs(abs(10000*"+electronSmearedD0WRTBeamspot+") - abs(10000*"+muonSmearedD0WRTBeamspot+")) <= 3"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 e-mu pair w/ correlated |d0|")
    )

emu_uncorrelated_d0_cut = cms.PSet (
    inputCollection = cms.vstring("electrons", "muons","beamspots"),
    cutString = cms.string("abs(abs(10000*"+electronSmearedD0WRTBeamspot+") - abs(10000*"+muonSmearedD0WRTBeamspot+")) > 3"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 e-mu pair w/ uncorrelated |d0|")
    )

emu_correlated_genD0_cut = cms.PSet (
    inputCollection = cms.vstring("electrons", "muons","beamspots"),
    cutString = cms.string("abs(abs(10000*electron.genD0) - abs(10000*muon.genD0)) <= 3"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 e-mu pair w/ correlated |genD0|")
    )

emu_uncorrelated_genD0_cut = cms.PSet (
    inputCollection = cms.vstring("electrons", "muons","beamspots"),
    cutString = cms.string("abs(abs(10000*electron.genD0) - abs(10000*muon.genD0)) > 3"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 e-mu pair w/ uncorrelated |genD0|")
    )


##########################################################################
# ELECTRON-JET OVERLAP VETO
electron_jet_deltaR_overlap_veto = cms.PSet (
        inputCollection = cms.vstring("electrons", "jets"),
        cutString = cms.string("deltaR(electron, jet) < 0.5"),
        numberRequired = cms.string("== 0"),
        isVeto = cms.bool(True),
        alias = cms.string("electron near jet veto (#DeltaR < 0.5))")
)

##########################################################################
# MUON-JET OVERLAP VETO
muon_jet_deltaR_overlap_veto = cms.PSet (
        inputCollection = cms.vstring("muons", "jets"),
        cutString = cms.string("deltaR(muon, jet) < 0.5"),
        numberRequired = cms.string("== 0"),
        isVeto = cms.bool(True),
        alias = cms.string("muon near jet veto (#DeltaR < 0.5)")
)

##########################################################################

# BEGIN MET CUTS

met_pt_40_cut = cms.PSet(
    inputCollection = cms.vstring("mets"),
    cutString = cms.string("pt > 40"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("met > 40")
    )

met_pt_60_cut =  cms.PSet (
    inputCollection = cms.vstring("mets"),
    cutString = cms.string("pt > 60"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("met > 60")
    )

##########################################################################

# BEGIN PHOTON CUTS

photon_lwp_id_cut = cms.PSet(
    inputCollection = cms.vstring("photons"),
    cutString = cms.string("passesVID_looseID"),
    numberRequired = cms.string(">= 0"),
    alias = cms.string(">=0 photons with versioned loose ID") # includes isolation
    )

photon_mwp_id_cut = cms.PSet(
    inputCollection = cms.vstring("photons"),
    cutString = cms.string("passesVID_mediumID"),
    numberRequired = cms.string(">= 0"),
    alias = cms.string(">=0 photons with versioned medium ID") # includes isolation
    )

photon_twp_id_cut = cms.PSet(
    inputCollection = cms.vstring("photons"),
    cutString = cms.string("passesVID_tightID"),
    numberRequired = cms.string(">= 0"),
    alias = cms.string(">=0 photons with versioned tight ID") # includes isolation
    )

photon_passElectronVeto_cut = cms.PSet(
    inputCollection = cms.vstring("photons"),
    cutString = cms.string("passElectronVeto"),
    numberRequired = cms.string(">= 0"),
    alias = cms.string(">=0 photons that pass the electron veto")
    )

photon_noPixelSeed_cut = cms.PSet(
    inputCollection = cms.vstring("photons"),
    cutString = cms.string("hasPixelSeed == 0"),
    numberRequired = cms.string(">= 0"),
    alias = cms.string(">=0 photons without a pixel seed")
    )

photon_genMatched_cut = cms.PSet(
    inputCollection = cms.vstring("photons"),
    cutString = cms.string("abs(genMatchedParticle.bestMatch.pdgId) == 22"),
    numberRequired = cms.string(">= 0"),
    alias = cms.string(">=0 photons matched to gen particle with PDG ID of 22")
    )

##########################################################################

# BEGIN EVENTVARIABLE CUTS

pass_trigger = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("eventvariable.passTrigger"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("pass trigger specified in config file")
    )

##########################################################################

# BEGIN CUTS TO REDUCE OVERLAP BETWEEN CHANNELS

# function to faciliate combining cuts by getting the cutstring and without the 'cms.string()'
def get_cutstring(cut):
   return str(cut.cutString)[12:-2]

# cut to veto events with a displaced electron that would pass the emu preselection electron selection
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    electron_emu_pt_cut = copy.deepcopy(electron_pt_42_cut)
elif (os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_")):
    electron_emu_pt_cut = copy.deepcopy(electron_pt_50_cut)

displaced_electron_emu_preselection_veto = cms.PSet(
    inputCollection = cms.vstring("electrons","beamspots"),
    cutString = cms.string("({}) & (electron.{}) & (electron.{}) & ({}) & ({})".format(
        get_cutstring(electron_eta_cut),
        get_cutstring(electron_emu_pt_cut),
        get_cutstring(electron_id_cut),
        get_cutstring(electron_iso_cut),
        get_cutstring(electron_d0_greaterThan100_cut)
        )),
    numberRequired = cms.string("== 0"),
    alias = cms.string("veto events with displaced electrons that pass the emu preselection electron selection")
    )

# cut to veto events with a displaced muon that would pass the emu preselection muon selection
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    muon_emu_pt_cut = copy.deepcopy(muon_pt_40_cut)
elif (os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_")):
    muon_emu_pt_cut = copy.deepcopy(muon_pt_50_cut)

displaced_muon_emu_preselection_veto = cms.PSet(
    inputCollection = cms.vstring("muons","beamspots"),
    cutString = cms.string("({}) & (muon.{}) & ({}) & ({}) & ({}) & ({})".format(
        get_cutstring(muon_eta_cut),
        get_cutstring(muon_emu_pt_cut),
        get_cutstring(muon_global_cut),
        get_cutstring(muon_id_cut),
        get_cutstring(muon_iso_cut),
        get_cutstring(muon_d0_greaterThan100_cut)
        )),
    numberRequired = cms.string("== 0"),
    alias = cms.string("veto events with displaced muons that pass the emu preselection muon selection")
    )
