from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview
from ttg import *
from pandas import *

class Calculadora():

    def __init__(self) -> None:
        self.root = Tk()
        self.janela()
        self.tela()
        self.botoes()
        self.root.mainloop()

    def janela(self) -> None:
        self.root.title("Calculadora Lógica")
        self.root.configure(background= "#87ceeb")
        self.root.geometry("350x500")
        self.root.minsize(width= 350,height= 500)

    def tela(self) -> None:
        self.display = Frame(self.root)
        self.display.place(relx= 0, rely= 0, relwidth= 1, relheight= 0.2)

        self.display.columnconfigure(index= 0, weight= 1, uniform = 'a')
        self.display.rowconfigure(index= 0, weight= 1, uniform = 'a')

        self.display_tela = Entry(self.display)
        self.display_tela.grid(row = 0, column= 0,sticky = NSEW)
        self.display_tela.bind("<KeyPress>", NONE)

        self.teclado = Frame(self.root)
        self.teclado.place(relx= 0, rely= 0.2, relwidth= 1, relheight= 0.8)

        self.teclado.columnconfigure(index= [0,1,2,3,4], weight= 1, uniform = 'a')
        self.teclado.rowconfigure(index= [0,1,2,3,4,5,6,7,8], weight= 1, uniform = 'a')

    def botoes(self) -> None:

        self.preposicoes = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        self.operadores_logicos = ["~","∧","∨","→","↔"]
        self.parenteses = ["(",")"]

        self.botao_preposicoes = list(range(len(self.preposicoes)))
        self.botao_operadores_logicos = list(range(len(self.operadores_logicos)))
        self.botao_parenteses = list(range(len(self.parenteses)))
        
        contador_preposicoes = 0
        contador_operadores_logicos = 0
        contador_parenteses = 0

        coluna = 0
        linha = 1
        
        for preposicao in self.preposicoes:
            if coluna == 4:
                coluna = 0 
                linha += 1
            self.botao_preposicoes[contador_preposicoes] = Button(self.teclado, text= preposicao, command= lambda x = preposicao: self.inserir_digito(x), bd = 3, bg = "#70757a", fg= "white", font=("Arial",10,"bold"))
            if preposicao != "Y" and preposicao != "Z":
                self.botao_preposicoes[contador_preposicoes].grid(row = linha, column = coluna, sticky = NSEW)
            else:
                self.botao_preposicoes[contador_preposicoes].grid(row = linha, column = coluna, columnspan = 2 , sticky = NSEW)
                coluna += 1
            contador_preposicoes += 1
            coluna += 1

        coluna = 0
        linha = 6

        for parentese in self.parenteses:
            self.botao_parenteses[contador_parenteses] = Button(self.teclado, text= parentese, command= lambda x = parentese: self.inserir_digito(x), bd = 3, bg = "#346c99", fg= "white", font=("Arial",10,"bold"))
            self.botao_parenteses[contador_parenteses].grid(row = linha, column = 4, sticky = NSEW)
            contador_parenteses += 1
            linha += 1
    
        linha = 1
        coluna = 0

        for operador_logico in self.operadores_logicos:
            self.botao_operadores_logicos[contador_operadores_logicos] = Button(self.teclado, text= operador_logico, command= lambda x = operador_logico: self.inserir_digito(x), bd = 3, bg = "#346c99", fg= "white", font=("Arial",10,"bold"))
            self.botao_operadores_logicos[contador_operadores_logicos].grid(row = linha, column = 4, sticky = NSEW)
            contador_operadores_logicos += 1
            if linha <= 8:
                linha += 1

        self.botao_limpar = Button(self.teclado, text= "Limpar", command= lambda: self.limpar(), bd = 3, bg = "#ffcd3b", fg= "white", font=("Arial",10,"bold"))
        self.botao_limpar.grid(row = 0, column = 0, columnspan= 4, sticky = NSEW)

        self.botao_deletar = Button(self.teclado, text= "Deletar", command= lambda: self.apagar(), bd = 3, bg = "#ffcd3b", fg= "white", font=("Arial",10,"bold"))
        self.botao_deletar.grid(row = 0, column = 4, sticky = NSEW)

        self.botao_calcular = Button(self.teclado, text= "Calcular", command= lambda: self.calcular(), bd = 3, bg = "#ffcd3b", fg= "white", font=("Arial",10,"bold"))
        self.botao_calcular.grid(row = 8, column = 0, columnspan = 5, sticky = NSEW)

    def limpar(self) -> None:

        self.display_tela.delete(0,END)
    
    def apagar(self) -> None:
        
        self.display_tela.delete(self.display_tela.index("end") - 1)

    def inserir_digito(self,digito) -> None:
        
        ultimo_digito = self.display_tela.get()
        if ultimo_digito:
            if ultimo_digito[-1] in self.preposicoes:
                if digito not in self.preposicoes:
                    if digito not in self.parenteses[0] and digito not in self.operadores_logicos[0]:
                        self.display_tela.insert(END,digito)
                else: pass
            elif ultimo_digito[-1] in self.parenteses:
                if digito in self.operadores_logicos[1:5] and ultimo_digito[-1] not in self.parenteses[0]:
                    self.display_tela.insert(END,digito)
                elif digito not in self.operadores_logicos[1:5]:
                    self.display_tela.insert(END,digito)
            elif ultimo_digito[-1] in self.operadores_logicos:
                if digito not in self.operadores_logicos[1:5]:
                    if digito in self.operadores_logicos[0] and ultimo_digito[-1] not in self.operadores_logicos[0] or digito in self.parenteses[0] and ultimo_digito[-1] in self.operadores_logicos[0] and ultimo_digito[-2:] != "(~":
                        self.display_tela.insert(END,digito)
                    elif digito not in self.operadores_logicos and digito not in self.parenteses[1]:
                        if len(ultimo_digito) >= 2:
                            if digito not in self.parenteses[0] and ultimo_digito[-2] != "(~":
                                self.display_tela.insert(END,digito)
                            else:
                                self.display_tela.insert(END,digito)
                            
                        else:
                            self.display_tela.insert(END,digito)
                else: pass
        else:
            if digito in self.preposicoes or digito in self.operadores_logicos[0] or digito in self.parenteses[0]: 
                self.display_tela.insert(END,digito)

    def calcular(self) -> None:
        operacao = self.display_tela.get() 

        try:
            abrir_parenteses = 0
            fechar_parenteses = 0
            for char in operacao:
                if(char == "("):
                    abrir_parenteses += 1
                elif (char == ")"):
                    fechar_parenteses += 1
            if abrir_parenteses != fechar_parenteses:
                raise Exception
            if operacao[-1] in self.operadores_logicos:
                raise Exception
            operacao = operacao.replace("∧"," and ")
            operacao = operacao.replace("∨"," or ")
            operacao = operacao.replace("→"," => ")
            operacao = operacao.replace("↔"," = ")
            preposicoes = list()
            for digito in operacao:
                if digito.isalpha() and digito.isupper():
                    if digito not in preposicoes:
                        preposicoes.append(digito)

            tabela_verdade = Truths(preposicoes, [operacao], ints = False)
            resultado = tabela_verdade.valuation()
            if resultado == "Tautology":
                resultado = "Tautologia"
            if resultado == "Contingency":
                resultado = "Contingência"
            if resultado == "Contradiction":
                resultado = "Contradição"
            self.janela_tabela_verdade(tabela_verdade,resultado)
        except Exception:
            self.warning = messagebox.showwarning(title = "Atenção",message = "Operação lógica inválida.", type= "retrycancel", parent = self.root)
            if self.warning == "retry":
                self.limpar()
            else:
                self.root.destroy()
    
    def janela_tabela_verdade(self,tabela_verdade, resultado) -> None:

        self.tabela_verdade = Toplevel()
        self.tabela_verdade.title("Tabela Verdade")
        self.tabela_verdade.geometry("1500x750")
        self.tabela_verdade.minsize(width= 1500,height= 750)
        self.tabela_verdade.transient(self.root)
        self.tabela_verdade.focus_force()
        self.tabela_verdade.grab_set()
        self.tabela_verdade.rowconfigure(0, weight= 1, uniform= "a")
        self.tabela_verdade.rowconfigure(1, weight= 10, uniform= "a")
        self.tabela_verdade.columnconfigure(0, weight= 1, uniform= "a")
        
        self.label_tabela_verdade_resultado = Label(self.tabela_verdade, text= resultado)
        self.label_tabela_verdade_resultado.grid(row = 0, column = 0, sticky = NSEW)

        tabela_verdade = tabela_verdade.as_pandas
        tabela_verdade.columns = [col.replace(" and "," ∧ ") for col in tabela_verdade.columns]
        tabela_verdade.columns = [col.replace(" or "," ∨ ") for col in tabela_verdade.columns]
        tabela_verdade.columns = [col.replace(" => "," → ") for col in tabela_verdade.columns]
        tabela_verdade.columns = [col.replace(" = ","↔ ") for col in tabela_verdade.columns]
        for col in tabela_verdade.columns:
            tabela_verdade[col] = tabela_verdade[col].replace({True:"V"})
            tabela_verdade[col] = tabela_verdade[col].replace({False:"F"})
        
        colunas = tabela_verdade.columns.tolist()
        linhas = tabela_verdade.values.tolist()

        self.label_tabela_verdade = Treeview(self.tabela_verdade, columns = colunas, show = "headings")
        indice = 0

        for col in colunas:
            self.label_tabela_verdade.heading(col,text=col)
        for val in linhas:
            indice += 1
            self.label_tabela_verdade.insert("", END, text = indice, values=val)
            
        self.label_tabela_verdade.grid(row = 1, column = 0,sticky = NSEW)

Calculadora()