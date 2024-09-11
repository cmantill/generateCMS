# Production nanoAODv12

- Get release
```
cmsrel CMSSW_13_0_13
cd CMSSW_13_0_13/src/
cmsenv
git cms-checkout-topic cmantill:13_0_13_ParT
wget https://coli.web.cern.ch/coli/tmp/.240120-181907_ak8_stage2/model.onnx -O $CMSSW_BASE/src/RecoBTag/ONNXRuntime/data/ParticleTransformerAK8/GlobalMD/V02/
scram b -j 10
```

- Clone repo
```
git clone https://github.com/cmantill/generateCMS.git -b ParT
cd generateCMS/nanoaod_pnetlegacy/
```

- Edit `submit_nanoaod.py` with the samples to submit
 
- To submit samples, specify era, key and username, e.g.:
```
python submit_nanoaod.py --era 2022EE --key mc --username cmantill
```

## Production Sep204

- Run container (NEEDS TO BE DONE EVERY TIME)
```
cmssw-el7 -p --bind `readlink $HOME` --bind `readlink -f ${HOME}/nobackup/` --bind /uscms_data --bind /cvmfs -- /bin/bash -l
voms-proxy-init --voms cms --valid 168:00
source /cvmfs/cms.cern.ch/crab3/crab.sh
```

- cmantill
```
python submit_nanoaod.py --era 2022 --key mc --username cmantill
python submit_nanoaod.py --era 2022EE --key mc --username cmantill
python submit_nanoaod.py --era 2023 --key mc --username cmantill
python submit_nanoaod.py --era 2023BPix --key mc --username cmantill
```

- woodson
```
python submit_nanoaod.py --era 2022 --key othermc --username cmantill
python submit_nanoaod.py --era 2022EE --key othermc --username cmantill
python submit_nanoaod.py --era 2023 --key othermc --username cmantill
python submit_nanoaod.py --era 2023BPix --key othermc --username cmantill
```

- sxie
```
python submit_nanoaod.py --era 2022 --key data --username sxie
python submit_nanoaod.py --era 2022EE --key data-C-E --username sxie
python submit_nanoaod.py --era 2022EE --key data-F-G --username sxie
python submit_nanoaod.py --era 2023 --key data --username sxie
python submit_nanoaod.py --era 2023BPix --key data --username sxie
```
