

Maxpooling2D(2,2),
Flatten(),
Dense (128, activation='relu'),
Droupout(0.5),
Dense(num_classes,
      activation='softmax')])

model.comile(optimizer='adam',
loss='categorical_crossentropy',
             metrics=['accuracy'])
return model
