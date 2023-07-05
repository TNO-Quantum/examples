"""Example that shows how to plot optimal key-rate versus attenuation"""
import matplotlib.pyplot as plt
import numpy as np

from tno.quantum.communication.qkd_key_rate.protocols.quantum.bb84 import (
    BB84AsymptoticKeyRateEstimate,
    BB84FiniteKeyRateEstimate,
    BB84FullyAsymptoticKeyRateEstimate,
)
from tno.quantum.communication.qkd_key_rate.protocols.quantum.bb84_single_photon import (
    BB84SingleAsymptoticKeyRateEstimate,
)
from tno.quantum.communication.qkd_key_rate.test.conftest import standard_detector

detector = standard_detector.customise(
    dark_count_rate=6e-7,
    polarization_drift=0.0707,
    error_detector=5e-3,
    efficiency_detector=0.1,
)

distance = np.arange(0, 40)
attenuation_factor = 1
attenuation = attenuation_factor * distance
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))


protocols = [
    ("Fully Asymptotic BB84", BB84FullyAsymptoticKeyRateEstimate(detector=detector)),
    ("Asymptotic BB84", BB84AsymptoticKeyRateEstimate(detector=detector)),
    (
        "Single photon Asymptotic BB84",
        BB84SingleAsymptoticKeyRateEstimate(detector=detector),
    ),
    (
        "Finite BB84",
        BB84FiniteKeyRateEstimate(detector=detector, number_of_pulses=1e12),
    ),
]


for label, protocol in protocols:
    print("Starting computation for:", label)
    key_rate = []
    intensity = []
    for i, att in enumerate(attenuation):
        try:
            mu, rate = protocol.optimize_rate(attenuation=att)
            key_rate.append(rate)
            intensity.append(mu[0])
        except Exception as e:
            print(f"Failed optimization for {label}, attenuation {att}:", e)
            break

    ax1.semilogy(attenuation[: len(key_rate)], key_rate, label=label)
    ax2.semilogy(attenuation[: len(intensity)], intensity, label=label)

# Labels/axis
ax1.set_xlabel("Loss (dB)", fontsize=14)
ax1.set_ylabel("Key-rate", fontsize=14)
ax1.set_title("Secure key-rate", fontsize=16)
ax1.legend()

ax2.set_xlabel("Loss (dB)", fontsize=14)
ax2.set_ylabel("Laser intensity", fontsize=14)
ax2.set_title("Intensity settings", fontsize=16)
ax2.legend()

fig.suptitle("BB84 Protocol", fontsize=16)
plt.show()
