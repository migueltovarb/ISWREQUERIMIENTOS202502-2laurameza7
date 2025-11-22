from django.db import models

class Categoria(models.Model):
	nombre = models.CharField(max_length=50)
	tipo = models.CharField(max_length=10, choices=[('ingreso', 'Ingreso'), ('gasto', 'Gasto')])

	def __str__(self):
		return f"{self.nombre} ({self.tipo})"

class Ingreso(models.Model):
	cantidad = models.DecimalField(max_digits=10, decimal_places=2)
	categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, limit_choices_to={'tipo': 'ingreso'})
	descripcion = models.CharField(max_length=200, blank=True)
	fecha = models.DateField(auto_now_add=True)

	def __str__(self):
		return f"Ingreso: {self.cantidad} - {self.categoria.nombre}"

class Gasto(models.Model):
	cantidad = models.DecimalField(max_digits=10, decimal_places=2)
	categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, limit_choices_to={'tipo': 'gasto'})
	descripcion = models.CharField(max_length=200, blank=True)
	fecha = models.DateField(auto_now_add=True)

	def __str__(self):
		return f"Gasto: {self.cantidad} - {self.categoria.nombre}"
