"""
    Módulo para comunicação com o arduíno via bluetooth.
"""
import bluetooth
import sys

class ComandosResidencia():

    def __init__(self, bt_addr): 
        self.port = 1
        self.bt_addr = bt_addr

        self.sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
        self.sock.connect((bt_addr, self.port))
        self.sock.settimeout(1.0)
        self.status = 'Conectado'

        self.comandos = {
            'led': self.led,
            'alarme': self.alarme,
            'ventilador': self.ventilador
        }

    def led(self, status=False):
        self.sock.send("led=%s"%status)

    def alarme(self, status=False, sensibilidade=100):
        self.sock.send("alarme=%s"%status)

    def ventilador(self, status=False, potencia=100):
        self.sock.send("ventilador=%s"%status)

    def executa(self, method, args=()):
        self.comandos[method](args)

    def encerrar_conexao(self):
        self.sock.close()