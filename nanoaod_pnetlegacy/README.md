# Production nanoAODv12

- Get release
```
cmsrel CMSSW_13_0_13
cd CMSSW_13_0_13/src/
cmsenv
git cms-checkout-topic cmantill:13_0_13_pNetLegacy
scram b -j 10
```

- Clone repo
```
git clone https://github.com/cmantill/generateCMS.git
cd generateCMS/nanoaod_pnetlegacy/
```

- Edit `submit_nanoaod.py` with the samples to submit

- Submit samples, specify era, key and username, e.g.:
```
python3 submit_nanoaod.py --era 2022EE --key mc --username cmantill
```