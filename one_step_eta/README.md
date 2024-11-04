# Eta to Gamma Aprime

## Generate Eta->GammaAprime -> Gamma + ElectronElectron

Use environment with pythia8 (run locally).

May use docker image (https://github.com/matthewfeickert/pythia-python):
```
docker run \
  --rm \
  -ti \
  --volume $PWD:/home/docker/work \
  matthewfeickert/pythia-python:latest
```

Generate events:
```
python EtaToGammaAp_ApToEE.py --nevents NEVENTS --mvector MASS[GeV] --ptfilter PTCUT[GeV] --seed SEEDINTEGER
```
This script will generate a CSV file. Copy it to CSV_LOCATION (/eos/ or similar)

## One step sequence in crab

1. Submit from el8 (At least this is where it has been tested)
2. Activate CRAB in cmsenv environment (do not use CMSSW_12_4_16)
   ```
   cmsrel CMSSW_13_0_13
   cd CMSSW_13_0_13/src/
   cmsenv
   git clone https://github.com/cmantill/generateCMS.git
   cd generateCMS/one_step_eta/
   ```
   Then:
   ```
   source /cvmfs/cms.cern.ch/common/crab-setup.sh
   ```
   
3. Edit lines in CSV file to allow GIT to recognize username: e.g. https://github.com/cmantill/generateCMS/blob/233fcb0e3b220d2e0d94945fe0d8165fb7a0d3a1/one_step_eta/exe_2022EE_csv.sh#L36-L38

4. Submit with dataset name and name of CSV file (accesible via xrootd):
```
python3 multi_crab_submit_csv.py  --name OUTPUT_DATASET --csvname CSVLOCATION
```

e.g.
```
python3 multi_crab_submit_csv.py  --name EtaToGammaAp_ApToEE_ApToEE_Ap0p300GeV_EtaPt10 --csvname  root://cmseos.fnal.gov//store/user/cmantill/EtaToGammaApr/
```
