from time import sleep
import datetime
import json
import sys
import os

print('ini')
while True:
    try:
        
        try:
            
            import requests
            import gspread

            gc = gspread.service_account(filename='spry-sequence-357517-d1ca6ab92278.json')
            sh = gc.open_by_key('1tfexKq7hD4Ri945jqB2ok12Mc3AUdjVlzFnnlIU62HY')

            token = '6645544649:AAF03ei6QzjvEYdcLHQx9EyudboVYGcibjM'
            url_base = f'https://api.telegram.org/bot{token}/'
            def restart_program():
                python = sys.executable
                os.execl(python, python, * sys.argv)

            while True:
                try:
                    def obter_novas_mensagens(update_id):
                        
                        link_requisicao = f'{url_base}getUpdates?timeout=100'
                        if update_id:
                            link_requisicao = f'{link_requisicao}&offset={update_id + 1}'
                        resultado = requests.get(link_requisicao)
                        return json.loads(resultado.content)

                    def responder2(resposta, chat_id):
                        link_requisicao = f'{url_base}sendMessage?chat_id={chat_id}&text={resposta}'
                        requests.get(link_requisicao)

                    def responder3(chat_id):
                        file_id = 'AgACAgEAAxkBAAID-GTwgiM7c2YjvUcs6d1drGXTNadmAALCqjEb1TOBR7YrLZ5G-4_pAQADAgADcwADMAQ'
                        link_requisicao = f'{url_base}sendPhoto?chat_id={chat_id}&photo={file_id}'
                        requests.get(link_requisicao)

                    def code():
                        agora = str(datetime.datetime.now())
                        print(agora)
                        dia1 = int(agora.strip()[8])
                        dia2 = int(agora.strip()[9])
                        mes1 = int(agora.strip()[5])
                        mes2 = int(agora.strip()[6])
                        dia = int(str(dia1)+str(dia2))
                        mes = int(str(mes1)+str(mes2))
                        hora = int(str(str(agora.strip()[11]) + str(agora.strip()[12])))-3
                        if hora == 0:
                            hora = 25
                        min = int(str(str(agora.strip()[14]) + str(agora.strip()[15])))
                        if min == 0:
                            min = 42

                        precod = dia * mes * hora * round(min/5) * 1000
                        if round(min/5) == 0:
                            precod = dia * mes * hora * 1000
                        codigo = int(str(precod).strip()[0]+str(precod).strip()[1]+str(precod).strip()[2]+str(precod).strip()[3])
                        hora = str(int(str(agora.strip()[11]) + str(agora.strip()[12]))-3)
                        min = str(str(agora.strip()[14]) + str(agora.strip()[15]))
                        
                        print(hora)
                        print(codigo)
                        return dia, mes, hora, min, codigo
                    
                    worksheet = sh.get_worksheet(33)
                    salva1 = worksheet.cell(2,5).value
                    salva2 = worksheet.cell(2,6).value
                    print(salva1)
                    print(salva2)

                    if int(salva1) == 1:
                        update_id = int(salva2)
                        worksheet.update_cell(2,5,"0")
                        print('que')

                    else:
                        print("uhu")
                        update_id = None
                        print("uhA")
                        #worksheet = sh.get_worksheet(33)
                        #print(update_id)
                        

                    while True:
                        
                        atualizacao = obter_novas_mensagens(update_id)       
                        dados = atualizacao["result"]

                        if dados:
                            for dado in dados:
                                
                                update_id = dado['update_id']
                                try:
                                    first_name = dado["message"]['from']['first_name']
                                    print(dado)        
                                    
                                    message_id = dado['message']['message_id']
                                    mensagem = str(dado["message"]["text"])
                                    chat_id = dado["message"]["chat"]["id"]
                                except:
                                    mensagem = '0000'
                                    chat_id = 1154633217

                                if ('afrt') in mensagem.lower():
                                    sys.exit()
                                    #chat_id = '-1001986357289'
                                    #responder2(resposta, chat_id)
                                    l = mensagem.lower().split()[1]
                                    if 5 > l:
                                        print('oxen')
                                    print("a")
                                    responder3(chat_id)

                                #elif ('help') in mensagem.lower():

                                    #resposta = 'Esse é o seu diário pessoal de vendas, escreva diariamente todas as interações com os seus leads, desde um follow-up até os resultados e objeções obtidos após uma apresentação de proposta.\n\nTemos cinco comandos principais:\n\n- /funil -> Lista todos os leads cadastrados no ploomes.\n\n- /prospectei -> Soma um valor à quantidade de leads prospectados por você hoje.\nEx.:\n/prospectei 11\n\n- /att -> Publica no ploomes alguma atualização sobre um lead específico.\nEx.:\n/att Natalia Alves\nReunião estava marcada pra hoje, dia 03/04/2023 às 14h, mas ela não apareceu\n\n- /cadastrar -> Cadastra um lead no ploomes através do seu @ do instagram e seu nome\nEx.:\n/cadastrar @nataliaalves\nNatalia Alves\n\n- /mover -> Move um lead para outra etapa do funil\nEx.:\n/mover Natalia Alves\nFollow-up'
                                    #responder2(resposta, chat_id)

                                elif ('start') in mensagem.lower() or ('help') in mensagem.lower():
                                    try:
                                        worksheet = sh.get_worksheet(33)
                                        codigos = worksheet.col_values(3)
                                        nomes = worksheet.col_values(2)
                                        print(list(codigos))
                                        list(nomes)
                                        print(chat_id)

                                        if str(chat_id) in list(codigos):
                                            resposta = 'Muito prazer, sou o J.E.T.T.A Office e estou aqui para monitorar a frequência dos membros na nossa querida salinha.'
                                            responder2(resposta, chat_id)
                                            resposta ='Para registrar sua entrada na salinha digite: /BPE [CODIGO]\nEx.; /BPE 5689'
                                            responder2(resposta, chat_id)
                                            resposta ='Para registrar sua saída na salinha digite: /BPS [CODIGO]\nEx.; /BPS 3987'
                                            responder2(resposta, chat_id)
                                            resposta ='Se não sabe como obter um codigo, utilize o comando /codigo'
                                            responder2(resposta, chat_id)
                                        else:
                                            resposta = 'Muito prazer, sou o J.E.T.T.A Office e estou aqui para monitorar a frequência dos membros na nossa querida salinha.'
                                            responder2(resposta, chat_id)
                                            resposta = 'Você ainda não possui um cadastro, por favor envie o número referente ao seu nome da seguinte forma:\n/CAD [SEU NÚMERO]\nEx.: /CAD 21'
                                            responder2(resposta, chat_id)
                                            resposta = '1 - Arthur\n2 - Artur\n3 - Bia\n4 - Brmat\n5 - Bruna\n6 - Claudio\n7 - Eduardo\n8 - Ermesson\n9 - George\n10 - Gibs\n11 - Hudson\n12 - Isaac\n13 - Isabela\n14 - Isac\n15 - Jefao\n16 - Jhonatan\n17 - Julia\n18 - Levy\n19 - Lídice\n20 - Lourrenny\n21 - Lucas\n22 - Natan\n23 - Nosep\n24 - Ph1\n25 - Ph2\n26 - Rômulo\n27 - Samuel G\n28 - Samuel T\n29 - Yankara\n30 - Yanne\n31 - Yasmine\n32 - Ycaro'
                                            responder2(resposta, chat_id)
                                    except:
                                        resposta = '[Erro ao acessar dados da planilha]\nPor favor, entre em contato com o suporte'
                                        responder2(resposta, chat_id)

                                elif ('cad') in mensagem.lower():
                                    #print(int(mensagem.strip()[1]))
                                    try:
                                        worksheet = sh.get_worksheet(33)
                                        #print(int(mensagem.strip()[1]))
                                        worksheet.update_cell(int(mensagem.split()[1])+1,3,chat_id)
                                        resposta = 'Cadastro realizado com sucesso!!'
                                        responder2(resposta, chat_id)
                                        resposta ='Para registrar sua entrada na salinha digite: /BPE [CODIGO]\nEx.; /BPE 5689'
                                        responder2(resposta, chat_id)
                                        resposta ='Para registrar sua saída na salinha digite: /BPS [CODIGO]\nEx.; /BPS 3987'
                                        responder2(resposta, chat_id)
                                        resposta ='Se não sabe como obter um codigo, utilize o comando /codigo'
                                        responder2(resposta, chat_id)
                                    except:
                                        resposta = 'Erro ao realizar o cadastro, por favor tente novamente ou entre em contato com o suporte'
                                        responder2(resposta, chat_id)
                                
                                elif ('bpe') in mensagem.lower():
                                    try:
                                        dia = mes = hora = min = codigo = 80
                                        ahai = code()
                                        dia = ahai[0]
                                        mes = ahai[1]
                                        hora = ahai[2]
                                        min = ahai[3]
                                        codigo = ahai[4]
                                        if len(mensagem.split()) != 2:
                                            resposta = 'Não foi possível realizar o registro, verifique a mensagem e tente novamente.'
                                            responder2(resposta, chat_id)
                                            resposta ='Para registrar sua entrada na salinha digite: /BPE [CODIGO]\nEx.; /BPE 5689'
                                            responder2(resposta, chat_id)
                                        elif codigo == int(mensagem.split()[1]):
                                            if hora != 80:
                                                worksheet = sh.get_worksheet(33)
                                                codigos = worksheet.col_values(3)
                                                nomes = worksheet.col_values(2)
                                                try:
                                                    indexMap = dict((x, i) for i, x in enumerate(list(codigos)))
                                                    ind = indexMap[str(chat_id)]
                                                    #print(ind)
                                                    #print(list(nomes)[ind])
                                                    worksheet = sh.get_worksheet(ind)
                                                    if len(str(dia).strip()) == 1:
                                                        dia = f'0{dia}'
                                                    if len(str(mes).strip()) == 1:
                                                        mes = f'0{mes}'
                                                    data = f'{dia}/{mes}/2023'
                                                    try:
                                                        indexMap = dict((x, i) for i, x in enumerate(list(worksheet.col_values(1))))
                                                        ind2 = indexMap[str(data)]
                                                        if worksheet.cell(ind2+1, 2).value == 0 or worksheet.cell(ind2+1, 2).value == None:
                                                            worksheet.update_cell(ind2+1,2,f'{hora}:{min}')
                                                            resposta = f'Entrada registrada às {hora}h e {min}min'
                                                            responder2(resposta, chat_id)
                                                            resposta = 'Lembre-se de registrar a sua saída ao fim do seu horário.'
                                                            responder2(resposta, chat_id)
                                                            #'AAMCAQADGQEAA05k51sQN1SkAxbSsxbe34TCgZZPUQACGQQAAiX88UehIWBtCo0ziQEAB20AAzAE'
                                                        elif 1 == 1:
                                                            indexMap = dict((x, i) for i, x in enumerate(list(worksheet.col_values(11))))
                                                            ind2 = indexMap[str(data)]
                                                            if worksheet.cell(ind2+1, 12).value == 0 or worksheet.cell(ind2+1, 12).value == None:
                                                                worksheet.update_cell(ind2+1,12,f'{hora}:{min}')
                                                                resposta = f'Entrada registrada às {hora}h e {min}min'
                                                                responder2(resposta, chat_id)
                                                                resposta = 'Lembre-se de registrar a saída ao fim do seu horário.'
                                                                responder2(resposta, chat_id)
                                                            else:
                                                                resposta = f'Entrada já registrada anteriormente'
                                                                responder2(resposta, chat_id)
                                                        else:
                                                            resposta = f'Erro ao registrar entrada, por favor entre em contato com o suporte'
                                                            responder2(resposta, chat_id)
                                                    except:
                                                        try:
                                                            indexMap = dict((x, i) for i, x in enumerate(list(worksheet.col_values(11))))
                                                            ind2 = indexMap[str(data)]
                                                            if worksheet.cell(ind2+1, 12).value == 0 or worksheet.cell(ind2+1, 12).value == None:
                                                                worksheet.update_cell(ind2+1,12,f'{hora}:{min}')
                                                                resposta = f'Entrada registrada às {hora}h e {min}min'
                                                                responder2(resposta, chat_id)
                                                                resposta = 'Lembre-se de registrar a saída ao fim do seu horário.'
                                                                responder2(resposta, chat_id)
                                                            else:
                                                                resposta = f'Entrada já registrada anteriormente, se isso for um erro por favor entre em contato com o suporte'
                                                                responder2(resposta, chat_id)
                                                        except:
                                                            resposta = 'Você não possui horário a cumprir hoje. Caso queira realizar alterações nos seus horários, por favor entre em contato com a vice presidência.'
                                                            responder2(resposta, chat_id)
                                                except:
                                                    resposta = 'Me parece que você ainda não possui um cadastro, por favor envie o número referente ao seu nome da seguinte forma:\n/CAD [SEU NÚMERO]\nEx.: /CAD 21'
                                                    responder2(resposta, chat_id)
                                                    resposta = '1 - Arthur\n2 - Artur\n3 - Bia\n4 - Brmat\n5 - Bruna\n6 - Claudio\n7 - Eduardo\n8 - Ermesson\n9 - George\n10 - Gibs\n11 - Hudson\n12 - Isaac\n13 - Isabela\n14 - Isac\n15 - Jefao\n16 - Jhonatan\n17 - Julia\n18 - Levy\n19 - Lídice\n20 - Lourrenny\n21 - Lucas\n22 - Natan\n23 - Nosep\n24 - Ph1\n25 - Ph2\n26 - Rômulo\n27 - Samuel G\n28 - Samuel T\n29 - Yankara\n30 - Yanne\n31 - Yasmine\n32 - Ycaro'
                                                    responder2(resposta, chat_id)
                                            else:
                                                resposta = f'Erro ao registrar entrada, por favor entre em contato com o suporte'
                                                responder2(resposta, chat_id)
                                        elif codigo == None:
                                            resposta = f'Erro ao validar código, por favor entre em contato com o suporte'
                                            responder2(resposta, chat_id)
                                        else:
                                            resposta = f'Código inválido, por favor aguarde um momento e tente novamente'
                                            responder2(resposta, chat_id)
                                    except:
                                        resposta = '[Erro ao acessar código de verificação]\nPor favor entre em contato com o suporte'
                                        responder2(resposta, chat_id)

                                elif ('bps') in mensagem.lower():
                                    try:
                                        dia = mes = hora = min = codigo = 80
                                        ahai = code()
                                        dia = ahai[0]
                                        mes = ahai[1]
                                        hora = ahai[2]
                                        min = ahai[3]
                                        codigo = ahai[4]
                                        if len(mensagem.split()) != 2:
                                            resposta = 'Não foi possível realizar o registro, verifique a mensagem e tente novamente.'
                                            responder2(resposta, chat_id)
                                            resposta ='Para registrar sua saída na salinha digite: /BPS [CODIGO]\nEx.; /BPS 3987'
                                            responder2(resposta, chat_id)
                                        elif codigo == int(mensagem.split()[1]):
                                            if hora != 80:
                                                worksheet = sh.get_worksheet(33)
                                                codigos = worksheet.col_values(3)
                                                nomes = worksheet.col_values(2)
                                                try:
                                                    indexMap = dict((x, i) for i, x in enumerate(list(codigos)))
                                                    ind = indexMap[str(chat_id)]
                                                    #print(ind)
                                                    #print(list(nomes)[ind])
                                                    worksheet = sh.get_worksheet(ind)
                                                    if len(str(dia).strip()) == 1:
                                                        dia = f'0{dia}'
                                                    if len(str(mes).strip()) == 1:
                                                        mes = f'0{mes}'
                                                    data = f'{dia}/{mes}/2023'
                                                    try:
                                                        indexMap = dict((x, i) for i, x in enumerate(list(worksheet.col_values(1))))
                                                        ind2 = indexMap[str(data)]
                                                        if worksheet.cell(ind2+1, 3).value == 0 or worksheet.cell(ind2+1, 3).value == None:
                                                            worksheet.update_cell(ind2+1,3,f'{hora}:{min}')
                                                            resposta = f'Saída registrada às {hora}h e {min}min'
                                                            responder2(resposta, chat_id)
                                                        elif 1 == 1:
                                                            indexMap = dict((x, i) for i, x in enumerate(list(worksheet.col_values(11))))
                                                            ind2 = indexMap[str(data)]
                                                            if worksheet.cell(ind2+1, 13).value == 0 or worksheet.cell(ind2+1, 13).value == None:
                                                                worksheet.update_cell(ind2+1,13,f'{hora}:{min}')
                                                                resposta = f'Saída registrada às {hora}h e {min}min'
                                                                responder2(resposta, chat_id)
                                                            else:
                                                                resposta = f'Saída já registrada anteriormente, se isso for um erro por favor entre em contato com o suporte'
                                                                responder2(resposta, chat_id)
                                                        else:
                                                            resposta = f'Erro ao registrar saída, por favor entre em contato com o suporte'
                                                            responder2(resposta, chat_id)
                                                    except:
                                                        try:
                                                            indexMap = dict((x, i) for i, x in enumerate(list(worksheet.col_values(11))))
                                                            ind2 = indexMap[str(data)]
                                                            if worksheet.cell(ind2+1, 13).value == 0 or worksheet.cell(ind2+1, 13).value == None:
                                                                worksheet.update_cell(ind2+1,13,f'{hora}:{min}')
                                                                resposta = f'Saída registrada às {hora}h e {min}min'
                                                                responder2(resposta, chat_id)
                                                            else:
                                                                resposta = f'Saída já registrada anteriormente, se isso for um erro por favor entre em contato com o suporte'
                                                                responder2(resposta, chat_id)
                                                        except:
                                                            resposta = 'Você não possui horário a cumprir hoje. Caso queira realizar alterações nos seus horários, por favor entre em contato com algum membro da vice presidência.'
                                                            responder2(resposta, chat_id)
                                                except:
                                                    resposta = 'Me parece que você ainda não possui um cadastro, por favor envie o número referente ao seu nome da seguinte forma:\n/CAD [SEU NÚMERO]\nEx.: /CAD 21'
                                                    responder2(resposta, chat_id)
                                                    resposta = '1 - Arthur\n2 - Artur\n3 - Bia\n4 - Brmat\n5 - Bruna\n6 - Claudio\n7 - Eduardo\n8 - Ermesson\n9 - George\n10 - Gibs\n11 - Hudson\n12 - Isaac\n13 - Isabela\n14 - Isac\n15 - Jefao\n16 - Jhonatan\n17 - Julia\n18 - Levy\n19 - Lídice\n20 - Lourrenny\n21 - Lucas\n22 - Natan\n23 - Nosep\n24 - Ph1\n25 - Ph2\n26 - Rômulo\n27 - Samuel G\n28 - Samuel T\n29 - Yankara\n30 - Yanne\n31 - Yasmine\n32 - Ycaro'
                                                    responder2(resposta, chat_id)
                                            else:
                                                resposta = f'Erro ao registrar saída, por favor entre em contato com o suporte'
                                                responder2(resposta, chat_id)
                                        elif codigo == None:
                                            resposta = f'Erro ao validar código, por favor entre em contato com o suporte'
                                            responder2(resposta, chat_id)   
                                        else:
                                            resposta = f'Código inválido, por favor aguarde um momento e tente novamente'
                                            responder2(resposta, chat_id)
                                    except:
                                        resposta = '[Erro ao acessar código de verificação]\nPor favor entre em contato com o suporte'
                                        responder2(resposta, chat_id)
                                    
                                elif ('codigo') in mensagem.lower() or ('código') in mensagem.lower():
                                    resposta = 'Para obter o seu código de validação ligue o computador da salinha e localize o seguinte aplicativo na área de trabalho:'
                                    responder2(resposta, chat_id)
                                    try:
                                        responder3(chat_id)
                                    except:
                                        resposta = '[Erro ao enviar imagem]'
                                        responder2(resposta, chat_id)
                                    resposta = 'Após isso é só executá-lo e gerar o seu código ;)'
                                    responder2(resposta, chat_id)
                                    resposta = 'Obs.: A senha do computador é projetta123'
                                    responder2(resposta, chat_id)
                                    

                                else:
                                    resposta = 'Puts! Não reconheci o começo da mensagem. 😅\nSe precisar de ajuda, clica em /help ou /start'
                                    responder2(resposta, chat_id)
                except:
                    print('ihh')
                    try:
                        
                        chat_id = 1154633217
                        resposta = 'Reiniciei aq, viu'
                        responder2(resposta, chat_id)
                    except:
                        sleep(5)
                        print('loucura')
                    try:
                        worksheet = sh.get_worksheet(33)
                        worksheet.update_cell(2,5,"1")
                        worksheet.update_cell(2,6,update_id)
                        restart_program()
                    except:
                        restart_program()
        except:
            def restart_program():
                python = sys.executable
                os.execl(python, python, * sys.argv)
            sleep(5)
            print('antefinal')
            sys.exit()
                
    except:
        print('last')
        break
python = sys.executable
os.execl(python, python, * sys.argv)