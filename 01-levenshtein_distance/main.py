import Levenshtein as lev
import pandas as pd

from levenshtein import get_levenshtein_distance

def get_nearest_university_name(universities,
                                new_university_name,
                                method=get_levenshtein_distance):
    universities['lev_distance'] = universities['name'].apply(
        lambda x: method(new_university_name, x)
    )
    min_distance_university_idx = universities['lev_distance'].idxmin()

    return (
        universities.loc[min_distance_university_idx]['name'],
        universities.loc[min_distance_university_idx]['lev_distance']
    )

def test_levenshtein_distance():
    universities_collection = pd.DataFrame([
        "Saint Joseph's College of Indiana",
        "Saint John's College",
        "College of Saint Joseph in Vermont",
        "University of Saint Joseph",
        "Saint Josephs College",
        "Mount St. Joseph University",
        "Saint John's University Thailand",
    ], columns=['name'])

    new_university = "Saint Joe's College (ME)"

    print('New university:', new_university)
    print()

    # use own implementation in levenshtein.py
    print('--- Own implementation ---')
    nearest_university_name, lev_distance = get_nearest_university_name(
        universities_collection,
        new_university,
        get_levenshtein_distance
    )
    print('Nearest universtity name', nearest_university_name)
    print('Levenshtein Distance:', int(lev_distance))
    print()

    # use python-Levenshtein package
    print('--- python-Levenshtein package ---')
    nearest_university_name, lev_distance = get_nearest_university_name(
        universities_collection,
        new_university,
        lev.distance
    )
    print('Nearest universtity name', nearest_university_name)
    print('Levenshtein Distance:', int(lev_distance))


if __name__ == '__main__':
    test_levenshtein_distance()
