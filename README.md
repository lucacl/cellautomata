1-dimensionale CA's kunnen op de volgende manier gemaakt worden:

Een CA kan nu aangemaakt worden door in het Console het volgende
te typen: naam van ca = CA_1D(n, rule, states, neighbourhood, edge_type)
met n een positief geheel getal, rule een geheel getal groter of gelijk
aan -1, states een positief geheel getal, neighbourhood een lijst en
edge type gelijk aan ”wrap”, ”mirror” of een geheel positief getal.
Vervolgens kan in het Console eventueel het volgende getypt worden
voor aanpassingen:
naam_van_ca.changes cell(a,b) om een stand van een cel te veranderen
met a de cel en b de nieuwe stand van deze cel, dus een geheel getal;
naam_van_ca.randomise grid() om alle cellen op het rooster een willekeurige
stand te geven; naam_van_ca.randomise_rule() om een willekeurige mogelijke
regel toe te kennen aan de CA. Ten slotte kan door in het Console
naam van ca.graph(c) te typen de grafiek bekeken worden die het verloop
van de CA over c tijdstappen toont.

2-dimensionale CA's kunnen op de volgende manier gemaakt worden:

Een CA kan nu aangemaakt worden door in het Console het volgende
te typen: naam_van_ca = CA_2D((m,n), rule, states, neighbourhood, edge_type)
met n een positief geheel getal, rule een geheel getal groter of gelijk
aan nul of -1 voor een willekeurige mogelijke regel, states een positief
geheel getal, neighbourhood een lijst van de vorm [( , ), ..., ( , )]
 ́of moore(r), neumann(r), plus(r) of cross(r) en edge_type gelijk aan
”wrap”, ”mirror” of een geheel positief getal. Vervolgens kan in het
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
