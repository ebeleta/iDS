# Instance

## MMR-MKP Instance format
> "Wu, W., Iori, M., Martello, S., & Yagiura, M. (2020). An Iterated Dual Substitution Approach for Binary Integer Programming Problems under the Min-Max Regret Criterion. arXiv preprint arXiv:2012.07530."
There are 270 data files.
  
The problem in each data file have an associated notation as follows:
  
 1010030-03: denotes that this is the 3rd instance  
			 in a group of problems  
			 with 10-dimensions, 100-items and  
			 the max 30%-uncertainty on profit intervals.  

The format for each of these data files is:
~~~
number of dimensions (m)	number of items (n)
the minimum profit of item j (j=1,...,n)
the maximum profit of item j (j=1,...,n)
for each dimension i (i=1,...,m) in turn:
    resource consumed in selecting item j in dimension i (j=1,...,n)
resource capacity of dimension i (i=1,...,m)
~~~

## MMR-GAP Instance format
> "Wu, W., Iori, M., Martello, S., & Yagiura, M. (2018). Exact and heuristic algorithms for the interval min-max regret generalized assignment problem. Computers & Industrial Engineering, 125, 98-110."

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
