# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: --python_filename Run3Summer22NanoAODv12_cfg.py --eventcontent NANOAODSIM --customise PhysicsTools/NanoAOD/custom_jme_cff.PrepJMECustomNanoAOD_MC,Configuration/DataProcessing/Utils.addMonitoring --datatier NANOAODSIM --fileout file:Run3Summer22NanoAODv12.root --conditions 132X_mcRun3_2022_realistic_v3 --step NANO --scenario pp --filein dbs:/WW_TuneCP5_13p6TeV_pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5-v2/MINIAODSIM --era Run3 --no_exec --mc -n 10
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
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/002fe031-e38f-451f-b391-40f5c2bf6d04.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/00ec5b92-d52f-4ba6-8456-5259d663908c.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/01c847b4-eaec-435e-8ece-3bf374ef6e77.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/0d873ed9-3ce3-4474-96d6-9573d935ef80.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/0e91720f-50f9-44e8-ad2d-a41b3a9ba431.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/0ec62b7c-0614-4930-a80b-f676f79e10b1.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/0fed9a74-7d61-4a92-9e95-3fc346c5226f.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/16357065-8d9f-4028-af06-9fd1f26112fd.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/1a519df5-acdd-4175-a0c3-d6ce77270b8c.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/1e83a69f-a217-4e33-aa98-3c25489bc3fc.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/22c82f10-4e3b-4a2a-9e7f-53db1eeb11f9.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/23422ca6-3972-4ce1-b103-45ffcf44cbd2.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/28f28919-9fc3-4266-9bd5-7b3fcc101580.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/29476ea3-8f45-44fe-be8a-2acf7d9de4cf.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/33c4dc7a-1450-4540-a68f-6c635974a35e.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/366feba1-b39a-4eb7-8261-af07a0346b07.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/3981aff0-2b1b-4200-9c24-72e0cb30be61.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/3f6d5e3e-97d4-423f-b29e-b1c6c6942e58.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/40641671-a375-40a9-aeb6-65cf9fc6fb9e.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/40ebea0e-1e39-4fe5-a9ff-0f42b4485a79.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/44e5dd67-c376-4618-9fb4-7970d6add44e.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/46d1649b-1adf-4de4-b8f0-919c55e8f879.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/4bf35d72-191b-4288-a631-d2a308bda0a2.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/4e4108c7-3f1e-44b2-8427-c3dd3a11b83f.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/553e073f-9a3b-47df-a891-61aad389e775.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/56454c74-b32d-4ffd-a3a0-ccf789fa1409.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/575ca972-e09d-4a02-83cd-6c61c9212035.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/57973c59-dccf-46bf-aef7-f16bdf6052a0.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/5c797813-dcb4-4050-87d1-aca63d58ae80.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/5d8353a7-8282-41bd-bd04-ddc592a6e63d.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/60217d8f-a738-4daf-b4d7-0a7cb573a9f0.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/60a4725f-0efa-433a-8b58-1c67df74a619.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/63421b28-12de-4cd7-bd0e-51179941ab01.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/63b1ab8c-66be-4870-a263-75ff1b084d65.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/6566a6b5-1987-49b4-9170-ff6643d8ee2f.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/6a05bd6c-67bb-47f3-a189-a9e7567f607b.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/6bef717c-1f2e-43cf-a6ff-361d43277678.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/6bf1637b-ca33-4f3c-826d-870ef80f1c11.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/6cb61453-d4af-4edf-95f6-f44f7410010d.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/6eed218e-64b5-426f-9cf5-73ce9cfc0a1c.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/70ab314c-cf62-41b6-94ed-2a5a210ead13.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/72636820-0e96-4df3-bcaa-816b57f0a452.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/72c47b86-6bb1-46bf-a09f-f3a3f6426fea.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/75face2b-284f-41bb-98d1-f31236dddb6a.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/7743c300-9a21-494f-b2b8-052e98ce66ee.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/7b1bed54-1889-4abc-b592-93af34973e2f.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/7b2d4915-6e60-4dc2-881a-c515d86fe09a.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/7cc9212c-b7a7-479f-ac7d-5240b62fd7c0.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/8653242f-116b-4daa-ac48-bef2cf88b10b.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/88236539-03af-401b-b41c-f4c4f2ee5196.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/8883c862-9932-4bff-a29e-54758b7c0127.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/89096119-a281-47bd-b91c-ab9771792160.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/8a78a70e-a40a-4b00-9418-80b791adb45a.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/8b031566-dbf7-4980-bbb4-7d26dc6498c8.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/8ebb27e4-17fc-4adb-9cd8-e1064b48dc93.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/8ebcf92c-dcb3-4948-adfd-c01ec21ffa54.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/95a9d7db-dbc9-4ad4-b14d-bbb83e9e524a.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/9802ee89-cd7b-412d-9f3b-4b4883e511d1.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/99261e09-c5a8-4f14-96bd-062caab804bc.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/9ba76b75-eb19-4721-9706-353dd5218324.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/9c203181-81d4-49ba-9969-db9b2e405302.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/9dcd8eea-2c48-424a-b2d4-47a4d05e60f9.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/9e7ddeaa-506e-4fd0-8992-7ca81564eec6.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/9fa45d33-3078-413b-b3e2-25a00edf96d3.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/a4a863d3-5180-419a-8a00-5510b079a3e6.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/a821344c-0ac0-4bd4-acc0-94be6acf4cef.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/a9a6b7fb-9733-423a-8d77-8ad421f75472.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/a9b85306-e5dd-47c5-9b08-b144bef13d90.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/aa0ded37-8141-4d9b-88de-b2c137493b72.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/addf7e77-e440-4835-9616-d2d6dc79192f.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/b11b8981-804e-4866-9e52-4ee6fe694767.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/b2b2b45f-d0ed-4260-8380-f487db4c3f75.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/b2fd5ab7-d68f-43ea-b2bb-42c5361e1e42.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/bb2f1b46-e8d2-47ed-9e75-d06488368cbf.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/be4a79c1-6b3f-4f17-9841-2d13e43701f2.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/c14301fe-add8-4b3d-87fd-24dd5b3ea188.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/c14fd0e6-775f-49ed-a177-90e3f234434c.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/c58bcfc9-62ce-4cd1-bc56-60691a104354.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/c862a28a-5b98-481a-a0cc-af5a820910a2.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/cdb937c0-957c-401b-b731-47b0a423d4a6.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/d02b4029-c18d-41f9-a259-456ec82effd8.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/d29aa708-cf44-4db7-b616-8a487113bdbe.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/d2d6673f-ff8e-4c89-9f3f-bb2b87234d33.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/d2da2d22-61ba-4535-a563-c4bd8a7e499a.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/d4aa0410-4efd-49c6-9f10-04a6cf639a4e.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/d7313ff5-f877-4ace-a58d-f633a06492b1.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/d7f09816-7106-4cb6-b81c-a3a34f71330f.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/daf93900-ab88-48ef-919e-2c81d0a60a7e.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/de62fb10-ba07-4faf-a73b-3daacbb11b2b.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/e2641e0b-0a0c-4d54-baf2-971f5106e2c2.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/e2c0fe26-9044-44c7-a283-39559c87b6e0.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/e3d1be65-dad4-42cc-ac72-1d640129d415.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/e9e42043-dd8a-4fd8-897e-db60d39f0bf2.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/ec7c3c2e-e5c6-49ed-b90f-4eb3e2e34443.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/eef1c756-7bab-4694-94b1-3b55cd36e2b6.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/f0fb51ef-1fa0-4dd9-9577-74d136ca155c.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/f421d954-dd09-420c-961b-77b15d615ce9.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/f5f1cc12-f3a9-486d-b82c-01710fcb41de.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/f6403f43-525b-44c1-bb60-42b283100886.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/fcd4c776-918a-42f2-b0ce-86fd2c006f41.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/fd494dfc-dc95-4e51-9bbb-500373f7b69d.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/fd802574-0fdc-4613-9e03-44ebe7f83c16.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2530000/4295d5bc-f723-4995-a733-b0aa51c77855.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2530000/55d0f801-e472-4b3e-94e5-1ab2cee17f24.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2530000/582f65c5-4f32-48bf-a53f-8f5ba031373e.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2530000/74d45cf4-00db-4cdc-b021-2795103c9ef7.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2530000/ae9da56f-d5fd-4e90-81df-60a98d1fde4b.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2530000/d951dc05-c66b-4875-90d4-3d4fa8e5308f.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2530000/f44bfa9f-c17c-4e11-8609-4c8e44fb9c8c.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2540000/5256d177-6b87-474c-86fb-45597bbcb5f3.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2540000/7da6f0bb-e7aa-46dd-9d28-63bb2e0224e2.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2540000/d87d7178-03d7-4b88-9312-9841a7d487fc.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2540000/fe03a34a-bcc7-469b-9a70-453c7c1a4a82.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/30000/0c0ada35-e9e7-448d-b3cb-f03e4d37fa60.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/30000/174e491d-e209-4fed-b8c2-8dc90c7bb513.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/30000/196cf415-0cbb-4597-9ad1-65dd52827039.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/30000/19e441ea-c94a-461e-9a77-6466cab013d6.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/30000/1e1b572f-c384-4276-bbef-0a3f7a0fab7f.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/30000/27baefd8-4cc7-4aad-a43a-3a5ddf760e00.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/30000/2d37caf7-5e27-4f29-9e21-06e97c551591.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/30000/311cd551-7dd0-44b3-b9c4-406078f70b18.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/30000/326196dd-666b-41a4-946a-ca81567ad117.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/30000/3319a094-19e1-4ca9-830b-8a715d995eb6.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/30000/3973ddb5-27c5-435d-bd96-db745e47a28f.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/30000/3cae508d-b290-4038-8c12-658f3ad584d3.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/30000/3d111d57-9eed-460b-823c-1b5045036033.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/30000/41d586f0-86b7-4594-bb76-ce379cdf160a.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/30000/5d188e45-0257-4e39-a49c-bb517cc921fa.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/30000/60710f31-d40a-4c99-aef5-b9a04b0cc313.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/30000/63c5c6eb-ea29-4d6c-9f78-a586568a8628.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/30000/698c9d36-585e-4569-b338-e845468492ac.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/30000/6a5b9883-4b4f-4153-bc6b-43adabe47429.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/30000/6eef0160-b717-4d8c-84ca-b59b168f2f20.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/30000/731bb281-7d39-4d1d-9869-36f32e35966b.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/30000/76577ba2-d3c3-4f18-b3aa-afb544cc2b72.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/30000/7e209794-c28d-498b-9140-3efd642239e5.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/30000/800de8a6-86ed-4bcc-9be1-70bab554c662.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/30000/81f27a97-759a-4727-a4fd-78e38048d6cd.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/30000/83eea005-3be6-4aa6-b240-4f3493869498.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/30000/89b7111d-00f4-4328-a0ba-7f9938f8051e.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/30000/8bb6afcc-e26e-470d-9c94-a7c6070314ad.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/30000/90cb1e35-5acf-44e4-bdf3-8a9a902633ed.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/30000/94505a73-5d75-4e83-842c-ecd410d43f9d.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/30000/945e8a68-fe84-4a56-93d6-beca951e8700.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/30000/94fda285-e76a-4de3-bc1b-fdea5fa9687e.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/30000/98412989-80b1-40c7-9e95-4151e79d3ff2.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/30000/9c389f3e-1416-4ce1-81ee-2ea0fca2ac13.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/30000/9d9345a7-d3a2-4269-b385-53ed8768e25d.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/30000/a0d4b588-d929-478d-9e51-f4495bb91356.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/30000/a4228a42-61de-45d7-8cf9-60044a2ba400.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/30000/a5bed618-c5fe-43a8-afa4-e4dd6affeba0.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/30000/a9795491-251a-4cfb-9195-04a84b1b6a02.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/30000/b0d52710-7bfd-40f2-8f5a-caa553ccfaa1.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/30000/b2fbc4fa-21eb-4e5b-a19e-80a4c20d4230.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/30000/b45acb2d-dfca-49fa-8289-1d5759d8525f.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/30000/b4c5ce14-04d3-4607-ac0a-6f52896ae420.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/30000/bb32c2e4-ae9a-47b4-8963-a500aad5c65a.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/30000/bbf04ea0-938c-4206-8f90-976c872a98d9.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/30000/c23ba73a-1a6d-4017-b6fb-685daa26fd7e.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/30000/c2ae6011-5b5d-4390-8ee6-3deb93435811.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/30000/c2daf6de-ac19-4a5d-ad5e-63df84ae5a4f.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/30000/c56ab7da-f9d6-4bc4-ba03-8a56b2be2043.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/30000/d1612520-eaee-4caf-b1b4-8c0d6bb3ca66.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/30000/d25426d3-cb30-4148-a33c-51e04f2e00ef.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/30000/d9425bf9-116d-4451-ad2f-7f6b20e70b4a.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/30000/de01c886-5a4d-4733-9d20-190facfcd389.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/30000/de44bf4f-c329-485e-8592-a29268db7ea0.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/30000/e17c5340-e794-4820-9000-11c2b556f540.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/30000/e24d3b77-3d6b-4b9f-b1ac-40524deb6f54.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/30000/e3ca5006-2e6c-4ebf-8173-5f55b001eefd.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/30000/e6cabb9e-e0e4-4c95-9f1e-76bf9930a39d.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/30000/e843d88e-4783-4b89-b946-1883527a140f.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/30000/ec73d509-65b7-4462-9b31-eeae70292b76.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/30000/ed66cf75-c701-45ca-85af-5359b72b9944.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/30000/eff0979f-1412-4dff-9290-c4927da88d48.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/30000/f116652b-1be8-420e-a706-2ccdec03aa3c.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/30000/f38a9ab3-8590-46b1-b916-eba48fcea58e.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/30000/f7c2c068-a6e2-45f1-9e04-4ace4d63e8d7.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/30000/fddd2ada-7a0e-4896-a0c7-6705ecf445aa.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/30000/ff877ecf-c0be-46bc-a2cc-4994d6b3b744.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/40000/03871276-fe10-47c8-bdcf-34911d4204c9.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/40000/1b891be7-136a-4b1d-ad28-62891d11f494.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/40000/1ef85522-78c0-40ae-8e07-3e2088222de6.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/40000/20870253-c15c-475c-a533-6eae6c102739.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/40000/3bc40ddd-7416-49d3-a403-c3c23c735f66.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/40000/48ed8a28-a6ac-4d40-a210-412646524131.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/40000/54931744-6c80-4fcd-86b6-3d708d54904f.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/40000/58a0eb75-d40a-420f-b8c7-0be4f880a6f9.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/40000/5bd42e5e-40d9-4383-8fb0-0ac462f45edc.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/40000/5cbf7ba6-cab5-49c4-b669-db0a1713dbb7.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/40000/64c5b020-c86f-44d6-92ea-50b51906b168.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/40000/6d92b0ea-8eff-408a-a880-102742009d3e.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/40000/88fe5c69-843c-4ba1-a81f-a12e409ea5f7.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/40000/9cbf31a4-a439-4a50-8d12-0760c9ae6723.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/40000/9d6f0d68-1f5b-4a99-8341-d4affa825ee1.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/40000/ad76cd8a-9fad-4d5a-be79-b6b259b07b98.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/40000/c323087c-df20-44f1-9a3f-2053be388837.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/40000/c395edfb-6407-4c8c-b1fc-2e116d3801ba.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/40000/e27c77ef-34ac-47cd-9346-85bff4908058.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/40000/e9dd89a6-18f9-4339-ba72-618ae6ee2e1c.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/50000/060326d7-cb5b-47ee-9856-0536f628fa4f.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/50000/138e102e-837e-4128-9644-a01815e78ef3.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/50000/160566a7-53a7-4339-a76f-60b9c2781da0.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/50000/20bd710b-055d-4f7d-9974-7a229db3c670.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/50000/32b4d281-decf-466c-9a1a-2692a17531e2.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/50000/32d6a701-b69c-4540-b4ab-64cdcd54ef84.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/50000/33815453-c55a-4007-b844-ff569dcffcca.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/50000/343f38ce-3725-4fe8-8511-fb901e5ff438.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/50000/349f975a-b17d-4c53-bc19-622a0d2d1b89.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/50000/355aba56-b86d-45db-8c2a-1308855d093f.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/50000/35ee36de-1192-405a-b9fe-7616c6a22d63.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/50000/38696b16-6094-4ffd-8f0f-9ba49a338aee.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/50000/4058e76c-7f9a-4719-88e8-8fe3851f9961.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/50000/437f8b63-31e2-4dc8-b5fc-2e70bfef957e.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/50000/49deb409-27c4-4cc1-aabc-91c2bbda2526.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/50000/6ae6f848-ef42-434f-8b39-191ad4a92ec5.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/50000/72c0424f-3393-4890-ad5f-8d63b84d48da.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/50000/84334887-0e2d-4551-9dd8-d6625e071472.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/50000/88b19959-b6db-4bf8-8c37-a0aef9afc983.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/50000/970d9b81-3f98-455c-a201-1bbe836cdc6d.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/50000/98f3faf4-1e9b-45ae-bc93-11ece97a29a9.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/50000/a3c6e4e6-7967-4d94-ba52-10e05553d167.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/50000/a5cd8eeb-4f63-4101-81c7-885d817f169c.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/50000/b8747ef3-71fb-4614-927d-cff0b046d4f4.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/50000/bb603861-fe6c-471c-9be1-7ee5701e1edf.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/50000/c16c43cf-2900-4d17-bf08-25bff5f5f51e.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/50000/c41c1596-f127-4579-a47c-0ec77374f758.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/50000/c5c6c5ca-8c37-4c97-9f4f-e4fe276b4748.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/50000/c7852c60-ed1f-4161-844e-7d7aac540394.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/50000/d913de74-1b69-442a-958e-780854973ead.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/50000/e4a8ebd4-07d5-4c31-a281-a5262d5ac10a.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/50000/e80451a2-6346-44cf-bcc2-3188783af24d.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/50000/e96d1bf4-431a-4c14-9c01-951253c63fda.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/50000/ec1f6a67-ebb6-4534-8a38-92ebd9735d32.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/50000/f9a02c5b-473a-497d-85d2-2995b3fc1748.root',
        '/store/mc/Run3Summer22MiniAODv4/WW_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/50000/fe712b39-e21f-48e4-ad43-608161108013.root'
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
    fileName = cms.untracked.string('file:Run3Summer22NanoAODv12.root'),
    outputCommands = process.NANOAODSIMEventContent.outputCommands
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '132X_mcRun3_2022_realistic_v3', '')

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

# Automatic addition of the customisation function from PhysicsTools.NanoAOD.custom_jme_cff
from PhysicsTools.NanoAOD.custom_jme_cff import PrepJMECustomNanoAOD_MC 

#call to customisation function PrepJMECustomNanoAOD_MC imported from PhysicsTools.NanoAOD.custom_jme_cff
process = PrepJMECustomNanoAOD_MC(process)

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
