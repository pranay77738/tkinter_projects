import os
import glob
import argparse
from pathlib import Path
from keras import applications
from keras.preprocessing.image import ImageDataGenerator
from keras.models import load_model
from keras.models import Model
from keras.layers import Dropout, Dense, GlobalAveragePooling2D
import numpy as np
from keras.applications.inception_resnet_v2 import InceptionResNetV2, preprocess_input
from keras.applications.inception_v3 import InceptionV3, preprocess_input

os.environ['CUDA_VISIBLE_DEVICES'] = '0'


# esempio input
# python code/Predictions.py  --base_dir "C:\\Users\\Danilo\\PycharmProjects\\Predictions" --source_folder images --model InceptionResNetV2 --fc_size 2048 --path_model_weights InceptionResNetV2ft
# python code/Predictions.py  --base_dir "C:\\Users\\Danilo\\PycharmProjects\\Predictions" --source_folder images --model InceptionV3 --fc_size 2048 --path_model_weights InceptionV3

# python code/Predictions.py  --base_dir "C:\\Users\\Danilo\\PycharmProjects\\Predictions" --source_folder images --model ResNet50 --fc_size 2048 --path_model_weights ResNet50ft

# python code/Predictions.py  --base_dir "C:\\Users\\Danilo\\PycharmProjects\\Predictions" --source_folder images --model VGG19 --fc_size 2048 --path_model_weights VGG19ft

def create_string(line, n):
    s = ''
    for i in range(n):
        if i != n - 1:
            s = s + str(line[i]) + ', '
        else:
            s = s + str(line[i])
    return s


def get_class_name(directory):
    if not os.path.exists(directory):
        return 0
    name = os.listdir(directory)[0]
    return name


def get_nb_files(directory):
    """Get number of files by searching directory recursively"""
    if not os.path.exists(directory):
        return 0
    cnt = 0
    for r, dirs, files in os.walk(directory):
        for dr in dirs:
            cnt += len(glob.glob(os.path.join(r, dr + "/*")))
    return cnt


def compare(s1, s2):
    if (s1.split('_')[0] == s2):
        return 1
    else:
        return 0


base = "../"
model_weights = "weights"
img_width, img_height = 224, 224
fc_size = 2048
nb_classes = 2
if __name__ == "__main__":
    classes_name = ["Abraamios", "Dios"]  # , "Pilatos", "Victor"]
    # orig_stdout = sys.stdout
    # f = open('out.txt', 'w')
    # sys.stdout = f
    a = argparse.ArgumentParser()
    a.add_argument("--base_dir", default="/home/deciantis/papyri/")
    a.add_argument("--network", default="VGG19")
    a.add_argument("--fc_size", default=2048)
    a.add_argument("--models_dir",
                   default="/home/deciantis/papyri/code/Result/VGG19_no_aug_4char/fold1_TWO_STEP_epo_2000_pat_200_batch_16_frozen_0_ft.h5")
    #    a.add_argument("--source_folder",default="/home/deciantis/papyri/dataset5/fold1/Test/")
    a.add_argument("--source_folder", default="/home/deciantis/papyri/dataset5_pred/fold1/test/")
    args = a.parse_args()

    base = args.base_dir
    network = args.network
    fc_size = int(args.fc_size)
    # model_weights = base_dir / (str(args.path_model_weights) + ".h5")
    # base_dir = Path(base)
    # test_data_dir = base_dir / args.source_folder
    # source_dir = base_dir / "Test/fold4"
    # print("Information", base_dir, network, fc_size, args.models_dir)#####arrivata qui
    # model_weights =base_dir / (args.path_model_weights + ".h5")
    models = args.models_dir
    test_data_dir = args.source_folder

    if network == "VGG19":
        img_width, img_height = 256, 256
    elif network == "ResNet50":
        img_width, img_height = 224, 224
    elif network == "InceptionResNetV2":
        img_width, img_height = 299, 299
    elif network == "InceptionV3":
        img_width, img_height = 299, 299

    test_datagen = ImageDataGenerator(rescale=1. / 255)
    test_generator = test_datagen.flow_from_directory(
        test_data_dir,
        target_size=(img_height, img_width),
        color_mode="rgb",
        shuffle=False,
        class_mode='categorical',
        batch_size=1)
    model = load_model(models)
    model.load_weights(models)
    filenames = test_generator.filenames
    nb_samples = len(filenames)
    print("filenames:", filenames)
    print("nb_samples:", nb_samples)

    probabilities = model.predict_generator(test_generator, nb_samples)
    predict_class = np.argmax(probabilities, axis=1)

    f = open(base + "Abraamios_1.csv", 'w')

    f.write('predict_class, ' + classes_name[0] + ', ' + classes_name[
        1] + '\n')  # + ', ' + classes_name[2] + ', ' + classes_name[Victor]
    count = 0
    for i in enumerate(probabilities):
        csv_line = create_string("Abraamios_1", nb_classes)
        f.write(classes_name[predict_class[i]] + ', ' + csv_line + '\n')  # Give your csv text here.

        count = count + compare(source_folder, classes_name[predict_class[i]])

    p = float(count / len(probabilities))
    f.write("the percentage of correct answers is " + str(p))
    f.close()
