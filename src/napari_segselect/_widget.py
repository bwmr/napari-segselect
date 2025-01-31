from typing import TYPE_CHECKING

import numpy as np

if TYPE_CHECKING:
    import napari


def select_label_widget(
    input_seg: "napari.types.LabelsData",
    feature_name: str = "selected",
    selected_components: str = "1,2",
) -> "napari.types.LayerDataTuple":
    """
    Widget to select specific components from label layer.

    Parameters
    ----------
    input_seg : Label layer to work on.
    feature_name : Name of the resulting label layer.
    selected_components : Label fields to keep, comma-separated.

    Returns
    -------
    output_seg : Label layer with selected components and given name.

    """

    output_seg = np.zeros(input_seg.shape, dtype=np.int8)

    seg_list = selected_components.split(",")

    for seg in seg_list:
        seg = int(seg)
        output_seg[np.where(input_seg == seg)] = 1

    return (output_seg, {"name": feature_name}, "labels")
