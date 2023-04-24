#!/usr/bin/env bash

files=("one_neural" "singlelayer_nn" "multilayer_ner")
idx=1

cfile=${files[$idx]}.c 
ofile=./outs/${files[$idx]}.out 
lfile=./logs/${files[$idx]}.log

gcc $cfile -o $ofile 

./$ofile | tee $lfile 
