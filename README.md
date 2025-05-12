# TNO Quantum: Examples


---

This repository is no longer maintained. Examples have been moved to the full toolbox documentation, which can be found [here](https://github.com/TNO-Quantum/documentation).

---

This repository contains elaborate examples for TNO Quantum software components.

TNO Quantum is dedicated to developing reusable software components for applying current and near-term quantum technology. Our code base is use-case driven and contains fully-functional, self-contained software components, which can be used as building blocks to enable further development of quantum applications. Currently, the focus of TNO Quantum is on secure communication, optimization, simulation, and machine learning.

## Content

1. Variational Classifier
   1. [Classification: demonstrates basic classifier usage.](examples\vc\classification.ipynb)
   1. [Decision Boundary: demonstrates how to calculate the decision boundary.](examples\vc\decision_boundary.ipynb)
   1. [Quantum Models: demonstrates how to use different models.](examples\vc\quantum_models.ipynb)
1. Quantum Key-Rate
   1. [Number of pulses](examples\qkd_key_rate\example_number_pulses.py)
   1. [BB84 protocol](examples\qkd_key_rate\example_bb84_plot.py)
   1. [Basic usage BB84 protocols](examples\qkd_key_rate\example_bb84.py)
   1. [Basic usage BB84 single photon protocol](examples\qkd_key_rate\example_bb84_single_photon.py)
   1. [Basic usage BBM92 protocols](examples\qkd_key_rate\example_bbm92.py)
   1. [Basic usage Cascade protocol](examples\qkd_key_rate\example_cascade.py)
   1. [Basic usage Winnow protocol](examples\qkd_key_rate\example_winnow.py)
   1. [Basic usage privacy amplification](examples\qkd_key_rate\example_privacy_amplification.py)
1. Portfolio Optimization
   1. [Pareto front](examples\portfolio_optimization\pareto_front.ipynb)
   1. [Different samplers](examples\portfolio_optimization\different_samplers.ipynb)
   1. [Emission constraint](examples\portfolio_optimization\emission_constraint.ipynb)
   1. [Different ROC formulations](examples\portfolio_optimization\different_roc_formulations.ipynb)


## Install requirements

The requirements to run specific examples can be found in the `requirements` folder and can be installed using pip

```commandline
pip install -r requirements/requirements_vc.txt
pip install -r requirements/requirements_qkd.txt
pip install -r requirements/requirements_portfolio_optimization.txt
```

## (End)use limitations
The content of this software may solely be used for applications that comply with international export control laws.

