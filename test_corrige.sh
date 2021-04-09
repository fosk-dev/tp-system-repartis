#!/bin/bash

for i in `seq 10`
do
   dest="log_10_clients"
   out="log_10_clients"
   rlog="log_10_clients/rcv_log_cl_fast.txt"
   slog="log_10_clients/sd_log_cl_fast.txt"
   rlog+=$i
   slog+=$i
   out+=$i
   dest+=$i
   dest+=$4
   ./client -s $1 -p $2 -P $3 -S $rlog -R $slog -i $4 -o $dest -f &
done
