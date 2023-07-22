import csv
import requests


def get_csv(url="https://drive.google.com/uc?export=download&id=13nk_FYpcayUck2Ctrela5Tjt9JQbjznt"):
    """
    :param:url: URL of file with data "https://drive.google.com/uc?export=download&id=13nk_FYpcayUck2Ctrela5Tjt9JQbjznt"
    :return:midle_weigth, midle_heigth: midle weigth and heigth of people in list
    """

    weigth = []
    heigth = []
    save_path = "wd/files_output/new_file.csv"
    response = requests.get(url)

    with open(save_path, "wb") as file:
        file.write(response.content)
    with open(save_path) as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            try:
                weigth.append(float(row[4]))
                heigth.append(float(row[2]))
            except (TypeError, ValueError):
                continue

    midle_weigth = round(sum(weigth) / len(weigth), 2)
    midle_heigth = round(sum(heigth) / len(heigth), 2)
    print(midle_heigth, midle_weigth)
    return midle_weigth, midle_heigth
