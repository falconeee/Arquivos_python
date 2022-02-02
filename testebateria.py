from datetime import datetime
from power_api import SixfabPower
import time

api = SixfabPower()

api.set_power_outage_event_status(2) #desabilita o evento de falta de energia que é desligar o sistema

while True:
    if api.get_battery_level() < 10:  #se o nivel de bateria cai abaixo de 10% habilita o desligamento
        api.set_power_outage_event_status(1)
        print('vou desligar')
    else:
        print('nao vou desligar'+ ' ' + str(api.get_battery_level()))
        
    time.sleep(5)
        