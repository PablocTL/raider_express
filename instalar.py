import sqlite3
connexion = sqlite3.connect("rider_express.db")
cursor = connexion-cursor()

cursor.execute("CREATE TABLE Usuario ()")
cursor.execute("CREATE TABLE Platos ()")
cursor.execute("CREATE TABLE Pedidos ()")
cursor.execute("CREATE TABLE Riders ()")
cursor.execute("CREATE TABLE Restaurante ()")
cursor.execute("CREATE TABLE Vehiculo ()")
cursor.execute("CREATE TABLE Categoria_Restaurante ()")
cursor.execute("CREATE TABLE Pedido_Plato ()")