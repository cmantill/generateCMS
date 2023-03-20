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

export SCRAM_ARCH=slc7_amd64_gcc700
export RELEASE=CMSSW_10_6_30_patch1
export RELEASE_HLT=CMSSW_8_0_36_UL_patch1
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

# following workflows 20UL chain
# copied from https://cms-pdmv.cern.ch/mcm/chained_requests?contains=EXO-RunIISummer20UL16MiniAODAPVv2-01795&page=0&shown=15

# begin LHEGEN
# SEED=$(($(date +%s) % 100000 + 1))
# SEED=$((${BEGINSEED} + ${JOBNUM}))
SEED=$(((${BEGINSEED} + ${JOBNUM}) * 100))

# need to specify seeds otherwise gridpacks will be chosen from the same routine!!
# remember to identify process.RandomNumberGeneratorService.externalLHEProducer.initialSeed="int(${SEED})" and externalLHEProducer->generator!!
echo Configuration/GenProduction/python/${PROCNAME}.py
cmsDriver.py Configuration/GenProduction/python/${PROCNAME}.py --python_filename wmLHEGEN_cfg.py --eventcontent RAWSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN --fileout file:lhegen.root --conditions 106X_mcRun2_asymptotic_preVFP_v8 --beamspot Realistic25ns13TeV2016Collision --customise_commands process.RandomNumberGeneratorService.generator.initialSeed="int(${SEED})"\\nprocess.source.numberEventsInLuminosityBlock="cms.untracked.uint32(100)" --step LHE,GEN --geometry DB:Extended --era Run2_2016_HIPM --mc --nThreads $NTHREAD -n $NEVENT # || exit $? ;

# begin SIM
cmsDriver.py  --python_filename SIM_cfg.py --eventcontent RAWSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM --fileout file:sim.root --conditions 106X_mcRun2_asymptotic_preVFP_v8 --beamspot Realistic25ns13TeV2016Collision --step SIM --geometry DB:Extended --filein file:lhegen.root --era Run2_2016_HIPM --runUnscheduled --mc --nThreads $NTHREAD -n $NEVENT || exit $? ;

# begin DRPremix
cmsDriver.py  --python_filename DIGIPremix_cfg.py --eventcontent PREMIXRAW --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM-DIGI --fileout file:digi.root --pileup_input "dbs:/Neutrino_E-10_gun/RunIISummer20ULPrePremix-UL16_106X_mcRun2_asymptotic_v13-v1/PREMIX" --conditions 106X_mcRun2_asymptotic_preVFP_v8 --step DIGI,DATAMIX,L1,DIGI2RAW --procModifiers premix_stage2 --geometry DB:Extended --filein file:sim.root --datamix PreMix --era Run2_2016_HIPM --runUnscheduled --mc --nThreads $NTHREAD -n $NEVENT > digi.log 2>&1 || exit $? ; # too many output, log into file 

# begin HLT
# load new cmssw env
if [ -r $RELEASE_HLT/src ] ; then
  echo release $RELEASE_HLT already exists
else
  scram p CMSSW $RELEASE_HLT
fi
cd $RELEASE_HLT/src
eval `scram runtime -sh`
cd $WORKDIR
cmsDriver.py  --python_filename HLT_cfg.py --eventcontent RAWSIM --outputCommand "keep *_mix_*_*,keep *_genPUProtons_*_*" --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM-RAW --inputCommands "keep *","drop *_*_BMTF_*","drop *PixelFEDChannel*_*_*_*" --fileout file:hlt.root --conditions 80X_mcRun2_asymptotic_2016_TrancheIV_v6 --customise_commands 'process.source.bypassVersionCheck = cms.untracked.bool(True)' --step HLT:25ns15e33_v4 --geometry DB:Extended --filein file:digi.root --era Run2_2016 --mc --nThreads $NTHREAD -n $NEVENT || exit $? ;

# begin RECO
# reload original env
cd ${CMSSW_BASE_ORIG}/src
eval `scram runtime -sh`
cd $WORKDIR

cmsDriver.py  --python_filename RECO_cfg.py --eventcontent AODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier AODSIM --fileout file:reco.root --conditions 106X_mcRun2_asymptotic_preVFP_v8 --step RAW2DIGI,L1Reco,RECO,RECOSIM --geometry DB:Extended --filein file:hlt.root --era Run2_2016_HIPM --runUnscheduled --mc --nThreads $NTHREAD -n $NEVENT || exit $? ;

## Run MiniAODv2 with -j FrameworkJobReport.xml 
cmsDriver.py  --python_filename MiniAODv2_cfg.py --eventcontent MINIAODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier MINIAODSIM --fileout file:miniv2.root --conditions 106X_mcRun2_asymptotic_preVFP_v11 --step PAT --procModifiers run2_miniAOD_UL --geometry DB:Extended --filein file:reco.root --era Run2_2016_HIPM --runUnscheduled --mc --nThreads $NTHREAD -n $NEVENT || exit $? ;

# uncomment if need to produce miniaod
# cmsDriver.py  --python_filename MiniAODv2_cfg.py --eventcontent MINIAODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier MINIAODSIM --fileout file:miniv2.root --conditions 106X_mcRun2_asymptotic_preVFP_v11 --step PAT --procModifiers run2_miniAOD_UL --geometry DB:Extended --filein file:reco.root --era Run2_2016_HIPM --runUnscheduled --mc --nThreads $NTHREAD -n $NEVENT --no_exec || exit $? ;
# cmsRun -j FrameworkJobReport.xml MiniAODv2_cfg.py

# comment if need to produce miniaod
## Run NanoAODv9
cmsDriver.py  --python_filename NanoAODv9_cfg.py --eventcontent NANOAODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier NANOAODSIM --fileout file:nanov9.root --conditions 106X_mcRun2_asymptotic_preVFP_v11 --step NANO --filein file:miniv2.root --era Run2_2016_HIPM,run2_nanoAOD_106Xv2 --mc --nThreads $NTHREAD -n $NEVENT --no_exec || exit $? ;
cmsRun -j FrameworkJobReport.xml NanoAODv9_cfg.py
