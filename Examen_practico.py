
class EmpleadoA_23:
    def __init__(self, rfc, apellidos, nombres):
        self._rfc = rfc
        self._apellidos = apellidos
        self._nombres = nombres

    def mostrar_informacion(self,):
        return f"RFC: {self._rfc}, Apellidos: {self._apellidos}, Nombres: {self._nombres}"
        

class EmpleadoVendedor(EmpleadoA_23):
    def __init__(self, rfc, apellidos, nombres, monto_vendido, tasa_comision):
        super().__init__(rfc, apellidos, nombres)
        self._monto_vendido = monto_vendido
        self._tasa_comision = tasa_comision

    def calcular_ingresos(self):
        return self._monto_vendido * self._tasa_comision

    def calcular_bonificacion(self):
        if self._monto_vendido < 1000:
            return 0
        elif 1000 <= self._monto_vendido <= 5000:
            return self.calcular_ingresos() * 0.05
        else:
            return self.calcular_ingresos() * 0.10

    def calcular_descuento(self):
        if self.calcular_ingresos() < 1000:
            return self.calcular_ingresos() * 0.11
        else:
            return self.calcular_ingresos() * 0.15

    def calcular_sueldo_neto(self):
        return self.calcular_ingresos() + self.calcular_bonificacion() - self.calcular_descuento()
    

class EmpleadoPermanente(EmpleadoA_23):
    def __init__(self, rfc, apellidos, nombres, sueldo_base, numero_seguro_social):
        super().__init__(rfc, apellidos, nombres)
        self._sueldo_base = sueldo_base
        self._numero_seguro_social = numero_seguro_social

    def ingresos(self):
        return self._sueldo_base

    def calcular_descuento(self):
        return self._sueldo_base * 0.11

    def calcular_sueldo_neto(self):
        return self.ingresos() - self.calcular_descuento()

class SalarioMinimoException(Exception):
    pass

class Empleado_23:
    def __init__(self, rfc, apellidos, nombres):
        if self.calcular_sueldo_neto() < 150:
            raise SalarioMinimoException("Salario mínimo no alcanzado")
        # ...

empleado = EmpleadoA_23("VABA960819TU6", "VAZQUEZ", "ABRAHAM")
print(empleado.mostrar_informacion())


monto_vendido = 12000
tasa_comision= .10

empleado_vendedor= EmpleadoVendedor("VABA960819TU6", "VAZQUEZ", "ABRAHAM", monto_vendido, tasa_comision)

print("Información del empleado vendedor:")
print(empleado_vendedor.mostrar_informacion())
print(f"Monto vendido: {monto_vendido}")
print(f"Tasa de comisión: {tasa_comision*100}%")
print(f"Ingresos: {empleado_vendedor.calcular_ingresos()}")
print(f"Bonificación: {empleado_vendedor.calcular_bonificacion()}")
print(f"Descuento: {empleado_vendedor.calcular_descuento()}")
print(f"Sueldo neto: {empleado_vendedor.calcular_sueldo_neto()}")

empleado_permanente = EmpleadoPermanente("VABA960819TU6", "VAZQUEZ", "ABRAHAM",3000, 598673948723)
print("INFORMACION DEL EMPLEADO PERMANENTE")
