Goldbach Lab

**A Computational Laboratory for Goldbach's Conjecture**

Goldbach Lab is a computational mathematics project that investigates the number of prime decompositions of even integers. It combines a C implementation, independent Python verification, statistical analysis, and data visualization.

> This project studies finite computational evidence. It does not claim to prove Goldbach's conjecture.

1. Mathematical Problem

Goldbach's conjecture states that every even integer greater than 2 can be expressed as the sum of two primes.

For an even integer \(N \geq 4\), define

\[
G(N)=\#\{(p,q):p+q=N,\ p\leq q,\ p,q\text{ prime}\}.
\]

The condition \(p\leq q\) ensures that each unordered prime pair is counted exactly once.

For example,

\[
10=3+7=5+5,
\]

so \(G(10)=2\).

2. Project Goals

- Compute \(G(N)\) for even integers within a specified finite range.
- Use C to generate computational results.
- Store results in CSV format.
- Independently recompute the values using Python.
- Summarize the data with descriptive statistics.
- Visualize the distribution and variation of \(G(N)\).

3. Project Structure

```text
Goldbach-Lab/
├── goldbach.c
├── analyze.py
├── goldbach_results.csv
├── results/
│   ├── goldbach_scatter.png
│   ├── goldbach_frequency.png
│   ├── goldbach_block_means.png
│   ├── verification.csv
│   └── report.txt
└── README.md
```

The structure above describes the intended layout. Adjust file paths if your actual project differs.

4. Methods

C computation

The C program uses the Sieve of Eratosthenes to identify primes and counts unordered prime pairs whose sum equals each target even integer.

Python verification

The Python program independently constructs a prime table and recomputes \(G(N)\). It compares the computed values with those recorded by the C program.

Statistical analysis

The analysis reports:

- Number of data points
- Mean and median of \(G(N)\)
- Minimum and maximum values
- The even integers associated with those extrema

Visualization

Three plots are generated:

1. `goldbach_scatter.png` — \(G(N)\) against \(N\).
2. `goldbach_frequency.png` — frequency distribution of \(G(N)\).
3. `goldbach_block_means.png` — mean \(G(N)\) over consecutive blocks.

The program also generates `verification.csv` and `report.txt`.

5. How to Run

Run the C program using the compilation command appropriate for your source file location. For example, if the source is `src/goldbach.c`:

```bash
gcc -std=c11 -Wall -Wextra -Werror src/goldbach.c -o goldbach
./goldbach
```

Ensure the C program writes `goldbach_results.csv` into the project root.

Install the Python plotting dependency if necessary:

```bash
python3 -m pip install matplotlib
```

Run the analysis from the project root:

```bash
python3 analyze.py
```

6. Current Experiment

The initial experiment examined even integers from 4 through 100,000, inclusive, in increments of 2.

- Data points: 49,999
- Mean \(G(N)\): 507.3498
- Median \(G(N)\): 456
- Minimum \(G(N)\): 1
- Maximum \(G(N)\): 2,168
- Location of the observed maximum: \(N=99,330\)
- C/Python matching rows: 49,999 out of 49,999

These results describe the current dataset only. They should be regenerated whenever the input range or implementation changes.

7. Limitations

- Finite computation cannot establish Goldbach's conjecture for all even integers.
- Agreement between two implementations does not rule out shared logical errors.
- Statistical patterns observed in this range do not, by themselves, establish a mathematical theorem.
- Reproducibility requires recording the program version, input range, and relevant execution environment.

8. Future Work

Potential extensions include:

- Additional independent correctness tests
- Performance benchmarking
- Analysis of how \(G(N)\) varies with \(N\)
- Comparison of different prime-generation and pair-counting algorithms
- Reproducible experiment records

9. Scope

Goldbach Lab is an educational computational mathematics project. Its purpose is to explore numerical evidence, practice algorithm implementation, and develop reliable methods for validating computational results.
