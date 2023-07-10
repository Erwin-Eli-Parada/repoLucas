from calculo import calcular
from customtkinter import CTk, CTkFrame, CTkLabel, CTkTextbox, CTkEntry, CTkButton, set_appearance_mode, set_default_color_theme
import tkinter

set_appearance_mode("dark")
set_default_color_theme("green")

class Miclase:
    def __init__(self):

        resultados=["0 [cm2]","0 [cm2]","0 [cm2]","Aun no se ha calculado"]

        self.ventana = CTk()
        self.ventana.geometry("820x420")


        etiqueta_salida2 = CTkLabel(self.ventana, text="Resolución de armadura a flexión según la norma ACI 318-14", font=('Helvetica', 18, 'bold'))
        etiqueta_salida2.pack(pady=10, padx=15)

        # Crear frame principal
        principal_frame = CTkFrame(self.ventana)
        principal_frame.pack(expand=True, fill="both")
        #Crear frame para el boton
        boton_frame = CTkFrame(self.ventana)
        boton_frame.pack(pady=20)

        # Crear frame para el formulario
        formulario_frame = CTkFrame(principal_frame)
        formulario_frame.pack(side="left", anchor = tkinter.CENTER, fill="both")

        # Crear inputs
        self.input_text1 = CTkEntry(formulario_frame, width=370, placeholder_text="ancho de la sección rectangular [m]", justify="center")
        self.input_text1.pack(pady=10,padx=15)

        self.input_text2 = CTkEntry(formulario_frame, width=370, placeholder_text="altura de la viga [m]", justify="center")
        self.input_text2.pack(pady=10, padx=15)

        self.input_text3 = CTkEntry(formulario_frame, width=370, placeholder_text="recubrimiento a los aceros [m]", justify="center")
        self.input_text3.pack(pady=10, padx=15)

        self.input_text4 = CTkEntry(formulario_frame, width=370, placeholder_text="resistencia característica del hormigón a compresión [MPa]", justify="center")
        self.input_text4.pack(pady=10, padx=15)

        self.input_text5 = CTkEntry(formulario_frame, width=370, placeholder_text="límite de fluencia del acero [MPa]", justify="center")
        self.input_text5.pack(pady=10, padx=15)

        self.input_text6 = CTkEntry(formulario_frame, width=370, placeholder_text="Momento último solicitante en la sección [MN-m]", justify="center")
        self.input_text6.pack(pady=10, padx=15)

        # Crear frame para la etiqueta de salida
        self.salida_frame = CTkFrame(principal_frame)
        self.salida_frame.pack(anchor = tkinter.CENTER, fill="both", expand=True)

        # Crear etiqueta de salida
        self.etiqueta_salida1 = CTkLabel(self.salida_frame, text=resultados[0], font=('Helvetica', 15, 'bold'))
        self.etiqueta_salida1.pack(pady=20, padx=15)

        self.etiqueta_salida2 = CTkLabel(self.salida_frame, text=resultados[1], font=('Helvetica', 15, 'bold'))
        self.etiqueta_salida2.pack(pady=20, padx=15)

        self.etiqueta_salida3 = CTkLabel(self.salida_frame, text=resultados[2], font=('Helvetica', 15, 'bold'))
        self.etiqueta_salida3.pack(pady=20, padx=15)

        self.etiqueta_salida4 = CTkLabel(self.salida_frame, text=resultados[3], font=('Helvetica', 15, 'bold'))
        self.etiqueta_salida4.pack(pady=20, padx=15)

        # Crear botón para concatenar los inputs
        boton_concatenar = CTkButton(boton_frame, text="Concatenar", command=self.calcular_handler)
        boton_concatenar.pack(anchor = tkinter.CENTER)

        # Iniciar bucle de eventos
        self.ventana.mainloop()

    def calcular_handler(self):       
        
        if self.es_float(self.input_text1.get(), "etiqueta_salida1") and self.es_float(self.input_text2.get(), "etiqueta_salida2") and self.es_float(self.input_text3.get(), "etiqueta_salida3") and self.es_float(self.input_text4.get(), "etiqueta_salida4") and self.es_float(self.input_text5.get(), "etiqueta_salida5") and self.es_float(self.input_text6.get(), "etiqueta_salida6"):

            resultados=calcular(float(self.input_text1.get()), float(self.input_text2.get()), float(self.input_text3.get()), float(self.input_text4.get()), float(self.input_text5.get()), float(self.input_text6.get()))
        
            if hasattr(self, "etiqueta_salida1"):
                self.etiqueta_salida1.destroy()

            if hasattr(self, "etiqueta_salida2"):
                self.etiqueta_salida2.destroy()

            if hasattr(self, "etiqueta_salida3"):
                self.etiqueta_salida3.destroy()

            if hasattr(self, "etiqueta_salida4"):
                self.etiqueta_salida4.destroy()
                
            self.etiqueta_salida1 = CTkLabel(self.salida_frame, text=resultados[0], font=('Helvetica', 15, 'bold'))
            self.etiqueta_salida1.pack(pady=20, padx=15)

            self.etiqueta_salida2 = CTkLabel(self.salida_frame, text=resultados[1], font=('Helvetica', 15, 'bold'))
            self.etiqueta_salida2.pack(pady=20, padx=15)

            self.etiqueta_salida3 = CTkLabel(self.salida_frame, text=resultados[2], font=('Helvetica', 15, 'bold'))
            self.etiqueta_salida3.pack(pady=20, padx=15)

            self.etiqueta_salida4 = CTkLabel(self.salida_frame, text=resultados[3], font=('Helvetica', 15, 'bold'))
            self.etiqueta_salida4.pack(pady=20, padx=15)

    def es_float(self, string, input):
        try:
            float(string)
            self.input_text1.configure(text_color="white", placeholder_text_color="white")
            self.input_text2.configure(text_color="white", placeholder_text_color="white")
            self.input_text3.configure(text_color="white", placeholder_text_color="white")
            self.input_text4.configure(text_color="white", placeholder_text_color="white")
            self.input_text5.configure(text_color="white", placeholder_text_color="white")
            self.input_text6.configure(text_color="white", placeholder_text_color="white")
            return True
        except ValueError:
            if input=="etiqueta_salida1":
                self.input_text1.configure(text_color="red", placeholder_text_color="red")
            if input=="etiqueta_salida2":
                self.input_text2.configure(text_color="red", placeholder_text_color="red")
            if input=="etiqueta_salida3":
                self.input_text3.configure(text_color="red", placeholder_text_color="red")
            if input=="etiqueta_salida4":
                self.input_text4.configure(text_color="red", placeholder_text_color="red")
            if input=="etiqueta_salida5":
                self.input_text5.configure(text_color="red", placeholder_text_color="red")
            if input=="etiqueta_salida6":
                self.input_text6.configure(text_color="red", placeholder_text_color="red")
            return False

mi_objeto = Miclase()