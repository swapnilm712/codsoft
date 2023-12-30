import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense, Embedding, LSTM
from tensorflow.keras.utils import to_categorical
import numpy as np
from PIL import Image

base_model = ResNet50(weights='imagenet')
image_model = Model(inputs=base_model.input, outputs=base_model.layers[-2].output)

embeddings_index = {}
with open('glove.6B.50d.txt', encoding='utf-8') as f:
    for line in f:
        values = line.split()
        word = values[0]
        coefs = np.asarray(values[1:], dtype='float32')
        embeddings_index[word] = coefs

max_caption_length = 20
embedding_dim = 50

input_image = Input(shape=(2048,))
image_embedding = Dense(embedding_dim, activation='relu')(input_image)

input_caption = Input(shape=(max_caption_length,))
caption_embedding = Embedding(input_dim=len(embeddings_index) + 1, output_dim=embedding_dim, input_length=max_caption_length)(input_caption)

decoder = LSTM(256)(caption_embedding)
output = Dense(len(embeddings_index) + 1, activation='softmax')(decoder)

caption_model = Model(inputs=[input_image, input_caption], outputs=output)

caption_model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

def generate_caption(image_path):
    img = Image.open(image_path)
    img = img.resize((224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    features = image_model.predict(img_array)
    initial_caption = ['<start>']

    for i in range(max_caption_length - 1):
        sequence = [embeddings_index[word] for word in initial_caption if word in embeddings_index]
        sequence = pad_sequences([sequence], maxlen=max_caption_length - 1, padding='pre')
        prediction = caption_model.predict([features, sequence], verbose=0)
        predicted_word = list(embeddings_index.keys())[np.argmax(prediction)]
        initial_caption.append(predicted_word)

        if predicted_word == '<end>':
            break

    generated_caption = ' '.join(initial_caption[1:-1])
    return generated_caption

image_path = 'path/to/your/image.jpg'
caption = generate_caption(image_path)
print(f'Caption for the image: {caption}')
