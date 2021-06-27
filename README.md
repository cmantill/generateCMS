# gen_flatHiggs
Generation config scripts for flat mass samples

## Setup

```
# clone repo
git clone git@github.com:cmantill/gen_flatHiggs.git
```

## Generation step
```
cmsrel CMSSW_9_3_16
cd CMSSW_9_3_16/src/

# setup crab
cmsenv
source /cvmfs/cms.cern.ch/common/crab-setup.sh prod

# copy generation scripts
cp PATH/gen_flatHiggs/generation_step/*.py .

# change settings in crab submission script: multi_crab_submit_GravitonToHHToWWWW_step0
# use JME-RunIIFall17GS-00017-GravitonToHHToWWWW_cfg.py for old generation
# use JME-RunIIFall17GS-00017-GravitonToHHToWWWW_highMX_cfg.py for new generation part 1
# use JME-RunIIFall17GS-00017-GravitonToHHToWWWW_highMX_part2_cfg.py for new generation part 2
# use JME-RunIIFall17GS-00017-GravitonToHHToWWWW_lnuqq_cfg.py for lnuqq generation part 1

# change output directory in crab config and configuration file/name

# submit crab job
python multi_crab_submit_GravitonToHHToWWWW_step0.py
```

## Simulation step

```

# setup	CMSSW
cmsrel CMSSW_9_4_7
cd CMSSW_9_4_7/src/

cmsenv
source /cvmfs/cms.cern.ch/common/crab-setup.sh prod

# Copy configs
cp PATH/gen_flatHiggs/simulation_step/*.py .

STEP1
# get dataset name of the private dataset with `crab status crab_directory_of_private_sample`
# change output directory in crab config and configuration file/name
python multi_crab_submit_step1.py
```