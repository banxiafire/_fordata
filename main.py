

def scipycalculation(country):


    df1 = pd.read_csv(country + '_Weekly_average_data_Cases.csv')
    df2 = pd.read_csv(country + '_Weekly_average_data_Mobility.csv')

    print(df1)
    print(df2)


    res1 = stats.pearsonr(df1.average_cases_7[3:17], df2.average_mobility_7[3:17])
    res2 = stats.pearsonr(df1.average_cases_7[79:96], df2.average_mobility_7[79:96])
    res3 = stats.pearsonr(df1.average_cases_7[99:112], df2.average_mobility_7[99:112])

    print(res1)
    print(res2)
    print(res3)

    import numpy as np

    differ = np.diff(df1.average_cases_7)

    print(differ)

    testvalue = []
    testindex = []



    for idx, dd in enumerate(differ):
        if dd > 100 or dd < -100:
            testvalue.append(dd)
            testindex.append(idx)


    print(testvalue)
    print(testindex)


from scipy import stats
import pandas as pd
scipycalculation('Denmark')