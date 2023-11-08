import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

class Trapecio:

    def __init__(self, a=None, b=None, n=999):
        self.n = n
        self.f = None
        self.a = a
        self.b = b
        self.deltax = None
        self.lista_funciones = []
        self.resultado = None
        self.x = sp.Symbol('x')

    def generar_resultado(self):
        self.generar_diferencial()

        for i in range(self.n + 1):
            xi = self.a + (i * self.deltax)
            fxi = self.f.subs(sp.Symbol('x'), xi)
            
            if (i in [0, self.n]):
                self.lista_funciones.append(fxi)
            
            else:
                self.lista_funciones.append(fxi*2)

        self.resultado = ((self.deltax) / 2) * sum(self.lista_funciones)

    def generar_diferencial(self):
        self.deltax = (self.b - self.a) / self.n

    def set_f(self, funcion):
        self.f = sp.sympify(funcion)

    def ver(self):
        print(f"""
        [-* Resultado Método del Trapecio *-]
        (Tipo {type(self)})
        -> ∫({self.f})dx
        n = {self.n}
        intervalo = [{self.a},{self.b}]
        Δx = {self.deltax}
        resultado = {self.resultado}
        """)

    def plot_funcion(self):
        if isinstance(self, Trapecio):
            x_vals = np.linspace(self.a, self.b, 1000)
            y_vals = [self.f.subs(sp.Symbol('x'), val) for val in x_vals]

            subintervalos = np.linspace(self.a, self.b, self.n+1)

            for i in range(self.n):
                x_trapecio = [subintervalos[i], subintervalos[i], subintervalos[i+1], subintervalos[i+1], subintervalos[i]]
                y_trapecio = [0, self.f.subs(sp.Symbol('x'), subintervalos[i]), self.f.subs(sp.Symbol('x'), subintervalos[i+1]), 0, 0]
                plt.fill(x_trapecio, y_trapecio, 'b', alpha=0.5)

            plt.plot(x_vals, y_vals, label=f'f(x) = {self.f}')
            plt.xlabel('x')
            plt.ylabel('f(x)')
            plt.title('Gráfico de la Función con Trapecios')
            plt.legend()

            plt.text(0.05, 0.8, f"Resultado: {self.resultado}", transform=plt.gca().transAxes, bbox=dict(facecolor='white', alpha=0.5))

            plt.show()




class Simpson13:

    def __init__(self, a=None, b=None, n=999):
        self.n = n
        self.f = None
        self.a = a
        self.b = b
        self.deltax = None
        self.lista_funciones = []
        self.resultado = None
        self.x = sp.Symbol('x')

    def verificar_n(self):
        if self.n % 2 != 0:
            self.n += 1
            self.verificar_n()

    def generar_resultado(self):
        self.verificar_n()
        self.generar_diferencial()
        marcador = 4

        for i in range(self.n + 1):
            xi = self.a + (i * self.deltax)
            fxi = self.f.subs(sp.Symbol('x'), xi)
            
            if (i in [0, self.n]):
                self.lista_funciones.append(fxi)
            
            elif (marcador == 4):
                self.lista_funciones.append(fxi*4)
                marcador = 2
            elif (marcador == 2):
                self.lista_funciones.append(fxi*2)
                marcador = 4

        self.resultado = (1/3) * (self.deltax) * sum(self.lista_funciones)

    def generar_diferencial(self):
        self.deltax = (self.b - self.a) / self.n

    def set_f(self, funcion):
        self.f = sp.sympify(funcion)


    def ver(self):
        print(f"""
        [-* Resultado Método de Simpson 1/3 *-]
        (Tipo {type(self)})
        -> ∫({self.f})dx
        n = {self.n}
        intervalo = [{self.a},{self.b}]
        Δx = {self.deltax}
        resultado = {self.resultado}
        """)

    def graficar_simpson_tercio(self):
        x_vals = np.linspace(self.a, self.b, 1000)
        y_vals = [self.f.subs(sp.Symbol('x'), val) for val in x_vals]

        subintervalos = np.linspace(self.a, self.b, self.n+1)

        for i in range(self.n):
            x_figura = [subintervalos[i], subintervalos[i], subintervalos[i+1], subintervalos[i+1], subintervalos[i]]
            y_figura = [0, self.f.subs(sp.Symbol('x'), subintervalos[i]), self.f.subs(sp.Symbol('x'), subintervalos[i+1]), 0, 0]
            plt.fill(x_figura, y_figura, 'b', alpha=0.5)

        plt.plot(x_vals, y_vals, label=f'f(x) = {self.f}')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.title('Gráfico de la Función con Simpson 1/3')
        plt.legend()

        plt.text(0.05, 0.8, f"Resultado: {self.resultado}", transform=plt.gca().transAxes, bbox=dict(facecolor='white', alpha=0.5))

        plt.show()


class Simpson38:

    def __init__(self, a=None, b=None, n=999):
        self.n = n
        self.f = None
        self.a = a
        self.b = b
        self.deltax = None
        self.lista_funciones = []
        self.resultado = None
        self.x = sp.Symbol('x')

    def verificar_n(self):
        if self.n % 3 != 0:
            self.n += 1
            self.verificar_n()

    def generar_resultado(self):
        self.verificar_n()
        self.generar_diferencial()

        for i in range(self.n + 1):
            xi = self.a + (i * self.deltax)
            fxi = self.f.subs(self.x, xi)

            if (i % 3 == 0):
                fxi *= 2

            else:
                fxi *= 3

            self.lista_funciones.append(fxi)


        self.resultado = (3/8 ) * self.deltax * sum(self.lista_funciones)
        return self.resultado

    def generar_diferencial(self):
        self.deltax = (self.b - self.a) / self.n

    def set_f(self, funcion):
        self.f = sp.sympify(funcion)

    def ver(self):
        print(f"""
        [-* Resultado Método de Simpson 3/8 *-]
        (Tipo {type(self)})
        -> ∫({self.f})dx
        n = {self.n}
        intervalo = [{self.a},{self.b}]
        Δx = {self.deltax}
        resultado = {self.resultado}
        """)

    def graficar_simpson_tres_octavos(self):
        x_vals = np.linspace(self.a, self.b, 1000)
        y_vals = [self.f.subs(sp.Symbol('x'), val) for val in x_vals]

        subintervalos = np.linspace(self.a, self.b, self.n+1)

        for i in range(self.n):
            x_fill = [subintervalos[i], subintervalos[i], subintervalos[i+1], subintervalos[i+1], subintervalos[i]]
            y_fill = [0, self.f.subs(sp.Symbol('x'), subintervalos[i]), self.f.subs(sp.Symbol('x'), subintervalos[i+1]), 0, 0]
            plt.fill(x_fill, y_fill, 'b', alpha=0.5)

        plt.plot(x_vals, y_vals, label=f'f(x) = {self.f}')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.title('Gráfico de la Función con Simpson 3/8')
        plt.legend()

        plt.text(0.05, 0.8, f"Resultado: {self.resultado}", transform=plt.gca().transAxes, bbox=dict(facecolor='white', alpha=0.5))

        plt.show()


x = sp.Symbol('x')



f1 = Simpson38(0, 3, 10)
f1.set_f((sp.E**x**2))
f1.generar_resultado()
f1.ver()
f1.graficar_simpson_tres_octavos()