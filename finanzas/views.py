def landing(request):
	return render(request, 'finanzas/landing.html')

def perfil(request):
	return render(request, 'finanzas/perfil.html')
from django.shortcuts import render, redirect
from .models import Ingreso, Gasto, Categoria

def dashboard(request):
	ingresos = Ingreso.objects.all()
	gastos = Gasto.objects.all()
	total_ingresos = sum(i.cantidad for i in ingresos)
	total_gastos = sum(g.cantidad for g in gastos)
	saldo = total_ingresos - total_gastos
	return render(request, 'finanzas/dashboard.html', {
		'ingresos': ingresos,
		'gastos': gastos,
		'total_ingresos': total_ingresos,
		'total_gastos': total_gastos,
		'saldo': saldo,
	})

def ingresos(request):
	mensaje = None
	if request.method == 'POST':
		cantidad = request.POST['cantidad']
		categoria_id = request.POST['categoria']
		descripcion = request.POST.get('descripcion', '')
		Ingreso.objects.create(
			cantidad=cantidad,
			categoria_id=categoria_id,
			descripcion=descripcion
		)
		mensaje = 'Ingreso registrado exitosamente.'
	categorias = Categoria.objects.filter(tipo='ingreso')
	ingresos = Ingreso.objects.all().order_by('-fecha')
	return render(request, 'finanzas/ingresos.html', {'ingresos': ingresos, 'categorias': categorias, 'mensaje': mensaje})

def gastos(request):
	mensaje = None
	if request.method == 'POST':
		cantidad = request.POST['cantidad']
		categoria_id = request.POST['categoria']
		descripcion = request.POST.get('descripcion', '')
		Gasto.objects.create(
			cantidad=cantidad,
			categoria_id=categoria_id,
			descripcion=descripcion
		)
		mensaje = 'Gasto registrado exitosamente.'
	categorias = Categoria.objects.filter(tipo='gasto')
	gastos = Gasto.objects.all().order_by('-fecha')
	return render(request, 'finanzas/gastos.html', {'gastos': gastos, 'categorias': categorias, 'mensaje': mensaje})

def categorias(request):
	if request.method == 'POST':
		nombre = request.POST['nombre']
		tipo = request.POST['tipo']
		Categoria.objects.create(nombre=nombre, tipo=tipo)
		return redirect('categorias')
	categorias = Categoria.objects.all()
	return render(request, 'finanzas/categorias.html', {'categorias': categorias})

def informe(request):
	ingresos = Ingreso.objects.all()
	gastos = Gasto.objects.all()
	categorias = Categoria.objects.all()
	resumen = {}
	for cat in categorias:
		if cat.tipo == 'ingreso':
			total = sum(i.cantidad for i in ingresos if i.categoria == cat)
		else:
			total = sum(g.cantidad for g in gastos if g.categoria == cat)
		resumen[cat.nombre] = {'tipo': cat.tipo, 'total': total}
	return render(request, 'finanzas/informe.html', {'resumen': resumen})
