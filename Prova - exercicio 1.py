primeiro= int(input ("escolha um valor"))
segundo= int(input ("escolha um valor"))
terceiro= int(input ("escolha um valor"))
if primeiro > segundo and primeiro > terceiro:
    maior= primeiro
elif segundo > primeiro and segundo > terceiro:
    maior= segundo
elif terceiro > primeiro and terceiro > segundo:
    maior= terceiro
    print( f"o maior numero digitado foi {maior}")