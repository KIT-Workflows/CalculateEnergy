import os
import yaml

from ase.io import read, write


def write_input_file(element, file_pattern, output_filename, crystal, kpts):
    """
    Writes the input file for strain calculation.

    Parameters:
    file_pattern (str): File pattern for reading the strained structure files ('structure_strain.traj').
    output_filename (str): Path to the output file for PWscf input ('strain.pwi').
    """

    os.environ['ESPRESSO_PSEUDO'] = os.getcwd()

    pseudopotentials = {element: f"{element}.pbe-n-kjpaw_psl.1.0.0.UPF"}
    input_data_static = {'calculation': 'scf'}

    structure_strain = read(file_pattern)

    write(
        output_filename,
        structure_strain,
        Crystal=crystal,
        kpts=kpts,
        input_data=input_data_static,
        pseudopotentials=pseudopotentials,
        tstress=True,
        tprnfor=True
    )


if __name__ == '__main__':
    with open("structure.yml", "r") as file:
        params = yaml.safe_load(file)

    write_input_file(
        element=params['element'],
        crystal=params['crystal'],
        kpts=tuple(map(int, params['kpts'].split(','))),
        file_pattern='structure_strain.traj',
        output_filename='strain.pwi'
    )
