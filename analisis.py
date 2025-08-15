import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def main():
    # Leer el archivo CSV
    # Nota: el separador es punto y coma (;) en lugar de coma
    try:
        df = pd.read_csv('table.csv', sep=';', header=None, names=['columna1', 'columna2'])
        print("Datos cargados exitosamente:")
        print(df.head())
        print("\n" + "="*50)
    except FileNotFoundError:
        print("Error: No se encontró el archivo 'table.csv'")
        return
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return

    # Calcular estadísticas descriptivas
    print("ESTADÍSTICAS DESCRIPTIVAS:")
    print("="*50)
    
    for columna in df.columns:
        print(f"\n{columna.upper()}:")
        print(f"  Media: {df[columna].mean():.2f}")
        print(f"  Mediana: {df[columna].median():.2f}")
        print(f"  Desviación estándar: {df[columna].std():.2f}")
        print(f"  Mínimo: {df[columna].min()}")
        print(f"  Máximo: {df[columna].max()}")
        print(f"  Rango: {df[columna].max() - df[columna].min()}")

    # Calcular correlación entre las columnas
    correlacion = df['columna1'].corr(df['columna2'])
    print(f"\nCorrelación entre columnas: {correlacion:.3f}")

    # Crear gráfica de dispersión
    plt.figure(figsize=(10, 6))
    plt.scatter(df['columna1'], df['columna2'], alpha=0.7, s=100, c='blue', edgecolors='black')
    
    # Añadir línea de tendencia
    z = np.polyfit(df['columna1'], df['columna2'], 1)
    p = np.poly1d(z)
    plt.plot(df['columna1'], p(df['columna1']), "r--", alpha=0.8, linewidth=2)
    
    # Personalizar la gráfica
    plt.title('Gráfica de Dispersión: Columna 1 vs Columna 2', fontsize=14, fontweight='bold')
    plt.xlabel('Columna 1', fontsize=12)
    plt.ylabel('Columna 2', fontsize=12)
    plt.grid(True, alpha=0.3)
    
    # Añadir anotación con la correlación
    plt.text(0.05, 0.95, f'Correlación: {correlacion:.3f}', 
             transform=plt.gca().transAxes, fontsize=10, 
             bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow", alpha=0.7))
    
    # Ajustar los límites de los ejes
    plt.xlim(df['columna1'].min() - 0.5, df['columna1'].max() + 0.5)
    plt.ylim(df['columna2'].min() - 0.5, df['columna2'].max() + 0.5)
    
    # Mostrar la gráfica
    plt.tight_layout()
    plt.show()
    
    print("\n" + "="*50)
    print("¡Análisis completado! La gráfica se ha abierto en una ventana externa.")

if __name__ == "__main__":
    main()
