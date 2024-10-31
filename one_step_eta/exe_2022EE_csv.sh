#!/bin/bash -x

## NOTE: difference made w.r.t. common exe script
## 1. __NEVENT__ not specify in the fragment
# 2. no LHE step, also need to change externalLHEProducer to generator
## 3. seeds have width 100

env

JOBNUM=${1##*=} # hard coded by crab
NEVENT=${2##*=} # ordered by crab.py script
NTHREAD=${3##*=} # ordered by crab.py script
CSVNAME=${4##*=} # ordered by crab.py script
BEGINSEED=${5##*=}

WORKDIR=`pwd`

export SCRAM_ARCH=el8_amd64_gcc10
export RELEASE=CMSSW_13_0_13
export RELEASE_1=CMSSW_12_4_16
source /cvmfs/cms.cern.ch/cmsset_default.sh

if [ -r $RELEASE_1/src ] ; then
  echo release $RELEASE_1 already exists
  echo "not recommended if GEN setup is not there"  
  cd $RELEASE_1/src
  eval `scram runtime -sh`
  cmd="ls -lrth "
  echo $cmd
  eval $cmd
else
  echo "release does not exist"
  scram p CMSSW $RELEASE_1
  cd $RELEASE_1/src
  eval `scram runtime -sh`
  git config --global user.name cmantill
  git config --global user.email criss.ms7@gmail.com
  git config --global user.github cmantill
  git cms-init
  #git cms-merge-topic cmantill:CSVReader-CMSSW_13_0_13
  git cms-addpkg Configuration/Generator
  git cms-addpkg GeneratorInterface/Pythia8Interface
  wget https://raw.githubusercontent.com/cmantill/cmssw/refs/heads/CSVReader-CMSSW_13_0_13/GeneratorInterface/Pythia8Interface/plugins/Py8CSVReaderGun.cc
  mv Py8CSVReaderGun.cc  GeneratorInterface/Pythia8Interface/plugins/Py8CSVReaderGun.cc
  wget https://raw.githubusercontent.com/cmantill/cmssw/refs/heads/CSVReader-CMSSW_13_0_13/Configuration/Generator/python/CSVReader_pythia8_cfi.py
  mv CSVReader_pythia8_cfi.py Configuration/Generator/python/CSVReader_pythia8_cfi.py
  echo "Copying pythia csv events file."
  echo ${CSVNAME}
  xrdcp ${CSVNAME} GeneratorInterface/Pythia8Interface/test/EtaToGammaAp_ApToEE.csv
  ls -lrth GeneratorInterface/Pythia8Interface/test/EtaToGammaAp_ApToEE.csv
fi

# compile
scram b -j $NTHREAD

# list
cmd="ls -lrth "
echo $cmd
eval $cmd

# following workflows
# /EtaTo2MuGamma_PtExpGun_TuneCP5_13p6TeV-pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v2/MINIAODSIM
# copied from https://cms-pdmv-prod.web.cern.ch/mcm/requests?prepid=BPH-Run3Summer22EEMiniAODv4-00125

# begin LHEGEN
SEED=$(((${BEGINSEED} + ${JOBNUM}) * 100))

echo "1.) Generating GEN-SIM from CSV events"
echo Configuration/GenProduction/python/CSVReader_pythia8_cfi.py
# need to specify SEED otherwise events will be chosen from the same routine!!
cmsDriver.py Configuration/Generator/python/CSVReader_pythia8_cfi.py --python_filename wmLHEGEN_cfg.py --eventcontent RAWSIM --customise Configuration/DataProcessing/Utils.addMonitoring --fileout file:sim.root \
	     --customise_commands process.RandomNumberGeneratorService.generator.initialSeed="int(${SEED})"\\nprocess.source.numberEventsInLuminosityBlock="cms.untracked.uint32(100)" \
	     --conditions 124X_mcRun3_2022_realistic_postEE_v1 --beamspot Realistic25ns13p6TeVEarly2022Collision --step GEN,SIM --geometry DB:Extended --era Run3 --mc --nThreads $NTHREAD -n $NEVENT || exit $? ;

# begin DRPremix
echo "2.) Generating DRPRemix from GEN-SIM"
cmsDriver.py  --python_filename DIGIPremix_cfg.py --eventcontent PREMIXRAW --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM-RAW --filein file:sim.root \
	      --pileup_input "dbs:/Neutrino_E-10_gun/Run3Summer21PrePremix-Summer22_124X_mcRun3_2022_realistic_v11-v2/PREMIX" \
	      --conditions 124X_mcRun3_2022_realistic_postEE_v1 --step DIGI,DATAMIX,L1,DIGI2RAW,HLT:2022v14 --procModifiers premix_stage2,siPixelQualityRawToDigi --geometry DB:Extended \
	      --fileout file:digi.root --datamix PreMix --era Run3 --runUnscheduled --mc --nThreads $NTHREAD -n $NEVENT > digi.log 2>&1 || exit $? ; # too many outputs, log into file 

echo "2.1) Generating AODSIM"
cmsDriver.py  --python_filename DIGIPremix_2_cfg.py --eventcontent AODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier AODSIM --filein file:digi.root \
	      --fileout aodsim.root --conditions 124X_mcRun3_2022_realistic_postEE_v1 --step RAW2DIGI,L1Reco,RECO,RECOSIM --procModifiers siPixelQualityRawToDigi --geometry DB:Extended --era Run3 --mc --nThreads $NTHREAD -n $NEVENT > aodsim.log 2>&1 || exit $? ;

# copy output to workdir
cd $WORKDIR
ls -lrth $RELEASE_1/src
cp $RELEASE_1/src/aodsim.root .

if [ -r $RELEASE/src ] ; then
  echo release $RELEASE already exists
else
  scram p CMSSW $RELEASE
fi
cd $RELEASE/src
eval `scram runtime -sh`
cd $WORKDIR

## Run MiniAODv4 with -j FrameworkJobReport.xml
echo "3.) Generating MiniAOD"
cmsDriver.py  --python_filename MiniAOD_cfg.py --eventcontent MINIAODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier MINIAODSIM --fileout file:mini.root --conditions 130X_mcRun3_2022_realistic_postEE_v6 \
	       --step PAT --geometry DB:Extended --filein file:aodsim.root --era Run3,run3_miniAOD_12X --mc --nThreads $NTHREAD -n $NEVENT || exit $? ;
cmsRun -j FrameworkJobReport.xml MiniAOD_cfg.py

## TODO: Add NanoAOD custom routine
