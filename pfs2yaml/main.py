from yaml import load

def pfs2dict(pfsstring):

    y = pfs2yaml(pfsstring)
    d = load(y)
    return d


def pfs2yaml(pfsstring):
    """[summary]

    Parameters
    ----------
    pfsstring : string
        contents of pfs file in pfs format

    Returns
    -------
    string
        contents of pfs file in yaml format
    """

    lines = pfsstring.split("\n")

    output = []
    output.append("---")

    level = 0

    for line in lines:
        s = line.strip()

        if len(s) > 0:
            if s[0] == "[":
                s = s.replace("[","")

            if s[-1] == "]":
                s = s.replace("]",":")

        s = (
              s.replace("//","#")
              .replace("|","") # TODO
            )

        if len(s) > 0 and s[0] != "!":
            if "=" in s:
                idx = s.index("=")

                key = s[0:idx]
                value = s[(idx+1):]
                key = key.lower()


                if s.count("'") == 2: # This is a quoted string and not an array
                    s = s
                else:
                    if "," in value:
                        value = f"[{value}]"

                s = f"{key}: {value}"


        if "EndSect" in line:
            s = ""

        ws = " " * 2 * level
        adj_line = ws + s

        s = line.strip()
        if len(s) > 0 and s[0] == "[":
            level +=1
        if "EndSect" in line:
            level -=1

        output.append(adj_line)

    out_text = "\n".join(output)
    return out_text