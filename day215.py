values=[7556, 7602]

#m=202300
m=202300

seb_c=m
se_c=m-1
s_count=1

#total_non_full=4*m+4*(m-1)+4=8*m

# m=2:
# full_quad_count_0=1
# full_quad_count_1=4

#m=4
# full_quad_count_0=1+8
# full_quad_count_1=4+12
# full_quad_count_0=1+8
# full_quad_count_1=4+12

full_quad_count_0=(m-1)*(m-1)
full_quad_count_1=m*m

total=0

seb=[970, 973, 959, 976]
se=[6623, 6618, 6638, 6610]
s=[5705, 5692, 5672, 5685]

total+=sum(s)
total+=sum([seb_c*s for s in seb])
total+=sum([se_c*s for s in se])

print("nonfull total?",total)
total+=full_quad_count_0*values[0]
total+=full_quad_count_1*values[1]
# for q in full_quads:
#     total+=values[(q[0]+q[1]+1)%2]
#
print(total)

#m=4 facit outside d<=1: 269405

#m=4 facit
#307231

#307783 [1]
#306633 [0]




