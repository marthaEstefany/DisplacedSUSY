 #!/usr/bin/env python
import os
from DisplacedSUSY.Configuration.limitOptions import *

#################################################################################
#################################################################################
### this file contains all information pertaining to systematic uncertainties ###
#################################################################################
#################################################################################


#####################################################
### signal cross sections and their uncertainties ###
#####################################################

#taken from https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SUSYCrossSections13TeVslepslep#NLO_NLL_any_single_generation_su
signal_cross_sections_sleptons_13TeV = {

    '50' : {
        'value' : '5.368',
        'error' : '1.039',
    },
    '100' : {
        'value' : '0.3657',
        'error' : '1.018',
    },
    '150' : {
        'value' : '0.08712',
        'error' : '1.017',
    },
    '200' : {
        'value' : '0.03031',
        'error' : '1.020',
    },
    '250' : {
        'value' : '0.01292',
        'error' : '1.021',
    },
    '300' : {
        'value' : '0.006254',
        'error' : '1.023',
    },
    '350' : {
        'value' : '0.002931',
        'error' : '1.026',
    },
    '400' : {
        'value' : '0.001859',
        'error' : '1.029',
    },
    '450' : {
        'value' : '0.001216',
        'error' : '1.031',
    },
    '500' : {
        'value' : '0.0006736',
        'error' : '1.033',
    },
    '600' : {
        'value' : '0.0002763',
        'error' : '1.036',
    },
    '700' : {
        'value' : '0.0001235',
        'error' : '1.038',
    },
    '800' : {
        'value' : '5.863e-05',
        'error' : '1.042',
    },
    '900' : {
        'value' : '2.918e-05',
        'error' : '1.046',
    },
    '1000' : {
        'value' : '1.504e-05',
        'error' : '1.052',
    },
}

#xs for sleptons * (BF tau-->electron/muon)^2,
#i.e. (.1782+.1739)^2 = 0.124
#because apply a lepton filter that only accepts events in which both taus decay leptonically
signal_cross_sections_staus_13TeV = {

    '50' : {
        'value' : '0.6656',
        'error' : '0.129',
    },
    '100' : {
        'value' : '0.04535',
        'error' : '0.126',
    },
    '150' : {
        'value' : '0.01080',
        'error' : '0.126',
    },
    '200' : {
        'value' : '0.003758',
        'error' : '0.126',
    },
    '250' : {
        'value' : '0.001602',
        'error' : '0.127',
    },
    '300' : {
        'value' : '0.0007755',
        'error' : '0.127',
    },
    '350' : {
        'value' : '0.0003634',
        'error' : '0.127',
    },
    '400' : {
        'value' : '0.0002305',
        'error' : '0.128',
    },
    '450' : {
        'value' : '0.0001508',
        'error' : '0.128',
    },
    '500' : {
        'value' : '0.00008353',
        'error' : '0.128',
    },
    '600' : {
        'value' : '0.00003426',
        'error' : '0.128',
    },
    '700' : {
        'value' : '0.00001531',
        'error' : '0.129',
    },
    '800' : {
        'value' : '7.270e-06',
        'error' : '0.129',
    },
    '900' : {
        'value' : '3.618e-06',
        'error' : '0.130',
    },
    '1000' : {
        'value' : '1.865e-06',
        'error' : '0.130',
    },
}

#from gridpacks
signal_cross_sections_HToSS_13TeV = {

    '110' : {
        'value' : '26.722390956061719',
        'error' : '1.0929',
    },
    '125' : {
        'value' : '21.459897483726280',
        'error' : '1.0740',
    },
    '150' : {
        'value' : '15.614146187994139',
        'error' : '1.0699',
    },
    '200' : {
        'value' : '8.7322438914694018',
        'error' : '1.0717',
    },
    '300' : {
        'value' : '4.9382937444987762',
        'error' : '1.0683',
    },
    '400' : {
        'value' : '5.0403083882366619',
        'error' : '1.0678',
    },
    '450' : {
        'value' : '3.7768002561767382',
        'error' : '1.0680',
    },
    '500' : {
        'value' : '2.5884317279268005',
        'error' : '1.0678',
    },
    '600' : {
        'value' : '1.1784666241700483',
        'error' : '1.0673',
    },
    '750' : {
        'value' : '0.41086256828334200',
        'error' : '1.0666',
    },
    '800' : {
        'value' : '0.30253991148407361',
        'error' : '1.0664',
    },
    '900' : {
        'value' : '0.17493668485618005',
        'error' : '1.0661',
    },
    '1000' : {
        'value' : '0.10770210813460095',
        'error' : '1.0663',
    },

}

#taken from https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SUSYCrossSections13TeVstopsbottom (NLO+NLL)
signal_cross_sections_13TeV = {

    '20' : { #H cross section
      'value' : '43.92',
      'error' : '1.10',
    },
    '50' : { #H cross section
      'value' : '43.92',
      'error' : '1.10',
    },


    '100' : {
      'value' : '1521.11',
      'error' : '1.154038',
    },
    '150' : {
      'value' : '249.409',
      'error' : '1.147477',
    },
    '175' : {
      'value' : '121.416',
      'error' : '1.146341',
    },
    '200' : {
      'value' : ' 64.5085',
      'error' : '1.144098',
    },
    '300' : {
      'value' : '8.51615',
      'error' : '1.139223',
    },
    '400' : {
      'value' : '1.83537',
      'error' : '1.136985',
    },
    '500' : {
      'value' : '0.51848',
      'error' : '1.133797',
    },
    '600' : {
      'value' : '0.174599',
      'error' : '1.132074',
    },
    '700' : {
      'value' : '0.0670476',
      'error' : '1.133429',
    },
    '800' : {
      'value' : '0.0283338',
      'error' : '1.14171',
    },
    '900' : {
      'value' : '0.0128895',
      'error' : '1.152026',
    },
    '1000' : {
      'value' : '0.00615134',
      'error' : '1.162953',
    },
    '1100' : {
      'value' : '0.00307413',
      'error' : '1.173377',
    },
    '1200' : {
      'value' : '0.00159844',
      'error' : '1.185209',
    },
    '1300' : {
      'value' : '0.000850345',
      'error' : '1.201604',
    },
    '1400' : {
      'value' : '0.000461944',
      'error' : '1.222704',
    },
    '1500' : {
      'value' : '0.000256248',
      'error' : '1.24372',
    },
    '1600' : {
      'value' : '0.000141382',
      'error' : '1.265291',
    },
    '1700' : {
      'value' : '8.07774e-05',
      'error' : '1.287497',
    },
    '1800' : {
      'value' : '4.67492e-05',
      'error' : '1.312291',
    },
    '1900' : {
      'value' : '2.73974e-05',
      'error' : '1.338247',
    },
    '2000' : {
      'value' : '1.62355e-05',
      'error' : '1.365277',
    },
}


signal_cross_sections_8TeV = {

    '200' : {
      'value' : '18.5245',
      'error' : '1.149147',
    },
    '300' : {
      'value' : '1.99608',
      'error' : '1.146905',
    },
    '400' : {
      'value' : '0.35683',
      'error' : '1.142848',
    },
    '500' : {
      'value' : '0.0855847',
      'error' : '1.149611',
    },
    '600' : {
      'value' : '0.0248009',
      'error' : '1.166406',
    },
    '700' : {
      'value' : '0.0081141',
      'error' : '1.184146',
    },
    '800' : {
      'value' : '0.00289588',
      'error' : '1.20516',
    },
    '900' : {
      'value' : '0.00109501',
      'error' : '1.239439',
    },
}


######################################################
### Experimental Systematic Uncertainty Parameters ###
######################################################

# list of backgrounds for which we take the yield from MC in some way
mc_normalized_processes = [
    'signal'
]


# uncertainties for which the same value applies to all datasets
global_systematic_uncertainties = {
    '2016' : {
        # taken from https://twiki.cern.ch/twiki/bin/viewauth/CMS/TWikiLUM#LumiComb
        'lumi_uncorrelated_2016' :  {
            'value' : '1.022',
            'applyList' : mc_normalized_processes,
            'channels' : ['ee', 'emu', 'mumu'],
        },
        'lumi_xyFactorization' :  {
            'value' : '1.009',
            'applyList' : mc_normalized_processes,
            'channels' : ['ee', 'emu', 'mumu'],
        },
        'lumi_beamBeamDeflection' :  {
            'value' : '1.004',
            'applyList' : mc_normalized_processes,
            'channels' : ['ee', 'emu', 'mumu'],
        },
        'lumi_dynamicBeta' :  {
            'value' : '1.005',
            'applyList' : mc_normalized_processes,
            'channels' : ['ee', 'emu', 'mumu'],
        },
        'lumi_ghostsAndSatellites' :  {
            'value' : '1.004',
            'applyList' : mc_normalized_processes,
            'channels' : ['ee', 'emu', 'mumu'],
        },

        # taken from the error on the trigger effieciency scale factor, see elog 1875
        'trigger_emu_electron' :  {
            'value' : '1.016',
            'applyList' : mc_normalized_processes,
            'channels' : ['emu'],
        },
        'trigger_emu_muon' :  {
            'value' : '1.016',
            'applyList' : mc_normalized_processes,
            'channels' : ['emu'],
        },
        'trigger_ee' :  {
            'value' : '1.099',
            'applyList' : mc_normalized_processes,
            'channels' : ['ee'],
        },
        'trigger_mumu' :  {
            'value' : '1.012',
            'applyList' : mc_normalized_processes,
            'channels' : ['mumu'],
        },

        #additional systematic to cover drop in muon trigger efficiency at large d0, see elog 1889
        'additional_trigger_emu_muon' :  {
            'value' : '1.20',
            'applyList' : mc_normalized_processes,
            'channels' : ['emu'],
        },
        'additional_trigger_mumu' :  {
            'value' : '1.20',
            'applyList' : mc_normalized_processes,
            'channels' : ['mumu'],
        },


        #taken from Ian's study
        'track_reco2016' :  { #2016 uncorrelated with 2017 and 2018 due to different pixel detector in 2016
            'value' : '1.141',
            'applyList' : ['signal'],
            'channels' : ['ee', 'emu', 'mumu'],
        }
    },
    '2017' : {
        # taken from https://twiki.cern.ch/twiki/bin/viewauth/CMS/TWikiLUM#LumiComb
        'lumi_uncorrelated_2017' :  {
            'value' : '1.020',
            'applyList' : mc_normalized_processes,
            'channels' : ['ee', 'emu', 'mumu'],
        },
        'lumi_xyFactorization' :  {
            'value' : '1.008',
            'applyList' : mc_normalized_processes,
            'channels' : ['ee', 'emu', 'mumu'],
        },
        'lumi_lengthScale' :  {
            'value' : '1.003',
            'applyList' : mc_normalized_processes,
            'channels' : ['ee', 'emu', 'mumu'],
        },
        'lumi_beamBeamDeflection' :  {
            'value' : '1.004',
            'applyList' : mc_normalized_processes,
            'channels' : ['ee', 'emu', 'mumu'],
        },
        'lumi_dynamicBeta' :  {
            'value' : '1.005',
            'applyList' : mc_normalized_processes,
            'channels' : ['ee', 'emu', 'mumu'],
        },
        'lumi_beamCurrentCalibration' :  {
            'value' : '1.003',
            'applyList' : mc_normalized_processes,
            'channels' : ['ee', 'emu', 'mumu'],
        },
        'lumi_ghostsAndSatellites' :  {
            'value' : '1.001',
            'applyList' : mc_normalized_processes,
            'channels' : ['ee', 'emu', 'mumu'],
        },

        # taken from the error on the trigger effieciency scale factor, see elog 1875
        'trigger_emu_electron' :  {
            'value' : '1.013',
            'applyList' : mc_normalized_processes,
            'channels' : ['emu'],
        },
        'trigger_emu_muon' :  {
            'value' : '1.014',
            'applyList' : mc_normalized_processes,
            'channels' : ['emu'],
        },
        'trigger_ee' :  {
            'value' : '1.131',
            'applyList' : mc_normalized_processes,
            'channels' : ['ee'],
        },
        'trigger_mumu' :  {
            'value' : '1.010',
            'applyList' : mc_normalized_processes,
            'channels' : ['mumu'],
        },

        #additional systematic to cover drop in muon trigger efficiency at large d0, see elog 1889
        'additional_trigger_emu_muon' :  {
            'value' : '1.20',
            'applyList' : mc_normalized_processes,
            'channels' : ['emu'],
        },
        'additional_trigger_mumu' :  {
            'value' : '1.20',
            'applyList' : mc_normalized_processes,
            'channels' : ['mumu'],
        },

        #taken from Ian's study
        'track_reco' :  {
            'value' : '1.058',
            'applyList' : ['signal'],
            'channels' : ['ee', 'emu', 'mumu'],
        }
    },
    '2018' : {
        # taken from https://twiki.cern.ch/twiki/bin/viewauth/CMS/TWikiLUM#LumiComb
        'lumi_uncorrelated_2018' :  {
            'value' : '1.015',
            'applyList' : mc_normalized_processes,
            'channels' : ['ee', 'emu', 'mumu'],
        },
        'lumi_xyFactorization' :  {
            'value' : '1.020',
            'applyList' : mc_normalized_processes,
            'channels' : ['ee', 'emu', 'mumu'],
        },
        'lumi_lengthScale' :  {
            'value' : '1.002',
            'applyList' : mc_normalized_processes,
            'channels' : ['ee', 'emu', 'mumu'],
        },
        'lumi_beamCurrentCalibration' :  {
            'value' : '1.002',
            'applyList' : mc_normalized_processes,
            'channels' : ['ee', 'emu', 'mumu'],
        },

        # taken from the error on the trigger effieciency scale factor, see elog 1875
        'trigger_emu_electron' :  {
            'value' : '1.012',
            'applyList' : mc_normalized_processes,
            'channels' : ['emu'],
        },
        'trigger_emu_muon' :  {
            'value' : '1.012',
            'applyList' : mc_normalized_processes,
            'channels' : ['emu'],
        },
        'trigger_ee' :  {
            'value' : '1.185',
            'applyList' : mc_normalized_processes,
            'channels' : ['ee'],
        },
        'trigger_mumu' :  {
            'value' : '1.011',
            'applyList' : mc_normalized_processes,
            'channels' : ['mumu'],
        },

        #additional systematic to cover drop in muon trigger efficiency at large d0, see elog 1889
        'additional_trigger_emu_muon' :  {
            'value' : '1.20',
            'applyList' : mc_normalized_processes,
            'channels' : ['emu'],
        },
        'additional_trigger_mumu' :  {
            'value' : '1.20',
            'applyList' : mc_normalized_processes,
            'channels' : ['mumu'],
        },

        #taken from Ian's study
        'track_reco' :  {
            'value' : '1.024',
            'applyList' : mc_normalized_processes,
            'channels' : ['ee', 'emu', 'mumu'],
        }
    }
}



# uncertainties that have different values for each dataset
unique_systematic_uncertainties = {
}


# defined in external text files (located in DisplacedSUSY/Configuration/data)
# external systematics with the same base name (i.e. BASE_CHANNEL_YEAR) will be treated as correlated across years
external_systematic_uncertainties = [
        'pileup_emu_2016',
        'pileup_ee_2016',
        'pileup_mumu_2016',
        'pileup_emu_2017',
        'pileup_ee_2017',
        'pileup_mumu_2017',
        'pileup_emu_2018',
        'pileup_ee_2018',
        'pileup_mumu_2018',

        'electronIDandIso_emu_2016',
        'muonIDandIso_emu_2016',
        'electronIDandIso_ee_2016',
        'muonIDandIso_mumu_2016',
        'electronIDandIso_emu_2017',
        'muonIDandIso_emu_2017',
        'electronIDandIso_ee_2017',
        'muonIDandIso_mumu_2017',
        'electronIDandIso_emu_2018',
        'muonIDandIso_emu_2018',
        'electronIDandIso_ee_2018',
        'muonIDandIso_mumu_2018',

        # there was no d0 smearing in 2016
        'electronD0Smearing_emu_2017',
        'muonD0Smearing_emu_2017',
        'electronD0Smearing_ee_2017',
        'muonD0Smearing_mumu_2017',
        'electronD0Smearing_emu_2018',
        'muonD0Smearing_emu_2018',
        'electronD0Smearing_ee_2018',
        'muonD0Smearing_mumu_2018',

    #make 2016 not correlated with (2017+2018) due to different pixel detectors
    'muonPixelHitEff16_emu_2016',
    'muonPixelHitEff16_mumu_2016',
    'muonPixelHitEff_emu_2017',
    'muonPixelHitEff_mumu_2017',
    'muonPixelHitEff_emu_2018',
    'muonPixelHitEff_mumu_2018',
]
