from pathlib import Path
from typing import List, Tuple

import mrcfile
import numpy as np


def write_segmentation(root_path: str, layer_data: List[Tuple]) -> List[str]:
    """Write labelsfield as binary segmentation to .mrc.

    In:
        root_path: Will be extended with label field name.
        layer_data: List of label layers to save.

    Returns:
        List of paths to which files were saved.
    """

    successfull_list = []

    root_path = Path(root_path)

    for layer in layer_data:

        labels, attributes, layer_type = layer

        output_seg = np.zeros(labels.shape, dtype=np.int8)

        output_seg[np.where(labels)] = 1

        output_path = root_path.parent / (
            root_path.stem + attributes["name"] + ".mrc"
        )

        mrcfile.write(output_path, output_seg, overwrite=True)

        successfull_list.append(output_path)

    return successfull_list
