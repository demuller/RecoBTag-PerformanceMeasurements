#!/bin/bash

set -e

if [ $# -ne 1 ]; then
  printf "\n%s\n\n" ">> argument missing - specify path to output directory"
  exit 1
fi

NEVT=-1

ODIR=${1}

if [ -d ${ODIR} ]; then
  printf "%s\n" "output directory already exists: ${ODIR}"
  exit 1
fi

declare -A samplesMap
# samplesMap["Run2018D_EphemeralHLTPhysics1_RAW_run323775_ls52to151"]="${CMSSW_BASE}"/src/JMETriggerAnalysis/NTuplizers/test/rates/data/Run2018D_EphemeralHLTPhysics1_RAW_run323775_ls52to151.json
samplesMap["Run2018D_EphemeralHLTPhysics1_RAW_run323775_ls52to151"]="${CMSSW_BASE}"/src/RecoBTag/PerformanceMeasurements/test/rates/data/tmp.json

recoKeys=(
  # HLT_GRun_oldJECs
  HLT_GRun
  HLT_GRun_PatatrackTriplets
  HLT_GRun_PatatrackQuadruplets
  # HLT_Run3TRK
  # HLT_Run3TRKWithPU
)

for recoKey in "${recoKeys[@]}"; do
  python "${CMSSW_BASE}"/src/RecoBTag/PerformanceMeasurements/test/rates/hltResults_cfg.py \
    dumpPython=.tmp_${recoKey}_cfg.py numThreads=1 reco=${recoKey}

  for sampleKey in ${!samplesMap[@]}; do
      echo ${sampleKey}
    sampleName=${samplesMap[${sampleKey}]}
    echo ${sampleName}

    # bdriver -c .tmp_${recoKey}_cfg.py --customize-cfg -m ${NEVT} -n 500 --cpus 1 --mem 2G --time 02:00:00 \
    bdriver -c .tmp_${recoKey}_cfg.py --customize-cfg -m ${NEVT} -n 500 --export-LD-LIBRARY-PATH -b htc \
      -d ${sampleName} -p 0 -o ${ODIR}/${recoKey}/${sampleKey} --cpus 1 --mem 1999 --time 03:00:00\
      --customise-commands \
       '# output' \
       "if hasattr(process, 'hltOutput'):" \
       '  process.hltOutput.fileName = opts.output'
  done

  rm -f .tmp_${recoKey}_cfg.py
done
