# IPython log file

get_ipython().run_line_magic('logstart', '')
get_ipython().run_line_magic('ls', '')
get_ipython().run_line_magic('run', '-i vectorsum.py 1000')
get_ipython().run_line_magic('run', '-d vectorsum.py 1000')
get_ipython().run_line_magic('run', '-p vectorsum.py 1000')
a=2+2
a
get_ipython().run_line_magic('hist', '')
a = arange(5)
a.dtype
a
a.shape
m = array([arange(2), arange(2)])
m
m.shape
a = array([[1, 2], [3, 4]])
a
a[0, 0]
a[0,1]
a[1,0]
a[1,1]
float64(42)
int8(42.0)
bool(42)
