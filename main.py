with open('text.txt', 'r', encoding='utf-8') as infile, open('output.txt', 'w', encoding='utf-8') as outfile:
    
    for line in infile:
        
        modified_line = ""
        
        for char in line:
            
            if char == 'о':
                
                modified_line += 'a'
                
            else:
                
                modified_line += char
                
        outfile.write(modified_line)