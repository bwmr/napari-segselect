"""
This module is an example of a barebones numpy reader plugin for napari.

It implements the Reader specification, but your plugin may choose to
implement multiple readers or even other plugin contributions. see:
https://napari.org/stable/plugins/guides.html?#readers
"""

import mrcfile
import numpy as np


def napari_get_reader(path: str):
    """Define which reader to use.

    Parameters
    ----------
    path (str): Path to file

    Returns
    -------
    function or None
        If the file ends with "_segmented.mrc", open as label. Open other ".mrc" as image.
    """

    if isinstance(path, str) and path.endswith("_segmented.mrc"):
        return read_mrc_labels
    elif isinstance(path, str) and path.endswith(".mrc"):
        return read_mrc_images
    else:
        return None


def read_mrc_labels(path):
    """Read mrc file as Label Layer."""
    with mrcfile.open(path, "r", permissive=True) as mrc:
        data = mrc.data
        # Ensure the data is of type int for label layer
        data = data.astype(np.int16)

        return [(data, {"name": "Connected Components"}, "labels")]


def read_mrc_images(path):
    """Read mrc file as Image Layer."""
    with mrcfile.open(path, "r", permissive=True) as mrc:
        data = mrc.data

        return [(data, {"name": "Tomo"}, "image")]
