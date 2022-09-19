import FWCore.ParameterSet.Config as cms

# link to cards:
# https://github.com/portalesHEP/genproductions/tree/8268afa49656697442cf771d359f964a52b641e1/bin/MadGraph5_aMCatNLO/cards/production/2017/13TeV/NMSSM_XToYH

externalLHEProducer = cms.EDProducer('ExternalLHEProducer',
                                     args = cms.vstring('/cvmfs/cms.cern.ch/phys_generator/gridpacks/UL/13TeV/madgraph/V5_2.6.5/NMSSM_XYH/NMSSM_XToYH_MX_{mxx}_MY_{myy}/v1/NMSSM_XToYH_MX_{mxx}_MY_{myy}_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz'),
                                     nEvents = cms.untracked.uint32(5000),
                                     numberOfParameters = cms.uint32(1),
                                     outputFile = cms.string('cmsgrid_final.lhe'),
                                     generateConcurrently = cms.untracked.bool(True),
                                     scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh')
)


from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *
from Configuration.Generator.PSweightsPythia.PythiaPSweightsSettings_cfi import *

generator = cms.EDFilter("Pythia8ConcurrentHadronizerFilter",
                         maxEventsToPrint = cms.untracked.int32(1),
                         pythiaPylistVerbosity = cms.untracked.int32(1),
                         filterEfficiency = cms.untracked.double(1.0),
                         pythiaHepMCVerbosity = cms.untracked.bool(False),
                         comEnergy = cms.double(13000.),
                         PythiaParameters = cms.PSet(
                                                     pythia8CommonSettingsBlock,
                                                     pythia8CP5SettingsBlock,
                                                     pythia8PSweightsSettingsBlock,
                                                     processParameters = cms.vstring(
                                                                                                                                                                                                                                                
    '25:onMode = off', # Turn off all H decays
    '25:oneChannel = 1 1 100 5 -5', # H->bb
    '25:onIfMatch = 22 22',
    '35:onMode = off',
    '35:oneChannel = 1 1 100 22 22',  # Y->gamma gamma
    # '35:onIfMatch = 5 -5',
    'ResonanceDecayFilter:filter = on',
    'ResonanceDecayFilter:exclusive = on', #off: require at least the specified number of daughters, on: require exactly the specified number of daughters
    'ResonanceDecayFilter:mothers = 25,35', #list of mothers not specified -> count all particles in hard process+resonance decays (better to avoid specifying mothers when including leptons from the lhe in counting, since intermediate resonances are not gauranteed to appear in general
    'ResonanceDecayFilter:daughters = 5,5,22,22',

                                                     ),
                                                     parameterSets = cms.vstring('pythia8CommonSettings',
                                                                                 'pythia8CP5Settings',
                                                                                 'pythia8PSweightsSettings',
                                                                                 'processParameters'
                                                                                 )
                                                     )
                         )


ProductionFilterSequence = cms.Sequence(generator)
