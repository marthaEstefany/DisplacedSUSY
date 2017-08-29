import FWCore.ParameterSet.Config as cms
import copy
import string

import DisplacedSUSY.Configuration.objectDefinitions as objectDefs

##########################################################################

# BEGIN JET CUTS

jet_eta_cut = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("abs(eta) < 2.4"),
    numberRequired = cms.string(">= 0")
    )

jet_pt_30_cut = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("pt > 30"),
    numberRequired = cms.string(">= 0")
    )

jet_id_cut = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = objectDefs.jet_id_cutstring,
    numberRequired = cms.string(">= 0"),
    alias = objectDefs.jet_id_alias
    )

jet_eta_real_cut = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("abs(eta) < 2.4"),
    numberRequired = cms.string(">= 2"),
    alias = cms.string('>= 2 jets w/ eta < 2.4')
    )

jet_pt_30_real_cut = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("pt > 30"),
    numberRequired = cms.string(">= 2"),
    alias = cms.string('>= 2 jets w/ pT > 30GeV')
    )

jet_loose_id_cut = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = objectDefs.jet_loose_id_cutstring,
    numberRequired = cms.string(">= 2"),
    alias = objectDefs.jet_loose_id_alias
    )

# CSV WPs taken from here: https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagRecommendation80XReReco
jet_csvl_veto = cms.PSet (
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("pfCombinedInclusiveSecondaryVertexV2BJetTags > 0.5426"),
    numberRequired = cms.string("== 0"),
    isVeto = cms.bool(True)
    )

jet_csvm_veto = cms.PSet (
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("pfCombinedInclusiveSecondaryVertexV2BJetTags > 0.8484"),
    numberRequired = cms.string("== 0"),
    isVeto = cms.bool(True)
    )

jet_btag_twp_cut = cms.PSet (
        inputCollection = cms.vstring("jets"),
        cutString = cms.string("pfCombinedInclusiveSecondaryVertexV2BJetTags > 0.935"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string('>= 1 tight b tags')
    )

jet_btag_mwp_cut = cms.PSet (
        inputCollection = cms.vstring("jets"),
        cutString = cms.string("pfCombinedInclusiveSecondaryVertexV2BJetTags > 0.800"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string('>= 1 medium b tags')
    )

jet_btag_lwp_cut = cms.PSet (
        inputCollection = cms.vstring("jets"),
        cutString = cms.string("pfCombinedInclusiveSecondaryVertexV2BJetTags > 0.5426"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string('>= 1 loose b tags')
    )

jet_btag_2_mwp_cut = cms.PSet (
        inputCollection = cms.vstring("jets"),
        cutString = cms.string("pfCombinedInclusiveSecondaryVertexV2BJetTags > 0.800"),
        numberRequired = cms.string(">= 2"),
        alias = cms.string('>= 2 medium b tags')
    )

##########################################################################

# BEGIN MET CUTS

met_pt_40_cut = cms.PSet(
    inputCollection = cms.vstring("mets"),
    cutString = cms.string("pt > 40"),
    numberRequired = cms.string(">= 1")
    )

##########################################################################

# BEGIN MUON CUTS

muon_eta_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("abs(eta) < 2.4"),
    numberRequired = cms.string(">= 2")
    )

muon_pt_20_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("pt > 20"),
    numberRequired = cms.string(">= 2")
    )

muon_pt_25_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("pt > 25"),
    numberRequired = cms.string(">= 1")
    )

muon_pt_40_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("pt > 40"),
    numberRequired = cms.string(">= 2")
    )

muon_global_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = objectDefs.muon_global_cutstring,
    numberRequired = cms.string(">= 2"),
    alias = objectDefs.muon_global_alias
    )

muon_id_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = objectDefs.muon_id_cutstring,
    numberRequired = cms.string(">= 2"),
    alias = objectDefs.muon_id_alias
    )

muon_iso_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = objectDefs.muon_iso_cutstring,
    numberRequired = cms.string(">= 2"),
    alias = objectDefs.muon_iso_alias
    )

muon_antiiso_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = objectDefs.muon_antiiso_cutstring,
    numberRequired = cms.string(">= 2"),
    alias = objectDefs.muon_antiiso_alias
    )

muon_2muon_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string("== 2"),
    alias = cms.string("extra muon veto")
    )

diMuon_invMass_Z_cut = cms.PSet (
    inputCollection = cms.vstring("muons", "muons"),
    cutString = cms.string("abs(invMass(muon,muon) - 91.2) < 10"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("abs(mass_mumu - mass_Z) < 10")
    )

diMuon_invMass_OutsideZWindow_cut = cms.PSet (
    inputCollection = cms.vstring("muons", "muons"),
    cutString = cms.string("abs(invMass (muon,muon) - 91 > 15.0)"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("diMuon invariant mass < 76 GeV OR > 106 GeV")
    )

diMuon_invMass_above20_cut = cms.PSet (
    inputCollection = cms.vstring("muons", "muons"),
    cutString = cms.string("invMass (muon,muon) > 20.0"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("diMuon invariant mass > 20.0GeV")
    )


# muon d0 < 100 microns
muon_d0_lt100_cut = cms.PSet(
    inputCollection = cms.vstring("muons","beamspots"),
    cutString = cms.string("10000*abs(d0) < 100"),
    numberRequired = cms.string(">= 2"),
    alias = cms.string("muon d0 < 100 mum")
    )

# muon 100 < d0 < 200 microns
muon_d0_100to200_cut = cms.PSet(
    inputCollection = cms.vstring("muons","beamspots"),
    cutString = cms.string("10000*abs(d0) > 100 & 10000*abs(d0) < 200"),
    numberRequired = cms.string(">= 2"),
    alias = cms.string("muon 100 < d0 < 200 mum")
    )

# muon d0 > 100 microns
muon_d0_above100_cut = cms.PSet(
    inputCollection = cms.vstring("muons","beamspots"),
    cutString = cms.string("10000*abs(d0) > 100"),
    numberRequired = cms.string(">= 2"),
    alias = cms.string("muon d0 > 100 mum")
    )

# muon d0 < 200 microns
muon_d0_below200_cut = cms.PSet(
    inputCollection = cms.vstring("muons","beamspots"),
    cutString = cms.string("10000*abs(d0) < 200"),
    numberRequired = cms.string(">= 2"),
    alias = cms.string("muon d0 < 200 mum")
    )

muon_d0_below2000_cut = cms.PSet(
    inputCollection = cms.vstring("muons","beamspots"),
    cutString = cms.string(objectDefs.muonAbsD0_cm + " < 0.2"),
    numberRequired = cms.string(">= 2"),
    alias = cms.string("muon d0 < 0.2 cm")
    )

muon_dZ_below5000_cut = cms.PSet(
    inputCollection = cms.vstring("muons","beamspots"),
    cutString = cms.string(objectDefs.muonAbsDz + " < 5000"),
    numberRequired = cms.string(">= 2"),
    alias = cms.string("muon dZ < 0.5 cm")
    )

##########################################################################

# BEGIN MUON-JET CUTS

muonjet_deltaR_veto = cms.PSet(
    inputCollection = cms.vstring("muons","jets"),
    cutString = cms.string("deltaR(muon, jet) < 0.5"),
    numberRequired = cms.string("== 0"),
    isVeto = cms.bool(True)
    )
