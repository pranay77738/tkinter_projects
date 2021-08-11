import shutil
import pandas as pd
import os
from pathlib import Path
import argparse


# terminal input example
#python newDataSet\\code\\3_createFold.py  --base_dir "C:\\Users\\Danilo\\PycharmProjects\\createDataset\\newDataset" --source_folder croppedImages --destination_folder dataset --excel_file_path "docs/fold"


def isNaN(num):
    return num != num


def removeNan(l):
    i = 0
    while i < len(l):
        if isNaN(l[i]):
            l.pop(i)
            i = i - 1
        i =  i + 1
    return l


def generateDataset(t, s, d, f):
    p = d / f
    print(p)

    # scrolls the single elements of the column of the excel file (del train, test and val depending on the variable t)
    for item in t:
        # take the name of the author
        name = item.split("_", 1)[0]

        if name == "Abraamios":
            des = p / name  # es-> ./dataset/test/Abraamios
        elif name == "Kyros":
            des = p / name
        elif name == "Victor":
            des = p / name
        elif name == "Pilatos":
            des = p / name
        elif name == "isak":
            des = p / name
        elif name == "Hermauos":
            des = p / name
        elif name == "Dioscorus":
            des = p / name
        elif name == "Theodosios":
            des = p / name
        else:
            des = p / "menas"

        if not os.path.exists(des):
            os.makedirs(des)

        # from the source it takes the folder containing rows of a single image
        sou = s / item  # es-> ../croppedImages/Abraamios/Abraamios_1
        print(sou)
        imgs = os.listdir(sou)  # all lines of the same image
        for i in imgs:
            i_source_path = sou / i  # es-> ../croppedImages/Abraamios/Abraamios_1/0_Abraamios_1.jpg

            # copy the row image in the appropriate folder
            shutil.copy(i_source_path, des)
            print(i_source_path)


f = ["fold1", "fold2", "fold3"]

if __name__ == "__main__":
    a = argparse.ArgumentParser()
    a.add_argument("--base_dir", default="C:\\Users\\yjasw\\PycharmProjects\\pythonProject5\\dataset24")
    a.add_argument("--excel_file_path", default="docs/fold")
    a.add_argument("--source_folder", default="croppedImages")
    a.add_argument("--destination_folder", default="finaldataset")


    # all inputs are handled
    args = a.parse_args()
    root = Path(args.base_dir)
    excel_file_name = root / args.excel_file_path
    source = root / args.source_folder
    destination = root / args.destination_folder

    for fold in f:

        dest = destination / fold
        data_frame = pd.read_excel(root / "docs" / (str(excel_file_name) + ".xlsx"), sheet_name = fold )

        #fetch the train column of the current fold
        tr = list(data_frame["train"].values)
        # removes any incorrect values (e.g. blanks)
        train = removeNan(tr)
        # function that generates the dataset
        generateDataset(train, source, dest, "Train")

        # for val and test the above is repeated
        val = list(data_frame["validation"].values)
        validation = removeNan(val)
        generateDataset(validation, source, dest, "Val")

        te = list(data_frame["test"].values)
        test = removeNan(te)
        generateDataset(test, source, dest, "Test")

        print("train:******:", train)
        print("validation:******:", validation)
        print("test:******:", test)


