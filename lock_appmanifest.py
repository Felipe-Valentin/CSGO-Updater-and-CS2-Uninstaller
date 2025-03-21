def no_update(os, AppManifest_path=r"C:\Program Files (x86)\Steam\steamapps\appmanifest_730.acf"):
    import stat
    from re import search

    current_permissions = os.stat(AppManifest_path).st_mode # Vê as propriedades do arquivo AppManifest
    if not current_permissions & stat.S_IWRITE:
        print('\n [Lock-AppManifest module] AppManifest is already in read-only mode, skipping actions...')
        return

    with open(AppManifest_path, "r") as file:
        content = file.read() # Lê o conteúdo do AppManifest
    if search(r'"StateFlags"\s*"4"', content):
        try:
            os.chmod(AppManifest_path, current_permissions & ~stat.S_IWRITE) # Trava o arquivo em read-only
            print('\n [Lock-AppManifest module] AppManifest locked in read-only mode! This should prevent most new CS2 updates.\n')
        except Exception as e:
            print(f'\n [Lock-AppManifest module] AppManifest could not be locked in read-only mode, because:  {e}\n')
    else:
        print('\n [Lock-AppManifest module] Counter-Strike needs to be manually updated on Steam, when `StateFlags` becomes `4` this program will try to freeze future updates.\n')