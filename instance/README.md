# Instance

## MMR-GAP Instance format
There are 300 data files and 60 files for each type.
  
The problem in each data file have an associated notation as follows:
  
 c054025-3.dat:	denotes that this is the 3rd instance  
		in a group of problems of type c  
		with 5-agents, 40-jobs and  
		the max 25%-uncertainty on cost intervals.

The format for each of these data files is:
~~~
number of agents (m)
number of jobs (n)
for each agent i (i=1,...,m) in turn:
    the minimum cost of allocating job j to agent i (j=1,...,n)
for each agent i (i=1,...,m) in turn:
    the maximum cost of allocating job j to agent i (j=1,...,n)
for each agent i (i=1,...,m) in turn:
    resource consumed in allocating job j to agent i (j=1,...,n)
resource capacity of agent i (i=1,...,m)
~~~
