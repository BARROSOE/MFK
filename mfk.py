import network


def procesar_datos(ssid, mac, normal_ssid):
    # Procesar SSID
    ssid_procesado = ssid.replace("UBEE", "").replace("-2.4G", "")

    # Procesar MAC
    mac_procesada = mac.replace(":", "")[2:]

    pawa = mac_procesada[:-2] + ssid_procesado

    return {"nombre_red": normal_ssid, "password": pawa}


def scan_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    ap_list = wlan.scan()
    nearby_aps = []
    for ap in ap_list:
        ssid = ap[0].decode("utf-8")
        rssi = ap[3]
        nearby_aps.append((ssid, rssi))
    return nearby_aps


contra = []


nearby_aps = scan_wifi()
for ap in nearby_aps:
    print("SSID:", ap[0])
    print("RSSI:", ap[1])
    print("--------------------")

    if ap[0].lower().startswith("ubee"):

        check = procesar_datos(ap[0], mac=ap[1], normal_ssid=ap[0])
        contra.append(check)

### tryer ###


sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect(f"{contra[0]['nombre_red']}", f"{contra[0]['password']}")

while not sta_if.isconnected():
    pass

ap_if = network.WLAN(network.AP_IF)
ap_if.active(True)
ap_if.config(essid="WOW", password="WOW")

print("Conexión exitosa. Dirección IP:", sta_if.ifconfig()[0])
