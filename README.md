1-dimensionale CA's kunnen op de volgende manier gemaakt worden:

A = CA_1D(n, rule, states, neighbourhood, edge_type)

    Parameters:    n: int, of 1-tuple
                     Een positief geheel getal of een 1-tuple van een positief 
                     geheel getal, die wordt gebruikt om het aantal cellen in de CA te bepalen.
                     
                   rule: int
                     Een geheel getal >= -1, die bepaalt hoe de volgende generatie van de CA er 
                     uit zal zien. Als -1 als waarde wordt gegeven genereert de code een 
                     random niet-negatief geheel getal die als regel zal worden gebruikt.
                     
                   states: int
                     Een positef geheel getal dat bepaalt hoeveel verschillende toestanden 
                     een cel binnen de CA kan aannemen. Als een cel dus alleen 0 of 1 als
                     toestand kan hebben dan is het aantal mogelijke toestanden voor een cel dus 2.
                     
                   neighbourhood: list gevuld met int
                     Een lijst met gehele getallen, die bepalen wat de buren zijn van een 
                     willekeurige cel. Bijvoorbeeld [-1, 0, 2]. In dit geval verwijst 0 naar de cel zelf, 
                     dus de cel is een buur van zichzelf. De -1 verwijst naar de cel direct 
                     links van de cel, en de 2 verwijst naar de cel twee posities naar rechts van de cel.
                     Het aantal elementen in de lijst mag zelf gekozen worden.
                     
                   edge_type: str
                     Een string de bepaalt hoe er wordt gehandeld als een buur van een cel buiten het 
                     raster van cellen valt, met als mogelijke waarde 'mirror', 'wrap' of een positief 
                     getal als string (bijvoorbeeld '1'). Als 'mirror' wordt gebruikt dan is elke 
                     buur van een willekeurige cel die buiten het raster valt gelijk aan de cel zelf.
                     Als 'wrap' wordt gebruikt dan vormt de CA in zekere zin een donut, in dat 
                     de laatste cel in het raster aansluit met de eerste cel in het raster.
                     Als een geheel getal als string als argument wordt gegeven dan nemen alle 
                     buren van een cel die buiten het raster vallen een constante toestand 
                     aan gelijk aan het getal dat als string werd gegeven.
    
    
    Class functions (bedoet om te worden gebruikt door gebruike):
                   randomise_grid()
                     Deze functie genereert een random toestand voor alle cellen in de CA.
                     
                   randomise_rule()
                     Deze functie genereert een random regel voor de CA die zal worden gebruikt om nieuwe generaties van de CA te genereren.
    
                   change_cell(i: int, b: int)
                     Deze functie verandert de toestand van de cel met index i naar toestand b.
                     
                   step():
                     Deze functie itereert de CA naar de volgende generatie door middel van het regel getal van de CA.
                     
                   run(n: int):
                     Deze functie roept n keer de step() functie aan.
                     
                   graph(n: int)
                     Deze functie maakt een grafiek van de CA met behulp van de matplotlib.pyplot library. 
                     De functie genereert de volgende n generaties van de CA, en zet de 
                     opeenvolgende generaties onder elkaar in een grafiek.
                     
Handleiding (text)
Een CA kan nu aangemaakt worden door in het Console het volgende
te typen: naam van ca = CA_1D(n, rule, states, neighbourhood, edge_type)
met n een positief geheel getal, rule een geheel getal groter of gelijk
aan -1, states een positief geheel getal, neighbourhood een lijst en
edge type gelijk aan ”wrap”, ”mirror” of een geheel positief getal.
Vervolgens kan in het Console eventueel het volgende getypt worden
voor aanpassingen:
naam_van_ca.change_cell(a,b) om een stand van een cel te veranderen
met a de cel en b de nieuwe stand van deze cel, dus een geheel getal;
naam_van_ca.randomise grid() om alle cellen op het rooster een willekeurige
stand te geven; naam_van_ca.randomise_rule() om een willekeurige mogelijke
regel toe te kennen aan de CA. Ten slotte kan door in het Console
naam van ca.graph(c) te typen de grafiek bekeken worden die het verloop
van de CA over c tijdstappen toont.

2-dimensionale CA's kunnen op de volgende manier gemaakt worden:

B = CA_2D((m, n), rule, states, neighbourhood, edge_type)

    Parameters:    (m, n): 2-tuple
                     Een 2-tuple van een positief geheel getal, die wordt gebruikt om een raster cellen 
                     met hoogte m en breedte n voor de CA te genereren.
                     
                   rule: int
                     Een geheel getal >= -1, die bepaalt hoe de volgende generatie van de CA er 
                     uit zal zien. Als -1 als waarde wordt gegeven genereert de code een 
                     random niet-negatief geheel getal die als regel zal worden gebruikt.
                     
                   states: int
                     Een positef geheel getal dat bepaalt hoeveel verschillende toestanden 
                     een cel binnen de CA kan aannemen. Als een cel dus alleen 0 of 1 als
                     toestand kan hebben dan is het aantal mogelijke toestanden voor een cel dus 2.
                     
                   neighbourhood: list gevuld met int
                     Een lijst met 2-tuples van gehele getallen, die bepalen wat de buren zijn van een 
                     willekeurige cel. Bijvoorbeeld [(-1, 0), (0, -1), (0, 0), (1, 0), (0, 1)]. In dit geval 
                     verwijst (0,0) naar de cel zelf, dus in dat geval is de cel is een buur van zichzelf. 
                     De andere tupels verwijzen naar de cellen direct links, rechts, boven en onder van de cel.
                     Het aantal tupels in de lijst mag zelf gekozen worden. Ook kunnen de functies moore(r), 
                     neumann(r), plus(r), cross(r) die in ca_2d.py worden gedefinieerd worden gebruikt 
                     om zo een lijst van tuples te genereren. Deze functies nemen een geheel getal r als 
                     argument dat de radius van deze buurten bepaalt.
                     
                   edge_type: str
                     Een string de bepaalt hoe er wordt gehandeld als een buur van een cel buiten het 
                     raster van cellen valt, met als mogelijke waarde 'mirror', 'wrap' of een positief 
                     getal als string (bijvoorbeeld '1'). Als 'mirror' wordt gebruikt dan is elke 
                     buur van een willekeurige cel die buiten het raster valt gelijk aan de cel zelf.
                     Als 'wrap' wordt gebruikt dan vormt de CA in zekere zin een donut, in dat 
                     de rechter kant van het raster cellen aansluit met de linker kant van het 
                     raster, en ook dat de bovenkant van het raster cellen aansluit met de 
                     onderkant van het raster. Als een geheel getal als string als argument wordt 
                     gegeven dan nemen alle buren van een cel die buiten het raster vallen 
                     een constante toestand aan gelijk aan het getal dat als string werd gegeven.
    
    
    Class functions (bedoet om te worden gebruikt door gebruike):
                   randomise_grid()
                     Deze functie genereert een random toestand voor alle cellen in de CA.
                     
                   randomise_rule()
                     Deze functie genereert een random regel voor de CA die zal worden gebruikt om nieuwe generaties van de CA te genereren.
    
                   change_cell((i, j): tuple, b: int)
                     Deze functie verandert de toestand van de cel met coordinaten (i, j) (genummerd zoals elementen van een matrix) naar toestand b.
                     
                   step():
                     Deze functie itereert de CA naar de volgende generatie door middel van het regel getal van de CA.
                     
                   run(n: int):
                     Deze functie roept n keer de step() functie aan.
                     
                   game_of_life_step(lower = 2: int, upper = 3: int, birth = 4: int):
                     Deze functie itereert de CA 1 tijdstap naar de volgende generatie door middel van het 
                     toepassen van de regels van game of life. Deze functie is ontworpen voor CA met maar 
                     twee toestanden, maar werkt in principe ook voor meer toestanden.
                     Hierbij worden de volgende regels gehandhaafd:
                         -als een cel minder dan 'lower' buren heetft met toestand != 0 dan wordt 
                             de toestand van de cel verandert naar 0
                         -als een cel meer dan 'upper' buren heeft met toestand != 0 dan wordt 
                             de toestand van de cel verandert naar 0
                         -als een cel met toestand = 0 precies 'birth' aantal buren heeft met 
                             toestand != 0 dan wordt de toestand van de cel verandert naar 1
                     Als er geen argumenten zijn gegeven voor de functie dan wordt dit geinterpreteerd 
                     als game_of_life(2, 3, 3), wat precies de regels zijn voor Conway's game of life. Als 
                     de CA ook nog eens een moore(1) neighbourhood heeft kan Conway's game 
                     of life volledig worden gesimuleerd met deze functie.
                     
                   graph(n: int)
                     Deze functie maakt een grafiek van de CA met behulp van de matplotlib.pyplot library. 
                     De functie genereert de huidige generatie van de CA als een grafiek.
                     

Handleiding (text)
Een CA kan nu aangemaakt worden door in het Console het volgende
te typen: naam_van_ca = CA_2D((m,n), rule, states, neighbourhood, edge_type)
met n een positief geheel getal, rule een geheel getal groter of gelijk
aan nul of -1 voor een willekeurige mogelijke regel, states een positief
geheel getal, neighbourhood een lijst van de vorm [( , ), ..., ( , )]
 ́of moore(r), neumann(r), plus(r) of cross(r), en edge_type gelijk aan
”wrap”, ”mirror” of een geheel positief getal als string. Vervolgens kan in het
Console eventueel het volgende getypt worden voor aanpassingen: naam_van_ca.changes_cell()
om een stand van een cel te veranderen met (m, n) de cel en b de nieuwe
stand van deze cel; naam_van_ca.randomise_grid() om alle cellen op het
rooster een willekeurige stand te geven; naam_van_ca.randomise rule()
om een willekeurige mogelijke regel toe te kennen aan de CA. Ten slotte
kan door in het Console naam_van_ca.graph() te typen wordt de tweedimensionale
CA getoond na een enkele stap. Vervolgens kan naam_van_ca.step_cell()
een willekeurig aantal keer getypt worden, oftewel er kunnen een willekeurig
aantal stappen gezet worden, waarna op elk moment de huidige stand
van de CA bekeken kan worden via naam van ca.graph(c). Er kan ook gekozen
worden voor een typische stap zoals in Game of Life, dit gaat via
naam_van_ca.game_of_life_step()
