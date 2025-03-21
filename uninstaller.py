def uninstall(os, directory_path=r"C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike Global Offensive\game"):
    from shutil import rmtree


    # Limite aceitável de tamanho, para o Counter-Strike 2
    limit_size = 2048  # (2kb) em bytes
    # Padrão: 2048


    # Calcula o tamanho total do Counter-Strike 2:
    total_size = sum(os.path.getsize(os.path.join(dirpath, filename)) 
                     for dirpath, dirnames, filenames in os.walk(directory_path) 
                     for filename in filenames)

    # Excluir todo o diretório do CS2:
    if total_size > limit_size:
        rmtree(directory_path) # Apaga a pasta do CS2 (tamanho maior que o limite)
        print(f'\n CS2 was deleted for being larger than {limit_size} bytes!\n')
    elif not total_size <= 0:
        print(f'\n CS2 Steam.inf kept. Current size, in bytes:  {total_size}\n')

    # Reconstruir fragmentos especificos, do diretório do CS2:
    if not os.path.exists(directory_path):
        os.makedirs(directory_path) # Fragmento necessário #1
        os.makedirs(directory_path + r"\csgo") # Fragmento necessário #2