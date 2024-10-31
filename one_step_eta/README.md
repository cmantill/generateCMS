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

Submit with dataset name and name of CSV file (accesible via xrootd):
```
python3 multi_crab_submit_csv.py  --name OUTPUT_DATASET --csvname CSVLOCATION
```

e.g.
```
python3 multi_crab_submit_csv.py  --name EtaToGammaAp_ApToEE_ApToEE_Ap0p300GeV_EtaPt10 --csvname  root://cmseos.fnal.gov//store/user/cmantill/EtaToGammaApr/
```




