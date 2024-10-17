import os
import ffmpeg
from mutagen.easyid3 import EasyID3

def convert_ts_to_mp3(ts_file, output_mp3):
    """
    Converte um arquivo .ts para .mp3 utilizando ffmpeg com sobrescrita automática.
    """
    ffmpeg.input(ts_file).output(output_mp3, format='mp3').run(overwrite_output=True)

def set_id3_tags(mp3_file, author, album, title):
    """
    Define as tags ID3 no arquivo mp3.
    """
    audio = EasyID3(mp3_file)
    audio['artist'] = author
    audio['album'] = album
    audio['title'] = title
    audio.save()

def process_directory(input_dir, output_dir):
    """
    Processa um diretório de arquivos .ts e converte-os para mp3 mantendo a estrutura de diretórios.
    """
    # Contar o número total de arquivos .ts para exibir o progresso
    total_files = sum(len(files) for _, _, files in os.walk(input_dir) if any(file.endswith('.ts') for file in files))
    processed_files = 0

    for root, _, files in os.walk(input_dir):
        relative_path = os.path.relpath(root, input_dir)
        output_subdir = os.path.join(output_dir, relative_path)
        os.makedirs(output_subdir, exist_ok=True)

        # Definir o autor e o álbum conforme especificado
        author = "Autor Padrão"
        album = os.path.basename(root) if relative_path != '.' else "Diversos"

        for file in files:
            if file.endswith('.ts'):
                ts_file = os.path.join(root, file)
                mp3_filename = os.path.splitext(file)[0] + '.mp3'
                output_mp3 = os.path.join(output_subdir, mp3_filename)

                # Exibir mensagem informando qual arquivo está sendo processado
                print(f'Convertendo "{ts_file}" para "{output_mp3}"...')

                # Converte o arquivo .ts para .mp3
                convert_ts_to_mp3(ts_file, output_mp3)

                # Define as tags ID3
                title = os.path.splitext(file)[0]
                set_id3_tags(output_mp3, author, album, title)

                # Atualiza o número de arquivos processados e mostra o progresso
                processed_files += 1
                percent_complete = (processed_files / total_files) * 100
                print(f'Arquivo {processed_files}/{total_files} convertido. ({percent_complete:.2f}% concluído)')

    print("Conversão concluída com sucesso!")

if __name__ == '__main__':
    input_directory = 'caminho/para/diretorio/com/ts'
    output_directory = 'caminho/para/diretorio/de/saida'

    process_directory(input_directory, output_directory)
