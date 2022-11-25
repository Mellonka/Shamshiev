import formating_to_stats
import formating_to_table


how_we_work = input("Как вывести данные?(Вакансии/Статистика): ")
if how_we_work == "Вакансии":
    formating_to_table.InputConnect().start_connection()
elif how_we_work == "Статистика":
    formating_to_stats.start()