# Copyright 2018 The Cirq Developers
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import numpy as np
import pytest

import cirq


def test_unitary():
    m = np.array([[0, 1], [1, 0]])
    d = np.array([])

    class NoMethod:
        pass

    class ReturnsNone:
        def _unitary_(self):
            return None

    class ReturnsSome:
        def _unitary_(self):
            return m

    with pytest.raises(TypeError):
        _ = cirq.unitary(NoMethod())
    with pytest.raises(TypeError):
        _ = cirq.unitary(ReturnsNone())
    assert cirq.unitary(ReturnsSome()) is m

    assert cirq.unitary(NoMethod(), None) is None
    assert cirq.unitary(ReturnsNone(), None) is None
    assert cirq.unitary(ReturnsSome(), None) is m

    assert cirq.unitary(NoMethod(), 1) == 1
    assert cirq.unitary(ReturnsNone(), 1) == 1
    assert cirq.unitary(ReturnsSome(), 1) is m

    assert cirq.unitary(NoMethod(), d) is d
    assert cirq.unitary(ReturnsNone(), d) is d
    assert cirq.unitary(ReturnsSome(), d) is m
