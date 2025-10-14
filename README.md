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

1. Clone the pyodide source repo and checkout a recent stable branch, e.g.
   `0.28.3`:
   ```shell
   $ git clone https://github.com/pyodide/pyodide.git
   $ git checkout 0.28.3
    ```
   The directory you cloned into is referred to as `PYODIDE_HOME` below.

1. Build pyodide from source
   (see [here](https://pyodide.org/en/stable/development/building-from-sources.html#using-docker)).
   The easiest way is to use the provided docker image.
   This will take a while, but only needs to be done once.

1. Clone this repo and set up the recipe:
   ```shell
   $ cd ${PYODIDE_HOME}/packages
   $ mkdir nleq2; cd nleq2
   $ git clone https://github.com/jmrohwer/nleq2_for_pyodide.git nleq2
   $ ln -s nleq2/pyodide_recipe/meta.yaml .
   ```

1. Build nleq2 using the provided docker image:
   ```shell
   $ cd $PYODIDE_HOME
   $ ./run_docker
   src $ pyodide build-recipes nleq2 --no-install
   ```
   The build will fail with an error but the wheel is nevertheless created.
   It has to be manually copied to the pyodide distribution directory.

1. Add the built wheel to your pyodide environment:
   ```shell
   $ cd $PYODIDE_HOME/packages
   $ cp nleq2/build/nleq2-4.3/dist/nleq2-4.3-cp313-cp313-pyodide_2025_0_wasm32.whl ../dist/
   ```

1. Add the metadata for the package to the pyodide environment lockfile.
   A convenient script has been provided for this:
   ```shell
   $ cd $PYODIDE_HOME/dist
   $ pip install simple_file_checksum
   $ python ../packages/nleq2/nleq2/utils/update_pyodide_lockfile nleq2-4.3-cp313-cp313-pyodide_2025_0_wasm32.whl 'numpy'
   ```

1. Serve the pyodide distribution:
   ```shell
   $ cd $PYODIDE_HOME
   $ python -m http.server -d dist
   ```

1. Test by pointing your browser to http://0.0.0.0:8000/, opening `console.html`,
   and running the following in the browser console:
   ```python
   >>> import nleq2
   >>> nleq2.test()
   ```
