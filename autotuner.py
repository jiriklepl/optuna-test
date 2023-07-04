#!/usr/bin/env python3

import optuna
from optuna import trial as trial_module

import time
import os
import math

def measure(X: trial_module.Trial):
  bs = X.suggest_int('BLOCK_SIZE', 1, 1260)
  o = X.suggest_int('OPT_LEVEL', 0, 3)
  c = X.suggest_categorical('COMPILER', ['gcc', 'clang'])
  name = './tmp.bin'

  # compile
  compl = os.popen(c + ' kernels/c_kernel.c -DBLOCK_SIZE=' + str(bs) + ' -O' + str(o) + ' -o' + name).close()
  if not compl is None and not compl // 256 == 0:
    return math.inf

  start = time.time()

  # run
  run = os.popen(name).close()

  end = time.time()

  return end - start if run is None or run // 256 == 0 else math.inf

study = optuna.create_study()
study.optimize(measure, n_trials=100)
