from data_class import DataClass

# Hardcoded for now, could be changed to a command line argument
CSV_PATH = "test_data/wrong_data_types.csv"


def main():
    data_class = DataClass(CSV_PATH)
    data_class.generate_report()


if __name__ == "__main__":
    main()
