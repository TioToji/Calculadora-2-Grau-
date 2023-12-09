from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.label import Label
import cmath

Window.size = (400, 600) #Definição do tamanho da janela do App
Builder.load_file("interface.kv") #Arquivo interface.kv, definições da interface gráfica

#Classe que gerencia as outras telas
class GerenciaTelas(ScreenManager):
    pass
#Primeira tela

class TelaInicio(Screen):
    #Método para limpar os Displays
    def limpaDisplay(self):
        self.ids.a.text = ''
        self.ids.b.text = ''
        self.ids.c.text = '' 
        
#Segunda tela
class ResultTela(Screen):
    #Método para limpar a tela de respostas
    def limparScroll(self):
        self.ids.result_label.text = ''
        
    #Método para calcular a equação
    def calcular(self, a, b, c):
        try:    
            try:
                a, b, c = float(a), float(b), float(c)
            #Erro por clicar no botão de calcular com os displays vazios
            except ValueError:
                popup = Popup(title='Erro 0x00',
                            content=Label(text='Por favor, insira números válidos.'),
                            size_hint=(None, None), size=(300, 180))
                popup.open()
                return
            
            if a == 0: #Se o coeficiente a for zero, mostrar um popup de erro
                popup = Popup(title="Erro 0x01", 
                              content=Label(text="O coeficiente (a) não pode ser zero"),
                              size_hint=(None, None), size=(300, 180))
                popup.open()
                return
            
            d = (b**2) - (4*a*c)
            if d < 0: #Condição 1: Se o delta for negativo, não há raízes reais
                x1 = (-b-cmath.sqrt(d))/(2*a)
                x2 = (-b+cmath.sqrt(d))/(2*a)
                self.ids.result_label.text += '\n'
                self.ids.result_label.text += f'Equação: {a}x² + {b}x + {c} = 0\n'
                self.ids.result_label.text += '\n'
                self.ids.result_label.text += f'Δ: b² - 4 * a * c =\n'
                self.ids.result_label.text += f'Δ: {b}² - 4*{a}*{c} = {d}\n'
                self.ids.result_label.text += '\n'
                self.ids.result_label.text += f'x = -{b} ± √{d} / 2*{a}\n'
                self.ids.result_label.text += '\n'
                self.ids.result_label.text += f"x¹= {x1}\n"
                self.ids.result_label.text += f"x² = {x2}\n"
                popup = Popup(title="Erro 0x02", 
                              content=Label(text="Delta é negativo, não há raizes reais"),
                              size_hint=(None, None), size=(300, 180))
                popup.open()
            
            elif d == 0: #Condição 2: Se o delta for zero, há uma raiz real
                x1 = (-b + cmath.sqrt(d))/(2*a)
                x2 = x1
                self.ids.result_label.text += '\n'
                self.ids.result_label.text += f'Equação: {a}x² + {b}x + {c} = 0\n'
                self.ids.result_label.text += '\n'
                self.ids.result_label.text += f'Δ: b² - 4 * a * c =\n'
                self.ids.result_label.text += f'Δ: {b}² - 4*{a}*{c} = {d}\n'
                self.ids.result_label.text += '\n'
                self.ids.result_label.text += f'x = -{b} ± √{d} / 2*{a}\n'
                self.ids.result_label.text += '\n'
                self.ids.result_label.text += f'x¹ = {x1}\n'
                self.ids.result_label.text += f'x² = {x2}\n'

            else: #Condição 3: O delta é maior que 0, logo tem raizes reais
                x1 = (-b + cmath.sqrt(d))/(2*a)
                x2 = x1
                self.ids.result_label.text += '\n'
                self.ids.result_label.text += f'Equação: {a}x² + {b}x + {c} = 0\n'
                self.ids.result_label.text += '\n'
                self.ids.result_label.text += f'Δ: b² - 4 * a * c =\n'
                self.ids.result_label.text += f'Δ: {b}² - 4*{a}*{c} = {d}\n'
                self.ids.result_label.text += '\n'
                self.ids.result_label.text += f'x = -{b} ± √{d} / 2*{a}\n'
                self.ids.result_label.text += '\n'
                self.ids.result_label.text += f'x¹ = {x1}\n'
                self.ids.result_label.text += f'x² = {x2}\n'
        
        # Transfromar tudo em Str
        except Exception as e:
            self.ids.result_label.text = str(e)
        self.manager.current = 'resultado'
        
#Classe CalculadoraApp que vai chamar o gerenciador de telas
class CalculadoraApp(App):
    def build(self):
        return GerenciaTelas()
        
#Executor da aplocação
if __name__ == '__main__':
    CalculadoraApp().run()
