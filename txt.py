import os

def merge_files(file_list, output_filename):
    file_data = []

    # Собираем информацию о файлах
    for filename in file_list:
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                file_data.append({
                    'name': filename,
                    'count': len(lines),
                    'content': lines
                })

    # Сортируем по количеству строк (пункт 1)
    file_data.sort(key=lambda x: x['count'])

    # Записываем в итоговый файл (пункт 2)
    with open(output_filename, 'w', encoding='utf-8') as out_f:
        for file in file_data:
            out_f.write(f"{file['name']}\n")
            out_f.write(f"{file['count']}\n")
            out_f.writelines(file['content'])
            out_f.write("\n")  # Добавляем перенос для порядка

# Запуск
files_to_read = ['1.txt', '2.txt', '3.txt']
merge_files(files_to_read, 'result.txt')
