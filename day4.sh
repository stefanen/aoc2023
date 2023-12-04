cat input_d_4.txt | sed -e 's/.*://' | awk -F' ' '{m++;delete a; t=0.5;
for (i=1; i<=NF ; i++) if (a[0+$i]++) {t=t*2}; if (t>=1) s=s+t}
END {print s}'
cat input_d_4.txt | sed -e 's/.*://' | awk -F' ' '{m++;delete a; t=0;
for (i=1; i<=NF ; i++) if (a[0+$i]++) {t=t+1;b[m+t]=b[m+t]+(1+b[m])}}
END {s=0;for (x in b) s=s+b[x];print s+m}'

