# aqc-anylabeling

Effortless data labeling with AI support from YOLO and Segment Anything from [Anylabeling](https://github.com/vietanhdev/anylabeling)

## Getting Started

Run the following commands to launch anylabeling:
```
pipenv install
pipenv run anylabeling
```

If there is an error with opencv library, please install an older version:
```
pip install opencv-python==4.6.0.66
```

## Download DB
Download the DB tables containing tiles, defects, and client metadata using the script `notebooks/download_db.ipynb`.

## Download tiles to annotate
Using the script in `notebooks/selecting_rolls_by_color_pattern.ipynb`, select the rolls to be annotated.

## More instructions
For more instruction on how to use anylabeling please, refer to anylabeling [Documentation](https://anylabeling.nrl.ai/docs)

## Load custom model
Follow the instructions on how to load a [Custom model](https://anylabeling.nrl.ai/docs/custom-models)