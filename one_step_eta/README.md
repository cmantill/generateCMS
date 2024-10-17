# Eta to Gamma Aprime

## Generate Eta->GammaAprime -> GamamElectronElectron

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



