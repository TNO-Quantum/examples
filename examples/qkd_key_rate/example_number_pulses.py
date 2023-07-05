"""Example BB84 FiniteKeyRate estimate for various number of pulses"""
import matplotlib.pyplot as plt
import numpy as np

from tno.quantum.communication.qkd_key_rate.protocols.quantum.bb84 import (
    BB84FiniteKeyRateEstimate,
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
fig, ax = plt.subplots()


number_of_pulses = [1e7, 1e8, 1e9, 1e10]
for n_pulses in number_of_pulses:
    print(f"Starting computation for 1e{int(np.log10(n_pulses))} pulses.")
    label = rf"N=$10^{{{int(np.log10(n_pulses))}}}$"
    protocol = BB84FiniteKeyRateEstimate(detector=detector, number_of_pulses=n_pulses)
    key_rate = []
    for att in attenuation:
        try:
            mu, rate = protocol.optimize_rate(attenuation=att)
            key_rate.append(rate)
        except Exception as e:
            print(
                f"Failed optimization for 1e{int(np.log10(n_pulses))} pulses"
                f", attenuation {att}:",
                e,
            )
            break
    ax.semilogy(attenuation[: len(key_rate)], key_rate, label=label)

# Labels/axis
ax.set_xlabel("Loss (dB)", fontsize=12)
ax.set_ylabel("Key-rate", fontsize=12)
ax.set_title("Secure key-rate", fontsize=14)
ax.legend()

plt.show()
