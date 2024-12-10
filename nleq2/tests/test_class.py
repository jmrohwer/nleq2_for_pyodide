import numpy as np
import scipy as sp
from nleq2 import nleq2

def lin3(x):
    v1 = 10 - x[0]
    v2 = 2 * x[0] - 5 * x[1]
    v3 = 10 * x[1]
    dx0dt = v1 - v2
    dx1dt = v2 - v3
    return [dx0dt, dx1dt]

class TestClass:

    def test_nleq2(self):
        initial = [1, 1]
        N = len(initial)
        iwk = np.zeros((N + 52), "i")
        rwk = np.zeros(((N + max(N, 10) + 15) * N + 61), "d")
        iopt = np.zeros((50), "i")
        rtol = 1e-14 * N
        iopt[2] = 2
        iopt[8] = 0
        iopt[10] = 0
        iopt[11] = 6
        iopt[12] = 0
        iopt[13] = 6
        iopt[14] = 0
        iopt[15] = 6
        iopt[30] = 4
        iopt[31] = 1
        iopt[34] = 0
        iopt[37] = 0
        iopt[38] = 2
        iwk[30] = 50

        nleq2_res, s_scale, rtol, iopt, ierr = nleq2.nleq2(
            lin3, lin3, initial, initial, rtol, iopt, iwk, rwk
        )

        sp_res = sp.optimize.fsolve(lin3, initial)

        assert np.allclose(nleq2_res, sp_res)

        print('scipy: ', sp_res)
        print('nleq2: ', nleq2_res)
