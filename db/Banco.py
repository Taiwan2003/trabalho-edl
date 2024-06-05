import sqlite3
from datetime import datetime

#fase de desenvolvimento,sujeito a alteracoes 

Saves=sqlite3.connect('saves.db')
cursor=Saves.cursor()

cursor.execute('''
     CREATE TABLE IF NOT EXISTS saves(
          save_id INTEGER PRIMARY KEY AUTOINCREMENT,
          user_name TEXT NOT NULL,
          game_state INTEGER NOT NULL,
          timestamp TEXT NOT NULL

     )
''')

Saves.commit()


def salvar(user_name,game_state):
    cursor.execute("SELECT COUNT(*) FROM saves")
    count=cursor.fetchone()[0]
    if count<3:
        timestamp=datetime.now().isoformat()
        cursor.execute("INSERT INTO saves (user_name,game_state,timestamp) VALUES(?,?,?)",(user_name,game_state,timestamp))
        Saves.commit()
        return True
    else:
        return False

def lista_saves_strings():
    cursor.execute("SELECT * FROM saves")
    lista=cursor.fetchall()
    nova_lista=[]
    for i in lista:
        nome="Nome: "+i[1]+"  "
        fase="Fase: "+str(i[2])+"  "
        data="Data: "+i[3][:10]
        aux=nome+fase+data
        nova_lista.append(aux)
    return nova_lista

def lista_saves():
    cursor.execute("SELECT * FROM  saves")
    lista=cursor.fetchall()
    return lista
    

def deletar(tup):
    username=tup[1]
    cursor.execute("DELETE FROM saves WHERE user_name=?",[username])
    Saves.commit()
    return True
    
print(lista_saves())
