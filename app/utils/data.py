import sqlalchemy
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey

path = 'data\\grade.db'
engine = sqlalchemy.create_engine(f'sqlite:///{path}', echo=True)

Base = declarative_base()
    
class Disciplina(Base):
    __tablename__ = 'disciplinas'
    id = Column(Integer, primary_key=True)
    codigo = Column(String(10))
    descricao = Column(String(50))
    faltas = Column(Integer)
    frequencias = Column(Float)
    media = Column(Float)
    avaliacoes = relationship("Avaliacao", back_populates="fk_disciplina")

    def __repr__(self):
        return '<Disciplina(id={}, codigo={}, descricao={}, ...)>'.format(
            self.id, self.codigo, self.descricao)

class Avaliacao(Base):
    __tablename__ = 'avaliacoes'
    id = Column(Integer, primary_key=True)
    descricao = Column(String(50))
    data = Column(Date)
    nota = Column(Float)
    fk_disciplina = Column(Integer, ForeignKey('disciplinas.id'))

    def __repr__(self):
        return '<Avaliacao(id={}, descricao={}, fk_disciplina={}...)>'.format(
            self.id, self.descricao, self.fk_disciplina)

Base.metadata.create_all(engine)