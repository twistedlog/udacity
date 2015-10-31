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
    SELECT fog, MAX(cast(maxtempi AS integer)) AS weather_data FROM weather_data GROUP BY fog;
    '''
    max_tmp_by_fog = pandasql.sqldf(q.lower(), locals())
    return max_tmp_by_fog


def avg_weekend_temprature(filename):
    weather_data = pandas.read_csv(filename, na_values='')
    q = '''
    SELECT AVG(cast(meantempi AS integer)) AS weather_data FROM weather_data WHERE cast(strftime('%w', date) as integer) IN (0, 6);
    '''
    avg_weekend_temp = pandasql.sqldf(q.lower(), locals())
    return avg_weekend_temp


def avg_min_temprature(filename):
    weather_data = pandas.read_csv(filename, na_values='')
    q = '''
    SELECT AVG(cast(mintempi AS integer)) AS weather_data FROM weather_data WHERE rain =1 AND mintempi > 55;
    '''
    avg_min_temp = pandasql.sqldf(q.lower(), locals())
    return avg_min_temp


if __name__ == "__main__":
    filename = 'weather_underground.csv'
    print num_rainy_days(filename)
    print max_temp_aggregate_by_fog(filename)
    print avg_weekend_temprature(filename)
    print avg_min_temprature(filename)
