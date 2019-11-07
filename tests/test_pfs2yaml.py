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



