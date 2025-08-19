import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo CSV con punto y coma como separador
df = pd.read_csv('./analizarventas/ventas.csv', sep=';')

# Convertir la columna fecha a datetime
df['fecha'] = pd.to_datetime(df['fecha'])
df['mes'] = df['fecha'].dt.to_period('M')

# Calcular ingresos
df['ingreso'] = df['cantidad_vendida'] * df['precio']

# Análisis por producto
ventas_por_producto = df.groupby('producto').agg({
    'cantidad_vendida': 'sum',
    'ingreso': 'sum'
}).round(2)

# Encontrar productos destacados
mas_vendido = ventas_por_producto['cantidad_vendida'].idxmax()
mayor_ingreso = ventas_por_producto['ingreso'].idxmax()

# Mostrar resultados
print("\n=== Análisis de Ventas ===\n")
print(f"Producto más vendido: {mas_vendido}")
print(f"Unidades vendidas: {ventas_por_producto.loc[mas_vendido, 'cantidad_vendida']}")
print(f"\nProducto con mayor ingreso: {mayor_ingreso}")
print(f"Ingreso total: ${ventas_por_producto.loc[mayor_ingreso, 'ingreso']:,.0f}")

# Ventas mensuales
ventas_mensuales = df.groupby('mes')['ingreso'].sum()
print(f"\nVentas por mes:\n{ventas_mensuales.apply(lambda x: f'${x:,.0f}')}")

# Gráfico de ventas mensuales
plt.figure(figsize=(10, 5))
ventas_mensuales.plot(kind='bar')
plt.title('Ventas Mensuales')
plt.xlabel('Mes')
plt.ylabel('Ventas Totales ($)')
plt.tight_layout()
plt.savefig('ventas_mensuales.png')
plt.close()

# Gráfico de top 5 productos
top5 = ventas_por_producto.nlargest(5, 'ingreso')
plt.figure(figsize=(12, 6))
plt.bar(top5.index, top5['ingreso'])
plt.title('Top 5 Productos por Ingreso')
plt.xlabel('Producto')
plt.ylabel('Ingreso Total ($)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('top5_productos.png')
plt.close()