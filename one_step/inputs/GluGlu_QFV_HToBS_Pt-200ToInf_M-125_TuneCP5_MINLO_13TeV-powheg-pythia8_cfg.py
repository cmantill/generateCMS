import FWCore.ParameterSet.Config as cms

# link to datacards: 
# https://github.com/cms-sw/genproductions/blob/9c5b7ae58b582c259019bc846c0234e3e97ff901/bin/Powheg/production/2017/13TeV/Higgs/HJ_MINLO_Pt-200ToInf/HJ_MiNLO_NNPDF31_13TeV.input

externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
    args = cms.vstring('/cvmfs/cms.cern.ch/phys_generator/gridpacks/UL/13TeV/powheg/V2/HJ_slc7_amd64_gcc820_CMSSW_10_6_29_HJ_MINLO_Pt-200ToInf-v3/v1/HJ_slc7_amd64_gcc820_CMSSW_10_6_29_HJ_MINLO_Pt-200ToInf-v3.tgz'),
    nEvents = cms.untracked.uint32(5000),
    generateConcurrently = cms.untracked.bool(True),
    numberOfParameters = cms.uint32(1),
    outputFile = cms.string('cmsgrid_final.lhe'),
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh')
)

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *
from Configuration.Generator.PSweightsPythia.PythiaPSweightsSettings_cfi import *
from Configuration.Generator.Pythia8PowhegEmissionVetoSettings_cfi import *

generator = cms.EDFilter("Pythia8HadronizerFilter",
                                    comEnergy = cms.double(13000.0),
                                    filterEfficiency = cms.untracked.double(1),
                                    maxEventsToPrint = cms.untracked.int32(1),
                                    pythiaHepMCVerbosity = cms.untracked.bool(False),
                                    pythiaPylistVerbosity = cms.untracked.int32(1),
                                    PythiaParameters = cms.PSet(
                           pythia8CommonSettingsBlock,
                           pythia8CP5SettingsBlock,
                           pythia8PSweightsSettingsBlock,
                           pythia8PowhegEmissionVetoSettingsBlock,
                                         processParameters = cms.vstring('POWHEG:nFinal = 2',
                                                                         '25:m0 = 125.0', 
                                                                         '25:addChannel 1 0.001 100 5 -3', 
                                                                         '25:addChannel 1 0.001 100 3 -5', 
                                                                         '25:onMode = off', 
                                                                         '25:onIfMatch 5 3'),
                          parameterSets = cms.vstring(
                                        'pythia8PowhegEmissionVetoSettings',
                                        'pythia8CommonSettings',
                                        'pythia8CP5Settings',
                                        'pythia8PSweightsSettings',
                                        'processParameters',
                                        )
                          )
            )
