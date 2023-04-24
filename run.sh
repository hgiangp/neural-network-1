#!/usr/bin/env bash

files=("one_neural" "singlelayer_nn" "singlelayer_nn_discrete" "multilayer_nn")
idx=3

cfile=${files[$idx]}.c 
ofile=./outs/${files[$idx]}.out 
lfile=./logs/${files[$idx]}.log

gcc $cfile -o $ofile 

./$ofile | tee $lfile 
