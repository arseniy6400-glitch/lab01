from app import loadData, saveData
import os
import json

#test1
def test_load_empty_if_no_file(tmp_path):
    os.chdir(tmp_path)
    data = loadData()
    assert data == []

#test2
def test_load_broken_json(tmp_path):
    os.chdir(tmp_path)

    with open("db.json", "w") as f:
        f.write("{ broken json")

    data = loadData()
    assert data == []

#test3
def test_save_and_load(tmp_path):
    os.chdir(tmp_path)
    test_data = [1, 2, 3]

    saveData(test_data)
    loaded = loadData()

    assert loaded == test_data