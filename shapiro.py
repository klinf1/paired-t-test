from scipy.stats import shapiro, ttest_rel

data_before = []
data_after = []
elements_number = int(input('How many objects are in each group? '))

for i in range(elements_number):
    value = float(input(f'Type element number {i+1} before the experiment '))
    data_before.append(value)

for i in range(elements_number):
    value_two = float(
        input(f'Type element number {i+1} after the experiment ')
        )
    data_after.append(value_two)


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

    print(ttest_rel(data_before, data_after))


analyze_data(data_before, data_after)
