import os
import urllib.request
from time import sleep

from lock_appmanifest import no_update
no_update(os)  # tenta impedir as atualizações do CS2 (travando o AppManifest em read-only)
from uninstaller import uninstall
uninstall(os) # Desinstala o Counter-Strike 2
from microsoft_windows_autorun import on_startup
on_startup(os)  # se estiver usando a versão executável, inicializará junto com o Windows
from reference import web_link
url = web_link()  # resgata o endereço web para o Steam.inf do CS2, de referência


# Caminhos para o Steam.inf, respectivos de cada jogo
local_path1 = r"C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike Global Offensive\csgo\steam.inf"  # do CS:GO
# Padrão: r"C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike Global Offensive\csgo\steam.inf"
local_path2 = r"C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike Global Offensive\game\csgo\steam.inf"  # do CS2
# Padrão: r"C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike Global Offensive\game\csgo\steam.inf"



# Obter referência online:
with urllib.request.urlopen(url) as response:
    online_content = response.read().decode("utf-8").splitlines() # Resgata a referência, e decodifica em UTF-8

# Processar os Steam.inf respectivos:
with open(local_path1, "r") as file:
    local_content1 = file.read().splitlines() # Lê linha por linha, do arquivo
try:
    with open(local_path2, "r") as file:
        local_content2 = file.read().splitlines() # Lê linha por ""
except FileNotFoundError:
    local_content2 = "ERROR__FILE_NOT_FOUND"
    pass  # trata o erro (esperado) com except agora, e reconstrói no futuro


# Atuar nas duas primeiras linhas, do Steam.inf do CSGO:
if ( online_content[:2] != local_content1[:2] ) or ( online_content != local_content2 ):
    print('\n New "ClientVersion" and "ServerVersion" found!  Updating...')
    updated_local_content1 = online_content[ :2 ] + local_content1[ 2: ] # Atualiza as versões
    # Salvar arquivo atualizado:
    with open(local_path1, "w") as file:
        file.write("\n".join(updated_local_content1) + "\n") # Reconstrói arquivo  (fragmento necessário #3)

    # Atuar no Steam.inf do CS2:
    with open(local_path2, "w") as file:
        file.write("\n".join(online_content) + "\n") # Reconstrói um novo arquivo  (fragmento necessário #4)
    print(' Steam.inf has been completely replaced by the found reference.')
    print('\n\n\n SUCCESSFUL UPDATE! Exiting updater, in 50 seconds...')
    sleep(50) # Aguarda 50 segundos

else:
    print('\n "ClientVersion" and "ServerVersion" are updated.\n No updates were applied.')
    print('\n\n\n Exiting updater, in 30 seconds...')
    sleep(30) # Aguarda 30 segundos