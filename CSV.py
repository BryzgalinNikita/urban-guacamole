import csv


def write_holiday_cities(first_letter):

    with open('travel_notes.csv', 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = list(reader)

    visited_cities = set()
    for row in data:
        if row['Имя'][0].lower() == first_letter.lower() and row['Посещен'] == 'Да':
            visited_cities.add(row['Город'])

    desired_cities = set()
    for row in data:
        if row['Имя'][0].lower() == first_letter.lower() and row['Посетить'] != '':
            desired_cities.add(row['Посетить'])

    all_cities = set()
    for row in data:
        all_cities.add(row['Город'])

    unvisited_cities = all_cities - visited_cities

    first_city_to_visit = sorted(unvisited_cities)[0] if unvisited_cities else None

    with open('holiday.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(
            ['Города, в которых уже были', 'Города, которые хотят посетить', 'Города, в которых еще не были',
             'Первый город для посещения'])
        writer.writerow(
            [', '.join(sorted(visited_cities)), ', '.join(sorted(desired_cities)), ', '.join(sorted(unvisited_cities)),
             first_city_to_visit])

write_holiday_cities('А')
