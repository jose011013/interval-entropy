# Generalized Entropy for Interval-Valued Data

This repository contains the implementation of the methods and algorithms presented in the paper **"Generalized Entropy for Interval-Valued Data"**. The paper introduces a novel framework for calculating entropy in symbolic data analysis, focusing on interval-valued variables. This approach broadens the traditional understanding of entropy by accounting for the variability and uncertainty inherent in interval representations.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Citation](#citation)
- [Contributing](#contributing)
- [License](#license)

## Overview

Traditional entropy measures are not well-suited for symbolic data types, such as intervals, sets, or histograms, which arise in applications where uncertainty or imprecision is present. This project implements a generalized entropy measure that:

1. Incorporates the variability within interval-valued data.
2. Preserves key properties of entropy, such as non-negativity and additivity.
3. Extends to more complex symbolic data structures in future work.

## Features

- Implementation of the generalized entropy formula for interval-valued data.
- Visualization tools for comparing entropy values across datasets.
- A modular design for extending the framework to other symbolic data types.

## Installation

Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/generalized-entropy-interval.git
cd generalized-entropy-interval
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

To calculate the generalized entropy for a dataset of interval-valued variables:

1. Prepare your data as a CSV file with each row representing an interval (e.g., `lower_bound,upper_bound`).
2. Use the provided script to compute entropy:

```bash
python compute_entropy.py --input data/intervals.csv --output results/entropy.json
```

### Command-Line Options

- `--input`: Path to the input file containing interval data.
- `--output`: Path to save the computed entropy results.
- `--plot`: (Optional) Generate visualizations of entropy distributions.

## Examples

An example dataset is provided in `data/example_intervals.csv`. To compute entropy for this dataset:

```bash
python compute_entropy.py --input data/example_intervals.csv --output results/example_entropy.json --plot
```

The results will include a JSON file with entropy values and visualizations saved in the `results` directory.

## Citation

If you use this code or refer to the paper, please cite:

```bibtex
@article{piedra2025generalizedentropy,
  title={Generalized Entropy for Interval-Valued Data},
  author={Piedra, José Andrés},
  journal={Journal of Symbolic Data Analysis},
  year={2025}
}
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add feature-name'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
