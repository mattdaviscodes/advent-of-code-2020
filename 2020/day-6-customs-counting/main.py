from data import DATA
from pprint import pprint

grouped_data = DATA.split('\n\n')
individual_data = [data.split('\n') for data in grouped_data]
cleaned_data = [block.replace('\n', '') for block in grouped_data]

if __name__ == "__main__":
    yes_count = 0
    for data in cleaned_data:
        unique = ''.join(set(data))
        yes_count += len(unique)

    print("PART ONE\n=======")
    print('Count of Individual Yes Answers: {}'.format(yes_count))

    yes_count = 0
    unique = [''.join(set(data)) for data in cleaned_data]

    for unique_answers, individual_answers in zip(unique, individual_data):
        for unique_answer in unique_answers:
            yes_count += all([unique_answer in i for i in individual_answers])
    
    print("\nPART TWO\n=======")
    print('Count of Group Yes Answers: {}'.format(yes_count))