from data import DATA
from seat import Seat

cleaned_data = DATA.splitlines()

if __name__ == "__main__":
    seats = [Seat.from_string(data) for data in cleaned_data]
    max_id = max([seat.id for seat in seats])

    print("PART ONE\n=======")
    print('Greatest passport ID: {}'.format(max_id))

    sorted_ids = [seat.id for seat in sorted(seats, key=lambda seat: seat.id)]
    expected_id = None
    for id in sorted_ids:
        if expected_id is None:
            expected_id = id + 1
            continue

        if not id == expected_id:
            break

        expected_id = id + 1

    print('Missing Seat ID: {}'.format(expected_id))
    print("\nPART TWO\n=======")