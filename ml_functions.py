# import libraries
import tensorflow as tf
import numpy as np
from PIL import Image

tf.compat.v1.enable_eager_execution()

def train_model(data_dir):
    #load image data
    img_height=1200 
    img_width=900
    batch_size=1
    train_ds = tf.keras.utils.image_dataset_from_directory(
                data_dir,
                label_mode='categorical',
                validation_split=0.2,
                subset="training",
                seed=123,
                image_size=(img_height, img_width),
                batch_size=batch_size)
    # define model
    input_=tf.keras.layers.Input((img_height,img_width,3))
    x=tf.keras.layers.Conv2D(64,(3,3), activation='relu')(input_)
    x=tf.keras.layers.MaxPool2D((10,10))(x)
    x=tf.keras.layers.Conv2D(64, (3,3),activation='relu')(x)
    x=tf.keras.layers.MaxPool2D((9,9))(x)
    x=tf.keras.layers.Flatten()(x)
    x=tf.keras.layers.Dense(50, activation='relu')(x)
    x=tf.keras.layers.Dense(2, activation='softmax')(x)

    model=tf.keras.Model(inputs=input_, outputs=x)
    
    model_chckpoint=tf.keras.callbacks.ModelCheckpoint(filepath='./models/best.hdf5', monitor='accuracy', 
                                                        save_best_only=True, mode='max')
    early_stop=tf.keras.callbacks.EarlyStopping(monitor='accuracy',patience=3, verbose=3)
    callback_list=[checkpoint,early_stop]

    #train

    model.compile(optimizer='Adam', loss=tf.keras.losses.CategoricalCrossentropy(), metrics=['accuracy'])
    model.fit(train_ds, epochs=10, callbacks=callback_list)

def who_is_this(image_loc,model_path):
    person=None 
    # load model architecture
    input_=tf.keras.layers.Input((img_height,img_width,3))
    x=tf.keras.layers.Conv2D(64,(3,3), activation='relu')(input_)
    x=tf.keras.layers.MaxPool2D((10,10))(x)
    x=tf.keras.layers.Conv2D(64, (3,3),activation='relu')(x)
    x=tf.keras.layers.MaxPool2D((9,9))(x)
    x=tf.keras.layers.Flatten()(x)
    x=tf.keras.layers.Dense(50, activation='relu')(x)
    x=tf.keras.layers.Dense(2, activation='softmax')(x)

    model=tf.keras.Model(inputs=input_, outputs=x)
    model.compile(optimizer='Adam', loss=tf.keras.losses.CategoricalCrossentropy(), metrics=['accuracy'])
    model.load_weights(model_path)

    # load image 
    image= np.array(Image.open(image_loc).resize((900,1200))).reshape((1,1200,900,3))

    # make prediction
    prediction=model.predict(image)
    max_val=max(prediction)
    if max_val > .8:
        person=model.class_labels[prediction.index(max_val)]
    return person


