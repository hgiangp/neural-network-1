#!/usr/bin/env bash

files=("one_neuron" "singlelayer_nn" "singlelayer_nn_discrete" "multilayer_nn" "autoassociate_mem" "one_neuron_perception")
idx=3

cfile=${files[$idx]}.c 
ofile=./outs/${files[$idx]}.out 
lfile=./logs/${files[$idx]}.log

gcc $cfile -o $ofile 

./$ofile | tee $lfile 
