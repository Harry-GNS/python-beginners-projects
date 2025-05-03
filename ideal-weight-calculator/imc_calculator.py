def calcular_imc(peso, altura):
    """Calcula el Índice de Masa Corporal"""
    return peso / (altura ** 2)

def clasificar_peso(imc):
    """Devuelve la categoría según el IMC"""
    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"

def main():
    print("Calculadora de IMC y Peso Ideal")
    print("-------------------------------")
    
    try:
        peso = float(input("Ingrese su peso en kg: "))
        altura = float(input("Ingrese su altura en metros: "))
        
        imc = calcular_imc(peso, altura)
        categoria = clasificar_peso(imc)
        
        print(f"\nIMC: {imc:.1f}")
        print(f"Categoría: {categoria}")
        
        # Mostrar rango de peso ideal
        peso_min = 18.5 * (altura ** 2)
        peso_max = 24.9 * (altura ** 2)
        print(f"\nPara tu altura ({altura}m), el peso ideal sería entre {peso_min:.1f}kg y {peso_max:.1f}kg")
    
    except ValueError:
        print("\nError: Ingresa valores numéricos válidos")

if __name__ == "__main__":
    main()