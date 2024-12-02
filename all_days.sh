#bash p_data.sh <d> writes input from day <d> to STDOUT

#Day1
for i in $(comm -12 <(bash p_data.sh 1 | awk '{print $1}' | sort -n) <(bash p_data.sh 1 | awk '{print $2}' | sort -n)); do v1=$(grep -c $i <(bash p_data.sh 1 | awk '{print $1}' | sort -n)); v2=$(grep -c $i <(bash p_data.sh 1 | awk '{print $2}' | sort -n));echo $(($i*$v2));done | awk '{s+=$1} END {print s}'
paste <(bash p_data.sh 1 | awk '{print $1}' | sort -n) <(bash p_data.sh 1 | awk '{print $2}' | sort -n) | awk '{s+=($1-$2)<0?$2-$1:$1-$2} END {print s}'
#Day2
bash p_data.sh 2 | awk '{s="";for (i=2;i<=NF;i++) {s=s" "($i-$(i-1))}; print s } ' | egrep -o "^(( [1-3]){1})*$|^(( -[1-3]){1})*$" | wc -l
bash p_data.sh 2 | awk '{print NR"_ "$0;for (j=1;j<=NF;j++) {s="";for (i=1;i<=NF;i++) {if (i!=j)s=s" "$i}; print NR"_"s} } '  | awk '{s=$1;for (i=3;i<=NF;i++) {s=s" "($i-$(i-1))}; print s } ' | egrep -o "^.*_(( [1-3]){1})*$|^.*_(( -[1-3]){1})*$" | grep -o ".*_" | sort | uniq | wc -l
