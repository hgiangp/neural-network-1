#!/usr/bin/env bash

files=("one_neuron" \
"singlelayer_nn" \
"singlelayer_nn_discrete" \
"multilayer_nn" \
"autoassociate_mem" \
"one_neuron_perception" \
"wta" \
"wta_bk" \
"sofm" \
)

idx=$1
file_name=${files[$idx]}
echo $file_name running ....

cfile=$file_name.c 
ofile=./outs/$file_name.out 
lfile=./logs/$file_name.log

gcc $cfile -o $ofile -lm
if [ $idx -eq 8 ]; then
    ./$ofile './data/feature_map_data.txt'| tee $lfile
else
    ./$ofile | tee $lfile
fi 

# python3 utils.py | tee data/iris.log