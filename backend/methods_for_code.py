import cv2
import time
import serial
# import libraries
import tensorflow as tf
import numpy as np
from PIL import Image
import os

tf.compat.v1.enable_eager_execution()

class MachineLearning:
    def __init__(self):
        self.personAdded = False;
        self.imageName = 'test.jpg';

    def togglePersonAdded(self):
        self.personAdded = not self.personAdded;

    def train_model(self,data_dir):
        #load image data
        img_height=900 
        img_width=1200
        batch_size=1
        train_ds = tf.keras.utils.image_dataset_from_directory(
                    data_dir,
                    label_mode='categorical',
                    subset="training",
                    validation_split=0.1,
                    seed=123,
                    image_size=(img_height, img_width),
                    batch_size=batch_size)
        
        # define model
        input_=tf.keras.layers.Input((img_height,img_width,3))
        x=tf.keras.layers.Conv2D(64,(3,3), activation='relu')(input_)
        #x=tf.keras.layers.Dropout(0.2)(x)
        x=tf.keras.layers.MaxPool2D((10,10))(x)
        x=tf.keras.layers.Conv2D(64, (3,3),activation='relu')(x)
        x=tf.keras.layers.MaxPool2D((9,9))(x)
        x=tf.keras.layers.Flatten()(x)
        x=tf.keras.layers.Dense(50, activation='relu')(x)
        #x=tf.keras.layers.Dropout(0.2)(x)
        x=tf.keras.layers.Dense(2, activation='softmax')(x)

        model=tf.keras.Model(inputs=input_, outputs=x)
        
        model_checkpoint=tf.keras.callbacks.ModelCheckpoint(filepath='./models/best.hdf5', monitor='accuracy', 
                                                            save_best_only=True, mode='max')
        early_stop=tf.keras.callbacks.EarlyStopping(monitor='accuracy',patience=3, verbose=3)
        callback_list=[model_checkpoint,early_stop]

        #train
        
        model.compile(optimizer='Adam', loss=tf.keras.losses.CategoricalCrossentropy(), metrics=['accuracy'])
        model.fit(train_ds, epochs=10, callbacks=callback_list)

    def who_is_this(self,image_loc,model_path, data_dir):
        person=None 
        img_height=900
        img_width=1200
        batch_size=1
        train_ds = tf.keras.utils.image_dataset_from_directory(
                    data_dir,
                    label_mode='categorical',
                    validation_split=0.1,
                    subset="training",
                    seed=123,
                    image_size=(img_height, img_width),
                    batch_size=batch_size)


        # load model architecture
        input_=tf.keras.layers.Input((img_height,img_width,3))
        x=tf.keras.layers.Conv2D(64,(3,3), activation='relu')(input_)
        #x=tf.keras.layers.Dropout(0.2)(x)

        x=tf.keras.layers.MaxPool2D((10,10))(x)
        x=tf.keras.layers.Conv2D(64, (3,3),activation='relu')(x)
        x=tf.keras.layers.MaxPool2D((9,9))(x)
        x=tf.keras.layers.Flatten()(x)
        x=tf.keras.layers.Dense(50, activation='relu')(x)
        #x=tf.keras.layers.Dropout(0.2)(x)

        x=tf.keras.layers.Dense(2, activation='softmax')(x)

        model=tf.keras.Model(inputs=input_, outputs=x)
        model.compile(optimizer='Adam', loss=tf.keras.losses.CategoricalCrossentropy(), metrics=['accuracy'])
        model.load_weights(model_path)

        # load image 
        image= np.array(Image.open(image_loc).resize((1200,900))).reshape((1,900,1200,3))

        # make prediction
        prediction=model.predict(image)
        print(prediction)
        max_val=max(prediction[0])

        if max_val > .80:
            person=train_ds.class_names[np.where(prediction[0]==max_val)[0][0]]
            print(person);
            # return person;
    def look_for_person(self):
        time.sleep(1)
        while True:
            
            if self.personAdded:
                self.train_model('../Images/')
                self.togglePersonAdded();
            elif os.listdir("../Images/") == "":
                # pass;
                print("Waiting")
            else:
                cam=cv2.VideoCapture(0)
                cv2.namedWindow("test")
                time.sleep(1)
                ret,frame = cam.read()
                img_name=self.imageName;
                cv2.imwrite(img_name, frame)
                cam.release()
                cv2.destroyAllWindows()
                person = self.who_is_this(self.imageName,"./models/best.hdf5",'../Images/')
                if person != None:
                    print(person)
                    break
                    
            
