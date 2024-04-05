from mentor import Mentor
from mentorando import Mentorando
from mentoria import Mentoria
from db_connector import DBConnector

db = DBConnector("mentorias.db")

#TESTANDO NOVO MENTOR
#novo_mentor = Mentor("Luiz Edu","www.testede link")
#novo_mentor.save(db.connect())
#print(novo_mentor.to_dict())

#TESTANDO NOVO MENTORANDO
#novo_mentorando = Mentorando("Caio","www.testedelink2")
#novo_mentorando.save(db.connect())
#print(novo_mentorando.to_dict())

#TESTANDO NOVA MENTORIA
#nova_mentoria = Mentoria(novo_mentor,novo_mentorando,"2023-08-11")
#nova_mentoria.save(db.connect())
#print(nova_mentoria.to_dict())

#print(Mentor.get_by_id(1, db.connect()).to_dict())

#print(Mentor.get_all(db.connect()))

print(Mentor.get_by_id(1, db.connect()).to_dict())
print(Mentor.get_all(db.connect()))

print(Mentorando.get_by_id(1, db.connect()).to_dict())
print(Mentorando.get_all(db.connect()))

print(Mentoria.get_by_id(1, db.connect()).to_dict())
print(Mentoria.get_all(db.connect()))