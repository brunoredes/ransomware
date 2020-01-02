#!/usr/bin/python3.6
import os

def discover(inital_path):
    #Extensões de possíveis arquivos alvos: o que estiver com comentário, não será encriptado

    extensions = [
        # 'exe,', 'dll', 'so', 'rpm', 'deb', 'vmlinuz', 'img'  # Arquivos do Sitema
        'jpg', 'jpeg', 'bmp', 'gif', 'png', 'svg', 'psd', 'raw',  # imagens
        'mp3', 'mp4', 'm4a', 'aac', 'ogg', 'flac', 'wav', 'wma', 'aiff', 'ape',  # Audios
        'avi', 'flv', 'm4v', 'mkv', 'mov', 'mpg', 'mpeg', 'wmv', 'swf', '3gp',  # Vídeos
        'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx',  # Microsoft office
        # OpenOffice, Adobe, Latex, Markdown, etc
        'odt', 'odp', 'ods', 'txt', 'rtf', 'tex', 'pdf', 'epub', 'md',
        'yml', 'yaml', 'json', 'xml', 'csv',  # dados estruturados e config
        'db', 'sql', 'dbf', 'mdb', 'iso',  # bancos de dados e imagens de disco

        'html', 'htm', 'xhtml', 'php', 'asp', 'aspx', 'js', 'jsp', 'css'  # tecnologias web
        'c', 'cpp', 'cxx', 'h', 'hpp', 'hxx' 'cs',  # Código fonte C e C++
        'java', 'class', 'jar'  # Códigos fonte Java
        'ps', 'bat', 'vb',  # Scripts de sistemas windows
        'awk', 'sh', 'cgi', 'pl', 'ada', 'swift',  # Scripts de sistemas unix
        'go', 'py', 'pyc', 'bf', 'coffee',  # Outros tipos de códigos fonte

        'zip', 'tar', 'tgz', 'bz2', '7z', 'rar', 'bak','txz'  # Arquivos compactados e Backups
    ]

    for dirpath, dirs, files in os.walk(inital_path):
        for _file in files:
            abspath = os.path.abspath(os.path.join(dirpath, _file))
            ext = abspath.split('.')[-1] #pega o primeiro item do indice ao contrario (ultimo item do array)
            if ext in extensions:
                yield abspath

# só será executado quando você executa o módulo diretamente

if __name__ == '__main__':
    x = discover(os.getcwd())
    for i in x:
        print(i)