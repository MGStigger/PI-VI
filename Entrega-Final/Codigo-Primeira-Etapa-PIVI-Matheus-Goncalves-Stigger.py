#AUTOR: MATHEUS GONÇALVES STIGGER

#INÍCIO

#IMPORTA AS BIBLIOTECAS
import time
import psutil
from datetime import datetime
from pytz import timezone

#IMPORTA O MÓDULO MYSQL CONNECTOR PYTHON PARA O USO DE SUA API PARA CONECTAR AO MYSQL
import mysql.connector

#O MÉTODO CONNECT ESTABELECE UMA CONEXÃO COM O BANCO DE DADOS MYSQL
mydb = mysql.connector.connect(
	host = "localhost", 
	user = "root", 
	password = "201811057", 
	database = "mydatabase")

#CURSOR É UM OBJETO QUE PERMITE REALIZAR OPERAÇÕES NO BANCO DE DADOS
mycursor = mydb.cursor()

while True:

	#DATA E HORA
	data_e_hora_atuais = datetime.now()
	fuso_horario = timezone('America/Sao_Paulo')
	data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
	data = data_e_hora_sao_paulo.strftime('%Y-%m-%d')
	hora = data_e_hora_sao_paulo.strftime('%H:%M:%S')

	#RETORNA UM FLOAT QUE REPRESENTA A UTILIZAÇÃO ATUAL DA CPU DE TODO O SISTEMA COMO UMA PORCENTAGEM
	cpu_percent = psutil.cpu_percent(interval = 0.1, percpu = False)
	
	#RETORNA A FREQUÊNCIA DA CPU, INCLUINDO A FREQUÊNCIA ATUAL EXPRESSA EM MHZ
	cpu_mhz = psutil.cpu_freq(percpu = False)[0]
	
	#RETORNA A TEMPERATURA MAIS ALTA ENTRE OS NÚCLEOS DA CPU
	temps = psutil.sensors_temperatures(fahrenheit=False)
	name = list(temps.keys())
	cpu_temp = temps[name[0]][0][1]
	
	#RETORNA ESTATÍSTICAS SOBRE O USO DE MEMÓRIA DO SISTEMA, INCLUINDO O CAMPO PERCENTUAL
	memory_percent = psutil.virtual_memory()[2]
	
	#RETORNA ESTATÍSTICAS DE USO DE DISCO INCLUINDO A PORCENTAGEM DE USO
	disk_percent = psutil.disk_usage('/')[3]
	
	#RETORNA AS INFORMAÇÕES DE STATUS DA BATERIA, INCLUINDO A PORCENTAGEM
	battery_percent = psutil.sensors_battery()[0]
	
	#EXECUÇÃO DAS CONSULTAS SQL EM PYTHON
	sql_zero = "INSERT INTO datahora (data, hora) VALUES (%s, %s)"
	sql_datahora = (data, hora)
	mycursor.execute(sql_zero, sql_datahora)
	
	sql_um = "INSERT INTO cpu (cpu_percent, cpu_mhz, cpu_temp) VALUES (%s, %s, %s)"
	sql_cpu = (cpu_percent, cpu_mhz, cpu_temp)
	mycursor.execute(sql_um, sql_cpu)
	
	sql_dois = "INSERT INTO memory (memory_percent) VALUES (%s)"
	sql_memory = (memory_percent)
	mycursor.execute(sql_dois, (sql_memory,))
	
	sql_tres = "INSERT INTO disk (disk_percent) VALUES (%s)"
	sql_disk = (disk_percent)
	mycursor.execute(sql_tres, (sql_disk,))
	
	sql_quatro = "INSERT INTO battery (battery_percent) VALUES (%s)"
	sql_battery = (battery_percent)
	mycursor.execute(sql_quatro, (sql_battery,))
	
	#CONFIRMA AS ALTERAÇÕES NO BANCO DE DADOS
	mydb.commit()
	
	#ADICIONA UM ATRASO NA EXECUÇÃO DO PROGRAMA EM SEGUNDOS
	time.sleep(120)

#FIM
