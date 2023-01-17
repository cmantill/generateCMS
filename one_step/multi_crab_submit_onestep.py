import os

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', type=str, default='GluGluToHHTobbVV_node_cHHH1_HpT190', help='name of dataset')
    parser.add_argument('--config', type=str, default='GluGluToHHTobbVV_node_cHHH1_HpT190_cfg',  help='config of dataset')
    parser.add_argument('--eosdir', type=str, default='/store/user/cmantill/privateProduction/ONESTEP/', help='eosdir')
    parser.add_argument('--site', type=str, default='T2_US_Caltech_Ceph', help='site')
    parser.add_argument('--begin-seed', type=int, default=0, help='begin seed, should be between 0 and 99')
    parser.add_argument('--year', type=str, default='2017', choices=['2016','2016APV','2017','2018'], help='year to make configs for')
    args = parser.parse_args()

    from CRABAPI.RawCommand import crabCommand
    from CRABClient.ClientExceptions import ClientException
    from httplib import HTTPException

    from WMCore.Configuration import Configuration
    config = Configuration()

    config.section_("General")
    config.General.workArea = 'crab'
    config.General.transferOutputs = True
    config.General.transferLogs = False

    config.section_("JobType")
    config.JobType.pluginName = 'PrivateMC'

    config.section_("Data")
    #nevent = 10
    nevent = 400
    config.Data.inputDBS = 'global'
    config.Data.splitting = 'EventBased'
    config.Data.unitsPerJob = nevent
    config.Data.totalUnits = 400000
    #config.Data.totalUnits = 2000000 
    #config.Data.totalUnits = 1 # for testing
    config.Data.publication = True
    config.Data.allowNonValidInputDataset = True

    config.section_("Site")
    config.Site.storageSite = args.site
    # We want to put all the CRAB project directories from the tasks we submit here into one common directory.
    # That's why we need to set this parameter (here or above in the configuration file, it does not matter, we will not overwrite it).

    def submit(config):
        try:
            crabCommand('submit', config = config)
        except HTTPException as hte:
            print("Failed submitting task: %s" % (hte.headers))
        except ClientException as cle:
            print("Failed submitting task: %s" % (cle))

    #############################################################################################
    ## From now on that's what users should modify: this is the a-la-CRAB2 configuration part. ##
    #############################################################################################
    pset_dir = os.environ["CMSSW_BASE"]+"/src"
    config.General.requestName = 'Private_'+args.name+'_ONESTEP'
    config.Data.outputDatasetTag = 'PrivateMC'
    config.Data.outputPrimaryDataset = args.name
    config.Data.outLFNDirBase = args.eosdir + args.name
    config.JobType.allowUndistributedCMSSW = True
    config.JobType.psetName = 'FAKEMiniAODv2_cfg.py'
    # config.JobType.psetName = 'FAKENanoAODv9_cfg.py'
    config.JobType.inputFiles = ['FrameworkJobReport.xml', 'inputs']
    config.JobType.maxMemoryMB = 5000
    config.JobType.numCores = 1
    config.JobType.sendExternalFolder = True
    config.JobType.scriptArgs = ['nevent=%i'%nevent, 'nthread=1', 'procname=%s'%args.config, 'beginseed=%i'%args.begin_seed]  
    config.JobType.scriptExe = 'exe_%s.sh'%args.year

    print('config %s' %(config.JobType.psetName))
    print('output %s' %(config.Data.outLFNDirBase))
    submit(config)
        
