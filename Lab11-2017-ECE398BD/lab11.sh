#!/bin/zsh
source activate ipykernel_py2

python lab11.py seq1.fna seq2.fna sub.txt -8 > align1.txt
python lab11.py BRCA1_part_mutated.fna BRCA1_part.fna sub.txt -8 > align2.txt
python lab11.py BRCA1_part_mutated.fna BRCA1_part.fna sub2.txt -1 > align3.txt
