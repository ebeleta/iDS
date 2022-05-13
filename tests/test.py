from mmrbipy import Model

for algo in ['fix', 'bc', 'bd', 'ds', 'ids-h', 'ids-b', 'bcds-h', 'bcds-b']:
    # build a model from instance file
    mod = Model(problem='scp', filename='../instance/SCP/B40130')

    # solve by iDS algorithm with best-scenario constraints
    print("run algorithm: {}".format(algo))
    mod.solve(algorithm=algo, timelimit=30)

    # print results
    print("algorithm: {}".format(algo))
    print("objective value: {}".format(mod.objval))
    print("time to best: {:.2f}\n".format(mod.ttb))
    mod.write("result_{}.txt".format(algo))