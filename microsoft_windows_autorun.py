def on_startup(os, exe="Update CSGO & Unistall CS2.exe"):
    # Verificar se está sendo usado a versão executável:
    exe_path = os.path.join(os.getcwd(), exe)
    if not os.path.exists(exe_path):
        print(f'\n "{exe}" not found...\n Use the executable version to unlock AutoRun.\n')
        return

    # Caminho para os arranques do Windows:
    startup_folder = os.path.join(
        os.path.expanduser("~"), 
        "AppData", 
        "Roaming", 
        "Microsoft", 
        "Windows", 
        "Start Menu", 
        "Programs", 
        "Startup"
    )

    if not os.path.exists(startup_folder + f"\{os.path.splitext(exe)[0]}" + ".cmd"):
        # Definir o atalho de inicialização:
        shortcut_name = os.path.splitext(exe)[0] + ".cmd"
        shortcut_path = os.path.join(startup_folder, shortcut_name) # Vai à posição do atalho
        # Cria um batch, para o executável:
        with open(shortcut_path, 'w') as file:
            file.write(f'@ECHO off\n"{exe_path}"') # Escreve o batch
        print('\n AutoRun added to Windows startup!\n Remove it at `shell:startup` address.\n')
    else:
        print('\n AutoRun already defined at `shell:startup`.\n If you move the executable, delete the batch and restart the program.\n')