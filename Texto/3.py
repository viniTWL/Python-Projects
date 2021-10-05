#detectar se a cidade tem santo no começo
cid = str(input('Em que cidade você nasceu?')).strip()
print(cid[:5].upper() == 'SANTO') #entre colchetes :5 para ver se as 5 primeiras letras são == SANTO, utilizei upper para não dar erro


