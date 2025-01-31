This plugin is meant to clean up membrane segmentations in cryo-ET data from `membrain-seg`.

1. Run `membrain-seg` with the `--store-connected-components` flag, meaning each membrane will get an individual number.

2. Open the segmentation in Napari (optionally, also your tomogram), find out which component numbers correspond to your feature.

3. Enter these numbers and a feature name in the widget, press run. 

4. Save the resulting layer using naparis built-in dialog. 

5. Now you have a standalone binary segmentation of your feature of interest. 