from pathlib import Path
import argparse
import sys

from CRABClient.UserUtilities import config
from CRABAPI.RawCommand import crabCommand

path_to_config = str(Path(__file__).parent)

config_per_eras = {
    "2022": {
        "mc": "Run3Summer22NanoAODv12_cfg.py",
        "data": "Run2022C-E-22Sep2023NanoAODv12_cfg.py",
    },
    "2022EE": {
        "mc": "Run3Summer22EENanoAODv12_cfg.py",
        "data-C-E": "Run2022C-E-22Sep2023NanoAODv12_cfg.py",
        "data-F-G": "Run2022F-G-22Sep2023NanoAODv12_cfg.py",
    },
    "2023-pre-Bpix": {
        "mc": "Run3Summer23NanoAODv12_cfg.py",
        "data": "Run2023-22Sep2023NanoAODv12_cfg.py",
    },
    "2023-Bpix": {
        "mc": "Run3Summer23BPixNanoAODv12_cfg.py",
        "data": "Run2023-22Sep2023NanoAODv12_cfg.py",
    },
}

# list of miniaod samples
# comment unused lines
all_samples = {
    "2022": {
        "data": {
            "JetMET": {
                #"JetHT_Run2022C": ["/JetHT/Run2022C-22Sep2023-v1/MINIAOD", "crab/nanoaod_v12/crab_nanoaod_v12_legacy_2022_JetHT_Run2022C/results/"],
                #"JetMET_Run2022C": ["/JetMET/Run2022C-22Sep2023-v1/MINIAOD", "crab/nanoaod_v12/crab_nanoaod_v12_legacy_2022_JetMET_Run2022C_recoveryMar25/results/"],
                "JetMET_Run2022D": ["/JetMET/Run2022D-22Sep2023-v1/MINIAOD", "crab/nanoaod_v12/crab_nanoaod_v12_legacy_2022_JetMET_Run2022D_recoveryMar25/results/"],
            },
        },
    },
    "2022EE": {
        "data-C-E": {
            "JetMET": {
                "JetMET_Run2022E": ["/JetMET/Run2022E-22Sep2023-v1/MINIAOD", "crab/nanoaod_v12/crab_nanoaod_v12_legacy_2022EE_JetMET_Run2022E_recoveryMar25/results/"],
            },
        },
        "data-F-G": {
            "JetMET": {
                "JetMET_Run2022F": ["/JetMET/Run2022F-22Sep2023-v2/MINIAOD", "crab/nanoaod_v12/crab_nanoaod_v12_legacy_2022EE_JetMET_Run2022F_recoveryMar25/results/"],
                #"JetMET_Run2022G": ["/JetMET/Run2022G-22Sep2023-v2/MINIAOD", "crab/nanoaod_v12/crab_nanoaod_v12_legacy_2022EE_JetMET_Run2022G_recoveryMar25/results/"],
            },
        },
    },
    "2023-pre-Bpix": {
        "data": {
            "JetMET": {
                # "JetMET_Run2023C_0v1": ["/JetMET0/Run2023C-22Sep2023_v1-v1/MINIAOD", "crab/nanoaod_v12/crab_nanoaod_v12_legacy_2023-pre-Bpix_JetMET_Run2023C_0v1_recoveryMar25/results/"],
                # "JetMET_Run2023C_0v2": ["/JetMET0/Run2023C-22Sep2023_v2-v1/MINIAOD", "crab/nanoaod_v12/crab_nanoaod_v12_legacy_2023-pre-Bpix_JetMET_Run2023C_0v2_recoveryMar25/results/"],
                # "JetMET_Run2023C_0v3": ["/JetMET0/Run2023C-22Sep2023_v3-v1/MINIAOD", "crab/nanoaod_v12/crab_nanoaod_v12_legacy_2023-pre-Bpix_JetMET_Run2023C_0v3/results/"],
                # "JetMET_Run2023C_0v4": ["/JetMET0/Run2023C-22Sep2023_v4-v1/MINIAOD", "crab/nanoaod_v12/crab_nanoaod_v12_legacy_2023-pre-Bpix_JetMET_Run2023C_0v4_recoveryMar26/results/"],
                #"JetMET_Run2023C_1v1": ["/JetMET1/Run2023C-22Sep2023_v1-v1/MINIAOD", "crab/nanoaod_v12/crab_nanoaod_v12_legacy_2023-pre-Bpix_JetMET_Run2023C_1v1_recoveryMar25/results/"],
                # "JetMET_Run2023C_1v2": ["/JetMET1/Run2023C-22Sep2023_v2-v1/MINIAOD", "crab/nanoaod_v12/crab_nanoaod_v12_legacy_2023-pre-Bpix_JetMET_Run2023C_1v2/results/"],
                #"JetMET_Run2023C_1v3": ["/JetMET1/Run2023C-22Sep2023_v3-v1/MINIAOD", "crab/nanoaod_v12/crab_nanoaod_v12_legacy_2023-pre-Bpix_JetMET_Run2023C_1v3_recoveryMar25/results/"],
                "JetMET_Run2023C_1v4": ["/JetMET1/Run2023C-22Sep2023_v4-v1/MINIAOD", "crab/nanoaod_v12/crab_nanoaod_v12_legacy_2023-pre-Bpix_JetMET_Run2023C_1v4_recoveryMar28/results/"],
            },
        },
    },
    "2023-Bpix": {
        "data": {
            "JetMET": {
                #"JetMET_Run2023D_0v1": ["/JetMET0/Run2023D-22Sep2023_v1-v1/MINIAOD", "crab/nanoaod_v12/crab_nanoaod_v12_legacy_2023-Bpix_JetMET_Run2023D_0v1/results/"],
                #"JetMET_Run2023D_0v2": ["/JetMET0/Run2023D-22Sep2023_v2-v1/MINIAOD", "crab/nanoaod_v12/crab_nanoaod_v12_legacy_2023-Bpix_JetMET_Run2023D_0v2/results/"],
                "JetMET_Run2023D_1v1": ["/JetMET1/Run2023D-22Sep2023_v1-v1/MINIAOD", "crab/nanoaod_v12/crab_nanoaod_v12_legacy_2023-Bpix_JetMET_Run2023D_1v1_recoveryMar25/results/"],
                # "JetMET_Run2023D_1v2": ["/JetMET1/Run2023D-22Sep2023_v2-v1/MINIAOD", "crab/nanoaod_v12/crab_nanoaod_v12_legacy_2023-Bpix_JetMET_Run2023D_1v2/results/"],
            },
        },
    },
}

def main(args):
    username = args.username
    era = args.era
    key = args.key

    samples = all_samples[era][key]
    config_name = config_per_eras[era][key]

    for sample, dataset_dict in samples.items():
        for dataset, dataset_path in dataset_dict.items():
            dataset_path, path_to_lumis = dataset_path
            this_config = config()
            this_config.section_('General')
            this_config.General.workArea = 'crab/nanoaod_v12/'
            this_config.General.transferOutputs = True
            this_config.General.transferLogs = True
            # this_config.General.requestName = f'nanoaod_v12_legacy_{era}_{dataset}_recoveryMar25'
            # this_config.General.requestName = f'nanoaod_v12_legacy_{era}_{dataset}_recoveryMar26'            
            # this_config.General.requestName = f'nanoaod_v12_legacy_{era}_{dataset}_recoveryMar27'
            # this_config.General.requestName = f'nanoaod_v12_legacy_{era}_{dataset}_recoveryMar28'
            this_config.General.requestName = f'nanoaod_v12_legacy_{era}_{dataset}_recoveryMar29'

            this_config.section_('JobType')
            this_config.JobType.psetName = f'{path_to_config}/{config_name}'
            this_config.JobType.pluginName = 'Analysis'
            this_config.JobType.numCores = 2
            this_config.JobType.allowUndistributedCMSSW = True
            this_config.JobType.maxMemoryMB = 5000
            
            this_config.section_('Data')
            this_config.Data.inputDataset = dataset_path
            this_config.Data.outputDatasetTag = dataset
            this_config.Data.publication = True
            this_config.Data.inputDBS = 'global'
            this_config.Data.splitting = 'Automatic'
            this_config.Data.outLFNDirBase = f'/store/group/lpcdihiggsboost/NanoAOD_v12/{username}/{era}/{sample}'
            this_config.Data.lumiMask = f"{path_to_config}/{path_to_lumis}/notFinishedLumis.json"
            
            this_config.section_('Site')
            this_config.Site.storageSite = 'T3_US_FNALLPC'
            
            this_config.section_('User')
            this_config.section_('Debug')
            
            print(this_config)
            crabCommand('submit', config=this_config)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--era",
        choices=list(config_per_eras.keys()),
        required=True,
        help="era",
        type=str,
    )
    parser.add_argument(
        "--key",
        choices=["data","mc","data-C-E","data-F-G"],
        required=True,
        help="key data or mc",
        type=str,
    )
    parser.add_argument(
        "--username",
        required=True,
        type=str,
        help="username"
    )
    args = parser.parse_args()

    sys.exit(main(args))
