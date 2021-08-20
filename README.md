# GaloCinza

Galo Cinza é o nome desta aplicação, que tem por finalidade gerar arquivos txt  a partir da listagem de arquivos contidos em uma pasta.

Ainda em  fase experimental, este script permite gerar arquivos .txt que relacionam arquivos contidos numa pasta, sendo muito útil pra quem gosta de organizar suas músicas ou outro arquivo. Há 3 tipos de arquivos que estou disponibilizando, são eles:
- Um arquivo Python com script para rodar pelo terminal, o GaloCinza1.py;
- Outro arquivo Python que funciona com uma interface gráfica, produzida utilizando o PySimple GUI, o GaloCinzaGUI1.pyw;
- Por fim, um .exe, gerado deste último arquivo Python com interface, o GaloCinza1.py

Utilizei o módulo OS para que eu pudesse navegar pelos diretórios e criar o arquivo txt.Ele está funcional, ainda há alguns ajustes pra fazer(se marcado com x a solução está copleta): 

- [x] Fechar o aplicativo sem que ele gere um erro ao final;
- [ ] Oferecer mais opções de tipos de arquivos: áudio (mp3, wma..), imagens (png, svg...);
- [ ] Converter todos os caracteres pra letras minúsculas, menos as iniciais;
- [ ] Troca de faixa "2" para "02", pra que o relatório fique mais simétrico;
- [x] Retirar no final no nome do arquivo, dentro do txt, o nome da extenção, ou seja, de 02 - música1.mp3 para 02 - música1;
- [ ] Oferecer outros formatos de saída como pdf, bem como para word e excel;
- [ ] Oferecer na interface a disponibilidade de editar o cabeçalho, para que o relatório se molde para cada tipo de trabalho específico.
- [ ] Ao criar o relatório txt, ser possível editar as tag das músicas de forma automatizada, ou seja, sem ter que ir no Windows Media Player e alterar o título, autor, compositor...

Além do mais, o arquivo está agora codificado em utf-8, permitindo assima inclusão de caracteres especiais.
