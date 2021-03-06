import sys
import os
import numpy as np
import pytest

thisfile = os.path.abspath(__file__)
modulepath = os.path.dirname(os.path.dirname(thisfile))

sys.path.insert(0, modulepath)
import tensorcircuit as tc


def universal_vmap():
    def sum_real(x, y):
        return tc.backend.real(x + y)

    vop = tc.backend.vmap(sum_real)
    t = tc.gates.array_to_tensor(np.ones([20, 1]))
    return vop(t, 2.0 * t)


def test_vmap_np():
    r = universal_vmap()
    assert r.shape == (20, 1)


def test_vmap_jax(jaxb):
    r = universal_vmap()
    assert r.shape == (20, 1)


def test_vmap_tf(tfb):
    r = universal_vmap()
    assert r.numpy()[0, 0] == 3.0


def test_vmap_torch(torchb):
    r = universal_vmap()
    assert r.numpy()[0, 0] == 3.0
