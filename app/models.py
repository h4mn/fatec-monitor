from django.db import models

# Create your models here.

class Disciplina(models.Model):
    __tablename__ = 'disciplinas'
    id = models.AutoField(primary_key=True)
    codigo = models.TextField(max_length=15)
    descricao = models.TextField(max_length=50)
    faltas = models.IntegerField()
    frequencias = models.FloatField()
    media = models.FloatField()
    importado = models.DateField(auto_now_add=True)
    #avaliacoes = relationship("Avaliacao", back_populates="fk_disciplina")

    def __repr__(self):
        return '<Disciplina(id={}, codigo={}, descricao={}, ...)>'.format(
            self.id, self.codigo, self.descricao)
    
    def __str__(self) -> str:
        return self.descricao

class Avaliacao(models.Model):
    __tablename__ = 'avaliacoes'
    id = models.AutoField(primary_key=True)
    descricao = models.TextField(max_length=50)
    data = models.DateField()
    nota = models.FloatField()
    importado = models.DateField(auto_now_add=True)
    fk_disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)

    def __repr__(self):
        return '<Avaliacao(id={}, descricao={}, fk_disciplina={}...)>'.format(
            self.id, self.descricao, self.fk_disciplina)
    
    def __str__(self) -> str:
        return f'{self.descricao} - {self.nota}'
