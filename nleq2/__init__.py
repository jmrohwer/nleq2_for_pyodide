import numpy as np
# from .nleq2 import nleq2

def test():
    def lin3(x):
        v1 = 10 - x[0]
        v2 = 2 * x[0] - 5 * x[1]
        v3 = 10 * x[1]
        dx0dt = v1 - v2
        dx1dt = v2 - v3
        return [dx0dt, dx1dt]
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

    test_res = np.array([4.28571429, 0.57142857])

    assert np.allclose(nleq2_res, test_res)

    print('nleq2: ', nleq2_res)
