# Contenido de la demo Hotel Boutique Casa Morisca (Granada) (es/ca/en/fr). Hechos de hotelcasamorisca.com leidos el 29/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma; sin precios ni valoraciones.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran las habitaciones reales.','ca':' Les imatges són il·lustracions i no mostren les habitacions reals.','en':' Images are illustrations and do not show the actual rooms.','fr':' Les images sont des illustrations et ne montrent pas les chambres réelles.'}
H={'es':['Dobles estándar','Dobles superior y ejecutiva','Deluxe y Mirador'],'ca':['Dobles estàndard','Dobles superior i executiva','Deluxe i Mirador'],'en':['Standard doubles','Superior and executive doubles','Deluxe and Mirador'],'fr':['Doubles standard','Doubles supérieure et exécutive','Deluxe et Mirador']}
RD={
'es':['En planta baja o alta, con cama de matrimonio o dos camas, aire acondicionado, minibar, caja fuerte y baño privado.','Exteriores, con vistas laterales a la Alhambra, el Generalife o el Albaicín; la ejecutiva, de 20 m², con balcón.','La Deluxe, de unos 32 m² con salón y techo de madera policromada del siglo XV; la Mirador, con vistas a la Alhambra desde la habitación y el baño.'],
'ca':['A la planta baixa o alta, amb llit de matrimoni o dos llits, aire condicionat, minibar, caixa forta i bany privat.','Exteriors, amb vistes laterals a l\'Alhambra, el Generalife o l\'Albaicín; l\'executiva, de 20 m², amb balcó.','La Deluxe, d\'uns 32 m² amb saló i sostre de fusta policromada del segle XV; la Mirador, amb vistes a l\'Alhambra des de l\'habitació i el bany.'],
'en':['On the ground or upper floor, with a double bed or two beds, air conditioning, minibar, safe and private bathroom.','Exterior rooms with side views of the Alhambra, the Generalife or the Albaicín; the executive, 20 m², with a balcony.','The Deluxe, about 32 m² with a lounge and an original 15th-century painted wooden ceiling; the Mirador, with Alhambra views from the room and the bathroom.'],
'fr':['Au rez-de-chaussée ou à l\'étage, avec lit double ou deux lits, climatisation, minibar, coffre-fort et salle de bain privée.','Extérieures, avec vue latérale sur l\'Alhambra, le Generalife ou l\'Albaicín ; l\'exécutive, de 20 m², avec balcon.','La Deluxe, d\'environ 32 m² avec salon et plafond en bois polychrome du XVe siècle ; la Mirador, avec vue sur l\'Alhambra depuis la chambre et la salle de bain.']}
ART={
'hero':('arches',9901,['#f3e7d4','#e6b783','#a94f2c','#6e2a17','#43190c']),
'intro':('skyline',9902,['#6e2a17','#e7a56a','#f6d6a4','#2b4c3f','#233f34','#162a22']),
'r1':('columns',9911,['#f0ede6','#f8f6f1','#b25a33','#6e2a17','#43190c']),
'r2':('arches',9912,['#f1e6d3','#e3b47f','#a64c29','#6e2a17','#43190c']),
'r3':('hills',9913,['#e7ede6','#f2ead4','#eebd7b','#a8be9e','#7c9b82','#53745d']),
'g1':('skyline',9921,['#6e2a17','#e4a266','#f5d3a0','#294a3d','#213c32','#152820']),
'g2':('arches',9922,['#efe3cf','#e0b07b','#a34926','#6e2a17','#43190c']),
'g3':('columns',9923,['#eeebe3','#f7f4ee','#ae5730','#6e2a17','#43190c']),
'g4':('hills',9924,['#e4ebe3','#efe7cf','#ebba76','#a5bb9b','#79987f','#50715a']),
'g5':('waves',9925,['#2b4c3f','#eebf84','#f6dfb7','#3b6556','#2b4c3f','#1a3028']),
'g6':('arches',9926,['#ede0cb','#ddad77','#a04623','#6e2a17','#43190c'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2','r3'],gallery=['g1','g2','g3','g4','g5','g6'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Hotel Boutique Casa Morisca · Albaicín, frente a la Alhambra',see_rooms='Ver habitaciones',hero_k='Granada · Albaicín',hero_t='Una casa morisca frente a la Alhambra',hero_s='14 habitaciones en el Albaicín, al final de la Carrera del Darro y a 5 minutos a pie de la Alhambra.',
 intro_t='Restaurada por Carlos Sánchez',intro_p1='La casa la restauró el arquitecto granadino Carlos Sánchez y recibió, entre otros, el premio Europa Nostra de 2001, el año en que abrió el hotel.',
 intro_p2='Recepción 24 horas, wifi gratuito en todo el hotel, desayuno buffet y reserva de espectáculos, restaurantes y visitas guiadas a la Alhambra desde recepción.',
 stats=['14 habitaciones','Vistas a la Alhambra','Recepción 24 h','Desde 2001'],nav_rooms='Habitaciones',rooms_t='Habitaciones',rooms_s='Dobles estándar, superiores, ejecutivas, Deluxe y Mirador, para 2 adultos; algunas con vistas a la Alhambra.',
 svcs=['Recepción 24 horas','Wifi gratuito','Desayuno buffet de 7:30 a 11:00','Bebidas y algo ligero a cualquier hora','Traslados al aeropuerto','Parking previa reserva','Gestión de la Granada Card','Venta de entradas y visitas guiadas'],
 loc_p='Cuesta de la Victoria, 9, Bajo · Albaicín · 18010 Granada. Junto al paseo de los Tristes.',
 chips=['¿Qué habitaciones tiene?','¿Tiene vistas a la Alhambra?','¿Hay parking?','¿Cómo se reserva?']),
'ca':dict(title='Hotel Boutique Casa Morisca · Albaicín, davant de l\'Alhambra',see_rooms='Veure habitacions',hero_k='Granada · Albaicín',hero_t='Una casa morisca davant de l\'Alhambra',hero_s='14 habitacions a l\'Albaicín, al final de la Carrera del Darro i a 5 minuts a peu de l\'Alhambra.',
 intro_t='Restaurada per Carlos Sánchez',intro_p1='La casa la va restaurar l\'arquitecte granadí Carlos Sánchez i va rebre, entre d\'altres, el premi Europa Nostra del 2001, l\'any que va obrir l\'hotel.',
 intro_p2='Recepció 24 hores, wifi gratuït a tot l\'hotel, esmorzar bufet i reserva d\'espectacles, restaurants i visites guiades a l\'Alhambra des de recepció.',
 stats=['14 habitacions','Vistes a l\'Alhambra','Recepció 24 h','Des del 2001'],nav_rooms='Habitacions',rooms_t='Habitacions',rooms_s='Dobles estàndard, superiors, executives, Deluxe i Mirador, per a 2 adults; algunes amb vistes a l\'Alhambra.',
 svcs=['Recepció 24 hores','Wifi gratuït','Esmorzar bufet de 7:30 a 11:00','Begudes i alguna cosa lleugera a qualsevol hora','Trasllats a l\'aeroport','Pàrquing amb reserva prèvia','Gestió de la Granada Card','Venda d\'entrades i visites guiades'],
 loc_p='Cuesta de la Victoria, 9, Bajo · Albaicín · 18010 Granada. Al costat del passeig dels Tristes.',
 chips=['Quines habitacions té?','Té vistes a l\'Alhambra?','Hi ha pàrquing?','Com es reserva?']),
'en':dict(title='Hotel Boutique Casa Morisca · Albaicín, facing the Alhambra',see_rooms='See the rooms',hero_k='Granada · Albaicín',hero_t='A Moorish house facing the Alhambra',hero_s='14 rooms in the Albaicín, at the end of the Carrera del Darro and a 5-minute walk from the Alhambra.',
 intro_t='Restored by Carlos Sánchez',intro_p1='The house was restored by Granada architect Carlos Sánchez and received, among others, the Europa Nostra award in 2001, the year the hotel opened.',
 intro_p2='24-hour reception, free wifi throughout, buffet breakfast and booking of shows, restaurants and guided Alhambra tours at reception.',
 stats=['14 rooms','Alhambra views','24 h reception','Since 2001'],nav_rooms='Rooms',rooms_t='Rooms',rooms_s='Standard, superior, executive, Deluxe and Mirador doubles for 2 adults; some with Alhambra views.',
 svcs=['24-hour reception','Free wifi','Buffet breakfast 7:30 to 11:00','Drinks and light bites at any time','Airport transfers','Parking on prior booking','Granada Card arranged','Tickets and guided tours'],
 loc_p='Cuesta de la Victoria, 9, Bajo · Albaicín · 18010 Granada. Next to the Paseo de los Tristes.',
 chips=['What rooms does it have?','Does it have Alhambra views?','Is there parking?','How do I book?']),
'fr':dict(title='Hotel Boutique Casa Morisca · Albaicín, face à l\'Alhambra',see_rooms='Voir les chambres',hero_k='Grenade · Albaicín',hero_t='Une maison mauresque face à l\'Alhambra',hero_s='14 chambres dans l\'Albaicín, au bout de la Carrera del Darro et à 5 minutes à pied de l\'Alhambra.',
 intro_t='Restaurée par Carlos Sánchez',intro_p1='La maison a été restaurée par l\'architecte grenadin Carlos Sánchez et a reçu, entre autres, le prix Europa Nostra en 2001, l\'année d\'ouverture de l\'hôtel.',
 intro_p2='Réception 24h/24, wifi gratuit dans tout l\'hôtel, petit-déjeuner buffet et réservation de spectacles, restaurants et visites guidées de l\'Alhambra à la réception.',
 stats=['14 chambres','Vue sur l\'Alhambra','Réception 24h/24','Depuis 2001'],nav_rooms='Chambres',rooms_t='Chambres',rooms_s='Doubles standard, supérieures, exécutives, Deluxe et Mirador pour 2 adultes ; certaines avec vue sur l\'Alhambra.',
 svcs=['Réception 24h/24','Wifi gratuit','Petit-déjeuner buffet de 7h30 à 11h00','Boissons et en-cas à toute heure','Transferts aéroport','Parking sur réservation','Gestion de la Granada Card','Billetterie et visites guidées'],
 loc_p='Cuesta de la Victoria, 9, Bajo · Albaicín · 18010 Grenade. À côté du Paseo de los Tristes.',
 chips=['Quelles chambres a-t-il ?','A-t-il vue sur l\'Alhambra ?','Y a-t-il un parking ?','Comment réserver ?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'ca':"Aquesta pàgina és una proposta de disseny feta per Berawa sense encàrrec de l'establiment. Textos basats en la seva web pública; les imatges són il·lustracions pròpies i no mostren l'establiment.",
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement."}
RES='https://www.hotelcasamorisca.com/reservas/'; REN='https://www.hotelcasamorisca.com/en/book-now/'
BOOK=dict(mode='engine',url={'es':RES,'ca':RES,'en':REN,'fr':REN})
D=dict(name='Hotel Boutique Casa Morisca',ac='#6b3a1f',ac2='#2f6b5a',ac2_a11y='#235246',book=BOOK,around=[],foot=FOOT,
 address='Cuesta de la Victoria, 9, Bajo · Albaicín · 18010 Granada',phones=['+34 958 221 100'],emails=['reservas@hotelcasamorisca.com'],maps='Hotel Casa Morisca, Cuesta de la Victoria 9, Granada',t=T)
META=dict(repo='demo-hotel-casa-morisca-granada',name='Hotel Boutique Casa Morisca',legal_name='Ajxaris, S.L.',registry_ids=['NIF B18477190'],
 url='https://www.hotelcasamorisca.com/',domain='hotelcasamorisca.com',municipality='Granada',province='Granada',sector='hotel boutique en una casa morisca del Albaicín (Granada)',
 read_at='2026-10-29T15:12:00+01:00',created_at='2026-10-29T15:12:00+01:00',built_at='2026-10-29T15:20:00+01:00',audit_date='2026-10-29T15:08:52+01:00',
 rating=dict(value=4.6,coincide=['telefono','web'],date='2026-10-29T11:02:27+01:00',url='https://www.google.com/maps/place/Hotel+Casa+Morisca/@37.1797017,-3.589179,17z/data=!4m9!3m8!1s0xd71fcc8323b31e3:0x427cacbe62070ad8!5m2!4m1!1i2!8m2!3d37.1797017!4d-3.589179!16s%2Fg%2F1ynnq2xj5'),
 book=dict(mode='engine',url=BOOK['url'],note='Las reservas van a la pagina de reservas del propio hotel (hotelcasamorisca.com/reservas, que carga en un iframe su motor real de bookerclub; /en/book-now/ para ingles y frances); la demo no construye ningun motor.'),
 first_of_type='no aplica: hotel con precedente en demos anteriores')
QS={
'es':[('¿Qué habitaciones tiene?','K01'),('¿Tiene vistas a la Alhambra?','K02'),('¿Dónde está?','K03'),('¿Hay parking?','K04'),('¿Tienen desayuno?','K05'),('¿Hay traslado al aeropuerto?','K06'),('¿Qué es la Granada Card?','K07'),('¿Hay wifi?','K08'),('¿Quién restauró la casa?','K09'),('¿Puedo añadir una cama supletoria?','K10'),('¿Cómo reservo?','K11'),('¿Quién es el titular?','K12'),('¿Cuánto cuesta una noche?',None),('Confírmame que hay una habitación libre mañana','K11'),('¿Tienen piscina?',None),('¿Admiten mascotas?',None)],
'ca':[('Quines habitacions té?','K01'),('Té vistes a l\'Alhambra?','K02'),('On és?','K03'),('Hi ha pàrquing?','K04'),('Teniu esmorzar?','K05'),('Hi ha trasllat a l\'aeroport?','K06'),('Què és la Granada Card?','K07'),('Hi ha wifi?','K08'),('Qui va restaurar la casa?','K09'),('Puc afegir un llit supletori?','K10'),('Com reservo?','K11'),('Qui és el titular?','K12'),('Quant costa una nit?',None),('Confirma\'m que hi ha una habitació lliure demà','K11'),('Teniu piscina?',None),('Admeteu mascotes?',None)],
'en':[('What rooms does it have?','K01'),('Does it have Alhambra views?','K02'),('Where is it?','K03'),('Is there parking?','K04'),('Do you serve breakfast?','K05'),('Is there an airport transfer?','K06'),('What is the Granada Card?','K07'),('Is there wifi?','K08'),('Who restored the house?','K09'),('Can I add an extra bed?','K10'),('How do I book?','K11'),('Who is the owner?','K12'),('How much is a night?',None),('Confirm that there is a free room tomorrow','K11'),('Is there a pool?',None),('Are pets allowed?',None)],
'fr':[('Quelles chambres a-t-il ?','K01'),('A-t-il vue sur l\'Alhambra ?','K02'),('Où est-il ?','K03'),('Y a-t-il un parking ?','K04'),('Servez-vous le petit-déjeuner ?','K05'),('Y a-t-il un transfert aéroport ?','K06'),('Qu\'est-ce que la Granada Card ?','K07'),('Y a-t-il le wifi ?','K08'),('Qui a restauré la maison ?','K09'),('Puis-je ajouter un lit supplémentaire ?','K10'),('Comment réserver ?','K11'),('Qui est le titulaire ?','K12'),('Combien coûte une nuit ?',None),('Confirmez-moi qu\'il y a une chambre libre demain','K11'),('Y a-t-il une piscine ?',None),('Les animaux sont-ils admis ?',None)]}
