import time
from functools import wraps
from pytube import YouTube

def temporizador(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        tempo_inicial = time.time()
        
        resultado = func(*args, **kwargs)
        
        tempo_final = time.time()
        tempo_decorrido = tempo_final - tempo_inicial
        
        print(f"Tempo decorrido: {tempo_decorrido:.2f} segundos")
        
        return resultado
    
    return wrapper

@temporizador
def baixar_video(url):
    try:
        youtube = YouTube(url)
        titulo = youtube.title
        streams = youtube.streams.filter(progressive=True)

        print("Opções de qualidade disponíveis:")
        for i, stream in enumerate(streams):
            print(f"{i + 1}. Resolução: {stream.resolution}, Extensão: {stream.mime_type.split('/')[-1]}")

        opcao = int(input("Digite o número da opção desejada: ")) - 1
        if opcao < 0 or opcao >= len(streams):
            print("Opção inválida.")
            return

        selected_stream = streams[opcao]
        selected_stream.download(filename=f'{titulo}.{selected_stream.mime_type.split("/")[-1]}')

        print("Download concluído.")
    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")

# Exemplo de uso
url = input("Digite a URL do vídeo do YouTube: ")
baixar_video(url)
