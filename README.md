# Hybrid Learning Automata (HLA)

Python implementation of the **Hybrid Learning Automaton**, which combines a fixed-structure and a
variable-structure learning automaton in one decision maker. The code was developed in joint work
between Saber Gholami and Ali Mohammad Saghiri, as the learning component for an adaptive dropout
method for neural networks.

## Publication

S. Gholami, A. M. Saghiri, S. M. Vahidipour, M. R. Meybodi,
"HLA: a novel hybrid model based on fixed structure and variable structure learning automata,"
*Journal of Experimental & Theoretical Artificial Intelligence*, 2023.

## What is in the repository

| File | What it is |
| --- | --- |
| `LA.py` | Variable-structure learning automaton (`LA`). |
| `FixedStructureLearningAutomata.py` | Fixed-structure learning automaton with memory depth `N`. |
| `HybridLearningAutomata.py` | The hybrid automaton (`HybridLearningAutomata`), which switches between the two. |
| `HLA_EX1.py` | Experiment: hybrid automata with different depths compared against a pure-chance automaton. |
| `Copy_of_MABgame.ipynb` | Multi-armed bandit game notebook used for comparison. |

## Run the experiment

Requires Python 3 with NumPy and Matplotlib.

```bash
pip install numpy matplotlib
python HLA_EX1.py
```

The script runs a two-action environment in which action 0 is rewarded with probability 0.9, and
saves two figures in the `Hybrid Results/` folder:

- `1_1_1.png` – total number of rewards (TNR) over time
- `1_1_2.png` – total number of action switches (TNAS) over time

## Using the automaton in your own code

```python
from HybridLearningAutomata import HybridLearningAutomata

# r actions, depth N, reward rate lambda1, penalty rate lambda2, starting action c
hla = HybridLearningAutomata(r=2, N=4, lambda1=0.1, lambda2=0, c=1)

action = hla.action_selection()   # choose an action
hla.update(1)                     # 1 = reward, 0 = penalty
```

## Related repositories

- [Adaptive-Dropout-Algorithm2](https://github.com/amsaghiri/Adaptive-Dropout-Algorithm2) – the neural-network experiment framework with dropout
- [Learning-Automata](https://github.com/amsaghiri/Learning-Automata) – an introductory single-automaton implementation
