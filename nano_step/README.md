# Private NanoAOD

## Recipe for NanoAODv11 with modified PNet training for AK4 (and no ParT scores for AK4)

```
cmsrel CMSSW_12_6_4
cd CMSSW_12_6_4/src
eval `scram runtime -sh`
scram b
```

# Modify NanoAOD
```
git cms-addpkg PhysicsTools/NanoAOD
git clone -b nanov11-btagak4 https://github.com/cmantill/generateCMS.git
cp generateCMS/nano_step/LeptonInJetProducer.cc PhysicsTools/NanoAOD/plugins/LeptonInJetProducer.cc
cp generateCMS/nano_step/jetsAK4_Puppi_cff.py PhysicsTools/NanoAOD/python/jetsAK4_Puppi_cff.py
cp  generateCMS/nano_step/triggerObjects_cff.py PhysicsTools/NanoAOD/python/triggerObjects_cff.py 
scram b -j 8
```

Note: At some point, we	will switch to ReReco
https://cms-pdmv-prod.web.cern.ch/pmp/historical?r=27Jun2023&showDoneRequestsList=true
Run3_2022_rereco, 124X_dataRun3_v15

2022-ABCDPrompt
```
cmsDriver.py --python_filename test_nanoTuples_data2022_ABCDPrompt_cfg.py --eventcontent NANOAOD --datatier NANOAOD --customise_commands "process.options.wantSummary = cms.untracked.bool(True)" \
--fileout file:nano_data2022_PromptNano.root \
--conditions 124X_dataRun3_PromptAnalysis_v1 --step NANO --scenario pp \
--filein /store/data/Run2022D/MuonEG/MINIAOD/PromptReco-v1/000/357/542/00000/750cf639-99bb-401a-a9b2-2b82d17a3082.root \
--era Run3,run3_nanoAOD_124 --nThreads 4 --no_exec --data -n 100
```

2022-EFGPrompt
```
# adapted from: https://cmsweb.cern.ch/couchdb/reqmgr_config_cache/10fc675e782eab01d6a5188185536e42/configFile
# adapted from Marina
cmsDriver.py --python_filename test_nanoTuples_data2022_EFGPrompt_cfg.py --eventcontent NANOAOD --datatier NANOAOD --customise Configuration/DataProcessing/Utils.addMonitoring \
--fileout file:nano_data2022_PromptNano.root \
--conditions 124X_dataRun3_Prompt_v10 --step NANO --scenario pp \
--filein /store/data/Run2022G/MuonEG/MINIAOD/PromptReco-v1/000/362/365/00000/c54ae566-34fd-4c05-87d8-b011b542ecc4.root \
--era Run3,run3_nanoAOD_124 --nThreads 4 --no_exec --data -n 100
```

2022-MC Run3Summer22:
```
cmsDriver.py --python_filename test_nanoTuples_mc2022.py --eventcontent NANOAODSIM --datatier NANOAODSIM \
--fileout file:nano_mc2022_v11.root \
--conditions 126X_mcRun3_2022_realistic_v2 --step NANO --scenario pp \
--filein /store/mc/Run3Summer22MiniAODv3/GluGluHto2B_PT-200_M-125_TuneCP5_13p6TeV_powheg-minlo-pythia8/MINIAODSIM/124X_mcRun3_2022_realistic_v12-v2/40000/06ecc7c6-d1d0-4ae5-8438-c3dfd666a6e7.root \
--era Run3,run3_nanoAOD_124 --nThreads 4 --no_exec --mc -n 100
```

2022-MC Run3Summer22EE:
```
cmsDriver.py --python_filename test_nanoTuples_mc2022EE.py --eventcontent NANOAODSIM --datatier NANOAODSIM \
--fileout file:nano_mc2022EE_v11.root \
--conditions 126X_mcRun3_2022_realistic_postEE_v1 --step NANO --scenario pp \
--filein /store/mc/Run3Summer22EEMiniAODv3/GluGluHto2B_PT-200_M-125_TuneCP5_13p6TeV_powheg-minlo-pythia8/MINIAODSIM/124X_mcRun3_2022_realistic_postEE_v1-v2/40000/01eb51b6-9cf1-44a5-8aa4-df1b60c1ccd5.root \
--era Run3,run3_nanoAOD_124 --nThreads 4 --no_exec --mc	-n 100
```

# To Submit

e.g.
```
python3 submit.py -y samples_MC_2022EE.yaml --username cmantill
```