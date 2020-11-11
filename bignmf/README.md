This directory contains code from the [BigNmf package](https://github.com/thenmf/bignmf/commit/8d6761e71857858cff84fc03a318de0ad4a3ace2), which implements joint NMF and integrative NMF in Python.

Three changes/bug fixes were made and the fixed code directly included in this repository for ease of installation for our students running the tutorial code:
1. Removed function `def cophenetic_correlation(consensus_matrix)` in `bignmf/models/nmf.py` to remove a dependency that is not needed when running the tutorial code.
2. Added random state seed to fix the random number generations used in initializing factors in `bignmf/models/jnmf/integrative.py` and `bignmf/models/jnmf/standard.py`.
3. Fixed bug with updating Ws and Vs and calculating objective in `bignmf/models/jnmf/integrative.py`
