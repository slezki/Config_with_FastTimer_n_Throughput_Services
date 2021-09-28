# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step3 --conditions auto:phase2_realistic_T15 -s RAW2DIGI,RECO:reconstruction_trackingOnly --datatier GEN-SIM-RECO,DQMIO -n 100 --geometry Extended2026D49 --era Phase2C9 --eventcontent RECOSIM,DQM --filein file:step2.root --fileout file:step3.root --no_exec --mc
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Phase2C9_cff import Phase2C9

process = cms.Process('RECO',Phase2C9)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.Geometry.GeometryExtended2026D49Reco_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.MessageLogger.categories.append('FastReport')
process.MessageLogger.cerr.FastReport = cms.untracked.PSet( limit = cms.untracked.int32( 10000000 ) )

process.ThroughputService = cms.Service('ThroughputService',
    eventRange = cms.untracked.uint32(1000),
    eventResolution = cms.untracked.uint32(10),
    printEventSummary = cms.untracked.bool(True),
    enableDQM = cms.untracked.bool(True),
    dqmPathByProcesses = cms.untracked.bool(False),
    dqmPath = cms.untracked.string('Throughput'),
    timeRange = cms.untracked.double(1000),
    timeResolution = cms.untracked.double(1)
)

process.MessageLogger.categories.append('ThroughputService')
process.MessageLogger.cerr.ThroughputService = cms.untracked.PSet(
    limit = cms.untracked.int32(10000000)
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(5000),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/group/phys_tracking/GNNTrackingHackathon/relval/TTbar/PU50/GEN-SIM-DIGI-RAW/da7dc7fc-e6c7-4731-b725-1042fbf5206c.root'
        ),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(
    FailPath = cms.untracked.vstring(),
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    SkipEvent = cms.untracked.vstring(),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(
            allowAnyLabel_=cms.required.untracked.uint32
        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(1)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    makeTriggerResults = cms.obsolete.untracked.bool,
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(1),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(8),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(True)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step3 nevts:100'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.RECOSIMoutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-RECO'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:step3.root'),
    outputCommands = process.RECOSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

process.DQMoutput = cms.OutputModule("DQMRootOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('DQMIO'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:step3_inDQM.root'),
    outputCommands = process.DQMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase2_realistic_T15', '')

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.reconstruction_step = cms.Path(process.reconstruction_trackingOnly)
process.RECOSIMoutput_step = cms.EndPath(process.RECOSIMoutput)
process.DQMoutput_step = cms.EndPath(process.DQMoutput)

process.consumer = cms.EDAnalyzer("GenericConsumer",
    eventProducts = cms.untracked.vstring('generalTracks')
)

process.consume_step = cms.EndPath(process.consumer)

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,process.reconstruction_step,process.consume_step,process.RECOSIMoutput_step,process.DQMoutput_step)
#process.schedule = cms.Schedule(process.raw2digi_step,process.reconstruction_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)


# remove any instance of the FastTimerService
if 'FastTimerService' in process.__dict__:
    del process.FastTimerService

# instrument the menu with the FastTimerService
process.load( "HLTrigger.Timer.FastTimerService_cfi" )

# print a text summary at the end of the job
process.FastTimerService.printEventSummary        = False
process.FastTimerService.printRunSummary          = False
process.FastTimerService.printJobSummary          = True

# enable DQM plots
process.FastTimerService.enableDQM                = True

# enable per-path DQM plots (starting with CMSSW 9.2.3-patch2)
process.FastTimerService.enableDQMbyPath          = True

# enable per-module DQM plots
process.FastTimerService.enableDQMbyModule        = True

# enable DQM plots vs lumisection
process.FastTimerService.enableDQMbyLumiSection   = True
process.FastTimerService.dqmLumiSectionsRange     = 2500    # lumisections (23.31 s)

# set the time resolution of the DQM plots
process.FastTimerService.dqmTimeRange             = 1000.   # ms
process.FastTimerService.dqmTimeResolution        =    5.   # ms
process.FastTimerService.dqmPathTimeRange         =  100.   # ms
process.FastTimerService.dqmPathTimeResolution    =    0.5  # ms
process.FastTimerService.dqmModuleTimeRange       =   40.   # ms
process.FastTimerService.dqmModuleTimeResolution  =    0.2  # ms

# set the base DQM folder for the plots
process.FastTimerService.dqmPath                  = "HLT/TimerService"
process.FastTimerService.enableDQMbyProcesses     = False
#process.FastTimerService.writeJSONSummary         = True
#process.FastTimerService.jsonFileName             = "test.json"

# save the DQM plots in the DQMIO format
#process.dqmOutput = cms.OutputModule("DQMRootOutputModule",
#    fileName = cms.untracked.string("DQM.root")
#)
#process.FastTimerOutput = cms.EndPath( process.DQMoutput )
'''
# DQMStore service
process.load('DQMServices.Core.DQMStore_cfi')
process.DQMStore.enableMultiThread = True

# FastTimerService client
process.load('HLTrigger.Timer.fastTimerServiceClient_cfi')
process.fastTimerServiceClient.dqmPath = "HLT/TimerService"

#process.ThroughputService.enableDQM = False

process.throughputServiceClient = cms.EDProducer('ThroughputServiceClient',
  dqmPath = cms.untracked.string('HLT/Throughput'),
  createSummary = cms.untracked.bool(True),
  mightGet = cms.optional.untracked.vstring
)

# DQM file saver
process.load('DQMServices.Components.DQMFileSaver_cfi')
process.dqmSaver.workflow = "/HLT/FastTimerService/All"

process.DQMFileSaverOutput = cms.EndPath( process.fastTimerServiceClient + process.throughputServiceClient + process.dqmSaver )
'''
# Customisation from command line

#Have logErrorHarvester wait for the same EDProducers to finish as those providing data for the OutputModule
from FWCore.Modules.logErrorHarvester_cff import customiseLogErrorHarvesterUsingOutputCommands
process = customiseLogErrorHarvesterUsingOutputCommands(process)

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
