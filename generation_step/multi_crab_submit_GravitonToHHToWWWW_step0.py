if __name__ == '__main__':

    #filter efficiency

    from CRABAPI.RawCommand import crabCommand
    from CRABClient.ClientExceptions import ClientException
    from httplib import HTTPException

    #from CRABClient.UserUtilities import config
    #config = config()
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
    #config.Site.storageSite = 'T2_US_Caltech'
    config.Site.storageSite = 'T2_US_Caltech_Ceph'
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
    ev = 150000 #100k events
    mode_list = ["GravitonToHHToWWWW_part1"]
    # mode_list = ["GravitonToHHToWWWW_part2"]
    # mode_list = ["GravitonToHHToWWWW_lnuqq"]
    pset_dir = "/afs/cern.ch/user/c/cmantill/work/public/samples/Fall17/CMSSW_9_3_16/src"
    for i in range(len(mode_list)):
	mode = mode_list[i]
        spec = mode
        
        config.General.requestName = 'PrivateProduction_Fall17_'+mode+'_GENSIM_batch1'
        config.Data.outputPrimaryDataset = spec
        config.Data.outLFNDirBase = '/store/user/cmantill/privateProduction/GS/RunIIFall17/GENSIM/'+ mode + "/v1/batch1/"
        config.JobType.psetName = pset_dir + "/JME-RunIIFall17GS-00017-GravitonToHHToWWWW_highMX_cfg.py"
        # config.JobType.psetName = pset_dir + "/JME-RunIIFall17GS-00017-GravitonToHHToWWWW_highMX_part2_cfg.py"
        # config.JobType.psetName = pset_dir + "/JME-RunIIFall17GS-00017-GravitonToHHToWWWW_lnuqq_cfg.py"
        config.JobType.numCores = 1
        print 'config %s' %(config.JobType.psetName)
        print 'output %s' %(config.Data.outLFNDirBase)
        submit(config)
        
