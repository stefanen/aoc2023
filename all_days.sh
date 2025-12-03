#bash p_data.sh <d> writes input from day <d> to STDOUT

for i in $(comm -12 <(bash p_data.sh 1 | awk '{print $1}' | sort -n) <(bash p_data.sh 1 | awk '{print $2}' | sort -n)); do v1=$(grep -c $i <(bash p_data.sh 1 | awk '{print $1}' | sort -n)); v2=$(grep -c $i <(bash p_data.sh 1 | awk '{print $2}' | sort -n));echo $(($i*$v2));done | awk '{s+=$1} END {print s}'
paste <(bash p_data.sh 1 | awk '{print $1}' | sort -n) <(bash p_data.sh 1 | awk '{print $2}' | sort -n) | awk '{s+=($1-$2)<0?$2-$1:$1-$2} END {print s}'

bash p_data.sh 2 | awk '{s="";for (i=2;i<=NF;i++) {s=s" "($i-$(i-1))}; print s } ' | egrep -o "^(( [1-3]){1})*$|^(( -[1-3]){1})*$" | wc -l
bash p_data.sh 2 | awk '{print NR"_ "$0;for (j=1;j<=NF;j++) {s="";for (i=1;i<=NF;i++) {if (i!=j)s=s" "$i}; print NR"_"s} } '  | awk '{s=$1;for (i=3;i<=NF;i++) {s=s" "($i-$(i-1))}; print s } ' | egrep -o "^.*_(( [1-3]){1})*$|^.*_(( -[1-3]){1})*$" | grep -o ".*_" | sort | uniq | wc -l

cat input3.txt | egrep -o "mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)" | sed -e 's/^don.*/99999/g' | sed -e 's/^do.*/00000/g' | sed -e 's/[^0-9,]//g' | awk -F, '{if ($1=="99999") d=1;if ($1=="00000") d=0; if (d==0 && $2!="") print $0}' | awk -F, '{s+=$1*$2} END {print s}'
cat input3.txt | egrep -o "mul\([0-9]+,[0-9]+\)" | sed -e 's/[^0-9,]//g' | awk -F, '{s+=$1*$2} END {print s}'


bash p_data.sh 5 | head -n 1176 | awk -F'|' '{print $2"#"$1}' | tr '\n' '|' | sed -e 's/.$//' | xargs -I% egrep -v % <(bash p_data.sh 5 | tail -n 197 | awk -F, '{s=$((NF+1)/2)"_";for (i=1; i<=NF;i++) {for (j=i+1; j<=NF;j++) s=s$i"#"$j}; print s}') | awk -F_ '{s+=$1; print s}'
#day5p2 see cmd.sh


