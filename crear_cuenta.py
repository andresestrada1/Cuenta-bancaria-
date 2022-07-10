from cuenta_bancaria import CuentaBancaria

cuenta1 = CuentaBancaria(0,0.05)
cuenta2 = CuentaBancaria(100,0.01)

cuenta1.deposito(100).deposito(500).deposito(1500).retiro(100).generar_interés().mostrar_info_cuenta()
print("________________")
cuenta2.deposito(1000).deposito(3000).retiro(500).retiro(200).retiro(400).retiro(100).informacion_de_retiro().generar_interés().mostrar_info_cuenta()
print("________________")
cuenta1.informacion_general_de_cuenta()