# Calculate Energy

**Version:** 0.0.1

**Author:** J. Schaarschmidt

## Description

This script calculates the strain of a crystal structure, then writes the energy and volume data to a file.

## Inputs
- `structure.yml`: Input file for the structure.
- `structure_strain.traj`: Trajectory file for the structure.

## Outputs
- Energy and volume data: Saved in a text file (e.g., `energy_volume_data.txt`).
- Error logs: Documenting any issues encountered (e.g., `error_data.txt`).

## Dependencies
- ASE
- pwtools
- Quantum Espresso
