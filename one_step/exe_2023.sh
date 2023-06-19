#!/bin/bash -x

## NOTE: difference made w.r.t. common exe script
## 1. __NEVENT__ not specify in the fragment
## 2. no LHE step, also need to change externalLHEProducer to generator
## 3. seeds have width 100

env

JOBNUM=${1##*=} # hard coded by crab
NEVENT=${2##*=} # ordered by crab.py script
NTHREAD=${3##*=} # ordered by crab.py script
PROCNAME=${4##*=} # ordered by crab.py script
BEGINSEED=${5##*=}

WORKDIR=`pwd`

export SCRAM_ARCH=el8_amd64_gcc10
export RELEASE=CMSSW_12_6_4
source /cvmfs/cms.cern.ch/cmsset_default.sh

if [ -r $RELEASE/src ] ; then
  echo release $RELEASE already exists
else
  scram p CMSSW $RELEASE
fi
cd $RELEASE/src
eval `scram runtime -sh`
CMSSW_BASE_ORIG=${CMSSW_BASE}

# untar CMSSW code
#tar xaf $WORKDIR/inputs/cmssw.tar.gz

# copy the fragment
mkdir -p Configuration/GenProduction/python/
cp $WORKDIR/inputs/${PROCNAME}.py Configuration/GenProduction/python/${PROCNAME}.py
# replace the event number
# NOTE: this routine does not specify NEVENT in the fragment
# grep -q "__NEVENT__" Configuration/GenProduction/python/${PROCNAME}.py || exit $? ;
sed "s/__NEVENT__/$NEVENT/g" -i Configuration/GenProduction/python/${PROCNAME}.py
eval `scram runtime -sh`
scram b -j $NTHREAD

cd $WORKDIR

# following workflows 
# copied from https://cms-pdmv.cern.ch/mcm/chained_requests?contains=TSG-Run3Winter23MiniAOD-00146

# begin LHEGEN
# SEED=$(($(date +%s) % 100000 + 1))
# SEED=$((${BEGINSEED} + ${JOBNUM}))
SEED=$(((${BEGINSEED} + ${JOBNUM}) * 100))

# need to specify seeds otherwise gridpacks will be chosen from the same routine!!
# remember to identify process.RandomNumberGeneratorService.externalLHEProducer.initialSeed="int(${SEED})" and externalLHEProducer->generator!!
echo Configuration/GenProduction/python/${PROCNAME}.py
cmsDriver.py Configuration/GenProduction/python/${PROCNAME}.py --python_filename wmLHEGEN_cfg.py --eventcontent RAWSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM --fileout file:sim.root \
--conditions 126X_mcRun3_2023_forPU65_v1 --beamspot Realistic25ns13p6TeVEarly2022Collision --customise_commands process.RandomNumberGeneratorService.generator.initialSeed="int(${SEED})"\\nprocess.source.numberEventsInLuminosityBlock="cms.untracked.uint32(100)" \
--step GEN,SIM --geometry DB:Extended --era Run3 --mc --nThreads $NTHREAD -n $NEVENT # || exit $? ;

# begin DRPremix
cmsDriver.py  --python_filename DIGIPremix_cfg.py --eventcontent RAWSIM --pileup 2023_LHC_Simulation_12p5h_9h_hybrid2p23 ---pileup_input "dbs:/MinBias_TuneCP5_13p6TeV-pythia8/Run3Winter23GS-126X_mcRun3_2023_forPU65_v1-v1/GEN-SIM" \
--step DIGI,L1,DIGI2RAW,HLT:2022v15 --geometry DB:Extended --filein file:sim.root --era Run3 --conditions 126X_mcRun3_2023_forPU65_v3 \
--customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM-RAW --fileout file:digi.root \
--customise_commands 'process.hltParticleFlowClusterHBHE.seedFinder.thresholdsByDetector[0].seedingThreshold=[0.6,0.5,0.5,0.5]\n process.hltParticleFlowClusterHBHE.initialClusteringStep.thresholdsByDetector[0].gatheringThreshold=[0.4,0.3,0.3,0.3]\n process.hltParticleFlowClusterHBHE.pfClusterBuilder.recHitEnergyNorms[0].recHitEnergyNorm=[0.4,0.3,0.3,0.3]\n process.hltParticleFlowClusterHBHE.pfClusterBuilder.positionCalc.logWeightDenominatorByDetector[0].logWeightDenominator=[0.4,0.3,0.3,0.3]\n process.hltParticleFlowClusterHBHE.pfClusterBuilder.allCellsPositionCalc.logWeightDenominatorByDetector[0].logWeightDenominator=[0.4,0.3,0.3,0.3]\n process.hltParticleFlowClusterHCAL.pfClusterBuilder.allCellsPositionCalc.logWeightDenominatorByDetector[0].logWeightDenominator=[0.4,0.3,0.3,0.3]\n process.hltParticleFlowRecHitHBHE.producers[0].qualityTests[0].cuts[0].threshold=[0.4,0.3,0.3,0.3]\n process.hltEgammaHoverE.eThresHB=[0.4,0.3,0.3,0.3]\n process.hltEgammaHoverEUnseeded.eThresHB=[0.4,0.3,0.3,0.3]\n process.hltEgammaHToverET.eThresHB=[0.4,0.3,0.3,0.3]\n process.hltFixedGridRhoFastjetECALMFForMuons.eThresHB=[0.4,0.3,0.3,0.3]\n process.hltFixedGridRhoFastjetAllCaloForMuons.eThresHB=[0.4,0.3,0.3,0.3]\n process.hltFixedGridRhoFastjetHCAL.eThresHB=[0.4,0.3,0.3,0.3]\n process.hltParticleFlowClusterHBHECPUOnly.seedFinder.thresholdsByDetector[0].seedingThreshold=[0.6,0.5,0.5,0.5]\n process.hltParticleFlowClusterHBHECPUOnly.initialClusteringStep.thresholdsByDetector[0].gatheringThreshold=[0.4,0.3,0.3,0.3]\n process.hltParticleFlowClusterHBHECPUOnly.pfClusterBuilder.recHitEnergyNorms[0].recHitEnergyNorm=[0.4,0.3,0.3,0.3]\n process.hltParticleFlowClusterHBHECPUOnly.pfClusterBuilder.positionCalc.logWeightDenominatorByDetector[0].logWeightDenominator=[0.4,0.3,0.3,0.3]\n process.hltParticleFlowClusterHBHECPUOnly.pfClusterBuilder.allCellsPositionCalc.logWeightDenominatorByDetector[0].logWeightDenominator=[0.4,0.3,0.3,0.3]\n process.hltParticleFlowClusterHCALCPUOnly.pfClusterBuilder.allCellsPositionCalc.logWeightDenominatorByDetector[0].logWeightDenominator=[0.4,0.3,0.3,0.3]\n process.hltParticleFlowRecHitHBHECPUOnly.producers[0].qualityTests[0].cuts[0].threshold=[0.4,0.3,0.3,0.3]\n process.hltTowerMakerForAll.HBThreshold1=0.4\n process.hltTowerMakerForAll.HBThreshold2=0.3\n process.hltTowerMakerForAll.HBThreshold=0.3' \
--runUnscheduled --mc --nThreads $NTHREAD -n $NEVENT > digi.log 2>&1 || exit $? ; # too many output, log into file 

# begin RECO
cmsDriver.py  --python_filename RECO_cfg.py --eventcontent AODSIM --customise RecoParticleFlow/PFClusterProducer/particleFlow_HB2023.customiseHB2023,Configuration/DataProcessing/Utils.addMonitoring \
--datatier GEN-SIM-RECO,AODSIM --fileout file:reco.root --filein file:sim.root --conditions 126X_mcRun3_2023_forPU65_v3 --step RAW2DIGI,L1Reco,RECO,RECOSIM --geometry DB:Extended \
--era Run3_2023 --mc --runUnscheduled --nThreads $NTHREAD -n $NEVENT || exit $? ;

## Run MiniAODv2 with -j FrameworkJobReport.xml 
cmsDriver.py  --python_filename MiniAOD_cfg.py --eventcontent MINIAODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier MINIAODSIM --fileout file:mini.root --conditions 126X_mcRun3_2023_forPU65_v3 --step PAT --geometry DB:Extended --filein file:reco.root --era Run3_2023 --runUnscheduled --mc --no_exec --nThreads $NTHREAD -n $NEVENT || exit $? ;
cmsRun -j FrameworkJobReport.xml MiniAOD_cfg.py

# comment if need to produce miniaod
## Run NanoAODv9
#cmsDriver.py  --python_filename NanoAOD_cfg.py --eventcontent NANOAODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier NANOAODSIM --fileout file:nano.root --conditions 126X_mcRun3_2023_forPU65_v3 --step NANO --filein file:mini.root --era Run3_2023  --mc --nThreads $NTHREAD -n $NEVENT --no_exec || exit $? ;
#cmsRun -j FrameworkJobReport.xml NanoAOD_cfg.py
