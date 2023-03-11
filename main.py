from scipy.stats import shapiro, ttest_rel
import pandas


def import_data(path):
    data = pandas.read_excel(path)
    new_data = list(data.T.to_dict().values())
    data_before = []
    data_after = []
    for item in new_data:
        data_before.append((list(item.values()))[0])
        data_after.append((list(item.values()))[1])
    return data_before, data_after


def analyze_data(data_before, data_after):
    normal_before = shapiro(data_before)
    normal_after = shapiro(data_after)
    if normal_before.pvalue < 0.05:
        raise ValueError(
            'Data distribution before the experiment is not normal'
            )

    if normal_after.pvalue < 0.05:
        raise ValueError(
            'Data distribution after the experiment is not normal'
            )

    return (ttest_rel(data_before, data_after))


def main():
    file = input('Enter the file name. Note that it must be in .xlsx format: ')
    data_before, data_after = import_data(f'{file}.xlsx')
    result = analyze_data(data_before, data_after)
    print(result)


if __name__ == '__main__':
    main()
