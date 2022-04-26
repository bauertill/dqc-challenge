from data_class import DataClass


def test_wrong_data_types():
    data_class_wrong_data = DataClass("test_data/wrong_data_types.csv")

    assert data_class_wrong_data


test_wrong_data_types()
