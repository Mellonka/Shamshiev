import csv

salary_by_year = {2007: 38916, 2008: 43646, 2009: 42492, 2010: 43846, 2011: 47451, 2012: 48243, 2013: 51510, 2014: 50658, 2015: 52696, 2016: 62675, 2017: 60935, 2018: 58335, 2019: 69467, 2020: 73431, 2021: 82690, 2022: 91795}
vacancy_count_by_year = {2007: 2196, 2008: 17549, 2009: 17709, 2010: 29093, 2011: 36700, 2012: 44153, 2013: 59954, 2014: 66837, 2015: 70039, 2016: 75145, 2017: 82823, 2018: 131701, 2019: 115086, 2020: 102243, 2021: 57623, 2022: 18294}
selec_salary_by_year = {2007: 40641, 2008: 48428, 2009: 48109, 2010: 49577, 2011: 52794, 2012: 58341, 2013: 57004, 2014: 58768, 2015: 53326, 2016: 54236, 2017: 56558, 2018: 61080, 2019: 71288, 2020: 80145, 2021: 87473, 2022: 91340}
selec_vacancy_count_by_year = {2007: 34, 2008: 196, 2009: 171, 2010: 328, 2011: 418, 2012: 374, 2013: 420, 2014: 504, 2015: 749, 2016: 911, 2017: 1201, 2018: 1578, 2019: 1482, 2020: 1349, 2021: 805, 2022: 305}
salary_by_city = {'Москва': 76970, 'Санкт-Петербург': 65286, 'Новосибирск': 62254, 'Екатеринбург': 60962, 'Казань': 52580, 'Краснодар': 51644, 'Челябинск': 51265, 'Самара': 50994, 'Пермь': 48089, 'Нижний Новгород': 47662}
frac_by_city = {'Москва': 0.3246, 'Санкт-Петербург': 0.1197, 'Новосибирск': 0.0271, 'Казань': 0.0237, 'Нижний Новгород': 0.0232, 'Ростов-на-Дону': 0.0209, 'Екатеринбург': 0.0207, 'Краснодар': 0.0185, 'Самара': 0.0143, 'Воронеж': 0.0141}

path = r'files/'
for year in salary_by_year:
    with open(path+f'{year}_file.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['year', 'salary', 'vacancy count', 'selected salary', 'selected_vacancy_count'])
        writer.writerow([year, salary_by_year[year], vacancy_count_by_year[year], selec_salary_by_year[year], selec_vacancy_count_by_year[year]])

