# PFS2YAML

> [!NOTE]
> This functionality is now part of [MIKE IO](https://github.com/DHI/mikeio)

Convert PFS files to YAML or python dictionary.

For a complete example of extracting coordinates of all sources see this [notebook](notebooks/Roskilde%20sources.ipynb).

## Installation
    pip install https://github.com/DHI/pfs2yaml/archive/master.zip

## Usage

```python
Python 3.6.6 |Anaconda, Inc.| (default, Jun 28 2018, 11:27:44) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import pfs2yaml
>>> pfs = """

... [FemEngineHD]
...    [DOMAIN]
...       Touched = 1
...       discretization = 2
...       number_of_dimensions = 2
...       number_of_meshes = 1
...       file_name = |.\weird.mesh|
...       type_of_reordering = 1
...       number_of_domains = 16
...       coordinate_type = 'PROJCS["UTM-32",GEOGCS["Unused",DATUM["UTM Projections",SPHEROID["WGS 1984",6378137,298.257223563]],PRIMEM["Greenwich",0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",500000],PARAMETER["False_Northing",0],PARAMETER["Central_Meridian",9],PARAMETER["Scale_Factor",0.9996],PARAMETER["Latitude_Of_Origin",0],UNIT["Meter",1]]'
...       minimum_depth = -4.98911480069749
...       datum_depth = 0.0
...       vertical_mesh_type_overall = 1
...       number_of_layers = 10
...       z_sigma = -7.464212579701861
...       vertical_mesh_type = 1
...       layer_thickness = 0.1, 0.1, 0.1, 0.3, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1
...     EndSect
... EndSect"""

>>> yml = pfs2yaml.pfs2yaml(pfs)
>>> print(yml)
---

FemEngineHD:
  DOMAIN:
    touched :  1
    discretization :  2
    number_of_dimensions :  2
    number_of_meshes :  1
    file_name :  .\weird.mesh
    type_of_reordering :  1
    number_of_domains :  16
    coordinate_type :  'PROJCS["UTM-32",GEOGCS["Unused",DATUM["UTM Projections",SPHEROID["WGS 1984",6378137,298.257223563]],PRIMEM["Greenwich",0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",500000],PARAMETER["False_Northing",0],PARAMETER["Central_Meridian",9],PARAMETER["Scale_Factor",0.9996],PARAMETER["Latitude_Of_Origin",0],UNIT["Meter",1]]'
    minimum_depth :  -4.98911480069749
    datum_depth :  0.0
    vertical_mesh_type_overall :  1
    number_of_layers :  10
    z_sigma :  -7.464212579701861
    vertical_mesh_type :  1
    layer_thickness : [ 0.1, 0.1, 0.1, 0.3, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]


>>> d = pfs2yaml.pfs2dict(pfs)
>>> d
{'FemEngineHD': {'DOMAIN': {'touched': 1, 'discretization': 2, 'number_of_dimensions': 2, 'number_of_meshes': 1, 'file_name': '.\\weird.mesh', 'type_of_reordering': 1, 'number_of_domains': 16, 'coordinate_type': 'PROJCS["UTM-32",GEOGCS["Unused",DATUM["UTM Projections",SPHEROID["WGS 1984",6378137,298.257223563]],PRIMEM["Greenwich",0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",500000],PARAMETER["False_Northing",0],PARAMETER["Central_Meridian",9],PARAMETER["Scale_Factor",0.9996],PARAMETER["Latitude_Of_Origin",0],UNIT["Meter",1]]', 'minimum_depth': -4.98911480069749, 'datum_depth': 0.0, 'vertical_mesh_type_overall': 1, 'number_of_layers': 10, 'z_sigma': -7.464212579701861, 'vertical_mesh_type': 1, 'layer_thickness': [0.1, 0.1, 0.1, 0.3, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]}}}
>>> d = pfs2yaml.pfs2dict(pfs)
>>> d
>>> d["FemEngineHD"]["DOMAIN"]["layer_thickness"][3]
0.3
```

## Command line interface
```
C:\>pfs2yaml --help
Usage: pfs2yaml [OPTIONS] INPUT [OUTPUT]

  Convert PFS files to YAML

  Output filename is optional.

  Default value is input filename with .yml extension

Options:
  --help  Show this message and exit.

C:\>pfs2yaml Odense.m21fm
Writing YAML file: Odense.m21fm.yml

C:\>more Odense.m21fm.yml
---
! Created     : 2018-01-16 10:31:3
! DLL id      : C:\Program Files (x86)\DHI\2017\bin\x64\pfs2004.dll
! PFS version : Apr  4 2017 19:09:27

FemEngineHD:
  DOMAIN:
    touched :  1
    discretization :  2
    number_of_dimensions :  2
    number_of_meshes :  1
    file_name :  .\Input\odense_rough.mesh
    type_of_reordering :  0
    number_of_domains :  16
    coordinate_type :  'UTM-33'
```
