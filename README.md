# mmrbipy: A solver for the min-max regret binary integer programming problem (MMR-BIP)

## Installation

In a virtual environment with Python 3.6+, mmrbipy can be installed via

```bash
pip install mmrbipy
```

## Using mmrbipy

With a compatible instance file, mmrbipy solves the MMR-BIP from a Python script:

```python
from mmrbipy import Model

# Generate a model from instance file
mod = Model(problem='kp', filename='../instance/KP/1-70-01-45-20')

# Solve by iDS algorithm with best-scenario constraints
mod.solve(algorithm='ids-b', timelimit=100)

# Print results
print("objective value: {}".format(mod.objval))
print("time to best: {:.2f}".format(mod.ttb))

# Write the results to file
mod.write("result.txt")
```
## Model
To solve the MMR-BIP, mmrbipy provides five types of instance format:

- min-max binary integer programming problem (*bip*)
- min-max regret knapsack problem (*kp*)
- min-max regret multidimensional knapsack problem (*mkp*)
- min-max regret set covering problem (*scp*)
- min-max regret generalized assignment problem (*gap*)

See [instance page](https://github.com/ebeleta/iDS/tree/main/instance) for the details of each type

### Set problem type in constructor of _Model_ class
```python
# Generate a model from instance file
mod = Model(problem='kp', filename='../instance/KP/1-70-01-45-20')
```

_Note: Benchmark instances for_

- _min-max regret knapsack problem_
- _min-max regret multidimensional knapsack problem_
- _min-max regret set covering problem_
- _min-max regret generalized assignment problem_

_are available in the `instance` directory on the [project's homepage](https://github.com/ebeleta/iDS/). For easy access to the example files, we recommend cloning the repository._

## Algorithm

To solve the MMR-BIP, mmrbipy provides five algorithms:
- fixed scenario algorithm (*fix*);
- branch-and-cut algorithm (*bc*);
- dual substitution algorithm (*ds*);
- iterated dual substitution algorithm with best-scenario constraints (*ids-b*);
- iterated dual substitution algorithm with Hamming-distance constraints (*ids-h*).

### Set algorithm type in _solve_ function
```python
# Solve by iDS algorithm with best-scenario constraints
mod.solve(algorithm='ids-b', timelimit=100)
```

_Note: The implement are based on [gurobypy](https://pypi.org/project/gurobipy/)._

## Additional information

For more information about the algorithms used in the solver, see [Wu et al. (2022)](https://arxiv.org/abs/2012.07530).