# CSGO Updater & CS2 Uninstaller
> WARNING: this repository and everything included in it has no official connection to Steam or Valve Corporation, it is simply a tool for update ClientVersion and ServerVersion of CS:GO & uninstall CS2, with the [Steam.inf GameTracking-CS2 repository](https://github.com/SteamDatabase/GameTracking-CS2/blob/master/game/csgo/steam.inf) publicly released by SteamDB.info

<br/>

## Para que serve esse programa?
Sobre o *CSGO Updater & CS2 Uninstaller*:

- Um programa leve **<9mb** (agradecimentos ao [PyInstaller](https://pyinstaller-org.translate.goog/en/stable/?_x_tr_sl=auto&_x_tr_tl=pt&_x_tr_hl=pt-BR)), com objetivo de manter o `ClientVersion` e `ServerVersion` do **CS:GO Legacy** atualizado, possibilitando acesso ao inventário dentro do *CS:GO*, e lhe permitindo juntar-se à partidas on-line em servidores da comunidade (para *CS:GO Legacy*).

- Nosso **CSGO Updater & CS2 Uninstaller** possui um *AutoRun* não-invasivo (escrito em batch no `shell:startup`), que fará o programa arrancar automaticamente quando o Windows inicializar, mantendo seu *CS:GO* sempre atualizado! **–** *limites: necessário usar a versão executável `EXE` do programa; Uma vez que o executável for movido para outro diretório, será preciso deletar a batch, e executar o programa manualmente para reabilitar o* AutoRun *de novo.*
<br/>

![Antigo ícone do Counter-Strike: Global Offensive](https://upload.wikimedia.org/wikipedia/pt/c/ce/Counter-Strike_Global_Offensive.jpg)

<br/>

## Como está o CS:GO Legacy, nos dias de hoje?

**CS:GO Legacy** é o antecessor do **Counter-Strike 2**, que pode ser baixado oficialmente na aba "Betas", em "Propriedades...", na biblioteca *Steam* do *CS2*. Esta versão do jogo foi a oficial entre 2012-2023, aonde em 2024 foi substituída abruptamente pela versão do *CS2*. A versão do *CS:GO Legacy*, é conhecida por ser melhor otimizada em termos de FPS (quadros por segundo), tendo uma jogabilidade e gráficos similares ao seu sucessor não tão bem otimizado (para computadores mais antigos), o *CS2*.

A comunidade de *CS:GO* permanece super ativa, com vários jogadores e partidas acontecendo em qualquer horário do dia, com altos e baixos picos de atividade. Redes brasileiras como a [FireGames Network](https://www.firegamesnetwork.com), e o [Savage Servidores](https://savageservidores.com/servidores?gamemode=5X5&type=csgo&rules=false) mantém o jogo popular, e a diversão como em 2023. Nós conseguimos parar o tempo!
<br/>

![Banner oficial do Counter-Strike: Global Offensive](https://media.steampowered.com/apps/csgo/blog/images/fb_image.png)

A *Steam* por sua vez, obriga ter o **Counter-Strike 2** instalado para podermos iniciar o **CS:GO Legacy**, que sem modificações especificas nos arquivos do jogo se encontrará limitado, com inventário e servidores da comunidade bloqueados. O nosso programa **CSGO Updater & CS2 Uninstaller**, corrige essas limitações, e desinstala o *CS2* de forma que não obrigue-o instalar novamente (até agora, funcionando em março de 2025).

*CS2*? Para nós, isso nunca existiu...
~ Um jogo de FPS, que não tem FPS ~

<br/>

## Há como usar o AutoRun, na versão de script Python?

Sim, é possível iniciar o **CSGO Updater & CS2 Uninstaller** no arranque do Windows através do script Python, mas isso não é recomendável devido as instabilidades desse método, se você decidir por prosseguir mesmo assim, siga essas etapas:

1. Pressione as teclas `Windows + R`, ao mesmo tempo;
2. Digite: `shell:startup`, na caixa de diálogo;
3. Crie um arquivo de texto, e chame o script Python pelo interpretador;
```Exemplo:
@ECHO off
python.exe "\path\to\main.py"
```
4. Salve o arquivo de texto, em formato `BAT` (se desejar usar `CMD`, certifique-se de não usar o nome de arquivo **Update CSGO & Unistall CS2**, senão causará conflitos/erros no script);
5. Pronto, execute o batch criado e veja se funciona bem.

<br/>

> Please, note that the source code contained in this repository is only released for use under the "[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) [(Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International)](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode.txt)" license.