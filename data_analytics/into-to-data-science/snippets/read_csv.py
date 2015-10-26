import pandas


def add_full_name(path_to_csv, path_to_new_csv):
    csv = pandas.read_csv(path_to_csv)


if __name__ == "__main__":
    path_to_csv = "master.csv"
    path_to_new_csv = "output.csv"
    add_full_name(path_to_csv, path_to_new_csv)
