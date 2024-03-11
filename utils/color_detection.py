import os
import numpy as np
from PIL import Image
import extcolors
from colordict import ColorDict
from typing import List
from enum import Enum


class FabricPattern(Enum):
    uniform = 1
    simple = 2
    complex = 3


def distance(a, b) -> float:
    dist = np.linalg.norm(np.array(a) - np.array(b))
    return dist


def most_common_colors(colors, palette):
    common_colors = []
    for value in colors[0]:
        color = value[0]
        count = value[1]
        if count > 1000:  # TODO change contrast
            min_dist = [distance(color, palette[key]) for key in palette]
            min_dist = np.array(min_dist).argmin()
            common_colors.append(list(palette.keys())[min_dist])
    return np.unique(common_colors)


def color_detection(path_to_images: List[str], factor: int = 2, pallette: str = None):
    """ """
    if pallette is None:
        list_of_colors = ColorDict()
    else:
        list_of_colors = ColorDict(palettes_path=pallette)
    final_colors = []
    for path in path_to_images:
        # Reading and resizing image
        im = Image.open(path)
        w, h = im.size
        resize = (w // factor, h // factor)
        im = im.resize(resize)
        # Extracting colors from image
        colors_x = extcolors.extract_from_image(im, tolerance=12, limit=10)
        colors = most_common_colors(colors_x, list_of_colors)
        for clr in colors:
            if clr not in final_colors:
                final_colors.append(clr)

    values = [list_of_colors[x] for x in final_colors]

    # Fabric pattern
    if len(final_colors) == 1:
        pattern = FabricPattern.uniform
    elif len(final_colors) < 4:
        pattern = FabricPattern.simple
    elif len(final_colors) >= 4:
        pattern = FabricPattern.complex
    else:
        pattern = -1

    return final_colors, values, pattern


if __name__ == "__main__":
    # paths = ["./data/F7520_R0_C1.jpg"]
    # #paths = ["./data/F6959_R6_C2.jpg"]
    # colors, pattern = color_detection(paths)
    # print(colors, pattern)
    pass
