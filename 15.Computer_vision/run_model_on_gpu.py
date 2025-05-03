
import pandas as pd

import tensorflow as tf

from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications.resnet import ResNet50
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense, Dropout, Flatten
from tensorflow.keras.optimizers import Adam


def load_train(path):
    """
    The training portion of the dataset is loaded from the path.
    """

    train_datagen = ImageDataGenerator(
        horizontal_flip=True,
        rescale=1/255,
        rotation_range=30,
        validation_split=0.25,
        zoom_range=0.2
    )
    
    train_datagen_flow = train_datagen.flow_from_dataframe(
        batch_size=16,
        class_mode='raw',
        dataframe=faces_labels,
        directory='/datasets/faces/final_files/',
        seed=12345,
        subset='training',
        target_size=(150, 150),
        x_col='file_name',
        y_col='real_age'
    )
    
    return train_datagen_flow


def load_test(path):
    """
    The validation/test portion of the dataset is loaded from the path
    """
    test_datagen = ImageDataGenerator(
        rescale=1/255,
        validation_split=0.25
    )
    
    test_datagen_flow = test_datagen.flow_from_dataframe(
        batch_size=32,
        class_mode='raw',
        dataframe=faces_labels,
        directory='/datasets/faces/final_files/',
        seed=12345,
        subset='validation',
        target_size=(150, 150),
        x_col='file_name',
        y_col='real_age'
    )
    
    return test_datagen_flow


def create_model(input_shape):
    """
    Define the model using ResNet50 as a backbone for regression.
    """
    backbone = ResNet50(input_shape=input_shape, weights='imagenet', include_top=False)
    backbone.trainable = False  # Optional: freeze the pretrained layers

    model = Sequential()
    model.add(backbone)
    model.add(GlobalAveragePooling2D())
    model.add(Dense(64, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(1, activation='linear'))  # or 'relu' if output must be >= 0

    model.compile(
        loss='mse',
        optimizer=Adam(learning_rate=0.0001),
        metrics=['mae']
    )
    
    return model


def train_model(model, train_data, test_data, batch_size=None, epochs=20,
                steps_per_epoch=None, validation_steps=None):
    """
    The model is trained using the provided training and validation data.

    Parameters:
    - model: compiled Keras model.
    - train_data: training generator or dataset.
    - test_data: validation generator or dataset.
    - batch_size: batch size (only relevant if a generator is not used).
    - epochs: number of training epochs.
    - steps_per_epoch: steps per epoch (optional).
    - validation_steps: validation steps per epoch (optional).

    Returns:
    - The trained model.
    """

    # Steps per epoch are defined if not specified
    if steps_per_epoch is None:
        steps_per_epoch = len(train_data)

    if validation_steps is None:
        validation_steps = len(test_data)

    # The model is trained
    model.fit(
        train_data,
        validation_data=test_data,
        batch_size=batch_size,
        epochs=epochs,
        steps_per_epoch=steps_per_epoch,
        validation_steps=validation_steps,
        verbose=2
    )

    return model


