# Target Weight Combinations

This Python script helps determine which combination of available weight plates should be used with adjustable dumbbells to achieve a target weight, by finding the combination with the smallest sum closest to half of the specified target weight.

## Usage

1. **Input**: Run the script and provide a target weight (in kg) when prompted.
2. **Output**: The script will calculate combinations of predefined weights to find the smallest sum closest to half of the target weight.

## Requirements

- `itertools` module

## Example

Suppose the target weight is `5.0` kg and available weights are `[2.5, 2, 1.5, 1.25]`.
The script will find combinations that sum up to `2.5 kg` (half of `5.0 kg`) and output the smallest sum with its combination.