# nleq2

This is a stand-alone compile and testing of the `nleq` Fortran extension module
used by [PySCeS](https://github.com/PySCeS/pysces).
The module is built using `f2py` and `meson-python`.
The main purpose is for testing and debugging the compilation with
[Pyodide](https://pyodide.org/en/stable/index.html).

The module defines a single wrapped Fortran function:

```python
In [2]: nleq2.nleq2.nleq2?
Signature:   nleq2.nleq2.nleq2(*args, **kwargs)
Type:        fortran
String form: <fortran function nleq2>
Docstring:  
x,xscal,rtol,iopt,ierr = nleq2(fcn,jac,x,xscal,rtol,iopt,iwk,rwk,[n,liwk,lrwk,fcn_extra_args,jac_extra_args])

Wrapper for ``nleq2``.

Parameters
----------
fcn : call-back function
jac : call-back function
x : input rank-1 array('d') with bounds (n)
xscal : input rank-1 array('d') with bounds (n)
rtol : input float
iopt : input rank-1 array('i') with bounds (50)
iwk : input rank-1 array('i') with bounds (liwk)
rwk : input rank-1 array('d') with bounds (lrwk)

Other Parameters
----------------
n : input int, optional
    Default: len(x)
fcn_extra_args : input tuple, optional
    Default: ()
jac_extra_args : input tuple, optional
    Default: ()
liwk : input int, optional
    Default: len(iwk)
lrwk : input int, optional
    Default: len(rwk)

Returns
-------
x : rank-1 array('d') with bounds (n)
xscal : rank-1 array('d') with bounds (n)
rtol : float
iopt : rank-1 array('i') with bounds (50)
ierr : int

Notes
-----
Call-back functions::

    def fcn(x,ifail,[n]): return f,ifail
    Required arguments:
        x : input rank-1 array('d') with bounds (n)
        ifail : input int
    Optional arguments:
        n : input int, optional
    Default: len(x)
    Return objects:
        f : rank-1 array('d') with bounds (n)
        ifail : int
    def jac(x,[n,m1]): return a
    Required arguments:
        x : input rank-1 array('d') with bounds (n)
    Optional arguments:
        n : input int, optional
    Default: len(x)
        m1 : input int, optional
    Default: shape(a,0)
    Return objects:
        a : rank-2 array('d') with bounds (m1,n)
```

## Build instructions

1. Clone the repo:
   ```shell 
   $ git clone https://github.com/jmrohwer/nleq2_for_pyodide.git
   ```
2. Build / install:
   ```shell
   $ cd nleq2_for_pyodide
   $ python -m build .      or
   $ pip install .
   ```
3. Pyodide build:    
   A build recipe is provided under `pyodide recipe`. This assumes that the source lives
   in `packages/nleq2/nleq2_for_pyodide` in the Pyodide build tree.
4. Test:
   ```python
   import nleq2
   nleq2.test()
   ```
