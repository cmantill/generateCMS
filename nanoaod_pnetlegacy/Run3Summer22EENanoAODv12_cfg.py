# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: --python_filename Run3Summer22EENanoAODv12_cfg.py --eventcontent NANOAODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier NANOAODSIM --fileout file:Run3Summer22EENanoAODv12.root --conditions 130X_mcRun3_2022_realistic_postEE_v6 --step NANO --scenario pp --filein dbs:/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v1/MINIAODSIM --era Run3 --no_exec --mc -n 10
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run3_cff import Run3

process = cms.Process('NANO',Run3)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('PhysicsTools.NanoAOD.nano_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2540000/2a4009ad-866a-46af-b25c-82621c8c77f7.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2540000/44c23656-9755-4de1-982b-17be21d66be1.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2540000/698f1f3a-e28b-4b48-bacf-1a7514d8aa86.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2550000/964c94fc-c68a-4a3f-953c-39ef3d65d809.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2550000/9e748f5f-bb37-4504-9e23-ea0d8903e876.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2550000/f3fa08c6-c238-4fc1-82df-ae7fcff4e653.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2560000/33eec594-88a6-48a2-b4cc-649222e8e356.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2560000/36d07e27-88d9-4861-a629-6dab40407857.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2560000/a72e26d6-086b-4da9-8842-a0ada46a60ff.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2560000/bff9f312-b22a-44b2-ade4-7c14f24908c0.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2560000/ec61ec9c-f675-4e5d-8562-8ccd3b41c673.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/01f6d12d-7669-4831-b497-ea69a236f1c3.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/02674fc6-8872-4d5a-9835-679d32817317.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/02c89d99-9af6-4ec8-bd4b-9eb5eeb3b492.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/04cb2d10-003b-40f9-b296-9fa025cd19d5.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/068b1e51-e02a-4db8-bfc3-c50ce63f40c9.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/0c56de7c-d601-40c2-8537-25182f1c8cff.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/0c5dd4b1-11f0-4b9e-a92a-a6bde82a4a5c.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/0d044d4d-b2af-4622-8b68-9cbb4aab57cb.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/0e763407-0651-4cca-ab51-c7d1f0bcfe6a.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/111fcafc-6647-4e26-8c06-f7d0fc6f93a5.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/1251d4d1-5d85-4ada-b241-2683e1f8e7b8.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/2014a02c-b595-4f51-8919-811b3735ea31.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/22554813-2659-4efa-ae0b-b58413b4cb14.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/2709eca9-d1a1-486f-8a2e-2d5bd299bc39.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/2845b265-333b-494e-a51b-551fbadeca28.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/2c7cd976-3c4d-49cc-bef2-57045022e3bd.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/2f1f1cef-f83d-4a66-a39f-3d9633f622ca.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/30da9905-24ea-4ec6-b301-894677de1446.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/3236e2e2-c3f2-496f-b3a7-c7449dc4e1d5.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/325a7ab3-eace-4a68-b48e-a0336d49c851.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/3388fa04-23f4-42c5-a816-47600372894c.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/36ed09e1-b3d2-462a-bdb4-d5f03f06d46e.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/37e0624a-ba25-49e0-84a5-048e1ff89674.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/39fdb112-f8dc-48c5-86b4-dd0ef0792de5.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/3bb2fdb9-affe-49dd-bd0f-8a601f41de66.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/3c599d10-30a3-4d51-881c-4e2a1c7bdff6.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/3c6be49c-a454-4d6a-af0e-da0a34d88f2f.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/3c95ced5-6515-4663-a968-809377ff558b.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/3deabc67-9dd5-4f15-9f2e-f72c664dbd0a.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/3def9836-b1bb-4ff6-8470-fdb0dd00fa0b.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/401bdda1-0b31-44f3-9bd7-ba763671fe07.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/4232c806-da06-4faa-9d2a-266fbdcb190b.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/43098e6a-2bed-477f-b77a-0aa174f3065f.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/4fb6d033-ab18-43a3-9fb2-5895659aa879.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/50d5e580-f290-4a86-a11e-a775d4af137d.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/51ea3999-e2c7-45b4-a2e7-347f6b027e73.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/5681e438-ea9c-4e67-84b4-8093f4670bd0.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/598e069d-a106-49f0-a046-b97fdd93a0a2.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/5b5555b8-3fd0-4c59-9a7e-56cf88c850c8.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/5c8449e7-f283-4157-963d-b7bfcf226130.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/5d0310f2-4384-482f-aaed-1f74c0711c39.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/5dde792f-2762-43a3-9b4e-5bd5b501b2c9.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/5ea96b30-8170-4c58-99cc-216d8e662fe1.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/5f745e42-c8e9-4382-8122-62f1059c37d3.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/6087570f-3fb5-4c87-9fc6-d9c57c4028bf.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/60e04cc2-6ad3-4017-ae20-0bd2942b9d03.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/64e61e57-2d80-491c-abce-5ddf690d8c2b.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/6d06a56a-855b-406c-b401-2b0dfdf7c51d.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/6df26d3f-4ee4-496b-b2a6-6636ba2958a7.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/6e7c1fff-d055-45fd-bef2-4cf9416b004c.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/6f075980-fc2a-46d1-b745-049fb33c80bf.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/70274ea3-a06b-412c-a4d0-e7279c155248.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/78b97da7-f10f-41c2-8af2-d66e7bd6fd57.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/7b4c58f8-c159-4722-b8e3-1e9b681a7fea.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/7b97d94b-9ca6-429f-a5c8-61fded8fda8f.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/7c61ece7-48e8-461b-b6e0-27f6fdf82cf4.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/7e86a7fa-3f82-4074-9d35-d969fea45f85.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/81704a68-9ebc-4f66-b207-08ea8fda2abb.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/8474f788-4dc7-4a54-869b-2d782633c67a.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/84b02c36-bea6-42cf-a3cf-c51165c7333f.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/866e5cc9-536e-40f6-9904-488275de6410.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/8688506d-cb83-442d-a13b-06e02827bdab.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/8b4448b9-458d-4d46-a879-0d6adf585b75.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/8c43204b-f487-4cd9-b560-0235544f87a1.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/8f0b9f65-3b69-4fc2-96e2-a6bafc8b30c0.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/91931677-4372-45d3-84ef-fdab1e4627a8.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/92f51595-b918-4197-9155-8d3db240750d.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/93124688-597a-4410-8c12-21c43e7cd5cf.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/96838201-7538-4646-91bf-636dd9f0bd9a.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/96f44012-3158-419b-9a0e-b193c06d1c26.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/999aa779-edce-4d4c-aadb-6a47677c98a8.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/9a7064fb-0e54-43f9-aa06-03999ed191a1.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/9e85dfe4-db2e-495f-b348-c5d87575e108.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/9f40b420-753c-4bf2-9ef5-8895747a2e02.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/9fbc9527-aeb9-4710-845f-4e13e00b0b9f.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/9fe59370-1100-48d1-822d-4ee433fb108d.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/a0e83bc3-4ea6-41c6-98ea-36b254cc0516.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/a1af5a15-f9be-448b-a411-e94e3a7c611e.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/a5c43418-4c50-4267-a3b7-cac7fb7b97e5.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/aaa74920-9062-4316-9a8c-f53a15820144.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/abb7cfad-d812-497f-b8d5-1f9e778135fb.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/abccea03-8fb1-4ee7-a559-950b1d9fcb7e.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/ac0f80cd-42a7-424f-99a2-63af88620781.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/acc4ab35-8805-48e7-ad17-d6c3f47c1834.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/b16acaac-9e27-49b1-9c49-0cd896a64728.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/b3b16ee7-239f-485b-aae0-0836234ceffe.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/b46184e3-c567-400d-9f43-72080fb9795d.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/b55a275c-464c-4eb8-bbf7-33e69acc8745.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/b86533fc-7cea-45b5-b4e8-caea8835b333.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/b90e6d71-dc65-4109-a77d-229b908455c0.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/ba2c95e6-403c-4a41-abeb-cca1e61e47e0.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/bf73a297-ba12-415b-9174-9ec070e1a284.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/c004883c-7046-4f71-be02-a23c76de98cf.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/c0762ce8-f93a-4fb8-92c6-1562d02adf9b.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/c28fc1b5-5eb9-4347-ada3-db2cb72cbdbc.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/c3e145ce-8068-4484-9629-c76632ff79ee.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/c3fb94c8-f7f9-437d-9016-df33826a8b7c.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/c49982e6-9b5f-4616-9ab1-03f42a733657.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/c5f6f405-5065-4272-b99d-a0f7b04bd493.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/c78883e3-c52c-4cb6-a086-a932ed211ff6.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/c9950243-8543-4308-93c7-ef59b0285100.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/c9de0d06-d5ce-44a8-a308-4ef358d0ba72.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/cde13803-9358-46d1-8ffc-0d673e9b9162.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/ce1fd24d-56c7-4b01-b121-70155dd86dcd.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/cff1e5a3-3f3b-4dfd-aeeb-14210c92687f.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/d1b1c6a2-c85c-446c-b7ba-0ce7735864bd.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/d300cf7d-99de-4c6e-b6f2-bff30d252407.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/d3560507-909e-46e0-90de-b8d7d94f638c.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/d431537b-9378-4cb0-b855-4736ac110e9a.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/d5c04d59-f6ff-46c5-be2e-b97c048afbce.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/d8d894c9-fde8-49d0-91ae-017958c14d64.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/d8fa71f1-ca76-410b-8273-b2bc6942d591.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/dbb418fa-b868-4ee5-92df-fc0106d51489.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/dc40d64d-623f-4ed2-a6d9-41b45e4d1449.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/dee4bc4b-be22-4ed2-8751-aab06e254214.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/e0847692-ed3b-4f26-a6fd-6a17f2068649.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/e0cb97a2-a9b3-4ccf-a5de-a97f9e06b258.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/e81782b8-8f00-4edd-bc6f-6aa9b0b85cba.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/eafb1454-7417-425f-a900-63bef4684bc3.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/eb8dbba4-e977-499c-880e-ae775e70ea7a.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/ec56a1f8-d8d4-45a0-a5c1-36a0aa1e5950.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/ec9ac2fa-810e-4436-b875-aed00c43b682.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/eca22027-d43b-40e4-a94d-cf29c73fb9d7.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/eedafb64-fd58-4934-8e0c-418252837a56.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/eef09857-342e-4b71-b3a3-1e3ce29decbd.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/eef419d6-f6c9-44f9-bd4c-ca3c72ebde70.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/ef7b50db-d3e8-472f-b0d7-1fe90e6259bc.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/f0b3b561-934c-41b1-8e18-cb36ec3f1a74.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/f133b3b2-f7b6-446c-8524-eb32ce77788d.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/f1ad0224-0e03-463f-9193-ea4c527a2079.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/f1cf72e4-d4da-40f5-afd6-64db9ea01649.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/fc26c1d3-2eb3-454c-9075-6aa615a51fd6.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/2810000/ffe80f0d-391c-46b0-b7ec-c8951c15ae53.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/30000/01e79e68-ab4e-49d6-8da7-5cd836614fee.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/30000/102a7a9d-c958-484b-9e92-1d9bfb820a9b.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/30000/37deda38-195b-4b89-8b2d-c58ebed47699.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/30000/3c032217-9011-430d-b821-149d52b03340.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/30000/41b53887-f55f-4726-ba14-74394d5c286e.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/30000/b81a7cac-3f6d-4cfd-b699-a05915b70550.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/30000/c2483e3c-d0a8-46de-8b6a-7a7f89da2665.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/30000/df55aec3-39ac-4e4f-b2e5-d82bcbc7aa08.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/30000/e1f6d1f5-ee69-44ab-9190-64cf66ffe4c5.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/30000/eaea1022-9fb5-4ba4-ae30-3393f00264c4.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/30000/ec3f2a02-47c6-44c3-a9a7-c7823cafdd0b.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/30000/ed8c969a-138c-4494-9e0b-98d33d252e76.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/50000/1b3de11e-df7f-420b-9bd4-42c397c859cd.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/50000/1cf116f2-f005-4f7f-81da-001ea9b98d5b.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/50000/3df7f58a-dd17-4a27-9d25-b34cc859d70d.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/50000/55fd534b-8349-461f-9bb7-29c156da155e.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/50000/5d242b15-0c8c-4008-8a08-6e30c69ab5ff.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/50000/60baacf5-c236-46c1-8697-9800fde228c8.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/50000/71edb8e5-7266-473f-b02f-d296ae075c74.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/50000/90e9db1d-0a4f-42b3-bd72-8a17404c8c07.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/50000/9959e380-e937-4325-9ed2-04fe4d395971.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/50000/b093f0ae-21ad-4498-b0ff-88af03e5f6da.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/80000/d94accd2-f87e-4ad6-982a-4dcca89e2b90.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/80000/f2b4094d-54e4-4c18-8816-d7456a96c411.root',
        '/store/mc/Run3Summer22EEMiniAODv4/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v1/80000/f43c8a9f-618f-40bd-8dba-0ae4af15adfc.root'
    ),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(
    FailPath = cms.untracked.vstring(),
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    SkipEvent = cms.untracked.vstring(),
    accelerators = cms.untracked.vstring('*'),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    deleteNonConsumedUnscheduledModules = cms.untracked.bool(True),
    dumpOptions = cms.untracked.bool(False),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(
            allowAnyLabel_=cms.required.untracked.uint32
        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(0)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    holdsReferencesToDeleteEarly = cms.untracked.VPSet(),
    makeTriggerResults = cms.obsolete.untracked.bool,
    modulesToIgnoreForDeleteEarly = cms.untracked.vstring(),
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(0),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(2),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(False)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('--python_filename nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.NANOAODSIMoutput = cms.OutputModule("NanoAODOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(9),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('NANOAODSIM'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:Run3Summer22EENanoAODv12.root'),
    outputCommands = process.NANOAODSIMEventContent.outputCommands
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '130X_mcRun3_2022_realistic_postEE_v6', '')

# Path and EndPath definitions
process.nanoAOD_step = cms.Path(process.nanoSequenceMC)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.NANOAODSIMoutput_step = cms.EndPath(process.NANOAODSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.nanoAOD_step,process.endjob_step,process.NANOAODSIMoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# customisation of the process.

# Automatic addition of the customisation function from PhysicsTools.NanoAOD.nano_cff
from PhysicsTools.NanoAOD.nano_cff import nanoAOD_customizeCommon 

#call to customisation function nanoAOD_customizeCommon imported from PhysicsTools.NanoAOD.nano_cff
process = nanoAOD_customizeCommon(process)

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# End of customisation functions


# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
