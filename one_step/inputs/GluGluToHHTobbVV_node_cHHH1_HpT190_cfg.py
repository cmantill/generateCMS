import FWCore.ParameterSet.Config as cms

externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
    args = cms.vstring('/cvmfs/cms.cern.ch/phys_generator/gridpacks/2017/13TeV/powheg/V2/GluGluToHH/ggHH_EWChL_slc7_amd64_gcc700_CMSSW_10_6_19_cHHH1_working.tgz'),
    nEvents = cms.untracked.uint32(1),
    numberOfParameters = cms.uint32(1),
    outputFile = cms.string('cmsgrid_final.lhe'),
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh')
)


from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *
from Configuration.Generator.PSweightsPythia.PythiaPSweightsSettings_cfi import *
from Configuration.Generator.Pythia8PowhegEmissionVetoSettings_cfi import *

generator = cms.EDFilter("Pythia8HadronizerFilter",
    PythiaParameters = cms.PSet(
            pythia8CommonSettingsBlock,
            pythia8CP5SettingsBlock,
            pythia8PSweightsSettingsBlock,
            pythia8PowhegEmissionVetoSettingsBlock,
            processParameters = cms.vstring('POWHEG:nFinal = 2', 
                                            '25:m0 = 125.0', 
                                            '25:onMode = off', 
                                            '25:onIfMatch = 5 -5', 
                                            '25:onIfMatch = 23 23', 
                                            '25:onIfMatch = 24 -24', 
                                            'ResonanceDecayFilter:filter = on', 
                                            'ResonanceDecayFilter:exclusive = on', 
                                            'ResonanceDecayFilter:eMuTauAsEquivalent = on', 
                                            'ResonanceDecayFilter:allNuAsEquivalent = on', 
                                            'ResonanceDecayFilter:udscAsEquivalent = on', 
                                            'ResonanceDecayFilter:mothers = 23,24,25', 
                                            'ResonanceDecayFilter:daughters = 5,5,1,1,1,1'),
            parameterSets=cms.vstring(
                    "pythia8CommonSettings",
                    "pythia8CP5Settings",
                    "pythia8PSweightsSettings",
                    "pythia8PowhegEmissionVetoSettings",
                    "processParameters",
            )
    ),
    comEnergy = cms.double(13000.0),
    filterEfficiency = cms.untracked.double(1.0),
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    pythiaPylistVerbosity = cms.untracked.int32(1)
)

gencount = cms.EDFilter("CandViewCountFilter",
    minNumber = cms.uint32(1),
    src = cms.InputTag("genfilter")
)

genfilter = cms.EDFilter("GenParticleSelector",
                                 cut = cms.string('(pdgId==25) && pt>190. && isLastCopy()'),
                                 src = cms.InputTag("genParticlesForFilter")
)

genParticlesForFilter = cms.EDProducer("GenParticleProducer",
    abortOnUnknownPDGCode = cms.untracked.bool(False),
    saveBarCodes = cms.untracked.bool(True),
    src = cms.InputTag("generator","unsmeared")
)

LHEHiggsPtFilter = cms.EDFilter("LHEPtFilter",
  selectedPdgIds = cms.vint32(25),
  ptMin=cms.double(135.),
  ptMax=cms.double(1e10),
  src=cms.InputTag("externalLHEProducer")
)

ProductionFilterSequence = cms.Sequence(LHEHiggsPtFilter+generator+genParticlesForFilter+genfilter+gencount)
