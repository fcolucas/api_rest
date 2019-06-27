import json, requests

key = input("Digite a chave de acesso: ")

if(key == "XA5V3DBKLNE1Z6ZG"):
        response = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=^BVSP&apikey=" + key)
        cotacoes = json.loads(response.content)
        diario = cotacoes['Time Series (Daily)']
        datas = list(diario.keys())
        #print (datas)
        for d in datas[:10]:
                print("Data: " + d)
                print("Abertura: " + diario[d]['1. open'])
                print("Máximo: "+ diario[d]['2. high'])
                print("Mínimo: "+ diario[d]['3. low'])
                print("Fechamento: "+ diario[d]['4. close'])
                print("Volume: "+ diario[d]['5. volume'])
                print ("\n")
                

else:
	print ("Código de acesso inválido!")
