from gtts import gTTS

def get_name(list_caminhos):
    return [caminho.split('/')[-1].split('.')[0] for caminho in list_caminhos]

def get_text(file):
    arquivos = file.split(';')
    nomes = get_name(arquivos)
    textos = []

    for arquivo in arquivos:
        with open(arquivo,'r',encoding='utf-8') as conteudo:
            textos.append(conteudo.read())

    return textos, nomes

def text_to_audio(window,arquivos,linguagem,audio_lento=False):
    try:
        textos, nomes = get_text(arquivos)
    except FileNotFoundError:
        window.write_event_value('erro','')
    
    print('Iniciando a conversão!')
    for texto,nome in zip(textos,nomes):
        audio = gTTS(text=texto,lang=linguagem,slow=audio_lento)
        audio.save(f'{nome}.mp3')
    
    window.write_event_value('Finalizado', 'Conversão concluída!')
