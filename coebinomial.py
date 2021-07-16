numero = int(input("Digite a quantidade total de elementos: "))
numeroDois = int(input("Digite a quantidade de elementos por conjuntos: "))
numeroTres = numero - numeroDois



resul = 1


if numero == 1:
         resul = 1

if numero == 0:
         resul = 1

while (numero != 0) and (numero != 1) :
          parte = numero - 1
          resul = resul*numero*parte
          numero = parte - 1


resulDois = 1


if numeroDois == 1:
         resulDois = 1

if numeroDois == 0:
         resulDois = 1

while (numeroDois != 0) and (numeroDois != 1) :
          parteDois = numeroDois - 1
          resulDois = resulDois*numeroDois*parteDois
          numeroDois = parteDois - 1



resulTres = 1

if numeroTres == 1:
         resulTres = 1

if numeroTres == 0:
         resulTres = 1

while (numeroTres != 0) and (numeroTres != 1) :
          parteTres = numeroTres - 1
          resulTres = resulTres*numeroTres*parteTres
          numeroTres = parteTres - 1

           
total =  resul / (resulDois * resulTres)
  
if total != 1:
      print("Há", total, "conjuntos possíveis.")
else: 
      print("Há", total, "conjunto possível.")
