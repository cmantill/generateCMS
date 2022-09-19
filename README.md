# generateCMS
Generation config scripts for MC samples in CMS.

## Setup

```
# clone repo
git clone git@github.com:cmantill/generateCMS.git
```
## One step

This step does all of the GEN steps (step1 to step3 - miniAOD) in a single crab job. Make sure you are in a crab environment and that you have a proxy.

- Go into directory:
```
cd one_step/
```

- Add your input config to `inputs/`.

- Modify parameters in CRAB script. Common parameters to modify:
  - nevent
  - config.Data.totalUnits

- Submit files:
```
python multi_crab_submit_onestep.py --name NAME_OF_SAMPLE --config NAME_OF_INPUT_CONFIG  --begin-seed SEED --eosdir EOSDIR --site SITE
```

e.g.
```
python multi_crab_submit_onestep.py --name NMSSM_XToYH_MX1000_MY200_HtobbYtoWWhad --config NMSSM_XToYH_MX1000_MY200_HtobbYtoWWhad_cfg --begin-seed 0 --eosdir /store/group/lpcpfnano/cmantill/miniaod/2017/XHYPrivate/ --site T3_US_FNALLPC
```

## Generation step
NOTE: for `GluGluToHHTobbVV_node_cHHH1_HpT190_cfg.py` use `CMSSW_10_6_27` release.
```
cmsrel CMSSW_9_4_14_UL_patch1
cd CMSSW_9_4_14_UL_patch1/src/

# setup crab
cmsenv
source /cvmfs/cms.cern.ch/common/crab-setup.sh prod

# copy generation scripts
cp PATH/generateCMS/generation_step/*.py .

# submit crab job e.g.
python multi_crab_submit_step0.py --name GravitonToHHToWWWW --config GravitonToHHToWWWW_lowMX_cfg.py --eosdir EOSDIR --site SITE
```


## Simulation step

In CMSSW_10_6_20:
```
cmsrel CMSSW_10_6_20

# Copy configs
cp PATH/generateCMS/simulation_step/step1*.py .
cp PATH/generateCMS/simulation_step/multi_crab_submit_reco.py .

STEP1
# get dataset name of the private dataset with `crab status crab_directory_of_private_sample`, e.g.
python multi_crab_submit_reco.py --step 1 --dataset /GravitonToHHToWWWW_part1/cmantill-crab_PrivateProduction_Fall17_GravitonToHHToWWWW_part1_GENSIM_batch1_try3-166da30d6b0bc00e6b7f096d2276e006/USER --name GravitonToHHToWWWW
```

Go back to CMSSW_9_4_14_UL_patch1:
```
cp PATH/generateCMS/simulation_step/step1*.py .
cp PATH/generateCMS/simulation_step/multi_crab_submit_reco.py .

STEP1p5
python multi_crab_submit_reco.py --step 1p5 --dataset /GravitonToHHToWWWW_lnuqq/cmantill-crab_UL17_step1_lnuqq-c7276a76d06b45ee1f500f5860c54a3b/USER --name GravitonToHHToWWWW
```

In CMSSW_10_6_20:
```
# Copy configs
cp PATH/generateCMS/simulation_step/step2*.py . 
cp PATH/generateCMS/simulation_step/step3*.py .
cp PATH/generateCMS/simulation_step/multi_crab_submit_reco.py	.

STEP2
python multi_crab_submit_reco.py --step 2 --dataset /GravitonToHHToWWWW_lnuqq/cmantill-crab_UL17_HLT_step1p5_lnuqq-1cba7fad1227c919886864247a60b1e3/USER --name GravitonToHHToWWWW

STEP3
python multi_crab_submit_reco.py --step	2 --dataset /GravitonToHHToWWWW_lnuqq/cmantill-crab_UL17_RECO_step2_lnuqq-733eec30f6bf11e3a0accc1c2b7bc1aa/USER --name GravitonToHHToWWWW
```
