import sys
import click
from .main import pfs2yaml


@click.command()
@click.argument('input', required=True, type=click.Path(exists=True))
@click.argument('output', required=False)
def cli(input, output=None):
    """Convert PFS files to YAML

    Output filename is optional.

    Default value is input filename with .yml extension
    """

    with(open(input)) as f:
        pfs = f.read()

    res = pfs2yaml(pfs)

    if output is None:
        output = input + ".yml"

    print(f"Writing YAML file: {output} ")
    with(open(output,'w')) as f:
        f.write(res)



#if __name__ == '__main__':
#    input_file = sys.argv[1]
#    out_file = sys.argv[2]
#    cli(input_file, out_file)