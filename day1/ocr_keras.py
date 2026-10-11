import tensorflow as tf
from tensorflow import keras
import keras_ocr
import os
os.environ["TF_USE_LEGACY_KERAS"] = "1"

import matplotlib.pyplot as plt


pipeline = keras_ocr.pipeline.Pipeline()
image_path = '../images/sartre_nausea.jpeg'
extract_info = pipeline.recognize([image_path])
# print(extract_info[0][0])   

for word, box in extract_info[0]:
    print(word)

# import matplotlib.pyplot as plt

# import keras_ocr

# # keras-ocr will automatically download pretrained
# # weights for the detector and recognizer.
# pipeline = keras_ocr.pipeline.Pipeline()

# # Get a set of three example images
# images = [
#     keras_ocr.tools.read(url) for url in [
#         'https://upload.wikimedia.org/wikipedia/commons/b/bd/Army_Reserves_Recruitment_Banner_MOD_45156284.jpg',
#         'https://upload.wikimedia.org/wikipedia/commons/e/e8/FseeG2QeLXo.jpg',
#         'https://upload.wikimedia.org/wikipedia/commons/b/b4/EUBanana-500x112.jpg'
#     ]
# ]

# # Each list of predictions in prediction_groups is a list of
# # (word, box) tuples.
# prediction_groups = pipeline.recognize(images)

# # Plot the predictions
# fig, axs = plt.subplots(nrows=len(images), figsize=(20, 20))
# for ax, image, predictions in zip(axs, images, prediction_groups):
#     keras_ocr.tools.drawAnnotations(image=image, predictions=predictions, ax=ax)