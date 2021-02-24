from CommonTools.concat import concat

JNT = "JNT"
JNT_END = "JNT_END"
IKHL = "IKHL"
CONSTRAINTS = "CONSTRAINTS"
GEO = "GEO"
GEO_BASE = "GEO_BASE"
NBS = "NBS"
CTRL = "CTRL"
CRV = "CRV"
LOCATOR = "LOCATOR"
FOLLICLE = "FOLLICLE"
GRP = "GRP"

GEO_GRP = "GEO_GRP"
SKL_GRP = "SKL_GRP"
CTRL_GRP = "CTRL_GRP"
XTRAS_GRP = "XTRAS_GRP"


class Type(object):

    LINKS = {JNT: "jnt",
             JNT_END: "jntEnd",
             IKHL: "ikhl",
             CONSTRAINTS: ".+Constraint",
             GEO: "geo",
             GEO_BASE: "geoBase",
             NBS: "nbs",
             CTRL: "ctrl",
             CRV: "crv",
             LOCATOR: "locator",
             FOLLICLE: "follicle",
             GRP: "grp",
             GEO_GRP: "GEO",
             SKL_GRP: "SKL",
             CTRL_GRP: "CTRL",
             XTRAS_GRP: "XTRAS"
             }

    @classmethod
    def get(cls, name):

        if name in cls.LINKS:
            return cls.LINKS.get(name)
        else:
            raise NameError("Unknown", name, "Task")

    @staticmethod
    def pattern(*args):
        """

        Args:
            *args: multiple tasks allowed

        Returns:
            pattern for regex with given types

        """

        str_args = [str(arg) for arg in args]

        print(str_args)

        types = "|".join(str_args)

        pattern = concat(r"(?P<type>", types, r")$")

        return pattern



PROJECT_PATTERN = r"(?P<asset>[A-Z0-9]+)"
SIDE_PATTERN = r"(?P<side>[CLR])"
OBJECT_NAME_PATTERN = r"(?P<object>[A-Za-z0-9]+)"

PROJECT_GRP = concat(r"^", PROJECT_PATTERN, "_", Type.pattern(Type.get(GRP)))
MAIN_GRP = concat(r"^", PROJECT_PATTERN, "_", Type.pattern(Type.get(GEO_GRP), Type.get(CTRL_GRP), Type.get(XTRAS_GRP), Type.get(SKL_GRP)), "_", Type.pattern(Type.get(GRP)))
OBJECT_PATTERN = concat(r"^", PROJECT_PATTERN, "_", SIDE_PATTERN, "_", OBJECT_NAME_PATTERN, "_", Type.pattern(Type.get(JNT), Type.get(JNT_END), Type.get(IKHL), Type.get(CONSTRAINTS), Type.get(GEO), Type.get(GEO_BASE), Type.get(NBS), Type.get(CTRL), Type.get(CRV), Type.get(LOCATOR), Type.get(FOLLICLE), Type.get(GRP)))
