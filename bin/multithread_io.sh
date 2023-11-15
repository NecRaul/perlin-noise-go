#!/bin/bash

num=$1
numPadded=$(printf "%05d" "$num")

for ((i = 1; i <= 100; i++)); do
    mkdir -p "../results/mt_io"
    ./multithread_io $num 100 6 0.5 2 $i | sed "s/Time: //" | sed "s/µ/u/" >>"../results/mt_io/$numPadded.txt"
    rm noise-mp.png
done
