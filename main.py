from scipy.stats import shapiro, ttest_rel, ttest_ind
import pandas


def import_data(path):
    data = pandas.read_excel(path, usecols='A:B')
    new_data = list(data.T.to_dict().values())
    data_before = []
    data_after = []
    for item in new_data:
        data_before.append((list(item.values()))[0])
        data_after.append((list(item.values()))[1])
    return data_before, data_after


def check_normality(a, b):
    normal_a = shapiro(a)
    normal_b = shapiro(b)
    check = True
    if normal_a.pvalue < 0.05:
        print(
            'Data distribution in the first sample is not normal'
            )
        check = False

    if normal_b.pvalue < 0.05:
        print(
            'Data distribution in the second sample is not normal'
            )
        check = False
    return check


def analyze_data(sample_one, sample_two, test_type):
    norm = check_normality(sample_one, sample_two)
    if norm is True and test_type == 'yes':
        result = ttest_ind(sample_one, sample_two)
        to_return = result.pvalue
    elif norm is True and test_type == 'no':
        result = ttest_rel(sample_one, sample_two)
        to_return = result.pvalue
    else:
        to_return = 'Please, check your data.'
    return to_return


def get_test_type():
    test_type = input('Are your samples independent? Type yes/no. ')
    if test_type.lower() != 'yes' and test_type.lower() != 'no':
        print('Please type only "yes" or "no".')
        test_type = get_test_type()
    return test_type


def main():
    test_type = get_test_type()
    file = input('Enter the file path. Supported formats: xls, '
                 'xlsx, xlsm, xlsb, odf, ods and odt. ')
    sample_one, sample_two = import_data(f'{file}')
    print(analyze_data(sample_one, sample_two, test_type))


if __name__ == '__main__':
    main()
