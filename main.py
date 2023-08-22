from email_sender import Emailer

email = Emailer('jhonatandevaprender1@gmail.com', 'gxnxkxrvwnwbobbs')

lista_contatos = ['jhonatands.dev.2030@gmail.com',
                  'jhonatandevaprender1@gmail.com']
mensagem = '''
Olá seu pacote acaba de chegar nos correios!
'''
email.definir_conteudo(topico='Seu pacote chegou!', email_remetente='jhonatands.dev.2030@gmail.com',
                       lista_contatos=lista_contatos, conteudo_email=mensagem)

imagens = ['bluesky.jpg', 'retro.jpg']
email.anexar_imagem(imagens)

arquivos = ['csv_exemplo.csv', 'exemplo_word.docx',
            'ExemploPlanilha.xlsx', 'PDF_Exemplo.pdf', 'Untitled presentation.pptx']
email.anexar_arquivos(arquivos)
email.enviar_email(intervalo_em_segundos=30)