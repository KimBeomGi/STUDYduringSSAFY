home_to_school = int(input())
school_to_pc = int(input())
pc_to_inst = int(input())
inst_to_home = int(input())

A = home_to_school + school_to_pc + pc_to_inst + inst_to_home
print(A//60)
print(A%60)