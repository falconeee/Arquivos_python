from power_api import SixfabPower

api = SixfabPower()  
api.set_power_outage_event_status(2) #Mantém o evento de falta de energia desabilitado (apenas no começo do programa)
level_battery = 25     #Nível de bateria para o sistema desligar

while True:
    if api.get_battery_level() <= level_battery:  #Se o nível de bateria cai abaixo de um certo valor o sistema habilita o evento de falta de energia, 
                                                  #logo só desligará se estiver sem energia da rede e abaixo do nível especificado.
        api.set_power_outage_event_status(1)      #Evento habilitado e inicia o processo de desligamento
        print('SHUTDOWN')

        
