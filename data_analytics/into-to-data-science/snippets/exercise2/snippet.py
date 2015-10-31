import pandas
import pandasql


def num_rainy_days(filename):
    weather_data = pandas.read_csv(filename, na_values='')
    q = '''
    SELECT count(rain) AS weather_data from weather_data where rain = 1;
    '''
    rainy_days = pandasql.sqldf(q.lower(), locals())
    return rainy_days


def max_temp_aggregate_by_fog(filename):
    weather_data = pandas.read_csv(filename, na_values='')
    q = '''
    SELECT MAX(maxtempmi) AS maxtemp, fog from weather_data group by fog;
    '''
    max_tmp_by_fog = pandasql.sqldf(q.lower(), locals())
    return max_tmp_by_fog

if __name__ == "__main__":
    print num_rainy_days('weather_underground.csv')
    print max_temp_aggregate_by_fog('weather_underground.csv')
