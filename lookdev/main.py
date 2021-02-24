import maya.cmds as mc

import os

import re

def create_file_tx_nodes(name, type_):
    p_2d_tx = mc.shadingNode("place2dTexture", n=name + "_" + type_ + "_utility", au=True)

    file_node = mc.shadingNode("file", name=name + "_" + type_, icm=True, at=True)

    mc.connectAttr(p_2d_tx + ".coverage", file_node + ".coverage")
    mc.connectAttr(p_2d_tx + ".translateFrame", file_node + ".translateFrame")
    mc.connectAttr(p_2d_tx + ".rotateFrame", file_node + ".rotateFrame")
    mc.connectAttr(p_2d_tx + ".mirrorU", file_node + ".mirrorU")
    mc.connectAttr(p_2d_tx + ".mirrorV", file_node + ".mirrorV")
    mc.connectAttr(p_2d_tx + ".stagger", file_node + ".stagger")
    mc.connectAttr(p_2d_tx + ".wrapU", file_node + ".wrapU")
    mc.connectAttr(p_2d_tx + ".wrapV", file_node + ".wrapV")
    mc.connectAttr(p_2d_tx + ".repeatUV", file_node + ".repeatUV")
    mc.connectAttr(p_2d_tx + ".offset", file_node + ".offset")
    mc.connectAttr(p_2d_tx + ".rotateUV", file_node + ".rotateUV")
    mc.connectAttr(p_2d_tx + ".noiseUV", file_node + ".noiseUV")
    mc.connectAttr(p_2d_tx + ".vertexUvOne", file_node + ".vertexUvOne")
    mc.connectAttr(p_2d_tx + ".vertexUvTwo", file_node + ".vertexUvTwo")
    mc.connectAttr(p_2d_tx + ".vertexUvThree", file_node + ".vertexUvThree")
    mc.connectAttr(p_2d_tx + ".vertexCameraOne", file_node + ".vertexCameraOne")
    mc.connectAttr(p_2d_tx + ".outUvFilterSize", file_node + ".uvFilterSize")
    mc.connectAttr(p_2d_tx + ".outUV", file_node + ".uvCoord")

    return file_node


def get_files(directory):
    return os.listdir(directory)


def main():
    dir = "C:/temp/aces_testing/designer/udim/"

    files_ = get_files(dir)

    shader = "aiStandardSurface1"

    no_udim_tx_pattern = re.compile(r"^(?P<asset>[A-Za-z0-9]+)_(?P<type>[A-Za-z]+)_(?P<colorspace>[A-Za-z0-9 -]+)$")
    udim_tx_pattern = re.compile(r"^(?P<asset>[A-Za-z0-9]+)_(?P<type>[A-Za-z]+)_(?P<colorspace>[A-Za-z0-9 -]+)_(?P<udim>\d{4})$")

    actual_type = None

    for file_ in files_:
        file_name, _ = os.path.splitext(file_)

        is_udim = udim_tx_pattern.match(file_name)

        is_not_udim = no_udim_tx_pattern.match(file_name)

        if is_not_udim:
            file_data = is_not_udim.groupdict()
        elif is_udim:
            file_data = is_udim.groupdict()
        else:
            file_data = dict()
            file_data["asset"] = file_name.split("_")[0]
            file_data["type"] = file_name.split("_")[1]


        name = file_data["asset"]
        type_ = file_data["type"]

        if actual_type != type_:
            actual_type = type_

            file_node = create_file_tx_nodes(name, type_)

            if "color" in file_name.lower():
                mc.connectAttr(file_node + ".outColor", shader + ".baseColor")
                mc.setAttr(file_node + ".fileTextureName", dir + file_, type="string")
                if is_udim:
                    mc.setAttr(file_node + ".uvTilingMode", 3)
            if "roughness" in file_name.lower():
                mc.connectAttr(file_node + ".outColorR", shader + ".specularRoughness")
                mc.setAttr(file_node + ".fileTextureName", dir + file_, type="string")
                if is_udim:
                    mc.setAttr(file_node + ".uvTilingMode", 3)
            if "metalness" in file_name.lower() or "metallic" in file_name.lower():
                mc.connectAttr(file_node + ".outColorR", shader + ".metalness")
                mc.setAttr(file_node + ".fileTextureName", dir + file_, type="string")
                if is_udim:
                    mc.setAttr(file_node + ".uvTilingMode", 3)
            if "normal" in file_name.lower():
                normal_map = mc.shadingNode("aiNormalMap", n=name + "_normalMap", au=True)

                mc.connectAttr(file_node + ".outColor", normal_map + ".input")
                mc.connectAttr(normal_map + ".outValue", shader + ".normalCamera")
                if is_udim:
                    mc.setAttr(file_node + ".uvTilingMode", 3)




if __name__ == '__main__':
    main()
