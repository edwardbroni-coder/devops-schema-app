# WMO:s kodtabell 4677 (Aktuellt väder)  Dict
# SAMT matchande ikoner som Dict

weathercodes = {
    # Koder 00–19: Ingen nederbörd vid stationen
    # Dessa koder beskriver förhållanden utan nederbörd, och inkluderar observerade förändringar i moln eller siktförhållanden. 
    "0": "Ingen nederbörd, dammstorm, sandstorm, tjock dimma, tjock iskristalldimma, driv- eller blåsande snö vid observationstidpunkten eller under den senaste timmen.",
    "1": "Ingen nederbörd",
    "2": "Ingen nederbörd",
	"3": "Ingen nederbörd",
    "4": "Sikt nedsatt av rök.",
    "5": "Dis (fuktig dis).",
    "6": "Utbredd uppvirvlad sand eller damm i luften.",
    "7": "Damm eller sand som virvlar upp av vinden.",
    "8": "Väldefinierade damm- eller sandvirvlar.",
    "9": "Dammstorm eller sandstorm inom synhåll.",
    "10": "Fuktig dis.",
    "11": "Stråk av dimma.",
    "12": "Mer eller mindre sammanhängande dimma.",
    "13": "Blixtar i sikte, ingen åska.",
    "14": "Nederbörd i sikte, men når inte marken.",
    "15": "Nederbörd i sikte, når marken en bit bort.",
    "16": "Nederbörd i sikte, når marken nära stationen.",
    "17": "Åska, ingen nederbörd.",
    "18": "Fallvindar vid stationen.",
    "19": "Molnformiga virvelvindar (vatten- eller landvirvel).", 

# Koder 20–29: Nederbörd, åska eller dimma under den senaste timmen men inte nu
# Dessa koder indikerar väder som inträffade under den senaste timmen, men som har upphört vid observationstillfället. 
    "20": "Duggregn eller snökorn under den senaste timmen.",
    "21": "Regn under den senaste timmen.",
    "22": "Snöfall under den senaste timmen.",
    "23": "Regn och snöblandat regn under den senaste timmen.",
    "24": "Underkylt regn under den senaste timmen.",
    "25": "Regnskurar under den senaste timmen.",
    "26": "Snöskurar eller slaskskurar under den senaste timmen.",
    "27": "Hagelskur under den senaste timmen.",
    "28": "Dimma under den senaste timmen.",
    "29": "Åska under den senaste timmen.",

# Koder 30–39: Dammstorm, sandstorm eller blåsande snö
# Dessa koder indikerar olika typer av uppvirvlat material i atmosfären. 
    "30": "Dammstorm eller sandstorm, lätt till måttlig eller kraftig, minskande, ingen förändring eller ökande.",
	"31": "Dammstorm eller sandstorm, lätt till måttlig eller kraftig, minskande, ingen förändring eller ökande.",
	"32": "Dammstorm eller sandstorm, lätt till måttlig eller kraftig, minskande, ingen förändring eller ökande.",
    "33": "Dammstorm eller sandstorm, lätt till måttlig eller kraftig, minskande, ingen förändring eller ökande.",
    "34": "Dammstorm eller sandstorm, lätt till måttlig eller kraftig, minskande, ingen förändring eller ökande.",
    "35": "Dammstorm eller sandstorm, lätt till måttlig eller kraftig, minskande, ingen förändring eller ökande.",
    "36": "Dammstorm eller sandstorm, lätt till måttlig eller kraftig, minskande, ingen förändring eller ökande.",
    "37": "Kraftig blåsande snö.",
    "38": "Lätt drivsnö.",
    "39": "Kraftig drivsnö.",

# Koder 40–49: Dimma
# Dessa koder indikerar dimma eller iskristalldimma vid observationstillfället. 
    "40": "Dimma vid observationstillfället, sikt oförändrad.",
    "41": "Dimma i stråk, ej vid stationen.",
    "42": "Dimma lättare på stationen.",
    "43": "Dimma, ingen förändring.",
    "44": "Dimma tätare på stationen.",
    "45": "Dimma lättare, efter regn.",
    "46": "Dimma, ingen förändring, efter regn.",
    "47": "Dimma tätare, efter regn.",
    "48": "Dimma med ispartiklar, dimma lättare.",
    "49": "Dimma med ispartiklar, dimma tjockare.",

# Koder 50–59: Duggregn
# Dessa koder beskriver duggregn med varierande intensitet. 
    "50": "Lätt, måttligt eller kraftigt duggregn, med eller utan underkylning.",
	"51": "Lätt, måttligt eller kraftigt duggregn, med eller utan underkylning.",
	"52": "Lätt, måttligt eller kraftigt duggregn, med eller utan underkylning.",
	"53": "Lätt, måttligt eller kraftigt duggregn, med eller utan underkylning.",
	"54": "Lätt, måttligt eller kraftigt duggregn, med eller utan underkylning.",
	"55": "Lätt, måttligt eller kraftigt duggregn, med eller utan underkylning.",
    "56": "Lätt, måttligt eller kraftigt duggregn, med eller utan underkylning.",
    "57": "Måttligt till kraftigt underkylt duggregn.",
    "58": "Lätt duggregn med regn.",
    "59": "Måttligt till kraftigt duggregn med regn.",

# Koder 60–69: Regn
# Dessa koder beskriver regn med varierande intensitet. 
    "60": "Lätt, måttligt eller kraftigt regn, med eller utan underkylning.",
	"61": "Lätt, måttligt eller kraftigt regn, med eller utan underkylning.",
	"62": "Lätt, måttligt eller kraftigt regn, med eller utan underkylning.",
	"63": "Lätt, måttligt eller kraftigt regn, med eller utan underkylning.",
	"64": "Lätt, måttligt eller kraftigt regn, med eller utan underkylning.",
	"65": "Lätt, måttligt eller kraftigt regn, med eller utan underkylning.",
    "66": "Lätt underkylt regn.",
    "67": "Måttligt till kraftigt underkylt regn.",
    "68": "Lätt regn med duggregn.",
    "69": "Måttligt till kraftigt regn med duggregn.",

# Koder 70–79: Fast nederbörd
# Dessa koder beskriver olika typer av fast nederbörd, som snö och is. 
    "70": "Lätt, måttligt eller kraftigt snöfall.",
	"71": "Lätt, måttligt eller kraftigt snöfall.",
	"72": "Lätt, måttligt eller kraftigt snöfall.",
	"73": "Lätt, måttligt eller kraftigt snöfall.",
	"74": "Lätt, måttligt eller kraftigt snöfall.",
	"75": "Lätt, måttligt eller kraftigt snöfall.",
    "76": "Lätta iskristaller i luften.",
    "77": "Snökorn.",
    "78": "Is pellets.",
    "79": "Lätt till måttligt eller kraftigt hagel. ",

# Koder 80–99: Skurbyar eller åska
# Dessa koder indikerar skurar eller åskväder. 
    "80": "Skurar av regn, snö, snöblandat regn, hagel eller snökorn.",
	"81": "Skurar av regn, snö, snöblandat regn, hagel eller snökorn.",
	"82": "Skurar av regn, snö, snöblandat regn, hagel eller snökorn.",
	"83": "Skurar av regn, snö, snöblandat regn, hagel eller snökorn.",
	"84": "Skurar av regn, snö, snöblandat regn, hagel eller snökorn.",
    "85": "Lätta snöskurar.",
    "86": "Måttliga till kraftiga snöskurar.",
    "87": "Lätta skurar av snöblandat regn.",
    "88": "Måttliga till kraftiga skurar av snöblandat regn.",
    "89": "Lätta skurar av hagel.",
    "90": "Måttliga till kraftiga skurar av hagel.",
    "91": "Åska under den senaste timmen, med lätt eller måttlig nederbörd.",
	"92": "Åska under den senaste timmen, med lätt eller måttlig nederbörd.",
	"93": "Åska under den senaste timmen, med lätt eller måttlig nederbörd.",
	"94": "Åska under den senaste timmen, med lätt eller måttlig nederbörd.",
    "95": "Åska med regn eller snöblandat regn.",
    "96": "Åska med hagel.",
    "97": "Kraftigt åskväder med regn eller snöblandat regn.",
    "98": "Kraftigt åskväder med hagel.",
    "99": "Kraftigt åskväder med tornados.",
}

# MATCHING .PNG ICONS TO WEATHER
weather_icons= {
    "0": "01d@2x.png", #SOL
    "1": "01d@2x.png", #SOL
    "2": "01d@2x.png", #SOL
	"3": "02d@2x.png", #SOLMOLN
    "4": "50d@2x.png", #DIMMA
    "5": "50d@2x.png", #DIMMA
    "6": "50d@2x.png", #DIMMA
    "7": "50d@2x.png", #DIMMA
    "8": "50d@2x.png", #DIMMA
    "9": "50d@2x.png", #DIMMA
    "10": "50d@2x.png", #DIMMA
    "11": "50d@2x.png", #DIMMA
    "12": "50d@2x.png", #DIMMA
    "13": "11d@2x.png", #ÅSKA
    "14": "04d@2x.png", #MOLNDARK
    "15": "04d@2x.png", #MOLNDARK
    "16": "04d@2x.png", #MOLNDARK
    "17": "11d@2x.png", #ÅSKA
    "18": "04d@2x.png", #MOLNDARK
    "19": "04d@2x.png", #MOLNDARK

# Koder 20–29: Nederbörd, åska eller dimma under den senaste timmen men inte nu
# Dessa koder indikerar väder som inträffade under den senaste timmen, men som har upphört vid observationstillfället. 
    "20": "10d@2x.png", #REGNSOL
    "21": "09d@2x.png", #REGNMOLN
    "22": "13d@2x.png", #SNÖ
    "23": "10d@2x.png", #REGNSOL
    "24": "10d@2x.png", #REGNSOL
    "25": "10d@2x.png", #REGNSOL
    "26": "13d@2x.png", #SNÖ
    "27": "13d@2x.png", #SNÖ
    "28": "50d@2x.png", #DIMMA
    "29": "11d@2x.png", #ÅSKA

# Koder 30–39: Dammstorm, sandstorm eller blåsande snö
# Dessa koder indikerar olika typer av uppvirvlat material i atmosfären. 
    "30": "04d@2x.png", #MOLNDARK
    "31": "04d@2x.png", #MOLNDARK
	"32": "04d@2x.png", #MOLNDARK
    "33": "04d@2x.png", #MOLNDARK
    "34": "04d@2x.png", #MOLNDARK
    "35": "04d@2x.png", #MOLNDARK
    "36": "04d@2x.png", #MOLNDARK
    "37": "13d@2x.png", #SNÖ
    "38": "13d@2x.png", #SNÖ
    "39": "13d@2x.png", #SNÖ

# Koder 40–49: Dimma
# Dessa koder indikerar dimma eller iskristalldimma vid observationstillfället. 
    "40": "50d@2x.png", #DIMMA
    "41": "50d@2x.png", #DIMMA
    "42": "50d@2x.png", #DIMMA
    "43": "50d@2x.png", #DIMMA
    "44": "50d@2x.png", #DIMMA
    "45": "50d@2x.png", #DIMMA
    "46": "50d@2x.png", #DIMMA
    "47": "50d@2x.png", #DIMMA
    "48": "50d@2x.png", #DIMMA
    "49": "50d@2x.png", #DIMMA

# Koder 50–59: Duggregn
# Dessa koder beskriver duggregn med varierande intensitet. 
    "50": "10d@2x.png", #REGNSOL
	"51": "10d@2x.png", #REGNSOL
	"52": "10d@2x.png", #REGNSOL
	"53": "10d@2x.png", #REGNSOL
	"54": "09d@2x.png", #REGNMOLN
	"55": "10d@2x.png", #REGNSOL
    "56": "10d@2x.png", #REGNSOL
    "57": "09d@2x.png", #REGNMOLN
    "58": "10d@2x.png", #REGNSOL
    "59": "09d@2x.png", #REGNMOLN

# Koder 60–69: Regn
# Dessa koder beskriver regn med varierande intensitet. 
    "60": "10d@2x.png", #REGNSOL
	"61": "10d@2x.png", #REGNSOL
	"62": "10d@2x.png", #REGNSOL 
	"63": "10d@2x.png", #REGNSOL
	"64": "10d@2x.png", #REGNSOL
	"65": "09d@2x.png", #REGNMOLN
    "66": "09d@2x.png", #REGNMOLN
    "67": "09d@2x.png", #REGNMOLN
    "68": "09d@2x.png", #REGNMOLN
    "69": "09d@2x.png", #REGNMOLN

# Koder 70–79: Fast nederbörd
# Dessa koder beskriver olika typer av fast nederbörd, som snö och is. 
    "70": "13d@2x.png", #SNÖ
	"71": "13d@2x.png", #SNÖ
	"72": "13d@2x.png", #SNÖ
	"73": "13d@2x.png", #SNÖ
	"74": "13d@2x.png", #SNÖ
	"75": "13d@2x.png", #SNÖ
    "76": "13d@2x.png", #SNÖ
    "77": "13d@2x.png", #SNÖ
    "78": "13d@2x.png", #SNÖ
    "79": "13d@2x.png", #SNÖ

# Koder 80–99: Skurbyar eller åska
# Dessa koder indikerar skurar eller åskväder. 
    "80": "09d@2x.png", #REGNMOLN
	"81": "09d@2x.png", #REGNMOLN
	"82": "09d@2x.png", #REGNMOLN
	"83": "09d@2x.png", #REGNMOLN
	"84": "13d@2x.png", #SNÖ
    "85": "13d@2x.png", #SNÖ
    "86": "13d@2x.png", #SNÖ
    "87": "13d@2x.png", #SNÖ
    "88": "13d@2x.png", #SNÖ
    "89": "09d@2x.png", #REGNMOLN
    "90": "09d@2x.png", #REGNMOLN
    "91": "11d@2x.png", #ÅSKA
	"92": "11d@2x.png", #ÅSKA
	"93": "11d@2x.png", #ÅSKA
	"94": "11d@2x.png", #ÅSKA
    "95": "11d@2x.png", #ÅSKA
    "96": "11d@2x.png", #ÅSKA
    "97": "11d@2x.png", #ÅSKA
    "98": "11d@2x.png", #ÅSKA
    "99": "11d@2x.png", #ÅSKA
}

