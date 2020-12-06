CREATE TABLE datahora (
	id SMALLINT PRIMARY KEY AUTO_INCREMENT,
	data DATE,
    hora TIME
) AUTO_INCREMENT = 1;

CREATE TABLE cpu (
	id SMALLINT PRIMARY KEY AUTO_INCREMENT,
	cpu_percent DECIMAL(3,1),
    cpu_mhz DECIMAL(4,0),
    cpu_temp DECIMAL(3,1)
) AUTO_INCREMENT = 1;

CREATE TABLE memory (
	id SMALLINT PRIMARY KEY AUTO_INCREMENT,
    memory_percent DECIMAL(3,1)
) AUTO_INCREMENT = 1;

CREATE TABLE disk (
	id SMALLINT PRIMARY KEY AUTO_INCREMENT,
    disk_percent DECIMAL(3,1)
) AUTO_INCREMENT = 1;

CREATE TABLE battery (
	id SMALLINT PRIMARY KEY AUTO_INCREMENT,
    battery_percent DECIMAL(3,0)
) AUTO_INCREMENT = 1;

SELECT * FROM mydatabase.datahora;
SELECT * FROM mydatabase.cpu;
SELECT * FROM mydatabase.memory;
SELECT * FROM mydatabase.disk;
SELECT * FROM mydatabase.battery;

SELECT  CONCAT(data) AS 'DATA',
		CONCAT(hora) AS 'HORA',
        CONCAT(cpu_percent, ' %') AS 'CPU (%)',
        CONCAT(cpu_mhz, ' MHZ') AS 'CPU (MHZ)',
        CONCAT(cpu_temp, ' °C') AS 'CPU (°C)',
        CONCAT(memory_percent, ' %') AS 'MEMÓRIA (%)',
        CONCAT(disk_percent, ' %') AS 'DISCO (%)',
        CONCAT(battery_percent, ' %') AS 'BATERIA (%)'
        
FROM mydatabase.datahora 
INNER JOIN mydatabase.cpu ON mydatabase.datahora.id = mydatabase.cpu.id 
INNER JOIN mydatabase.memory ON mydatabase.datahora.id = mydatabase.memory.id
INNER JOIN mydatabase.disk ON mydatabase.datahora.id = mydatabase.disk.id
INNER JOIN mydatabase.battery ON mydatabase.datahora.id = mydatabase.battery.id;

SELECT datahora.data, cpu.cpu_percent FROM mydatabase.datahora, mydatabase.cpu 
WHERE datahora.id = cpu.id 
AND cpu.cpu_percent < 20 OR cpu.cpu_percent > 80;

SELECT dh.data, dh.hora, b.battery_percent FROM datahora AS dh
INNER JOIN battery AS b ON dh.id = b.id 
WHERE b.battery_percent <= 25;

SELECT datahora.data, MIN(cpu.cpu_mhz) 
FROM datahora, cpu 
GROUP BY datahora.data;

SELECT datahora.data, MAX(cpu.cpu_temp)
FROM datahora, cpu
GROUP BY datahora.data 
ORDER BY datahora.data DESC;