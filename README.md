# gen_flatHiggs
Generation config scripts for flat mass samples

## Setup

```
# clone repo
git clone git@github.com:cmantill/gen_flatHiggs.git
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
cp PATH/gen_flatHiggs/generation_step/*.py .

# submit crab job e.g.
python multi_crab_submit_step0.py --name GravitonToHHToWWWW --config GravitonToHHToWWWW_lowMX_cfg.py --eosdir EOSDIR --site SITE
```


## Simulation step

In CMSSW_9_4_14_UL_patch1:
```
# Copy configs
cp PATH/gen_flatHiggs/simulation_step/step1*.py .
cp PATH/gen_flatHiggs/simulation_step/multi_crab_submit_reco.py .

STEP1
# get dataset name of the private dataset with `crab status crab_directory_of_private_sample`, e.g.
python multi_crab_submit_reco.py --step 1 --dataset /GravitonToHHToWWWW_part1/cmantill-crab_PrivateProduction_Fall17_GravitonToHHToWWWW_part1_GENSIM_batch1_try3-166da30d6b0bc00e6b7f096d2276e006/USER --name GravitonToHHToWWWW

STEP1p5
python multi_crab_submit_reco.py --step 1p5 --dataset /GravitonToHHToWWWW_lnuqq/cmantill-crab_UL17_step1_lnuqq-c7276a76d06b45ee1f500f5860c54a3b/USER --name GravitonToHHToWWWW
```

In CMSSW_10_6_20:
```
cmsrel CMSSW_10_6_20

# Copy configs
cp PATH/gen_flatHiggs/simulation_step/step2*.py . 
cp PATH/gen_flatHiggs/simulation_step/step3*.py .
cp PATH/gen_flatHiggs/simulation_step/multi_crab_submit_reco.py	.

STEP2
python multi_crab_submit_reco.py --step 2 --dataset /GravitonToHHToWWWW_lnuqq/cmantill-crab_UL17_HLT_step1p5_lnuqq-1cba7fad1227c919886864247a60b1e3/USER --name GravitonToHHToWWWW

STEP3
python multi_crab_submit_reco.py --step	2 --dataset /GravitonToHHToWWWW_lnuqq/cmantill-crab_UL17_RECO_step2_lnuqq-733eec30f6bf11e3a0accc1c2b7bc1aa/USER --name GravitonToHHToWWWW
```
