from mmrbipy import Model

# build a model from instance file
mod = Model(problem='scp', filename='../instance/SCP/B40130')

# solve by iDS algorithm with best-scenario constraints
mod.solve(algorithm='ids-b', timelimit=3600)

# print results
print("objective value: {}".format(mod.objval))
print("time to best: {:.2f}".format(mod.ttb))

# write the results to file
mod.write("result.txt")