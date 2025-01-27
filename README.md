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
git clone https://github.com/jose011013/interval-entropy.git
cd interval-entropy
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

To calculate the generalized entropy for a dataset of interval-valued variables:

1. Read your data as a pandas Data Frame.
2. Use the provided script to compute entropy.

### Command-Line Options

- `--input`: Path to the input file containing interval data.
- `--output`: Path to save the computed entropy results.
- `--plot`: (Optional) Generate visualizations of entropy distributions.

