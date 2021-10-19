# Certificate Filler

Este script preencherá suas centenas de certificados de participação de eventos sem você ter que fazer à mão (pelo menos até a hora de assinar).

## Modo de usar

- Certifique-se de ter o Python instalado na sua máquina: [Baixar o Python](https://www.python.org/downloads/);
- Você também precisará dos seguintes módulos:

  - PIL:

  ```
  pip install Pillow
  ```

  - img2pdf:

  ```
  pip install img2pdf
  ```

- Clone ou baixe o projeto na sua máquina:

```
git clone https://github.com/cirops/certificate-filler.git
```

- Use seu terminal de linha de comando para ir até a pasta em que o projeto foi clonado. Ex:

  - Linux:

    ```
    cd /home/user/certificate-filler
    ```

  - Windows:

    ```
    cd C:\algumapasta\certificate-filler
    ```

- Copie a imagem de fundo do seu certificado para a pasta do projeto (outros formatos de imagem provavelmente funcional também, teste e me diga);
- Copie um arquivo .csv com uma lista de nomes, um por linha, para a pasta do projeto;
- Rode:

```
python certificate-filler.py imagem-de-fundo.png lista-de-participantes.csv pasta-de-saida
```

- Cheque se tudo funcionou corretamente abrindo a pasta de saíde e abrindo os arquivos;
- Opcionalmente, você pode mudar o tipo de fonte, tamanho e alinhamento de texto mudando as seguintes linhas:

```
title_font = ImageFont.truetype("FreeSansBold.ttf", 28, encoding="unic")
```

e

```
image_editable.text((W/2-w ,355), title_text, (0, 0, 0), font=title_font)
```

...talvez eu transforme-os em parâmetros do script, veremos.
