if __name__ == '__main__':

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
    config.General.transferLogs = True

    config.section_("JobType")
    config.JobType.pluginName = 'Analysis'
    config.JobType.psetName = "/afs/cern.ch/user/c/cmantill/work/public/samples/Fall17/CMSSW_9_4_7/src/step3_MINIAODSIM_cfg.py"
    config.JobType.numCores = 1
    config.section_("Data")
    config.Data.inputDBS = 'phys03'
    config.Data.splitting = 'FileBased'
    config.Data.unitsPerJob = 5 #when splitting is 'Automatic', this represents jobs target runtime(minimum 180)
    config.Data.publication = True
    config.Data.ignoreLocality = False

    config.section_("Site")
    config.Site.storageSite = 'T2_US_Caltech_Ceph'
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

    datasetToNameDict = {  
        '/GravitonToHHToWWWW_part1/cmantill-crab_PrivateProduction_Fall17_DR_step2_GravitonToHHToWWWW_batch1_try3-f4da9481f485a161f85554a43e15b2d7/USER': 'PrivateProduction_Fall17_DR_step3_GravitonToHHToWWWW_batch1_try3',
        '/GravitonToHHToWWWW_part1/cmantill-crab_PrivateProduction_Fall17_DR_step2_GravitonToHHToWWWW_batch1_try2-f4da9481f485a161f85554a43e15b2d7/USER': 'PrivateProduction_Fall17_DR_step3_GravitonToHHToWWWW_batch1_try2',
        }

    datasetToOutput = {    
        '/GravitonToHHToWWWW_part1/cmantill-crab_PrivateProduction_Fall17_DR_step2_GravitonToHHToWWWW_batch1_try3-f4da9481f485a161f85554a43e15b2d7/USER': '/store/user/cmantill/privateProduction/DR/step3_MINIAODSIM/RunIIFall17/GravitonToHHToWWWW_part1/v1/batch1_try3/',
        '/GravitonToHHToWWWW_part1/cmantill-crab_PrivateProduction_Fall17_DR_step2_GravitonToHHToWWWW_batch1_try2-f4da9481f485a161f85554a43e15b2d7/USER': '/store/user/cmantill/privateProduction/DR/step3_MINIAODSIM/RunIIFall17/GravitonToHHToWWWW_part1/v1/batch1_try2/'
        }

    for dataset in datasetToNameDict :
        name = datasetToNameDict[dataset]
        output = datasetToOutput[dataset]
        config.General.requestName = name
        config.Data.inputDataset = dataset
        config.Data.outLFNDirBase = output
        config.JobType.maxMemoryMB = 2500
        print(config.Data.inputDataset)
        print(config.JobType.psetName)
        print(config.Data.outLFNDirBase)
        submit(config)

