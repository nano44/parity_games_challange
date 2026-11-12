#!/bin/bash
# The 78 frozen genomes of box 208 par. 7 as paths readable from experiments/red-b (data of L-NEW, read, not edited):
# 23 of the 25 records and all 53 corpus genomes are on trunk under experiments/new/; CFI3_n48 and RINT_n48 (box 207,
# not on trunk at 471aba45) are copied as data into inst/ (sha1 d55b20b8..., 35b48913..., equal to l-new 8db300fe
# experiments/new/box207/inst/SHA1SUMS). Source this file: it sets REC and COR.
N=../new
REC="$N/box203/inst/MWR4_2.json $N/box203/inst/MWR8_2.json $N/box203/inst/MWR16_2.json $N/box206/inst/CW4_n.json $N/box206/inst/CW8_n.json
$N/box206/inst/CW16_n.json $N/box206/inst/CWRR4_n.json $N/box206/inst/CWRR8_n.json $N/box206/inst/CWRR16_n.json $N/box206/inst/CWRQ8_n.json
$N/box203/inst/K1F21_n48.json $N/box204/inst/K1F34_n84.json $N/box203/inst/K1C16_n400.json $N/box206/inst/K1L7_n48.json
$N/box206/inst/K1L10_n48.json $N/box206/inst/K1D4_n48.json $N/box206/inst/BLKX23_n48.json $N/box206/inst/BLKX26_n48.json
$N/box204/inst/B400_r32_a13d9661.json inst/CFI3_n48.json inst/RINT_n48.json $N/box202/k1fail_202.json $N/box205/inst/naive_k1_s71.json
$N/box203/inst/ST4_k1.json $N/box203/inst/ST8_k1.json"
COR="$(ls $N/box202/inst/*.json)"
