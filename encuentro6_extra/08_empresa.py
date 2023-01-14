"""A company has personnel from different areas with different hiring conditions and payment methods.
 The accounting department needs to calculate the weekly salaries (Monday to Friday) based on the 3 
 salary modalities:
(a) commission
b) fixed salary + commission, and
c) fixed salary
a) For the commission salary modality, the total amount of the sales made in the week must be entered,
 and 40% of that total amount corresponds to the employee's salary.
b) For the fixed salary + commission condition, the value paid per hour, the number of hours worked per week 
and the number of hours worked per week must be entered. 
of hours worked per week and the total amount of sales in that week. In this type of contract, overtime is not 
are not contemplated and a maximum of 40 hours per week is set. The sales commission is calculated as 
25% of the total sales value.
c) Finally, for the fixed salary modality, the value paid per hour and the number of hours worked in the week
 must be entered.
 hours worked in the week. In the case of exceeding 40 hours per week, overtime should be paid with 
 an extra 50% of the hourly rate. Create a menu of options to be able to choose the type of contract an employee
 has. an employee has.  """

menu = str(input("Select the option that best suits your needs. Select the option that best suits your needs: commission, fixed salary + commission, fixed salary: "))

if menu == "a" or menu == "A":
    montoTotalVentas = float(input("Ingresa cuantas ventas tuviste en total la semana: "))
    salario = montoTotalVentas * .40
    total = montoTotalVentas + salario
    print(total)

elif menu == "b" or menu == "B":
    tarifa = float(input("ingresar el valor que se paga por hora: ")) 
    horasTrabajadasSemanalmente = float(input("cantidad de horas trabajadas semanalmente: "))
    montoVentas = float(input("el monto total de las ventas en esa semana: "))

    if horasTrabajadasSemanalmente < 40:
        semanal = tarifa * horasTrabajadasSemanalmente
        comision = montoVentas * .25
        total = semanal + comision
        print(total)
    else: 
        print("Te pasaste de horas trabajadas")
        menu = str(input("Selecciona la opcion que mas te convenga \n(a)comision \n(b)salario fijo + comision \n(c)salario fijo: "))

elif menu == "c" or menu == "C":
    tarifa = float(input("ingresar el valor que se paga por hora: ")) 
    cantidadHorasXsemana = float(input("Ingresa cuantas horas trabajaste en la semana: ")) 

    if cantidadHorasXsemana > 40:  
        horasExtra = cantidadHorasXsemana - 40 
        tarifaPlus = tarifa + tarifa * .50 
        nuevoSueldo = tarifaPlus * horasExtra
        pagar = (tarifa * 40) + nuevoSueldo
        print(pagar)

    else:
        pago = cantidadHorasXsemana * tarifa
        print(pago)

else: 
    print("Respuesta no valida vuelve a intentarlo")
    menu = str(input("Selecciona la opcion que mas te convenga \n(a)comision \n(b)salario fijo + comision \n(c)salario fijo: "))