#!/usr/bin/env python
import sys
import os
import re
import time
from array import array
import math
from ROOT import TFile, TH2D, TH1D,TFile, gROOT, TGraphErrors, Double, TF1, TF2, TCanvas  

def FittingFunctionTurnOn(x,par):
    return par[2] / (1 + math.exp(-par[1]*(x[0] - par[0])))
def FittingFunctionStraightLine(x,par):
    return par[0]
def Round2DHistograms(histogram, precision):
    newHistogram = histogram.Clone()
    for j in range(1, histogram.GetYaxis().GetNbins() + 1):
        for i in range(1, histogram.GetXaxis().GetNbins() + 1): 
            newHistogram.SetBinContent(i, j, round(histogram.GetBinContent(i,j), precision))
            newHistogram.SetBinError(i, j, round(histogram.GetBinError(i,j), precision))
    return newHistogram

inputFileMC = TFile("/data/users/bing/condor/TriggerEfficiencyStudy_Dec2nd/TTJets_Lept_MiniAOD.root")
DenHistogramObj = inputFileMC.Get("TTbartoEMuMETTriggerMCPlotter/Electron-muon-beamspot Plots/electronPtMuonPtExtended")
NumHistogramObj = inputFileMC.Get("TTbartoEMuMETTriggerMCPassEMuTriggerPlotter/Electron-muon-beamspot Plots/electronPtMuonPtExtended")
NumHistogram = NumHistogramObj.Clone().ProjectionX("Num",0,-1,"e")
DenHistogram = DenHistogramObj.Clone().ProjectionX("Den",0,-1,"e")
xBins = array('d',[0,40,45,50,55,60,70,80,100,120])
yBins = array('d',[0,40,45,50,55,60,70,80,100,120])
NumHistogramNew = NumHistogram.Rebin(9,"numnew", xBins)
DenHistogramNew = DenHistogram.Rebin(9,"dennew", xBins)
EffHistogramMC = NumHistogramNew
EffHistogramMC.Sumw2()
EffHistogramMC.Divide(NumHistogramNew,DenHistogramNew,1,1,"B")
#EffHistogramMC = TGraphAsymmErrors()
#EffHistogramMC.BayesDivide(NumHistogramNew,DenHistogramNew,"w");

inputFileData = TFile("/data/users/bing/condor/TriggerEfficiencyStudy_Dec2nd/MET_2015D.root")
outputFile = TFile("DataMCRatio_Muon.root", "RECREATE")
DenHistogramObj = inputFileData.Get("TTbartoEMuMETTriggerPlotter/Electron-muon-beamspot Plots/electronPtMuonPtExtended")
NumHistogramObj = inputFileData.Get("TTbartoEMuMETTriggerPassEMuTriggerPlotter/Electron-muon-beamspot Plots/electronPtMuonPtExtended")
NumHistogram = NumHistogramObj.Clone().ProjectionX("Num",0,-1,"e")
DenHistogram = DenHistogramObj.Clone().ProjectionX("Den",0,-1,"e")
xBins = array('d',[0,40,45,50,55,60,70,80,100,120])
yBins = array('d',[0,40,45,50,55,60,70,80,100,120])
NumHistogramNew = NumHistogram.Rebin(9,"Parameter Summary", xBins)
DenHistogramNew = DenHistogram.Rebin(9,"dennew", xBins)
EffHistogramData = NumHistogramNew
EffHistogramData.Sumw2()
EffHistogramData.Divide(NumHistogramNew,DenHistogramNew,1,1,"B")
#EffHistogramData = TGraphAsymmErrors()
#EffHistogramData.BayesDivide(NumHistogramNew,DenHistogramNew,"w");

RatioHistogram = EffHistogramData.Clone()
RatioHistogram.Sumw2()
RatioHistogram.Divide(EffHistogramData,EffHistogramMC,1,1)

Fitting = TF1("Fitting",FittingFunctionStraightLine,0,500,3)
Fitting.SetParName(0, "efficiency")
Fitting.SetParameter(0, 1)
RatioHistogram.Fit(Fitting)

RatioHistogram.Write()
outputFile.Close()



DenHistogramObj = inputFileMC.Get("TTbartoEMuMETTriggerMCPlotter/Electron-muon-beamspot Plots/electronPtMuonPtExtended")
NumHistogramObj = inputFileMC.Get("TTbartoEMuMETTriggerMCPassEMuTriggerPlotter/Electron-muon-beamspot Plots/electronPtMuonPtExtended")
NumHistogram = NumHistogramObj.Clone().ProjectionY("Num",0,-1,"e")
DenHistogram = DenHistogramObj.Clone().ProjectionY("Den",0,-1,"e")
xBins = array('d',[0,40,45,50,55,60,70,80,100,120])
yBins = array('d',[0,40,45,50,55,60,70,80,100,120])
NumHistogramNew = NumHistogram.Rebin(9,"numnew", yBins)
DenHistogramNew = DenHistogram.Rebin(9,"dennew", yBins)
EffHistogramMC = NumHistogramNew
EffHistogramMC.Sumw2()
EffHistogramMC.Divide(NumHistogramNew,DenHistogramNew,1,1,"B")
#EffHistogramMC = TGraphAsymmErrors()
#EffHistogramMC.BayesDivide(NumHistogramNew,DenHistogramNew,"w");

outputFile = TFile("DataMCRatio_Electron.root", "RECREATE")
DenHistogramObj = inputFileData.Get("TTbartoEMuMETTriggerPlotter/Electron-muon-beamspot Plots/electronPtMuonPtExtended")
NumHistogramObj = inputFileData.Get("TTbartoEMuMETTriggerPassEMuTriggerPlotter/Electron-muon-beamspot Plots/electronPtMuonPtExtended")
NumHistogram = NumHistogramObj.Clone().ProjectionY("Num",0,-1,"e")
DenHistogram = DenHistogramObj.Clone().ProjectionY("Den",0,-1,"e")
xBins = array('d',[0,40,45,50,55,60,70,80,100,120])
yBins = array('d',[0,40,45,50,55,60,70,80,100,120])
NumHistogramNew = NumHistogram.Rebin(9,"Parameter Summary", yBins)
DenHistogramNew = DenHistogram.Rebin(9,"dennew", yBins)
EffHistogramData = NumHistogramNew
EffHistogramData.Sumw2()
EffHistogramData.Divide(NumHistogramNew,DenHistogramNew,1,1,"B")
#EffHistogramData = TGraphAsymmErrors()
#EffHistogramData.BayesDivide(NumHistogramNew,DenHistogramNew,"w");

RatioHistogram = EffHistogramData.Clone()
RatioHistogram.Sumw2()
RatioHistogram.Divide(EffHistogramData,EffHistogramMC,1,1)

Fitting = TF1("Fitting",FittingFunctionStraightLine,0,500,3)
Fitting.SetParName(0, "efficiency")
Fitting.SetParameter(0, 1)
RatioHistogram.Fit(Fitting)

RatioHistogram.Write()
outputFile.Close()


Canvas = TCanvas("Ratio")

DenHistogramObj = inputFileMC.Get("TTbartoEMuMETTriggerMCPlotter/Electron-muon-beamspot Plots/electronPtMuonPtExtended")
NumHistogramObj = inputFileMC.Get("TTbartoEMuMETTriggerMCPassEMuTriggerPlotter/Electron-muon-beamspot Plots/electronPtMuonPtExtended")
NumHistogram = NumHistogramObj.Clone()
DenHistogram = DenHistogramObj.Clone()
xBins = array('d',[0,40,45,50,60,80,100])
yBins = array('d',[0,40,45,50,60,80,100])
NumHistogramNew = TH2D("Efficiency","Efficiency",6,xBins,6,yBins)
for j in range(1, NumHistogram.GetYaxis().GetNbins() + 1):
  for i in range(1, NumHistogram.GetXaxis().GetNbins() + 1): 
    NumHistogramNew.Fill(NumHistogram.GetXaxis().GetBinCenter(i),NumHistogram.GetYaxis().GetBinCenter(j),NumHistogram.GetBinContent(i,j));
DenHistogramNew = TH2D("Efficiency","Efficiency",6,xBins,6,yBins)
for j in range(1, DenHistogram.GetYaxis().GetNbins() + 1):
  for i in range(1, DenHistogram.GetXaxis().GetNbins() + 1): 
    DenHistogramNew.Fill(DenHistogram.GetXaxis().GetBinCenter(i),DenHistogram.GetYaxis().GetBinCenter(j),DenHistogram.GetBinContent(i,j));
EffHistogramMC = NumHistogramNew
EffHistogramMC.Sumw2()
EffHistogramMC.Divide(NumHistogramNew,DenHistogramNew,1,1,"B");
EffHistogramMC = Round2DHistograms(EffHistogramMC,3)

outputFile = TFile("DataMCRatio2D.root", "RECREATE")
DenHistogramObj = inputFileData.Get("TTbartoEMuMETTriggerPlotter/Electron-muon-beamspot Plots/electronPtMuonPtExtended")
NumHistogramObj = inputFileData.Get("TTbartoEMuMETTriggerPassEMuTriggerPlotter/Electron-muon-beamspot Plots/electronPtMuonPtExtended")
NumHistogram = NumHistogramObj.Clone()
DenHistogram = DenHistogramObj.Clone()
xBins = array('d',[0,40,45,50,60,80,100])
yBins = array('d',[0,40,45,50,60,80,100])
NumHistogramNew = TH2D("Efficiency","Efficiency",6,xBins,6,yBins)
for j in range(1, NumHistogram.GetYaxis().GetNbins() + 1):
  for i in range(1, NumHistogram.GetXaxis().GetNbins() + 1): 
    NumHistogramNew.Fill(NumHistogram.GetXaxis().GetBinCenter(i),NumHistogram.GetYaxis().GetBinCenter(j),NumHistogram.GetBinContent(i,j));
DenHistogramNew = TH2D("Efficiency","Efficiency",6,xBins,6,yBins)
for j in range(1, DenHistogram.GetYaxis().GetNbins() + 1):
  for i in range(1, DenHistogram.GetXaxis().GetNbins() + 1): 
    DenHistogramNew.Fill(DenHistogram.GetXaxis().GetBinCenter(i),DenHistogram.GetYaxis().GetBinCenter(j),DenHistogram.GetBinContent(i,j));
EffHistogramData = NumHistogramNew
EffHistogramData.Sumw2()
EffHistogramData.Divide(NumHistogramNew,DenHistogramNew,1,1,"B");
EffHistogramData = Round2DHistograms(EffHistogramData,3)

RatioHistogram = EffHistogramData
RatioHistogram.Sumw2()
RatioHistogram.Divide(EffHistogramData,EffHistogramMC,1,1)
RatioHistogram = Round2DHistograms(RatioHistogram,3)
RatioHistogram.SetDirectory(0)

Canvas.cd()
RatioHistogram.Draw("COLZ TEXT E")
Canvas.Write()
outputFile.Close()
inputFileData.Close()
inputFileMC.Close()
