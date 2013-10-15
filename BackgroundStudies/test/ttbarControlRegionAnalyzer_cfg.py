from OSUT3Analysis.AnaTools.osuAnalysis_cfi import *

###############################################################
##### Set Options for Running your Analyzer Interactively #####
###############################################################

dir = "/data/users/hart/condor/eMuMinimal/TTbar_Lep/EMu_Minimal/"

for file in os.listdir(dir):
        process.source.fileNames.extend(cms.untracked.vstring('file:' + dir + file))

process.OSUAnalysis.applyBtagSF = True
process.OSUAnalysis.doTopPtReweighting = True
        
########################################################################
##### Import the information about all the histograms to be filled #####
########################################################################

#import the desired sets of histograms from the standard python file which defines them
from OSUT3Analysis.Configuration.histogramDefinitions import *
from DisplacedSUSY.Configuration.histogramDefinitions import *

process.OSUAnalysis.histogramSets.append(ElectronHistograms)
process.OSUAnalysis.histogramSets.append(ElectronD0Histograms)

process.OSUAnalysis.histogramSets.append(MuonHistograms)
process.OSUAnalysis.histogramSets.append(MuonD0Histograms)

process.OSUAnalysis.histogramSets.append(ElectronMuonHistograms)
process.OSUAnalysis.histogramSets.append(ElectronMuonD0Histograms)

process.OSUAnalysis.histogramSets.append(JetHistograms)
process.OSUAnalysis.histogramSets.append(ElectronJetHistograms)
process.OSUAnalysis.histogramSets.append(MuonJetHistograms)

process.OSUAnalysis.histogramSets.append(EventHistograms)
process.OSUAnalysis.histogramSets.append(MetHistograms)

##########################################################
##### Add the Desired Channels to the List to be Run #####
##########################################################

from DisplacedSUSY.BackgroundStudies.TTbarControlRegion import *
#process.OSUAnalysis.channels.append(QCDinTTbarControlRegion_Prompt)
process.OSUAnalysis.channels.append(TTbarControlRegion_Prompt)
process.OSUAnalysis.channels.append(TTbarControlRegion_MuonPrompt)
process.OSUAnalysis.channels.append(TTbarControlRegion_ElectronPrompt)
#process.OSUAnalysis.channels.append(QCDinTTbarControlRegion_MuonPrompt)
#process.OSUAnalysis.channels.append(QCDinTTbarControlRegion_ElectronPrompt)
