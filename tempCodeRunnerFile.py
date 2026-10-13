while True: 
    print ("=== Cadastro de Ativos ===")
    localização_ativo = input ("Insira o ip do ativo de TI :")
    ID_ativo = input ("Insira o ID do ativo de TI:")
    responsável_ativo = input ("Insira o responsável pelo ativo:")
    
    print(f"Cadastro realizado com sucesso, confirme as informações : {localização_ativo},{ID_ativo}{responsável_ativo}")
    break