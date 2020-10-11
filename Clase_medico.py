class Medico:
  def __init__(self, nombre, apellido, cedula, sexo, especialidad):
    self.nombre=nombre
    self.apellido=apellido
    self.cedula=cedula
    self.sexo=sexo
    self.especialidad=especialidad
  
  def atender_paciente(self):
    print("El medico",self.nombre, "atiende a paciente")
  
  def recetar(self,paciente_nombre):
    print("Creando receta con cedula medica", self.cedula,"para el paciente",paciente_nombre)
  
  def dar_alta(self):
    print(" El Dr.",self.nombre,"especialista en",self.especialidad, "da de alta")

  def diagniostico_Covid(self):
    print("El Dr.", self.nombre, "realiza prueba de Covid-19")



################ Clase Extranjero ##################

class Extranjero(Medico):
  def __init__(self,nombre, apellido, cedula, sexo,especialidad, pais_origen,estadia,vijencia_visa,idioma):
    super().__init__(nombre, apellido, cedula, sexo, especialidad)
    self.pais_origen=pais_origen
    self.estadia=estadia
    self.vijencia_visa=vijencia_visa
    self.idioma=idioma
  
  def traduccion(self):
    print("Medico extranjero", self.nombre,"realiza traduccion")
  

################ Clase Pasante ##################
class Pasante(Medico):
  def __int__(self,nombre,apellido,cedula,sexo,especialidad,hospital_procedencia,horas_servicio):
    super().__int__(nombre,apellido,cedula,sexo,especialidad)
    self.hospital_procedencia=hospital_procedencia
    self.horas_servicio=horas_servicio
  
  def realizar_reporte(self):
    print("Medico pasante", self.nombre,"realiza reporte")

  def pasar_lista(self):
    print("El pasante del hospital",self.hospital, "pasa lista")


################ Clase con Plaza ##################
class Con_plaza(Medico):
  def __int__(self,nombre,apellido,cedula,sexo,especialidad,pago_mensual,anios_contrato):
    super().__int__(nombre,apellido,cedula,sexo,especialidad)
    self.pago_mensual=pago_mensual
    self.anios_contrato=anios_contrato

  #def Consultar_saldo():
   




   ################Clase Disponibilidad################
class Disponibilidad_medical(Medico):
  turno="-"
  dia="-"
  hora="-"
  anio="-"

  def __init__(self,nombre, apellido, cedula, sexo, especialidad):
    super().__init__(nombre, apellido, cedula, sexo, especialidad)

  def programar_cita(self):
    self.turno=input("Ingresa el turno")
    self.dia=input("Dia:")
    self.hora=input("Hora:")
    self.anio=input("Anio:")
    print("El turno del Dr.",self.nombre,"es",self.turno)
  
  def obtener_cita(self):

    if self.turno=="-":
      print("No existe registro, ingrese uno")
      self.programar_cita()

    else:
      print("La cita es el",self.dia,"del",self.anio,"a las",self.hora)
      print(self.turno)
      print(self.dia)
      print(self.hora)

  def cancelar_cita():

    self.turno=None
    self.dia=None
    self.hora=None
    self.anio=None






      ################Clase Experiencia#####################
   
class Experiencia(Medico):

    def __init__(self,nombre, apellido, cedula, sexo, anios_trabajando,pacientes_operados,eficacia):
      super().__init__(nombre, apellido, cedula, sexo, especialidad)
      self.anios_trabajando=anios_trabajando
      self.pacientes_operados=pacientes_operados
      self.no_de_decesos=no_de_decesos
      

    def Obtener_eficacia(self):
      self.pacientes_operados=int(self.pacientes_operados)
      self.no_de_decesos=int(self.no_de_decesos)

      self.eficacia= ((self.pacientes_operados/self.no_de_decesos)-1)*100

      print("Eficacia:",self.eficacia,"%")

    def Obtener_experiencia(self):




###################Fofmacion Academica#######################

class Formacion_Academica(Medico):
  def __init__(self,nombre,apellido,cedula,sexo,especialidad,universidad,titulo,maestria,posgrado):
    super().__init__(nombre, apellido, cedula, sexo, especialidad)
    self.universidad=universidad
    self.titulo=titulo
    self.maestria=maestria
    self.posgrado=posgrado

  def Obtener_trayectoria(self):
    print("Drcon titulo en",self.titulo,", maestria",self.maestria,"y  doctorados en",self.doctorado)

  def Obtener_procedencia(self):
    print("Dr. proviene de la universidad",self.universidad)
   
###################Actividades curriculares#######################
class Actividades_curriculares(Medico):
  def __init__(self, nombre, apellido,cedula,sexo,especialidad,curso,actualizacion,logros,trabajo_investigacion):
    super().__init__(nombre, apellido, cedula, sexo, especialidad)
    self.curso=curso
    self.se_actualiza=se_actualiza
    self.logros=logros
    self.trabajo_investigacion=trabajo_investigacion

  def Mostrar_logros(self):
    print("Logros del Dr.",self.nombre,":",self.logros)

  def Mostrar_investigacion(self):
    print("Actualmente trabaja en",self.trabajo_investigacion)

  



class Competencias(Medico):
  def __init__(self,nombre,apellido,cedula,sexo,especialidad,adaptabilidad,confianza,integridad,toleracia_al_estres,comunicacion,liderazgo):
    super().__init__(nombre,apellido,cedula,sexo,especialidad)
    self.confianza=confianza
    self.integridad=integridad
    self.tolerancia_al_estres=tolerancia_al_estres
    self.comunicacion=comunicacion
    self.liderazgo=liderazgo

  def Mostrar_softskills(self):
    print("Dr cuenta con las siguientes calificaciones:\n","confianza",self.confianza,"Integridad:",self.integridad,"Comunicacion:",self.comunicacion)



####################




class Habilidades(Medico):
  def __init__(self,nombre,apellido,cedula,sexo,especialidad,capacidad_de_razonar,prevencion_de_incidencias,organizacion,planificacion,analisis_y_sintesis):
    super().__init__(nombre,apellido,cedula,sexo,especialidad)
    self.capacidad_de_razonar=capacidad_de_razonar
    self.prevencion_de_incidencias=prevencion_de_incidencias
    self.organizacion=organizacion
    self.planificacion=planificacion
    self.analisis_y_sintesis=analisis_y_sintesis

  def Planificar(self):
    if self.planificacion==True:
      print("Medico planificando")
    else:
      print("Cambia de Doctor")

class Acciones(Medico):
  def __int__(self,nombre,apellido,cedula,sexo,especialidad, operar, transplantar,inyectar):
    super().__int__(nombre,apellido,cedula,sexo,especialidad)
    self.operar=operar
    self.transplantar=transplantar
    self.inyectar=inyectar
    
  def Inyectar(self):
      if self.inyectar==True:
          print("Inyectando")
      else:
          print("No puede inyectar")
          
  def Operar(self):
    if self.operar==True:
          print("Operando")
      else:
          print("No puede operar")



medico_disponibilidad=Disponibilidad_medical("Angelica","Moreno","0765050","M","Ginecologa")
#medico_disponibilidad.programar_cita()
medico_disponibilidad.obtener_cita()

med=Disponibilidad_medical("Angelica","Moreno","0765050","M","Ginecologa")
med.obtener_cita()

#def __init__(self,nombre, apellido, cedula, sexo, especialidad):

#Ejemplo de crear una disponibilidad
medico_extranjero=Extranjero("Martin","Navarro","78888","M","Pediatra","Cuba","2 años","06/11/23","Espaniol")

medico_extranjero.atender_paciente()
medico_extranjero.recetar("Luis Hernandez")

  

