#input_d_3.txt is the file containing the raw puzzle input.
cp input_d_3.txt 3t.txt; sed -i -e 's/^/ /' 3t.txt; for ((j=11; j>=0; j--)); do for ((i=9; i>=0; i--));  do sed -i -E "s/^([^ ]{$((11-j))})[ ][^$i]*$i(.{$j,})/\1$i \2/" 3t.txt; done; done; cat 3t.txt | awk '{s+=$1; print s}'
