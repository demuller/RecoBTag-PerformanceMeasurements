common = {
	'groups' : ['EventInfo','PV',
                # 'PFMuon',"PFElectron",
                "TagVar",'JetTrack',
                'JetInfo','JetSV','CSVTagVar','JetDeepCSV','JetDeepFlavour','CSVTagTrackVar', 'DeepFlavourFeat',
                'PuppiJetTagVar','PuppiJetTrack',
                # 'PuppiJetInfo','PuppiJetSV','PuppiJetCSVTagVar','PuppiJetDeepCSV','PuppiJetDeepFlavour','PuppiJetCSVTagTrackVar','PuppiJetDeepFlavourFeat',
                # 'PuppiJetTrack','PuppiJetTagVar',
                'CaloJetInfo','CaloJetSV','CaloJetTrack','CaloJetCSVTagVar','CaloJetDeepCSV','CaloJetTagVar','CaloJetCSVTagTrackVar',
                ],
	'eras' : ['Run3'],
    'runCaloJetVariables' : True,
    'runPuppiJetVariables' : False,
	'globalTag' : '121X_mcRun3_2021_realistic_v15', # mc
	# 'globalTag' : '121X_dataRun3_HLT_v9', # data
	'maxJetEta' : 2.5,
	'usePrivateJEC' : False,
	# 'jecDBFileMC' : 'PhaseIIFall17_V5b_MC',
	# 'inputFiles' : ['/store/relval/CMSSW_11_2_0_pre3/RelValTTbar_14TeV/GEN-SIM-DIGI-RAW/PU_112X_mcRun3_2021_realistic_v5-v1/20000/0F40986A-FECA-F04A-99E9-4F35A32C369E.root',],
	'inputFiles' : ['/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/120005/57b8b842-4736-4f6f-9627-38d4da5dc87d.root',],
	# 'inputFiles' : ['/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-RECO/FlatPU30to80_112X_mcRun3_2021_realistic_v16-v2/30000/bea867fa-fa28-4bb7-a554-da8987602685.root',],
	# 'inputFiles' : ['/store/mc/Run3Winter21DRMiniAOD/QCD_Pt-20To30_TuneCP5_14TeV-pythia8/GEN-SIM-RECO/FlatPU30to80_112X_mcRun3_2021_realistic_v16-v2/270000/007e8fd8-da92-4b93-b7ea-d613fd34bbf3.root',],
	# 'inputFiles' : ['/store/mc/Run3Winter21DRMiniAOD/DisplacedSUSY_stopToBottom_M_1000_1000mm_TuneCP5_14TeV_pythia8/GEN-SIM-DIGI-RAW/FlatPU20to70_112X_mcRun3_2021_realistic_v16-v2/270000/0050a3dc-310f-4aa2-b4b3-6bde141b9c33.root',],
    # 'JPCalibration' : 'JPcalib_MC81X_v0',
}
