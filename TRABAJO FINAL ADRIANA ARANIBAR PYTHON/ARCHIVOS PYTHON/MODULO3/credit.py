def prob5(numero):

	AMEX = [34, 37]
	MASTERCARD = [51, 52, 53, 54 , 55]

	def convert(numero2):
		lista = [ int(x) for x in list(str(numero2)) ]
		return sum(lista)

	num = str(numero)
	size = len(num)
	suma = 0
	for i in range(size-2, -1, -2):
		suma += convert(int(num[i])*2)
	for i in range(size-1, -1, -2):
		suma += int(num[i])

	if suma % 10 == 0:
		if int(num[0]) == 4:
			return "VISA"
		elif int(num[0:2]) in AMEX:
			return "AMEX"
		elif int(num[0:2]) in MASTERCARD:
			return "MASTERCARD"
	return "INVALID"

numTarjeta = int(input("Number: "))
print(prob5(numTarjeta))