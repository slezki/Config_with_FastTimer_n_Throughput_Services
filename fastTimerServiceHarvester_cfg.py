import FWCore.ParameterSet.Config as cms

process = cms.Process('HARVESTING')

# read all the DQMIO files produced by the previous jobs
process.source = cms.Source("DQMRootSource",
    fileNames = cms.untracked.vstring(
        "file:step3_inDQM.root",
    )
)

# DQMStore service
process.load('DQMServices.Core.DQMStore_cfi')
process.DQMStore.enableMultiThread = True

# FastTimerService client
process.load('HLTrigger.Timer.fastTimerServiceClient_cfi')
process.fastTimerServiceClient.dqmPath = "HLT/TimerService"

process.throughputServiceClient = cms.EDProducer('ThroughputServiceClient',
  dqmPath = cms.untracked.string('HLT/Throughput'),
  createSummary = cms.untracked.bool(True),
  mightGet = cms.optional.untracked.vstring
)

# DQM file saver
process.load('DQMServices.Components.DQMFileSaver_cfi')
process.dqmSaver.workflow = "/HLT/FastTimerService/All"

process.DQMFileSaverOutput = cms.EndPath( process.fastTimerServiceClient + process.throughputServiceClient + process.dqmSaver )