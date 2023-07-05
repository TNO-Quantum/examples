"""Example bb84 protocol"""
from tno.quantum.communication.qkd_key_rate.protocols.quantum.bb84 import (
    BB84AsymptoticKeyRateEstimate,
    BB84FiniteKeyRateEstimate,
    BB84FullyAsymptoticKeyRateEstimate,
)
from tno.quantum.communication.qkd_key_rate.test.conftest import standard_detector

detector = standard_detector.customise(
    dark_count_rate=1e-8,
    polarization_drift=0,
    error_detector=0.1,
    efficiency_party=1,
)

# Fully asymptotic key-rate protocol
fully_asymptotic_key_rate = BB84FullyAsymptoticKeyRateEstimate(detector=detector)
mu, rate = fully_asymptotic_key_rate.optimize_rate(
    attenuation=0.2, x_0=[0.5], bounds=[(0.1, 0.9)]
)
print(f"Intensity: {mu}, key-rate: {rate}")
assert rate == fully_asymptotic_key_rate.compute_rate(mu, attenuation=0.2)

# Asymptotic key-rate protocol
asymptotic_key_rate = BB84AsymptoticKeyRateEstimate(
    detector=detector, number_of_decoy=3
)
mu, rate = asymptotic_key_rate.optimize_rate(
    attenuation=0.2,
    x_0=[0.5, 0.3, 0.2, 0.4],
    bounds=[(0.1, 0.9), (0.1, 0.9), (0.1, 0.9), (0.1, 0.9)],
)
print(f"Intensity: {mu}, key-rate: {rate}")
assert rate == asymptotic_key_rate.compute_rate(mu, attenuation=0.2)

# Finite key-rate protocol
finite_key_rate = BB84FiniteKeyRateEstimate(detector=detector)
x, rate = finite_key_rate.optimize_rate(attenuation=0.2)

d = finite_key_rate._extract_parameters(x)
print(f"Intensity: {d['mu']}, key-rate: {rate}")

assert rate == finite_key_rate.compute_rate(
    mu,
    attenuation=0.2,
    probability_basis_X=d["probability_basis_X"],
    probability_basis_Z=d["probability_basis_Z"],
)
