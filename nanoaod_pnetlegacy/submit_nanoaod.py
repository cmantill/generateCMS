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
    "2022EE": {
        "mc": {
            # "QCD": {
            #     "QCD-4Jets_HT-1200to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8": "/QCD-4Jets_HT-1200to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v2/MINIAODSIM",
            #     "QCD-4Jets_HT-1000to1200_TuneCP5_13p6TeV_madgraphMLM-pythia8": "/QCD-4Jets_HT-1000to1200_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v2/MINIAODSIM",
            #     "QCD-4Jets_HT-1500to2000_TuneCP5_13p6TeV_madgraphMLM-pythia8": "/QCD-4Jets_HT-1500to2000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v2/MINIAODSIM",
            #     "QCD-4Jets_HT-2000_TuneCP5_13p6TeV_madgraphMLM-pythia8": "/QCD-4Jets_HT-2000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v2/MINIAODSIM",
            #     "QCD-4Jets_HT-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8": "/QCD-4Jets_HT-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v2/MINIAODSIM",
            #     "QCD-4Jets_HT-400to600_TuneCP5_13p6TeV_madgraphMLM-pythia8": "/QCD-4Jets_HT-400to600_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v2/MINIAODSIM",
            #     "QCD-4Jets_HT-600to800_TuneCP5_13p6TeV_madgraphMLM-pythia8": "/QCD-4Jets_HT-600to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v2/MINIAODSIM",
            #     "QCD-4Jets_HT-800to1000_TuneCP5_13p6TeV_madgraphMLM-pythia8": "/QCD-4Jets_HT-800to1000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v2/MINIAODSIM",
            # },
            # "HH4b": {
            #     # "GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8": "/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v1/MINIAODSIM",
            # },
            "TT": {
                # "TTto4Q_TuneCP5_13p6TeV_powheg-pythia8": "/TTto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v2/MINIAODSIM",
                # "TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8": "/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v2/MINIAODSIM",
                "TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8": "/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4-130X_mcRun3_2023_realistic_v14-v2/MINIAODSIM",
            }
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
            this_config = config()
            this_config.section_('General')
            this_config.General.workArea = 'crab/nanoaod_v12/'
            this_config.General.transferOutputs = True
            this_config.General.transferLogs = True
            this_config.General.requestName = f'nanoaod_v12_legacy_{era}_{dataset}'
            
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
            this_config.Data.outLFNDirBase = f'/store/group/lpcdihiggsboost/{username}/NanoAOD_v12/{era}/{sample}'
            this_config.Data.lumiMask = ''
            
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
