from pfs2yaml import pfs2yaml, pfs2dict
from yaml import load

def test_pfs_to_yaml():

    with open("tests/testdata/odense_rough.m3fm") as f:
        pfs = f.read()

        yaml = pfs2yaml(pfs)
        load(yaml)


def test_pfs_to_dict():
        with open("tests/testdata/odense_rough.m3fm") as f:
                pfs = f.read()

        d = pfs2dict(pfs)

        assert "FemEngineHD" in d.keys()

        assert d["FemEngineHD"]["ECOLAB_MODULE"]["STATE_VARIABLES"]["STATE_VARIABLE_10"]["description"] == "Inorganic phosphorous, g P/m3"



def test_pfs_with_comment():


        pfs = """
        // Created     : 2018-06-13 13:25:55
// DLL         : C:\Program Files (x86)\DHI\2017\bin\x64\pfs2004.dll
// Version     : 16.0.0.12105

[FemEngineHD]
   [DOMAIN]
      Touched = 1
      discretization = 2 // This is a comment
      type_of_gauss = 3
      [BOUNDARY_NAMES]
         Touched = 0
         MzSEPfsListItemCount = 1
         [CODE_2]
            Touched = 0
            name = 'Code 2'
         EndSect  // CODE_2

      EndSect  // BOUNDARY_NAMES

   EndSect  // DOMAIN
        """

        y = pfs2yaml(pfs)

        lines = y.split("\n")

        assert "#" in lines[9]