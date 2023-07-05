"""Example BB84 single photon protocol"""
from tno.quantum.communication.qkd_key_rate.protocols.quantum.bb84_single_photon import (
    BB84SingleAsymptoticKeyRateEstimate,
)
from tno.quantum.communication.qkd_key_rate.test.conftest import standard_detector

detector = standard_detector.customise(
    dark_count_rate=1e-8,
    polarization_drift=0,
    error_detector=0.1,
    efficiency_party=1,
)

asymptotic_key_rate = BB84SingleAsymptoticKeyRateEstimate(detector=detector)

mu, rate = asymptotic_key_rate.optimize_rate(attenuation=0.2)
print(f"intensity: {mu}, key-rate: {rate}")
assert rate == asymptotic_key_rate.compute_rate(mu, attenuation=0.2)
