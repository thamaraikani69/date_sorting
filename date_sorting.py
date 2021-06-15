# SWAMI KARUPPASWAMI THUNNAI
import datetime


def bubbleSort(arr):
    n = len(arr)

    for i in range(n-1):

        for j in range(0, n-i-1):

            date1 = str_date(arr[j]['date'])

            date2 = str_date(arr[j + 1]['date'])

            if date1 < date2:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    date_list = arr
    return date_list


def str_date(my_date):
    new_date = datetime.datetime.strptime(
        my_date, "%d/%m/%Y %H:%M")

    return new_date


if __name__ == "__main__":

    arr = [{"date": "15/06/2021 17:04", 'value': 100}, {"date": "30/06/2021 17:04", 'value': 100}, {"date": "1/07/2021 17:04", 'value': 100}, {
        "date": "5/07/2021 17:04", 'value': 100}, {"date": "31/07/2021 17:04", 'value': 100}, {"date": "29/05/2021 17:04", 'value': 100}]

    print(bubbleSort(arr))

    print("Sorted array is:")
    for i in range(len(arr)):
        print(arr[i])
