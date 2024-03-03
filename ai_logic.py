import numpy as np
from keras import models 
from keras.models import load_model
from keras.preprocessing import image
from PIL import Image, ImageOps
def lepigion(image_path,model='kerasik.h5',labels='labels2.txt'):
  np.set_printoptions(suppress=True)
  model = load_model("kerasik.h5", compile=False)
  class_names = open("labels2.txt", "r",encoding = 'utf_8').readlines()
  data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
  image = Image.open(image_path).convert("RGB")
  size = (224, 224)
  image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
  image_array = np.asarray(image)
  normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
  data[0] = normalized_image_array
  prediction = model.predict(data)
  index = np.argmax(prediction)
  class_name = class_names[index]
  confidence_score = prediction[0][index]
  class_name = class_name[2:]
  class_name = class_name[:-1]
  if class_name == 'Голубь':
    class_name2 = 'Голубь'
  else:
    class_name2 = 'Сгенерированный Голубь'
  return class_name2

