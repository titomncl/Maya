#!/usr/bin/env python
# -*- coding: utf-8 -*-

import maya.api.OpenMaya as om
import maya.OpenMaya as om_old
import maya.cmds as mc

import pickle
import os
import math

from CommonTools.concat import concat

# TODO script qui permet de selectionner une side, ou les deux pour faire une duplication, et mise en couleur auto sans casser le fonctionnement actuel

# TODO method to select a side or both to add the same name for two different side (like eyes ctrl or leg, or anything that is symmetrical) and colorize them. Different working if ultimate or switch
# TODO add color choice for special ctrl like sliders


def create_ctrl(name="", shape="", scale_factor=None):
    """

    Args:
        name (str):
        shape (str):
        scale_factor (float):

    Returns:

    """

    # check if an object is selected in the viewport

    target_list = mc.ls(sl=True, fl=True)

    if len(target_list) == 0:
        mc.group(n="empty", empty=True)


