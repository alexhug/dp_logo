# Logo Classification and Detection

This is a student project for Deep Learning Course at CentraleSupelec

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
You need to install TensorFlow and Keras

### Dataset

You need to download FlickrLogos-47 dataset.
You need to run parser and splitter to have the appropriate file architecture.
In both scripts you need to change initial path to the path containing your dataset.
The parser divides the dataset in folders of each class.
The splitter divides the dataset in train and val (80% et 20%)

```
python parser_alexia.py
python splitter_alexia.py
```

## Training the network


```
python transfer_learning.py --train_dir (to define) --val_dir (to define)

```

## Testing the network


```
python model1.py --image_url ou --image
```

