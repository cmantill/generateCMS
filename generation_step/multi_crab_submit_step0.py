import os

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', type=str, default='GravitonToHHToWWWW', help='name of dataset')
    parser.add_argument('--config', type=str, default='GravitonToHHToWWWW_lowMX_cfg.py',  help='config of dataset')
    parser.add_argument('--eosdir', type=str, default='/store/user/cmantill/privateProduction/GS/', help='eosdir')
    parser.add_argument('--site', type=str, default='T2_US_Caltech_Ceph', help='site')
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
    config.Data.inputDBS = 'global'
    config.Data.splitting = 'EventBased'
    config.Data.unitsPerJob = 500 
    config.Data.totalUnits = 3000000 
    # config.Data.totalUnits = 1 # for testing
    config.Data.publication = True

    config.section_("Site")
    config.Site.storageSite = args.site
    # We want to put all the CRAB project directories from the tasks we submit here into one common directory.
    # That's why we need to set this parameter (here or above in the configuration file, it does not matter, we will not overwrite it).

    def submit(config):
        try:
            crabCommand('submit', config = config)
        except HTTPException as hte:
            print "Failed submitting task: %s" % (hte.headers)
        except ClientException as cle:
            print "Failed submitting task: %s" % (cle)

    #############################################################################################
    ## From now on that's what users should modify: this is the a-la-CRAB2 configuration part. ##
    #############################################################################################
    pset_dir = os.environ["CMSSW_BASE"]+"/src"
    config.General.requestName = 'Private_'+args.name+'_GENSIM'
    config.Data.outputPrimaryDataset = args.name
    config.Data.outLFNDirBase = args.eosdir + args.name
    config.JobType.psetName = pset_dir + "/"+ args.config
    config.JobType.numCores = 1
    print 'config %s' %(config.JobType.psetName)
    print 'output %s' %(config.Data.outLFNDirBase)
    submit(config)
        
