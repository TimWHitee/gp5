# import os
# import numpy as np
# import matplotlib.pyplot as plt
# from PIL import Image
# img = Image.open("data/melspecs_train/1102.png")
# print(img.size)


# arr = np.array(img)
# plt.figure(figsize=(12, 4))
# plt.imshow(arr, aspect='auto', origin='lower', cmap='gray')
# plt.show()
# import os

# path = "data/melspecs_train"

# num_files = sum(
#     len(files)
#     for _, _, files in os.walk(path)
# )

# print(f"Количество файлов: {num_files}")

# path = "data/melspecs_val"


# num_files = sum(
#     len(files)
#     for _, _, files in os.walk(path)
# )

# print(f"Количество файлов: {num_files}")
# import numpy as np
# from PIL import Image


# for filename in os.listdir("data/audio_train"):
#     track_id = filename.replace(".wav", "")
#     y, sr = librosa.load(f"data/audio_train/{filename}", sr=None)

#     mel = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128)
#     mel_db = librosa.power_to_db(mel, ref=np.max)

#     mel_norm = (mel_db - mel_db.min()) / (mel_db.max() - mel_db.min()) * 255
#     img = Image.fromarray(mel_norm.astype(np.uint8))
#     img.save(f"data/melspecs_train/{track_id}.png")

# for filename in os.listdir("data/audio_val"):
#     track_id = filename.replace(".wav", "")
#     y, sr = librosa.load(f"data/audio_val/{filename}", sr=None)

#     mel = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128)
#     mel_db = librosa.power_to_db(mel, ref=np.max)

#     mel_norm = (mel_db - mel_db.min()) / (mel_db.max() - mel_db.min()) * 255
#     img = Image.fromarray(mel_norm.astype(np.uint8))
#     img.save(f"data/melspecs_val/{track_id}.png")
