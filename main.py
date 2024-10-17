with open('text.txt', 'r', encoding='utf-8') as infile, open('output.txt', 'w', encoding='utf-8') as outfile: # Открываем файл 'text.txt' для чтения и 'output.txt' для записи, оба с кодировкой utf-8
    
    for line in infile: # Перебираем каждую строку в файле 'text.txt'
        
        modified_line = "" # Создаем пустую строку для хранения модифицированной версии текущей строки
        
        for char in line: # Перебираем каждый символ в строке
            
            if char == 'о': # Если символ 'о'
                
                modified_line += 'a' # Заменяем символ 'о' на 'a'
                
            else: # Если символ не 'о'
                
                modified_line += char # Добавляем его в исходном виде
                
        outfile.write(modified_line) # Записываем модифицированную строку в файл 'output.txt'
