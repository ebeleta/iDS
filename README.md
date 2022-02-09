# mmrbipy: A solver for the min-max regret binary integer programming problem (MMR-BIP)

## Installation

In a virtual environment with Python 3.6+, mmrbipy can be installed via

```bash
pip install mmrbipy
```

## Using mmrbipy

With a compatible instance file, solve the MMR-BIP from a Python script:

```python
from mmrbipy import Model

# build a model from instance file
mod = Model(problem='kp', filename='../instance/KP/1-70-01-45-20')

# solve by iDS algorithm with best-scenario constraints
mod.solve(algorithm='ids-b', timelimit=100)

# print results
print("objective value: {}".format(mod.objval))
print("time to best: {:.2f}".format(mod.ttb))

# write the results to file
mod.write("result.txt")
```

_Note: Benchmark instances for_

- min-max regret knapsack problem
- min-max regret multidimensional knapsack problem
- min-max regret set covering problem
- min-max regret generalized assignment problem

_are available in the `instance` directory on the [project's homepage](https://github.com/ebereta/iDS/). For easy access to the example files, we recommend cloning the repository._

## Algorithm

To solve the MMR-BIP, mmrbipy provides four algorithms:
- fixed scenario algorithm (*fix*);
- branch-and-cut algorithm (*bc*);
- dual substitution algorithm (*ds*);
- iterated dual substitution algorithm with best-scenario constraints (*ids-b*);
- iterated dual substitution algorithm with Hamming-distance constraints (*ids-h*).

_Note: The implement are based on [gurobypy](https://pypi.org/project/gurobipy/)._

## Additional information

For more information about the algorithms used in the solver, see [Wu et al. (2022)](https://arxiv.org/abs/2012.07530).