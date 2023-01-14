""" Los empleados de una fábrica trabajan en dos turnos: Diurno y Nocturno. Se desea calcular el jornal diario 
de acuerdo con las siguientes reglas:
a) La tarifa de las horas diurnas es de $ 90
b) La tarifa de las horas nocturnas es de $ 125
c) En caso de ser feriado, la tarifa se incrementa en un 10% si el turno es diurno y en un 15% si el turno es 
nocturno.
El programa debe solicitar la siguiente información al usuario: el nombre del trabajador, el día de la semana, 
el turno (diurno o nocturno) y la cantidad de horas trabajadas. Además,
2
debemos preguntarle al usuario si el día de la semana (lunes, martes, miércoles, etc.) era festivo o no, para 
poder calcular el jornal diario. Utilice una función para realizar el cálculo. """

""" name = str(input("Enter your name: "))
shift = str(input("did you work at day or night: "))
hour = float(input("Enter a number of hours worked: "))
"""  """
def holidayParty(day2,night):
    float(day2)
    float(night)
    holiday = str(input("Is this day a holiday? yes or not "))
    if holiday == "yes":
        if shift == "day":
            f = day2 * .10
            total = f + day2
            print(total)
        else:
            print(night*.15)
    elif holiday == "not":
        if shift == "day":
            print(day2)
        else:
            print(night)
    else:
        print("No valide")

def pay(shift,hour):
    if shift == "day":
        day2 = hour * 90
        print(day2)
    elif shift == "night":
        night = hour * 125
        print(night)
    else:
        print("No es valido")

holidayParty(day2,night)
pay(shift,hour)"""

class Fabrica: 
    def __init__(self, nombre, diaSemana, turno, horasTrabajadas, esFeriado):
        self.nombre = nombre
        self.diaSemana = diaSemana
        self.turno = turno
        self.horasTrabajadas = horasTrabajadas
        self.esFeriado = esFeriado

        self.horaDiurna = 90
        self.horaNocturna = 125

        self.feriadoDiurno = (self.horaDiurna * .10) + self.horaDiurna
        self.feriadoNocturno = (self.horaNocturna * .10) + self.horaNocturna
        self.calculo(self.horasTrabajadas, self.turno, self.diaSemana)

    def diasLaborales(self, diaSemana):
        diasDeLaSemana = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes']
        
        if diaSemana.title() in diasDeLaSemana:
            return True

    def feriado(self, esFeriado):
        esFeriado.lower()
        if esFeriado == "si":
            return True

    def horario(self, turno):
        turno.lower()
        if turno == "diurno":
            return True

    def calculo(self, horasTrabajadas,turno,diaSemana):
        #pass ignora la funcion
        diaTrabajado = self.diasLaborales(diaSemana)
        diaFeriado = self.feriado(self.esFeriado)
        horarioTrabajado = self.horario(turno)

        if diaTrabajado and not diaFeriado:
            if horarioTrabajado:
                print("La tarifa es: ",self.horaDiurna * horasTrabajadas)
            else:
                print("La tarifa es: ",self.horaNocturna * horasTrabajadas)

        elif diaTrabajado and diaFeriado:
            if horarioTrabajado:
                print("La tarifa es: ",self.feriadoDiurno * horasTrabajadas)
            else:
                print("La tarifa es: ",self.feriadoNocturno * horasTrabajadas)


nombre = input('Ingrese su nombre: ')
diaSemana = input('Ingrese el dia de la semana: ')
turno = input('Ingrese el turno: ')
horasTrabajadas = int(input('Ingrese las horas trabajadas: '))
esFeriado = input('Ingrese si es feriado: ')

fabrica = Fabrica(nombre, diaSemana, turno, horasTrabajadas, esFeriado)

print(fabrica)


