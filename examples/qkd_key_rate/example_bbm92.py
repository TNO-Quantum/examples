"""Example BBM92 protocol"""

import numpy as np

from tno.quantum.communication.qkd_key_rate.protocols.quantum.bbm92 import (
    BBM92AsymptoticKeyRateEstimate,
    BBM92FiniteKeyRateEstimate,
)
from tno.quantum.communication.qkd_key_rate.test.conftest import standard_detector

detector = standard_detector.customise(
    dark_count_rate=1e-8,
    polarization_drift=0,
    error_detector=0.1,
    efficiency_party=1,
)

# Asymptotic key-rate protocol
asymptotic_key_rate = BBM92AsymptoticKeyRateEstimate(
    detector=detector, detector_alice=detector
)
mu, rate = asymptotic_key_rate.optimize_rate(attenuation=0.2)
print(f"Intensity: {mu}, key-rate: {rate}")
assert rate == asymptotic_key_rate.compute_rate(mu, attenuation=0.2)

# Finite key-rate protocol
finite_key_rate = BBM92FiniteKeyRateEstimate(detector=detector, detector_Alice=detector)
x, rate = finite_key_rate.optimize_rate(attenuation=0.2, x_0=np.array([0.3, 0.7, 0.7]))
d = finite_key_rate._extract_parameters(x)
print(f"Intensity: {d['mu']}, key-rate: {rate}")
assert rate == finite_key_rate.compute_rate(
    d["mu"],
    attenuation=0.2,
    probability_basis_X=d["probability_basis_X"],
    probability_basis_Z=d["probability_basis_Z"],
)
