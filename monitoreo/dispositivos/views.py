from django.shortcuts import render

# Create your views here.
def panel_dispositivos(request):
    dispositivos = [
        {"nombre":"Sensor Temperatura","consumo":50},
        {"nombre":"Medidor Solar","consumo":120},
        {"nombre":"Sensor Movimiento","consumo":30},
        {"nombre":"Calefactor","consumo":200},
    ]
    
    consumo_maximo = 100
    
    for d in dispositivos:
        if d["consumo"] <= consumo_maximo:
            d["estado"] = "Correcto"
        else:
            d["estado"] = "Exceso"
    
    return render(request, "dispositivos/panel.html",{
        "dispositivos":dispositivos,
        "consumo_maximo":consumo_maximo
    })