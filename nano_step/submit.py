#!/usr/bin/env python3

import os
import sys
#from input_crab_data import dataset_files
import yaml
import datetime
from fnmatch import fnmatch
from argparse import ArgumentParser
from multiprocessing import Process
import copy

from CRABClient.UserUtilities import config, ClientException
from CRABAPI.RawCommand import crabCommand
from CRABClient.ClientExceptions import ClientException

sys.path.append(".")

output_site = "T3_US_FNALLPC"
requestname_base = "privatenano"
production_tag = "v11_trigobj"

if __name__ == '__main__':

    def submit(config):
        print("DEBUG : In submit()")
        try:
            crabCommand('submit', config=config)
        except ClientException as cle:
            print("Failed submitting task: %s" % (cle))

    parser = ArgumentParser()
    parser.add_argument('-y', '--yaml', default = 'samples_datatest.yaml', help = 'File with dataset descriptions')
    parser.add_argument('--username', required=True, help = 'Username')
    args = parser.parse_args()

    output_lfn_base = "/store/group/lpcdihiggsboost/nano{production_tag}/{username}".format(
        username=args.username
    )
    with open(args.yaml) as f:
        doc = yaml.safe_load(f) # Parse YAML file
        defaults = doc['defaults'] if 'defaults' in doc else {}

        print(doc)
        for sample in sorted(doc["samples"].keys()):
            info = copy.deepcopy(defaults)
            info.update(doc["samples"][sample])
            print("\n\n*** Sample {} ***".format(sample))

            for dataset_shortname, dataset in info['datasets'].items():            
                print("\n*** Submitting {}: {}".format(dataset_shortname, dataset))

                isMC = info.get("isMC", None)
                if isMC == None:
                    raise ValueError("Please specify parameter isMC")

                this_config = config()

                this_config.section_('General')
                this_config.General.transferOutputs = True
                this_config.General.transferLogs = True
                this_config.General.workArea = "crab/{}_{}/".format(requestname_base, production_tag)
                this_config.General.requestName = "{}_{}_{}_{}".format(requestname_base, production_tag, info["year"], dataset_shortname)

                this_config.section_('JobType')
                this_config.JobType.pluginName = 'Analysis'
                this_config.JobType.psetName = os.path.expandvars(info.get("pset", None))
                this_config.JobType.allowUndistributedCMSSW = True
                this_config.JobType.numCores = 4
                this_config.JobType.maxMemoryMB = 8000
                this_config.JobType.pyCfgParams = [
                        'isMC={}'.format(isMC), 
                        'reportEvery=1000',
                        'tag={}'.format(production_tag),
                ]

                this_config.section_('User')
                this_config.section_('Site')
                this_config.Site.storageSite = output_site

                this_config.section_('Data')
                this_config.Data.publication = True
                this_config.Data.outLFNDirBase = "{}/{}/{}".format(output_lfn_base, info["year"], sample)
                this_config.Data.outputDatasetTag = dataset_shortname

                # Outputs land at outLFNDirBase/outputDatasetTag
                this_config.Data.inputDBS = 'global'
                if "private" in info.keys():
                    if info["private"]:
                        this_config.Data.inputDBS = 'phys03'
                this_config.Data.inputDataset = dataset
                splitting_mode = info.get("splitting", "Automatic")
                if not splitting_mode in ["Automatic", "FileBased", "LumiBased"]:
                    raise ValueError("Unrecognized splitting mode: {}".format(splitting_mode))
                this_config.Data.splitting = splitting_mode

                if not isMC:
                        this_config.Data.lumiMask = info.get('lumimask', None)
                else:
                        this_config.Data.lumiMask = ''

                unitsPerJob = info.get("unitsPerJob", None)
                if unitsPerJob is not None:
                    this_config.Data.unitsPerJob = unitsPerJob

                totalUnits = info.get("totalUnits", None)
                if totalUnits is not None:
                    this_config.Data.totalUnits = totalUnits

                allowInvalid = info.get("allowInvalid", False)
                if allowInvalid:
                    this_config.Data.allowNonValidInputDataset = True
                
                print(this_config)
                p = Process(target=submit, args=(this_config,))
                p.start()
                p.join()
                #submit(this_config)
            print("*** Done with Sample {} ***\n\n".format(sample))

