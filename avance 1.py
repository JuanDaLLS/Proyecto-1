# Clase Para el registro con constructor y metodo para mostrar informacion 
class Registro:
    def __init__(self, **kwargs):
        self.__nombre = kwargs.get('nombre')
        self.__edad = kwargs.get('edad')
        self.__carne = kwargs.get('carne')
        self.__correo = kwargs.get('correo')
        self.__tipo = kwargs.get('tipo')
        self.cursos = []  # 
        self.calificaciones = {}  # 
    
    def mostrar_info(self):
        return "Nombre: " + self.__nombre + ", Edad: " + str(self.__edad) + ", Carné: " + self.__carne + ", Correo: " + self.__correo + ", Tipo: " + self.__tipo

    def get_carne(self):
        return self.__carne

    def get_tipo(self):
        return self.__tipo

    def get_nombre(self):
        return self.__nombre


class SistemaRegistro:
    def __init__(self):
        self.usuarios = []
        self.carnets_registrados = set()
        self.cursos_disponibles = [
            "Programación", "Cálculo", "Análisis y Laboratorio de Datos",
            "Física", "Estrategias de Comunicación Lingüística"
        ]
        self.evaluaciones = {}  # 
    
    #
    def registrar_nuevo_usuario(self):
        print("\n--- REGISTRAR NUEVO USUARIO ---")
        while True:
            nuevoCarne = input("Ingrese el carné: ").strip()
            if nuevoCarne in self.carnets_registrados:
                print("Carnet " + nuevoCarne + " ya existe. Intente con otro.")
            else:
                break
        nuevoNombre = input("Ingrese el nombre: ").strip()
        if nuevoNombre == "":
            print("El nombre no puede estar vacío.")
            return
        while True:
            try:
                nuevoEdad = int(input("Ingrese la edad: ").strip())
                if nuevoEdad <= 0:
                    print("La edad debe ser mayor a 0.")
                    continue
                break
            except:
                print("Edad inválida. Intente de nuevo.")
        while True:
            nuevoCorreo = input("Ingrese el correo: ").strip()
            if "@" not in nuevoCorreo:
                print("El correo debe contener '@'. Intente de nuevo.")
            else:
                break
        while True:
            nuevoTipo = input("Ingrese el tipo de Miembro (profesor/estudiante): ").strip().lower()
            if nuevoTipo == "profesor" or nuevoTipo == "estudiante":
                break
            else:
                print("Tipo no válido. Debe ser 'profesor' o 'estudiante'.")
        nuevo_usuario = Registro(
            nombre=nuevoNombre,
            edad=nuevoEdad,
            carne=nuevoCarne,
            correo=nuevoCorreo,
            tipo=nuevoTipo
        )
        self.usuarios.append(nuevo_usuario)
        self.carnets_registrados.add(nuevoCarne)
        print("Usuario " + nuevoNombre + " registrado exitosamente!")

    def mostrar_todos_usuarios(self):
        print("\n--- LISTA DE USUARIOS REGISTRADOS ---")
        if len(self.usuarios) == 0:
            print("No hay usuarios registrados.")
            return
        i = 1
        for usuario in self.usuarios:
            print(str(i) + ". " + usuario.mostrar_info())
            i += 1
        print("Total: " + str(len(self.usuarios)) + " usuarios")

    # 
    def inscribir_curso(self):
        carne = input("Ingrese el carné del estudiante: ").strip()
        estudiante = None
        for u in self.usuarios:
            if u.get_carne() == carne and u.get_tipo() == "estudiante":
                estudiante = u
                break
        if estudiante == None:
            print("No se encontró el estudiante con ese carné.")
            return
        print("\n--- CURSOS DISPONIBLES ---")
        i = 1
        for curso in self.cursos_disponibles:
            print(str(i) + ". " + curso)
            i += 1
        opcion = input("Seleccione un curso (1-5): ").strip()
        try:
            opcion_num = int(opcion)
            if opcion_num >= 1 and opcion_num <= len(self.cursos_disponibles):
                curso = self.cursos_disponibles[opcion_num - 1]
                if curso not in estudiante.cursos:
                    estudiante.cursos.append(curso)
                    print(estudiante.get_nombre() + " inscrito en " + curso)
                else:
                    print("El estudiante ya está inscrito en este curso.")
            else:
                print("Opción inválida.")
        except:
            print("Opción inválida.")

    # 
    def crear_evaluacion(self):
        print("\n--- CREAR EVALUACIÓN ---")
        i = 1
        for curso in self.cursos_disponibles:
            print(str(i) + ". " + curso)
            i += 1
        opcion = input("Seleccione un curso (1-5): ").strip()
        try:
            opcion_num = int(opcion)
            if opcion_num >= 1 and opcion_num <= len(self.cursos_disponibles):
                curso = self.cursos_disponibles[opcion_num - 1]
                preguntas = []
                for i in range(1, 11):
                    print("\nPregunta " + str(i) + ":")
                    enunciado = input("Escriba la pregunta: ")
                    opciones = {}
                    opciones["a"] = input("Opción a: ")
                    opciones["b"] = input("Opción b: ")
                    opciones["c"] = input("Opción c: ")
                    opciones["d"] = input("Opción d: ")
                    preguntas.append({"pregunta": enunciado, "opciones": opciones})
                self.evaluaciones[curso] = preguntas
                print("Evaluación creada para " + curso)
            else:
                print("Opción inválida.")
        except:
            print("Opción inválida.")

    # 
    def registrar_calificacion(self):
        carne = input("Ingrese el carné del estudiante: ").strip()
        estudiante = None
        for u in self.usuarios:
            if u.get_carne() == carne and u.get_tipo() == "estudiante":
                estudiante = u
                break
        if estudiante == None:
            print("No se encontró el estudiante.")
            return
        if len(estudiante.cursos) == 0:
            print("El estudiante no tiene cursos inscritos.")
            return
        print("\nCursos inscritos:")
        i = 1
        for curso in estudiante.cursos:
            print(str(i) + ". " + curso)
            i += 1
        opcion = input("Seleccione un curso: ").strip()
        try:
            opcion_num = int(opcion)
            if opcion_num >= 1 and opcion_num <= len(estudiante.cursos):
                curso = estudiante.cursos[opcion_num - 1]
                nota = input("Ingrese la calificación (0-100): ").strip()
                try:
                    nota_val = float(nota)
                    if curso not in estudiante.calificaciones:
                        estudiante.calificaciones[curso] = []
                    estudiante.calificaciones[curso].append(nota_val)
                    print("Nota registrada en " + curso + " para " + estudiante.get_nombre())
                except:
                    print("Calificación inválida.")
            else:
                print("Opción inválida.")
        except:
            print("Opción inválida.")

    # ------------------ MENÚ ------------------
    def menu_principal(self):
        while True:
            print("="*50)
            print("SISTEMA DE REGISTRO DE USUARIOS")
            print("="*50)
            print("1. Registrar nuevo usuario")
            print("2. Ver todos los usuarios")
            print("3. Inscribir estudiante en curso")
            print("4. Crear evaluación")
            print("5. Registrar calificación")
            print("6. Salir")
            print("="*50)
            opcion = input("Seleccione una opción (1-6): ").strip()
            if opcion == "1":
                self.registrar_nuevo_usuario()
            elif opcion == "2":
                self.mostrar_todos_usuarios()
            elif opcion == "3":
                self.inscribir_curso()
            elif opcion == "4":
                self.crear_evaluacion()
            elif opcion == "5":
                self.registrar_calificacion()
            elif opcion == "6":
                print("bai")
                break
            else:
                print("Opción no válida. Intente de nuevo.")


sistema = SistemaRegistro()
sistema.menu_principal()
