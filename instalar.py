import sqlite3
connexion = sqlite3.connect("rider_express.db")
cursor = connexion-cursor()
#USuario
cursor.execute("DROP TABLE IF EXISTS Usuario ()")
cursor.execute("CREATE TABLE Usuario ()")
#Rider
cursor.execute("DROP TABLE IF EXISTS Rider ()")
cursor.execute("CREATE TABLE Riders (id, name, id_vehiculo)")
#Restaurante
cursor.execute("DROP TABLE IF EXISTS Restaurante ()")

#Platos
cursor.execute("CREATE TABLE Platos ()")
cursor.execute("CREATE TABLE Pedidos ()")
cursor.execute("CREATE TABLE Restaurante ()")
cursor.execute("CREATE TABLE Vehiculo ()")
cursor.execute("CREATE TABLE Categoria_Restaurante ()")
cursor.execute("CREATE TABLE Pedido_Plato ()")