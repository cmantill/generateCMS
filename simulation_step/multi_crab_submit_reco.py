if __name__ == '__main__':

    import os
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--step', type=str, choices=['1','1p5','2','3'], required=True)
    parser.add_argument('--dataset', type=str, required=True, help='name of crab dataset')
    parser.add_argument('--name', type=str, default='GravitonToHHToWWWW', help='name of dataset')
    parser.add_argument('--eosdir', type=str, default='/store/user/cmantill/privateProduction/DR/', help='eosdir')
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
    config.JobType.pluginName = 'Analysis'
    config.JobType.psetName = os.environ["CMSSW_BASE"] + "/src/step%s_cfg.py"%args.step
    config.JobType.numCores = 1

    config.section_("Data")
    config.Data.inputDBS = 'phys03'
    config.Data.splitting = 'FileBased'
    config.Data.unitsPerJob = 1 #when splitting is 'Automatic', this represents jobs target runtime(minimum 180)
    config.Data.publication = True
    config.Data.ignoreLocality = False

    config.section_("Site")
    config.Site.storageSite = args.site
    config.Site.ignoreGlobalBlacklist = True
    
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
    eos_dir = '/store/user/cmantill/privateProduction/DR/step%s/'%args.step
    output = eos_dir + args.name

    config.General.requestName = args.name + "step%s"%args.step
    config.Data.inputDataset = args.dataset
    config.Data.outLFNDirBase = output
    if args.step == "1":
        config.JobType.numCores = 8
        config.JobType.maxMemoryMB = 5000
    elif args.step == "2":
        config.JobType.maxMemoryMB = 4000
    elif args.step == "3":
        config.JobType.maxMemoryMB = 2500

    print(config.General.requestName)
    print(config.Data.inputDataset)
    print(config.Data.outLFNDirBase)

    #submit(config)

