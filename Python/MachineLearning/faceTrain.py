from keras.applications import mobilenet
from keras.models import Sequential,Model 
from keras.layers import Dense,Dropout,Activation,Flatten,GlobalAveragePooling2D
from keras.layers import Conv2D,MaxPooling2D,ZeroPadding2D
from keras.layers.normalization import batch_normalization
from keras.preprocessing.image import ImageDataGenerator


mobilenet=mobilenet(weights='none',include_top=False,input_shape=(224,224,3))


for layer in mobilenet.layers:
    layer.trainable = True

for (i,layer) in enumerate(mobilenet.layers):
    print(str(i),layer.__class__.__name__,layer.trainable)

def addTopModelmobilenet(bottom_model, num_classes):

    top_model = bottom_model.output
    top_model = GlobalAveragePooling2D()(top_model)
    top_model = Dense(1024,activation='relu')(top_model)
    
    top_model = Dense(1024,activation='relu')(top_model)
    
    top_model = Dense(512,activation='relu')(top_model)
    
    top_model = Dense(num_classes,activation='softmax')(top_model)

    return top_model

num_classes = 5

FC_Head = addTopModelmobilenet(mobilenet, num_classes)

model = Model(inputs = mobilenet.input, outputs = FC_Head)

print(model.summary())

train_data_dir = 'C:\\Users\\devas\\Documents\\PROGRAM\\Python\\MachineLearning\\archive\\train'
validation_data_dir = 'C:\\Users\\devas\\Documents\\PROGRAM\\Python\\MachineLearning\\archive\\test'

train_datagen = ImageDataGenerator(
                    rescale=1./255,
                    rotation_range=30,
                    width_shift_range=0.3,
                    height_shift_range=0.3,
                    horizontal_flip=True,
                    fill_mode='nearest'
                                   )

validation_datagen = ImageDataGenerator(rescale=1./255)

batch_size = 32

train_generator = train_datagen.flow_from_directory(
                        train_data_dir,
                        target_size = (224,224),
                        batch_size = batch_size,
                        class_mode = 'categorical'
                        )

validation_generator = validation_datagen.flow_from_directory(
                            validation_data_dir,
                            target_size=(224,224),
                            batch_size=batch_size,
                            class_mode='categorical')

from keras.optimizers import rmsprop_v2,adam_v2
from keras.callbacks import ModelCheckpoint,EarlyStopping,ReduceLROnPlateau

checkpoint = ModelCheckpoint(
                             'emotion_face_mobilNet.h5',
                             monitor='val_loss',
                             mode='min',
                             save_best_only=True,
                             verbose=1)

earlystop = EarlyStopping(
                          monitor='val_loss',
                          min_delta=0,
                          patience=10,
                          verbose=1,restore_best_weights=True)

learning_rate_reduction = ReduceLROnPlateau(monitor='val_acc', 
                                            patience=5, 
                                            verbose=1, 
                                            factor=0.2, 
                                            min_lr=0.0001)

callbacks = [earlystop,checkpoint,learning_rate_reduction]

model.compile(loss='categorical_crossentropy',
              optimizer=adam_v2(lr=0.001),
              metrics=['accuracy']
              )

nb_train_samples = 24176
nb_validation_samples = 3006

epochs = 25

history = model.fit_generator(
            train_generator,
            steps_per_epoch=nb_train_samples//batch_size,
            epochs=epochs,
            callbacks=callbacks,
            validation_data=validation_generator,
            validation_steps=nb_validation_samples//batch_size)