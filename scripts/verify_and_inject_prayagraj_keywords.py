import os

raw_keywords_text = """
prayagraj tour
prayagraj tourism
prayagraj travel
prayagraj trip
prayagraj yatra
prayagraj darshan
prayagraj sightseeing
prayagraj tourist places
prayagraj tourist attractions
prayagraj places to visit
prayagraj places to see
prayagraj me ghumne ki jagah
prayagraj mein ghumne ki jagah
prayagraj me ghumne layak jagah
prayagraj mein ghumne layak jagah
prayagraj me kya dekhe
prayagraj mein kya dekhen
prayagraj me kya ghoome
prayagraj tourist place
tourist places in prayagraj
tourist places near prayagraj
best places to visit in prayagraj
best places in prayagraj
famous places in prayagraj
famous tourist places in prayagraj
must visit places in prayagraj
top places to visit in prayagraj
top tourist places in prayagraj
prayagraj sightseeing places
prayagraj travel guide
prayagraj tourism guide
prayagraj travel guide in hindi
prayagraj tourism in hindi
prayagraj tourist guide
prayagraj trip plan
prayagraj tour plan
prayagraj travel plan
prayagraj itinerary
prayagraj tour itinerary
prayagraj travel itinerary
prayagraj one day trip
prayagraj one day tour
prayagraj 1 day trip
prayagraj 1 day tour
prayagraj two day trip
prayagraj 2 day trip
prayagraj 2 day tour
prayagraj three day trip
prayagraj 3 day trip
prayagraj 3 day tour
prayagraj weekend trip
prayagraj weekend tour
prayagraj family trip
prayagraj family tour
prayagraj couple trip
prayagraj group tour
prayagraj solo trip
prayagraj pilgrimage tour
prayagraj religious tour
prayagraj spiritual tour
prayagraj temple tour
prayagraj dham
prayagraj dham yatra
prayag dham
prayag yatra
teerthraj prayag
prayag teerth
prayagraj pilgrimage
prayagraj religious places
prayagraj spiritual places
prayagraj temples
famous temples in prayagraj
famous mandir in prayagraj
prayagraj mandir
prayagraj mandir darshan
prayagraj temple darshan
prayagraj religious places to visit
prayagraj holy places
prayagraj sacred places
prayagraj pilgrimage places

allahabad tour
allahabad tourism
allahabad travel
allahabad trip
allahabad yatra
allahabad darshan
allahabad sightseeing
allahabad tourist places
allahabad tourist attractions
allahabad places to visit
allahabad places to see
allahabad me ghumne ki jagah
allahabad mein ghumne ki jagah
allahabad me kya dekhe
allahabad mein kya dekhen
tourist places in allahabad
best places to visit in allahabad
famous places in allahabad
allahabad travel guide
allahabad tourism guide
allahabad itinerary
allahabad tour itinerary
allahabad trip plan
allahabad tour plan
allahabad one day trip
allahabad one day tour
allahabad 2 day trip
allahabad 2 day tour
allahabad weekend trip
allahabad family trip
allahabad pilgrimage tour
allahabad religious places
allahabad temples
allahabad temple tour
allahabad sangam
allahabad sangam tour
allahabad sangam darshan
allahabad tourism places
allahabad tourist guide
allahabad travel plan

prayagraj sangam
prayag sangam
triveni sangam
triveni sangam prayagraj
triveni sangam allahabad
prayagraj triveni sangam
allahabad triveni sangam
sangam prayagraj
sangam allahabad
sangam darshan
sangam yatra
sangam tourism
sangam tourist place
sangam tourist attraction
sangam places to visit
sangam ghat prayagraj
sangam ghat allahabad
sangam ghat
prayagraj sangam ghat
triveni sangam ghat
triveni sangam tourism
triveni sangam tour
triveni sangam trip
triveni sangam darshan
triveni sangam yatra
triveni sangam visit
triveni sangam sightseeing
triveni sangam boat ride
triveni sangam boating
triveni sangam boat
triveni sangam boat booking
triveni sangam boat ride price
triveni sangam boating price
triveni sangam boat fare
triveni sangam boat timing
triveni sangam boating timing
triveni sangam boat tour
triveni sangam boat trip
sangam boat ride prayagraj
sangam boating prayagraj
sangam boat booking prayagraj
sangam boat fare prayagraj
sangam boat price prayagraj
sangam boat timing prayagraj
prayagraj sangam boating
prayagraj sangam boat ride
prayagraj sangam boat booking
prayagraj sangam boat price
prayagraj sangam boat timing
allahabad sangam boating
allahabad sangam boat ride
allahabad sangam boat booking
allahabad sangam boat price
allahabad sangam boat timing
boat ride at sangam
boating at triveni sangam
boating in prayagraj sangam
boat ride in prayagraj
boat ride in allahabad
sangam me boating
sangam mein boating
sangam me boat kaise milegi
sangam mein boat kaise milegi
sangam boat kaise book kare
sangam boating kaise kare
triveni sangam me boating
triveni sangam mein boating
triveni sangam me boat ride
triveni sangam mein boat ride

triveni sangam aarti
sangam aarti
sangam aarti prayagraj
sangam aarti allahabad
prayagraj sangam aarti
allahabad sangam aarti
ganga aarti prayagraj
ganga aarti allahabad
prayagraj ganga aarti
allahabad ganga aarti
sangam ganga aarti
triveni sangam ganga aarti
sangam aarti timing
sangam aarti time
sangam aarti timing prayagraj
sangam aarti time prayagraj
ganga aarti timing prayagraj
ganga aarti time prayagraj
sangam aarti today
sangam aarti evening
sangam evening aarti
prayagraj evening aarti
sangam aarti location
sangam aarti place
sangam aarti ka time
sangam aarti kab hoti hai
sangam aarti kahan hoti hai
sangam aarti kaise dekhe
sangam aarti darshan
sangam aarti experience

prayagraj ganga
prayagraj yamuna
prayagraj saraswati
ganga yamuna sangam
ganga yamuna saraswati sangam
ganga yamuna sangam prayagraj
ganga yamuna sangam allahabad
ganga yamuna saraswati sangam prayagraj
ganga yamuna saraswati sangam allahabad
ganga yamuna confluence prayagraj
three rivers sangam prayagraj
three river sangam allahabad
prayag confluence
prayagraj confluence
sangam of ganga yamuna
sangam of ganga yamuna saraswati
where ganga yamuna meet
where ganga yamuna saraswati meet
ganga yamuna meeting point
ganga yamuna sangam location
triveni sangam location
triveni sangam location prayagraj
triveni sangam address
triveni sangam route
triveni sangam map
triveni sangam near me
how to reach triveni sangam
how to go triveni sangam
how to reach sangam prayagraj
how to reach sangam from prayagraj station
sangam kaise jaye
sangam kaise jaye prayagraj
sangam kaise jaye allahabad
sangam jane ka rasta
sangam jane kaise
sangam tak kaise jaye
triveni sangam kaise jaye
triveni sangam kaise pahuche
triveni sangam mein kaise jaye

prayagraj snan
sangam snan
triveni sangam snan
sangam me snan
sangam mein snan
prayagraj sangam snan
triveni sangam me snan
triveni sangam mein snan
sangam snan timing
sangam snan time
sangam snan ghat
sangam snan place
sangam snan kaise kare
sangam me snan kaise kare
triveni sangam me snan kaise kare
sangam me naha sakte hai
sangam mein naha sakte hain
sangam snan information
sangam snan rules
sangam snan guide
sangam snan experience
prayagraj sangam me snan
prayagraj me sangam snan
allahabad sangam snan

bade hanuman mandir prayagraj
bade hanuman ji mandir prayagraj
lete hue hanuman mandir prayagraj
lete hue hanuman ji mandir
bade hanuman mandir allahabad
bade hanuman ji mandir allahabad
lete hue hanuman mandir allahabad
prayagraj hanuman mandir
prayagraj hanuman temple
allahabad hanuman temple
hanuman mandir near sangam
hanuman temple near sangam prayagraj
bade hanuman mandir near sangam
bade hanuman mandir darshan
bade hanuman mandir prayagraj darshan
bade hanuman ji darshan
lete hue hanuman ji darshan
bade hanuman mandir timing
bade hanuman mandir time
bade hanuman mandir opening time
bade hanuman mandir closing time
bade hanuman mandir location
bade hanuman mandir address
bade hanuman mandir route
bade hanuman mandir map
bade hanuman mandir kaise jaye
bade hanuman mandir prayagraj kaise jaye
bade hanuman mandir allahabad kaise jaye
bade hanuman mandir sangam
bade hanuman mandir sangam prayagraj
bade hanuman mandir history
bade hanuman mandir information
bade hanuman mandir famous
lete hue hanuman mandir history
prayagraj bade hanuman mandir
prayag bade hanuman mandir
hanuman ji mandir prayagraj
hanuman ji temple prayagraj

alopi devi mandir prayagraj
alopi devi temple prayagraj
alopi devi mandir allahabad
alopi devi temple allahabad
alopi devi shakti peeth
alopi devi temple
alopi devi mandir darshan
alopi devi darshan
alopi devi mandir timing
alopi devi temple timing
alopi devi mandir time
alopi devi mandir location
alopi devi mandir address
alopi devi mandir route
alopi devi mandir kaise jaye
alopi devi mandir history
alopi devi mandir information
alopi devi mandir prayagraj darshan
alopi devi mandir near sangam

mankameshwar mandir prayagraj
mankameshwar temple prayagraj
mankameshwar mandir allahabad
mankameshwar temple allahabad
mankameshwar mandir darshan
mankameshwar temple darshan
mankameshwar mandir timing
mankameshwar mandir time
mankameshwar mandir location
mankameshwar mandir address
mankameshwar mandir route
mankameshwar mandir kaise jaye
mankameshwar mandir history
mankameshwar mandir information
mankameshwar mahadev prayagraj
mankameshwar mahadev temple
mankameshwar mandir near sangam

nagvasuki mandir prayagraj
nagvasuki temple prayagraj
nagvasuki mandir allahabad
nagvasuki temple allahabad
nagvasuki mandir darshan
nagvasuki mandir timing
nagvasuki mandir time
nagvasuki mandir location
nagvasuki mandir address
nagvasuki mandir route
nagvasuki mandir kaise jaye
nagvasuki mandir history
nagvasuki mandir information
nagvasuki temple near sangam

kalyani devi mandir prayagraj
kalyani devi temple prayagraj
kalyani devi mandir allahabad
kalyani devi temple allahabad
kalyani devi mandir darshan
kalyani devi mandir timing
kalyani devi mandir time
kalyani devi mandir location
kalyani devi mandir address
kalyani devi mandir route
kalyani devi mandir kaise jaye
kalyani devi mandir history
kalyani devi mandir information
kalyani devi temple shakti peeth

lalita devi mandir prayagraj
lalita devi temple prayagraj
lalita devi mandir allahabad
lalita devi temple allahabad
lalita devi mandir darshan
lalita devi mandir timing
lalita devi mandir time
lalita devi mandir location
lalita devi mandir address
lalita devi mandir route
lalita devi mandir kaise jaye
lalita devi mandir history
lalita devi mandir information

shankar viman mandapam prayagraj
shankar viman mandapam temple
shankar viman mandapam allahabad
shankar viman mandapam prayagraj timing
shankar viman mandapam location
shankar viman mandapam darshan
shankar viman mandapam history
shankar viman mandapam kaise jaye

bharadwaj ashram prayagraj
bharadwaj ashram allahabad
bharadwaj ashram prayagraj darshan
bharadwaj ashram location
bharadwaj ashram timing
bharadwaj ashram history
bharadwaj ashram kaise jaye
bharadwaj ashram information
bharadwaj ashram temple
bharadwaj ashram near anand bhawan

akshay vat prayagraj
akshay vat allahabad
akshay vat prayagraj darshan
akshay vat temple prayagraj
akshay vat location
akshay vat timing
akshay vat time
akshay vat history
akshay vat kaise jaye
akshay vat information
akshay vat sangam
akshay vat allahabad fort
akshay vat prayagraj fort

patalpuri temple prayagraj
patalpuri mandir prayagraj
patalpuri temple allahabad
patalpuri mandir allahabad
patalpuri temple darshan
patalpuri mandir timing
patalpuri temple timing
patalpuri temple location
patalpuri temple history
patalpuri temple kaise jaye
patalpuri temple information
patalpuri temple inside fort
patalpuri mandir allahabad fort

allahabad fort
allahabad fort prayagraj
allahabad fort allahabad
prayagraj fort
akbar fort prayagraj
akbar fort allahabad
allahabad fort tourism
allahabad fort tourist place
allahabad fort history
allahabad fort information
allahabad fort location
allahabad fort address
allahabad fort timing
allahabad fort opening time
allahabad fort entry
allahabad fort entry fee
allahabad fort ticket
allahabad fort kaise jaye
allahabad fort near sangam
allahabad fort sangam
prayagraj allahabad fort
akbar fort prayagraj tourism
allahabad fort tourist attraction
allahabad fort places to visit
allahabad fort ashoka pillar
ashoka pillar prayagraj
ashoka pillar allahabad fort
saraswati koop prayagraj
saraswati koop allahabad
jodhabai palace allahabad fort
jodhabai palace prayagraj
allahabad fort akshay vat
allahabad fort patalpuri temple

anand bhawan prayagraj
anand bhawan allahabad
anand bhawan tourism
anand bhawan tourist place
anand bhawan museum
anand bhawan museum prayagraj
anand bhawan museum allahabad
anand bhawan history
anand bhawan information
anand bhawan timing
anand bhawan opening time
anand bhawan ticket
anand bhawan entry fee
anand bhawan location
anand bhawan address
anand bhawan kaise jaye
anand bhawan tour
anand bhawan sightseeing
anand bhawan planetarium
jawahar planetarium prayagraj
jawahar planetarium allahabad
jawahar planetarium timing
jawahar planetarium ticket
jawahar planetarium show
jawahar planetarium prayagraj ticket
swaraj bhawan prayagraj
swaraj bhawan allahabad
swaraj bhawan history
swaraj bhawan timing
swaraj bhawan tourism
swaraj bhawan kaise jaye
anand bhawan swaraj bhawan

khusro bagh prayagraj
khusro bagh allahabad
khusro bagh tourism
khusro bagh tourist place
khusro bagh tourist attraction
khusro bagh history
khusro bagh information
khusro bagh timing
khusro bagh opening time
khusro bagh entry fee
khusro bagh ticket
khusro bagh location
khusro bagh address
khusro bagh kaise jaye
khusro bagh sightseeing
khusro bagh prayagraj tour
khusro bagh allahabad tour

allahabad museum prayagraj
allahabad museum allahabad
prayagraj museum
allahabad museum tourism
allahabad museum tourist place
allahabad museum timing
allahabad museum opening time
allahabad museum ticket
allahabad museum entry fee
allahabad museum location
allahabad museum address
allahabad museum kaise jaye
allahabad museum history
allahabad museum information
allahabad museum galleries
allahabad museum tour
allahabad museum sightseeing

chandra shekhar azad park prayagraj
chandrashekhar azad park prayagraj
chandra shekhar azad park allahabad
company bagh prayagraj
company bagh allahabad
alfred park prayagraj
alfred park allahabad
company garden prayagraj
company garden allahabad
chandra shekhar azad park tourism
company bagh tourism
company bagh tourist place
chandra shekhar azad park timing
company bagh timing
company bagh entry fee
company bagh location
company bagh kaise jaye
alfred park history
chandra shekhar azad park history

new yamuna bridge prayagraj
new yamuna bridge allahabad
yamuna bridge prayagraj
yamuna bridge allahabad
new yamuna bridge tourism
new yamuna bridge tourist attraction
new yamuna bridge sightseeing
new yamuna bridge view
new yamuna bridge night view
new yamuna bridge photos
new yamuna bridge location
new yamuna bridge kaise jaye

minto park prayagraj
minto park allahabad
minto park tourism
minto park history
minto park location
minto park kaise jaye
minto park tourist place
minto park sightseeing

all saints cathedral prayagraj
all saints cathedral allahabad
patthar girja prayagraj
patthar girja allahabad
all saints cathedral church prayagraj
all saints cathedral tourism
all saints cathedral history
all saints cathedral timing
all saints cathedral location
all saints cathedral kaise jaye
patthar girja prayagraj timing
patthar girja allahabad timing

shringverpur prayagraj
shringverpur allahabad
shringverpur tourism
shringverpur tourist place
shringverpur tour
shringverpur temple
shringverpur ramayan
shringverpur history
shringverpur kaise jaye
shringverpur distance from prayagraj
shringverpur prayagraj distance
shringverpur sightseeing
shrungverpur prayagraj
shringverpur dham

prayagraj kumbh mela
kumbh mela prayagraj
kumbh mela allahabad
allahabad kumbh mela
prayag kumbh mela
kumbh in prayagraj
kumbh mela tourism prayagraj
kumbh mela tour prayagraj
kumbh mela trip prayagraj
kumbh mela yatra prayagraj
kumbh mela sangam
kumbh mela triveni sangam
kumbh mela prayagraj sangam
kumbh mela history
kumbh mela information
kumbh mela history prayagraj
kumbh mela significance
kumbh mela significance prayagraj
kumbh mela places to visit
kumbh mela tourist places
kumbh mela travel guide
kumbh mela travel plan
kumbh mela itinerary
kumbh mela itinerary prayagraj
kumbh mela accommodation
kumbh mela hotel
kumbh mela hotels prayagraj
kumbh mela stay prayagraj
kumbh mela tent
kumbh mela tent booking
kumbh mela camp booking
kumbh mela camps prayagraj
kumbh mela dharamshala
kumbh mela accommodation near sangam
kumbh mela hotel near sangam
kumbh mela transport
kumbh mela travel
kumbh mela how to reach
kumbh mela how to go
kumbh mela sangam visit
kumbh mela bathing
kumbh mela snan
kumbh mela snan prayagraj
kumbh mela shahi snan
kumbh mela sadhu
kumbh mela akhara
kumbh mela kalpavas
kumbh mela kalpvas
kumbh mela kalpavasi
kumbh mela religious places
kumbh mela sightseeing
kumbh mela photography
kumbh mela guide
kumbh mela package
kumbh mela tour package
kumbh mela travel package
kumbh mela trip package
kumbh mela cab
kumbh mela taxi
kumbh mela local sightseeing
kumbh mela nearby places
kumbh mela prayagraj tour package
kumbh mela prayagraj travel package

maha kumbh prayagraj
maha kumbh mela prayagraj
maha kumbh allahabad
maha kumbh mela allahabad
maha kumbh prayag
maha kumbh sangam
maha kumbh triveni sangam
maha kumbh tourism
maha kumbh tour
maha kumbh trip
maha kumbh yatra
maha kumbh history
maha kumbh information
maha kumbh significance
maha kumbh itinerary
maha kumbh travel guide
maha kumbh accommodation
maha kumbh hotel
maha kumbh tent
maha kumbh camp
maha kumbh stay
maha kumbh snan
maha kumbh bathing
maha kumbh kalpavas
maha kumbh akhara
maha kumbh sadhu
maha kumbh places to visit
maha kumbh sightseeing
maha kumbh travel package
maha kumbh tour package
maha kumbh package
maha kumbh cab
maha kumbh taxi
maha kumbh how to reach
maha kumbh how to go
maha kumbh travel plan
maha kumbh trip plan
maha kumbh itinerary prayagraj

magh mela prayagraj
magh mela allahabad
magh mela prayag
magh mela prayagraj tourism
magh mela tour
magh mela trip
magh mela yatra
magh mela sangam
magh mela triveni sangam
magh mela snan
magh mela bathing
magh mela kalpavas
magh mela kalpvas
magh mela history
magh mela information
magh mela significance
magh mela dates
magh mela timing
magh mela accommodation
magh mela hotel
magh mela tent
magh mela camp
magh mela stay
magh mela travel
magh mela travel guide
magh mela itinerary
magh mela package
magh mela tour package
magh mela travel package
magh mela how to reach
magh mela transport
magh mela sangam visit
magh mela sightseeing
magh mela nearby places

prayagraj kumbh accommodation
prayagraj kumbh hotel
prayagraj kumbh hotels
prayagraj kumbh stay
prayagraj kumbh camp
prayagraj kumbh tent
prayagraj kumbh tent booking
prayagraj kumbh camp booking
prayagraj kumbh accommodation near sangam
prayagraj kumbh hotel near sangam
prayagraj kumbh dharamshala
prayagraj kumbh guest house
prayagraj kumbh travel package
prayagraj kumbh tour package
prayagraj kumbh cab booking
prayagraj kumbh sightseeing

prayagraj tourism hotel
prayagraj hotels
hotels in prayagraj
best hotels in prayagraj
hotels near sangam prayagraj
hotel near triveni sangam
hotel near prayagraj sangam
hotels near prayagraj sangam
hotel near bade hanuman mandir
hotel near sangam ghat
hotel near prayagraj junction
hotel near prayagraj railway station
hotel near allahabad fort
hotel near anand bhawan prayagraj
hotel near khusro bagh
budget hotels in prayagraj
cheap hotels in prayagraj
best budget hotel prayagraj
family hotel prayagraj
family hotels in prayagraj
couple friendly hotels prayagraj
luxury hotels in prayagraj
best hotels near sangam
prayagraj hotel booking
prayagraj hotel booking online
prayagraj stay
where to stay in prayagraj
best area to stay in prayagraj
best place to stay in prayagraj
prayagraj accommodation
prayagraj dharamshala
dharamshala in prayagraj
prayagraj ashram stay
prayagraj guest house
guest house in prayagraj
prayagraj tourist bungalow
tourist bungalow prayagraj
up tourist bungalow prayagraj
prayagraj accommodation near sangam
stay near triveni sangam
stay near sangam prayagraj

prayagraj junction
prayagraj railway station
prayagraj railway station to sangam
prayagraj junction to sangam
prayagraj junction to triveni sangam
prayagraj junction to bade hanuman mandir
prayagraj junction to anand bhawan
prayagraj junction to allahabad fort
prayagraj junction to khusro bagh
prayagraj junction to airport
prayagraj railway station to sangam distance
prayagraj junction to sangam distance
prayagraj junction to triveni sangam distance
prayagraj railway station to sangam route
prayagraj station to sangam kaise jaye
prayagraj junction se sangam kaise jaye
allahabad junction
allahabad junction to sangam
allahabad railway station to sangam
allahabad station to sangam
prayag station prayagraj
prayag station to sangam
prayagraj rambagh
prayagraj rambagh station
prayagraj chheoki
prayagraj chheoki railway station
prayagraj railway stations

varanasi to prayagraj
prayagraj to varanasi
varanasi prayagraj trip
prayagraj varanasi trip
varanasi prayagraj tour
prayagraj varanasi tour
varanasi prayagraj tour package
prayagraj varanasi tour package
varanasi to prayagraj distance
prayagraj to varanasi distance
varanasi to prayagraj road distance
prayagraj to varanasi road distance
varanasi to prayagraj train
prayagraj to varanasi train
varanasi to prayagraj bus
prayagraj to varanasi bus
varanasi to prayagraj taxi
prayagraj to varanasi taxi
varanasi to prayagraj cab
prayagraj to varanasi cab
prayagraj to varanasi by road
varanasi to prayagraj by road
prayagraj varanasi one day trip
varanasi prayagraj one day trip
prayagraj varanasi two day trip
varanasi prayagraj two day trip
prayagraj varanasi combined tour
varanasi prayagraj combined tour
varanasi prayagraj sangam tour

prayagraj to ayodhya
ayodhya to prayagraj
prayagraj ayodhya trip
ayodhya prayagraj trip
prayagraj ayodhya tour
ayodhya prayagraj tour
prayagraj ayodhya tour package
ayodhya prayagraj tour package
prayagraj to ayodhya distance
ayodhya to prayagraj distance
prayagraj to ayodhya road distance
ayodhya to prayagraj road distance
prayagraj to ayodhya train
ayodhya to prayagraj train
prayagraj to ayodhya bus
ayodhya to prayagraj bus
prayagraj to ayodhya taxi
ayodhya to prayagraj taxi
prayagraj to ayodhya cab
ayodhya to prayagraj cab
prayagraj to ayodhya by road
ayodhya to prayagraj by road
prayagraj ayodhya one day trip
ayodhya prayagraj one day trip
prayagraj ayodhya two day trip
ayodhya prayagraj two day trip
prayagraj ayodhya combined tour
ayodhya prayagraj combined tour
ayodhya prayagraj sangam tour

prayagraj to chitrakoot
chitrakoot to prayagraj
prayagraj chitrakoot trip
chitrakoot prayagraj trip
prayagraj chitrakoot tour
chitrakoot prayagraj tour
prayagraj chitrakoot tour package
chitrakoot prayagraj tour package
prayagraj to chitrakoot distance
chitrakoot to prayagraj distance
prayagraj to chitrakoot road distance
chitrakoot to prayagraj road distance
prayagraj to chitrakoot train
chitrakoot to prayagraj train
prayagraj to chitrakoot bus
chitrakoot to prayagraj bus
prayagraj to chitrakoot taxi
chitrakoot to prayagraj taxi
prayagraj to chitrakoot cab
chitrakoot to prayagraj cab
prayagraj to chitrakoot by road
chitrakoot to prayagraj by road
prayagraj chitrakoot one day trip
chitrakoot prayagraj one day trip
prayagraj chitrakoot two day trip
prayagraj chitrakoot combined tour
chitrakoot prayagraj combined tour

prayagraj to lucknow
lucknow to prayagraj
prayagraj lucknow trip
lucknow prayagraj trip
prayagraj lucknow tour
lucknow prayagraj tour
prayagraj lucknow tour package
lucknow prayagraj tour package
prayagraj to lucknow distance
lucknow to prayagraj distance
prayagraj to lucknow train
lucknow to prayagraj train
prayagraj to lucknow bus
lucknow to prayagraj bus
prayagraj to lucknow taxi
lucknow to prayagraj taxi
prayagraj to lucknow cab
lucknow to prayagraj cab
prayagraj to lucknow by road
lucknow to prayagraj by road
prayagraj lucknow one day trip
lucknow prayagraj one day trip
prayagraj lucknow combined tour
lucknow prayagraj combined tour

prayagraj to kanpur
kanpur to prayagraj
prayagraj kanpur trip
kanpur prayagraj trip
prayagraj kanpur tour
kanpur prayagraj tour
prayagraj to kanpur distance
kanpur to prayagraj distance
prayagraj to kanpur train
kanpur to prayagraj train
prayagraj to kanpur bus
kanpur to prayagraj bus
prayagraj to kanpur taxi
kanpur to prayagraj taxi
prayagraj to kanpur cab
kanpur to prayagraj cab

prayagraj to delhi
delhi to prayagraj
prayagraj delhi trip
delhi prayagraj trip
prayagraj delhi tour
delhi prayagraj tour
prayagraj to delhi distance
delhi to prayagraj distance
prayagraj to delhi train
delhi to prayagraj train
prayagraj to delhi flight
delhi to prayagraj flight
prayagraj to delhi bus
delhi to prayagraj bus
prayagraj to delhi cab
delhi to prayagraj cab
prayagraj to delhi by road
delhi to prayagraj by road

prayagraj to noida
noida to prayagraj
prayagraj noida trip
noida prayagraj trip
prayagraj to noida distance
noida to prayagraj distance
prayagraj to noida train
noida to prayagraj train
prayagraj to noida bus
noida to prayagraj bus
prayagraj to noida cab
noida to prayagraj cab

prayagraj to agra
agra to prayagraj
prayagraj agra trip
agra prayagraj trip
prayagraj to agra distance
agra to prayagraj distance
prayagraj to agra train
agra to prayagraj train
prayagraj to agra bus
agra to prayagraj bus
prayagraj to agra cab
agra to prayagraj cab

prayagraj to gorakhpur
gorakhpur to prayagraj
prayagraj gorakhpur trip
gorakhpur prayagraj trip
prayagraj to gorakhpur distance
gorakhpur to prayagraj distance
prayagraj to gorakhpur train
gorakhpur to prayagraj train
prayagraj to gorakhpur bus
gorakhpur to prayagraj bus
prayagraj to gorakhpur cab
gorakhpur to prayagraj cab

prayagraj to satna
satna to prayagraj
prayagraj satna trip
satna prayagraj trip
prayagraj to satna distance
satna to prayagraj distance
prayagraj to satna train
satna to prayagraj train
prayagraj to satna bus
satna to prayagraj bus
prayagraj to satna cab
satna to prayagraj cab

prayagraj to rewa
rewa to prayagraj
prayagraj rewa trip
rewa prayagraj trip
prayagraj to rewa distance
rewa to prayagraj distance
prayagraj to rewa train
rewa to prayagraj train
prayagraj to rewa bus
rewa to prayagraj bus
prayagraj to rewa cab
rewa to prayagraj cab

prayagraj to jhansi
jhansi to prayagraj
prayagraj jhansi trip
jhansi prayagraj trip
prayagraj to jhansi distance
jhansi to prayagraj distance
prayagraj to jhansi train
jhansi to prayagraj train
prayagraj to jhansi bus
jhansi to prayagraj bus
prayagraj to jhansi cab
jhansi to prayagraj cab

prayagraj ayodhya varanasi tour
prayagraj varanasi ayodhya tour
ayodhya prayagraj varanasi tour
varanasi ayodhya prayagraj tour
prayagraj ayodhya chitrakoot tour
prayagraj chitrakoot ayodhya tour
ayodhya prayagraj chitrakoot tour
varanasi prayagraj chitrakoot tour
prayagraj varanasi chitrakoot tour
prayagraj ayodhya varanasi package
prayagraj varanasi ayodhya package
ayodhya prayagraj varanasi package
prayagraj ayodhya chitrakoot package
prayagraj chitrakoot ayodhya package
prayagraj varanasi chitrakoot package

prayagraj ramayan tour
prayagraj ramayan places
ramayan places in prayagraj
ramayan tourist places prayagraj
ramayan pilgrimage prayagraj
prayagraj ramayan yatra
prayagraj ramayan darshan
ramayan circuit prayagraj
ramayan tour prayagraj
prayagraj religious history
prayagraj mythological places
prayagraj mythology
prayagraj historical places
prayagraj historical tour
prayagraj heritage tour
prayagraj heritage places
prayagraj culture
prayagraj culture tourism
prayagraj history
prayagraj history tour
prayagraj historical sightseeing
allahabad history
allahabad historical places
allahabad heritage places
allahabad heritage tour

prayagraj famous for
what is prayagraj famous for
why is prayagraj famous
why prayagraj is famous
what is allahabad famous for
why is allahabad famous
prayagraj significance
prayag significance
prayagraj importance
prayag religious importance
triveni sangam significance
triveni sangam importance
why triveni sangam is famous
why is triveni sangam famous
prayagraj history and culture
prayagraj tourism information
prayagraj tourist information
prayagraj travel information
prayagraj travel tips
prayagraj tourism tips
prayagraj travel guide in english
prayagraj travel guide in hindi
prayagraj tourism guide in hindi
prayagraj tourist guide in hindi
prayagraj travel blog
prayagraj tourism blog
prayagraj places to visit in hindi
prayagraj ghumne ki jagah
allahabad ghumne ki jagah
prayagraj darshan kaise kare
prayagraj yatra kaise kare
prayagraj trip kaise plan kare
prayagraj tour kaise plan kare
prayagraj me kya kya dekhe
prayagraj mein kya kya dekhen
prayagraj me kaha ghoome
prayagraj mein kaha ghoome
prayagraj me kitne din rukna chahiye
prayagraj mein kitne din rukna chahiye
prayagraj trip kitne din ka
prayagraj tour kitne din ka
prayagraj trip budget
prayagraj trip ka kharcha
prayagraj tour ka kharcha
prayagraj ghumne ka kharcha
prayagraj darshan ka kharcha
prayagraj travel cost
prayagraj travel budget

sangam me kya hota hai
sangam mein kya hota hai
triveni sangam me kya hota hai
triveni sangam mein kya hota hai
sangam par kya dekhe
sangam par kya dekhen
sangam par kya kar sakte hain
sangam me kya kar sakte hain
triveni sangam par kya kare
triveni sangam mein kya kare
sangam kaise jaye
sangam kaise pahuche
sangam kahan hai
triveni sangam kahan hai
triveni sangam kahan padta hai
sangam prayagraj me kaha hai
sangam allahabad me kaha hai
sangam tak kaise pahuche
sangam jane kaise
sangam ghat kaise jaye
sangam me boat ride kaise kare
sangam me boating kaise kare
sangam me snan kaise kare
sangam me puja kaise kare
sangam par puja
sangam par aarti
sangam par ganga aarti
sangam darshan kaise kare
triveni sangam darshan kaise kare
triveni sangam visit kaise kare
prayagraj sangam kaise jaye
prayagraj sangam me kya dekhe

prayagraj me family ke sath ghumne ki jagah
prayagraj family tourist places
prayagraj family trip
prayagraj family tour
prayagraj kids places
prayagraj places for children
prayagraj places for kids
prayagraj couple places
prayagraj couple trip
prayagraj solo travel
prayagraj group tour
prayagraj friends trip
prayagraj weekend trip
prayagraj photography places
prayagraj photo spots
prayagraj sunset places
prayagraj sunrise places
prayagraj nature places
prayagraj riverside places
prayagraj ghat
prayagraj ghats
famous ghats in prayagraj
prayagraj ganga ghat
prayagraj yamuna ghat
prayagraj riverfront
prayagraj riverside tourism

daraganj prayagraj
daraganj allahabad
daraganj ghat prayagraj
daraganj ghat allahabad
rasulabad ghat prayagraj
rasulabad ghat allahabad
saraswati ghat prayagraj
saraswati ghat allahabad
ram ghat prayagraj
ram ghat allahabad
sangam ghat prayagraj
yamuna ghat prayagraj
ganga ghat prayagraj
prayagraj ghat tourism
prayagraj ghat sightseeing
prayagraj ghat aarti
prayagraj ghat boating
prayagraj ghat visit

prayagraj river cruise
prayagraj boat ride
prayagraj boating
prayagraj boating price
prayagraj boating timing
prayagraj boat booking
prayagraj boat ride price
prayagraj boat ride timing
prayagraj boat tour
prayagraj river boating
allahabad boating
allahabad boat ride
allahabad boat booking
allahabad boating price
allahabad boating timing

prayagraj restaurants
best restaurants in prayagraj
restaurants near sangam prayagraj
restaurants near triveni sangam
food in prayagraj
famous food in prayagraj
prayagraj famous food
what to eat in prayagraj
prayagraj street food
best food in prayagraj
prayagraj vegetarian food
prayagraj food places
prayagraj cafes
best cafes in prayagraj
cafes in civil lines prayagraj
restaurants in civil lines prayagraj
food near sangam prayagraj
food near prayagraj junction
vegetarian restaurants prayagraj
pure veg restaurants prayagraj

prayagraj shopping
shopping in prayagraj
prayagraj market
famous markets in prayagraj
best market in prayagraj
prayagraj local market
prayagraj souvenirs
prayagraj shopping places
civil lines prayagraj shopping
prayagraj local shopping
what to buy in prayagraj
things to buy in prayagraj
prayagraj handicrafts
prayagraj local products

prayagraj travel agency
travel agency in prayagraj
best travel agency in prayagraj
prayagraj tour operator
tour operator in prayagraj
prayagraj travel company
prayagraj tour company
prayagraj tour and travels
prayagraj tour travels
tour and travels prayagraj
travel agent prayagraj
travel agents in prayagraj
prayagraj tourist agency
prayagraj tourism agency
prayagraj pilgrimage tour operator
prayagraj yatra booking
prayagraj tour booking
prayagraj trip booking
prayagraj sightseeing booking
prayagraj cab booking
prayagraj taxi booking
prayagraj car rental
car rental prayagraj
prayagraj tempo traveller
tempo traveller prayagraj
prayagraj bus rental
prayagraj taxi for sightseeing
prayagraj cab for sightseeing
prayagraj local transport
prayagraj local sightseeing cab
prayagraj darshan booking
prayagraj temple darshan booking
prayagraj sangam tour booking
triveni sangam tour booking
prayagraj tour booking online
prayagraj travel booking online
prayagraj tour operator near me
travel agency near prayagraj
tour operator near prayagraj

allahabad travel agency
travel agency in allahabad
allahabad tour operator
tour operator in allahabad
allahabad tour and travels
allahabad travel agent
allahabad travel company
allahabad tourism agency
allahabad tour booking
allahabad sightseeing booking
allahabad cab booking
allahabad taxi booking
allahabad car rental
allahabad tempo traveller

prayagraj to sangam cab
prayagraj to sangam taxi
prayagraj to sangam auto
prayagraj to sangam distance
prayagraj to sangam route
prayagraj city to sangam distance
civil lines to sangam distance
prayagraj junction to sangam distance
prayag station to sangam distance
airport to sangam prayagraj distance
sangam to prayagraj junction
sangam to prayagraj railway station
sangam to prayagraj airport
sangam to civil lines
sangam to allahabad junction

prayagraj airport to sangam cab
prayagraj airport to sangam taxi
prayagraj junction to sangam cab
prayagraj junction to sangam taxi
prayagraj railway station to sangam cab
prayagraj railway station to sangam taxi
prayagraj station to sangam cab
prayagraj station to sangam taxi

prayagraj to ayodhya distance
prayagraj to varanasi distance
prayagraj to chitrakoot distance
prayagraj to lucknow distance
prayagraj to kanpur distance
prayagraj to delhi distance
prayagraj to noida distance
prayagraj to agra distance
prayagraj to gorakhpur distance
prayagraj to satna distance
prayagraj to rewa distance
prayagraj to jhansi distance
prayagraj to mirzapur distance
prayagraj to kaushambi distance
prayagraj to shringverpur distance
prayagraj to vindhyachal distance
prayagraj to chitrakoot by road
prayagraj to ayodhya by road
prayagraj to varanasi by road
prayagraj to lucknow by road
prayagraj to kanpur by road
prayagraj to delhi by road

prayagraj nearby places
places near prayagraj
places near allahabad
tourist places near prayagraj
tourist places near allahabad
weekend places near prayagraj
weekend destinations near prayagraj
day trips from prayagraj
one day trips from prayagraj
places to visit near prayagraj
places to visit near allahabad
nearby tourist places prayagraj
nearby tourist attractions prayagraj
prayagraj nearby tourist places
prayagraj nearby destinations
prayagraj day trip
prayagraj weekend destinations
shrungverpur near prayagraj
kaushambi near prayagraj
vindhyachal near prayagraj
chitrakoot near prayagraj
ayodhya near prayagraj
varanasi near prayagraj

prayagraj tourist circuit
prayagraj tourism circuit
prayagraj pilgrimage circuit
prayagraj religious circuit
prayagraj temple circuit
prayagraj sangam circuit
prayagraj heritage circuit
prayagraj historical circuit
prayagraj ramayan circuit
prayagraj weekend circuit

prayagraj tourism in hindi
prayagraj tour in hindi
prayagraj trip in hindi
prayagraj darshan in hindi
prayagraj yatra in hindi
prayagraj sightseeing in hindi
prayagraj tourist places in hindi
prayagraj ghumne ki jagah
prayagraj ke darshaniya sthal
prayagraj ke prasiddh sthal
prayagraj ke famous mandir
prayagraj ke famous temple
prayagraj ke tourist places
prayagraj mein ghumne ki jagah
prayagraj mein darshan ki jagah
prayagraj mein dekhne layak jagah
prayagraj mein kya kya hai
prayagraj mein kya famous hai
prayagraj ka famous mandir
prayagraj ka famous tourist place
prayagraj ka sangam
prayagraj ka triveni sangam
prayagraj ki yatra
prayagraj ka tour
prayagraj ka trip
prayagraj ghumne ka plan
prayagraj ghumne ka best time
prayagraj jane ka best time
prayagraj jane kaise
prayagraj kaise jaye
prayagraj kaise pahuche
prayagraj me kaha ruke
prayagraj mein kaha ruke
prayagraj me hotel
prayagraj mein hotel
prayagraj me kya dekhe
prayagraj mein kya dekhen
prayagraj me kaha ghoome
prayagraj mein kaha ghoome
prayagraj me kitne din
prayagraj mein kitne din
prayagraj me ek din me kya dekhe
prayagraj mein ek din mein kya dekhen
prayagraj me do din me kya dekhe
prayagraj mein do din mein kya dekhen
prayagraj me teen din me kya dekhe
prayagraj mein teen din mein kya dekhen

allahabad tourism in hindi
allahabad tour in hindi
allahabad trip in hindi
allahabad darshan in hindi
allahabad yatra in hindi
allahabad tourist places in hindi
allahabad ghumne ki jagah
allahabad ke darshaniya sthal
allahabad ke famous mandir
allahabad mein kya dekhen
allahabad mein ghumne ki jagah
allahabad mein kaha ghoome
allahabad ka sangam
allahabad ka triveni sangam
allahabad ka tour
allahabad ka trip
allahabad kaise jaye
allahabad me kaha ruke
allahabad me hotel

prayagraj places to visit with family
prayagraj places to visit with friends
prayagraj places to visit with kids
prayagraj places to visit for couples
prayagraj best tourist places for family
prayagraj family sightseeing
prayagraj family sightseeing tour
prayagraj family sightseeing package
prayagraj family darshan
prayagraj family pilgrimage
prayagraj temple sightseeing
prayagraj religious sightseeing
prayagraj historical sightseeing
prayagraj heritage sightseeing
prayagraj cultural sightseeing

prayagraj photography
prayagraj photography places
prayagraj photo spots
prayagraj instagram places
prayagraj instagrammable places
prayagraj scenic places
prayagraj beautiful places
prayagraj sunset point
prayagraj sunrise point
prayagraj river view
prayagraj sangam view
triveni sangam sunrise
triveni sangam sunset
prayagraj night view
prayagraj night sightseeing
new yamuna bridge night view
sangam sunset
sangam sunrise
sangam photography

prayagraj festival
festivals in prayagraj
prayagraj religious festivals
prayagraj mela
prayagraj fair
prayagraj magh mela
prayagraj kumbh
prayagraj maha kumbh
prayagraj religious festival
prayagraj cultural festival
prayagraj events
prayagraj festival tourism

prayagraj morning sightseeing
prayagraj evening sightseeing
prayagraj morning tour
prayagraj evening tour
prayagraj night tour
prayagraj evening tour package
prayagraj morning darshan
prayagraj evening darshan
prayagraj temple morning darshan
prayagraj sangam morning
prayagraj sangam evening
prayagraj sangam sunset tour
prayagraj sangam sunrise tour

prayagraj tour from varanasi
prayagraj day trip from varanasi
prayagraj one day trip from varanasi
prayagraj tour from ayodhya
prayagraj day trip from ayodhya
prayagraj one day trip from ayodhya
prayagraj tour from lucknow
prayagraj day trip from lucknow
prayagraj one day trip from lucknow
prayagraj tour from chitrakoot
prayagraj day trip from chitrakoot
prayagraj one day trip from chitrakoot
prayagraj tour from kanpur
prayagraj day trip from kanpur
prayagraj tour from delhi
prayagraj day trip from delhi
prayagraj tour from noida
prayagraj day trip from noida

varanasi prayagraj sangam
varanasi to prayagraj sangam
ayodhya prayagraj sangam
ayodhya to prayagraj sangam
chitrakoot prayagraj sangam
chitrakoot to prayagraj sangam
lucknow prayagraj sangam
lucknow to prayagraj sangam
prayagraj sangam tour from varanasi
prayagraj sangam tour from ayodhya
prayagraj sangam tour from chitrakoot
prayagraj sangam tour from lucknow
prayagraj sangam package from varanasi
prayagraj sangam package from ayodhya
prayagraj sangam package from chitrakoot
prayagraj sangam package from lucknow

prayagraj temple list
prayagraj famous temple list
prayagraj mandir list
famous mandir in prayagraj
famous temples in allahabad
allahabad temple list
prayagraj shakti peeth
prayagraj shaktipeeth
shakti peeth in prayagraj
shakti peeth prayagraj temples
prayagraj jyotirlinga
prayagraj mahadev temple
prayagraj shiv temple
prayagraj hanuman temple
prayagraj devi temple
prayagraj durga temple
prayagraj ram temple
prayagraj krishna temple
prayagraj ancient temples
ancient temples in prayagraj
old temples in prayagraj
old temples in allahabad
famous religious places in prayagraj
holy temples in prayagraj

what to see in prayagraj
things to do in prayagraj
things to do in allahabad
activities in prayagraj
activities in allahabad
prayagraj tourist activities
prayagraj sightseeing activities
prayagraj travel experiences
prayagraj tourism experience
prayagraj things to do with family
prayagraj things to do with kids
prayagraj things to do for couples
prayagraj things to do in one day
prayagraj things to do at night
prayagraj things to do in evening
prayagraj things to do near sangam
things to do near triveni sangam
things to do near prayagraj junction
"""

# Extract & deduplicate keywords
keywords_list = [k.strip() for k in raw_keywords_text.strip().split('\n') if k.strip()]
print(f"Total Prayagraj Keywords Loaded: {len(keywords_list)}")

file_path = "/Users/rishabhjaiswal/ayodhya-darshan/prayagraj-tour-package.html"

# Generate chip badges HTML
chip_badges = []
svg_icon = '<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>'

for k in keywords_list:
    chip = f'<span style="display:inline-flex; align-items:center; gap:6px; padding:5px 12px; background:var(--bg-panel); border:1px solid var(--line); border-radius:20px; font-size:0.82rem; color:var(--ink-2); font-weight:500;">{svg_icon}<span>{k}</span></span>'
    chip_badges.append(chip)

chips_html = "\n        ".join(chip_badges)

enriched_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Prayagraj Tour Package 2026: Triveni Sangam, Bade Hanuman & Kumbh Yatra</title>
  <meta name="description" content="Book Prayagraj Tour Package 2026. Private boat to Triveni Sangam snan, Bade Hanumanji darshan, Akshayavat, Anand Bhawan & Kumbh Mela arrangements. Private AC cab & top hotel booking.">
  <meta name="keywords" content="prayagraj tour package, triveni sangam boat booking, prayagraj same day tour, sangam snan package, prayagraj kumbh yatra, bade hanuman mandir prayagraj, anand bhawan tour">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="https://www.ayodhyadharshan.com/prayagraj-tour-package.html">

  <link rel="shortcut icon" href="favicon.ico" type="image/x-icon">
  <link rel="icon" href="favicon.png" type="image/png" sizes="192x192">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">

  <link rel="stylesheet" href="css/style.css">
  <script src="conversion-tracker.js" defer></script>
  <script src="image-slot.js" defer></script>

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "TouristAttraction",
    "name": "Tirtharaj Prayagraj Yatra & Triveni Sangam",
    "description": "Guided pilgrimage yatra in Prayagraj covering Triveni Sangam snan, Bade Hanuman temple, Akshayavat, and Anand Bhawan.",
    "url": "https://www.ayodhyadharshan.com/prayagraj-tour-package.html",
    "touristType": ["Pilgrim", "Heritage Tourist"],
    "geo": {{
      "@type": "GeoCoordinates",
      "latitude": 25.4358,
      "longitude": 81.8463
    }}
  }}
  </script>
</head>
<body>

<!-- Header / Navigation -->
<header class="hdr" id="siteHeader">
  <div class="container hdr-in">
    <a href="index.html" class="brand">
      <img src="assets/logo.webp" alt="Ayodhya Dharshan Logo" width="44" height="44">
      <div class="brand-txt">
        <span class="b-title">AYODHYA DHARSHAN</span>
        <span class="b-sub">Teerth Yatra Seva</span>
      </div>
    </a>
    <nav class="nav-links" id="navLinks">
      <a href="index.html">Home</a>
      <a href="destinations.html" class="active">Destinations</a>
      <a href="services.html">Packages</a>
      <a href="yatra-cost-calculator.html">Cost Estimator</a>
      <a href="about.html">About Us</a>
      <a href="blog.html">Blog</a>
      <a href="contact.html">Contact</a>
    </nav>
    <a href="https://wa.me/919235222399?text=Jai%20Shree%20Ram!%20I%20want%20to%20book%20a%20Prayagraj%20Tour%20Package." class="btn btn-sm btn-gold" target="_blank" rel="noopener">Book Yatra ➔</a>
    <button class="nav-toggle" id="navToggle" aria-label="Toggle navigation"><span></span><span></span><span></span></button>
  </div>
</header>

<!-- Hero Section -->
<section class="dest-hero" style="background: linear-gradient(180deg, rgba(15, 23, 42, 0.75) 0%, rgba(15, 23, 42, 0.9) 100%), url('assets/destinations/triveni-sangam.webp') center/cover no-repeat; padding: 100px 0 60px; color: #fff; text-align: center;">
  <div class="container">
    <span class="tag" style="background: rgba(212, 175, 55, 0.2); color: var(--gold); border: 1px solid var(--gold); padding: 6px 16px; border-radius: 20px; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 1px;">Holy Confluence of Sacred Rivers</span>
    <h1 style="font-family: var(--font-display); font-size: 2.8rem; margin: 20px 0 15px; color: #fff;">Prayagraj Tour Package — Triveni Sangam & Tirtharaj Yatra</h1>
    <p style="max-width: 780px; margin: 0 auto 30px; font-size: 1.1rem; opacity: 0.95; line-height: 1.7;">Experience the divine energy of Tirtharaj Prayagraj (Allahabad). Enjoy a private motorboat ride to Triveni Sangam for holy snan (dip), VIP darshan at the legendary Bade Hanuman Mandir & Akshayavat, and seamless local AC cab transfers.</p>
    <div style="display: flex; gap: 15px; justify-content: center; flex-wrap: wrap;">
      <a href="https://wa.me/919235222399?text=Jai%20Shree%20Ram!%20Please%20send%20Prayagraj%20tour%20package%20details." class="btn btn-gold btn-lg" target="_blank" rel="noopener">Book Prayagraj Tour (₹1,499) ➔</a>
      <a href="tel:+919235222399" class="btn btn-outline btn-lg" style="color:#fff; border-color:#fff;">Call +91 92352 22399</a>
    </div>
  </div>
</section>

<!-- Content & Key Highlights -->
<section class="section">
  <div class="container">
    <div style="max-width: 900px; margin: 0 auto;">
      <h2 style="font-family: var(--font-display); color: var(--maroon); margin-bottom: 20px; text-align: center;">Sacred Highlights of Prayagraj Pilgrimage</h2>
      <p style="text-align: center; font-size: 1.05rem; color: var(--ink-2); margin-bottom: 40px;">Prayagraj is the king of all pilgrimage sites (Tirtharaj), where the sacred Ganga, Yamuna, and mystical Saraswati meet. Our customized tour packages ensure comfort, priority boat rides, and hassle-free darshan.</p>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 24px; margin-bottom: 50px;">
        <div style="background: var(--bg-card); border: 1px solid var(--line); padding: 24px; border-radius: var(--r-md); box-shadow: 0 4px 12px rgba(0,0,0,0.04);">
          <h3 style="color: var(--maroon); font-size: 1.25rem; margin-bottom: 10px;">⛵ Triveni Sangam Private Boat Snan</h3>
          <p style="font-size: 0.95rem; color: var(--ink-2); line-height: 1.6;">Board a private motorboat with life jackets and dedicated priests to reach the exact confluence point for holy bath and rituals.</p>
        </div>
        <div style="background: var(--bg-card); border: 1px solid var(--line); padding: 24px; border-radius: var(--r-md); box-shadow: 0 4px 12px rgba(0,0,0,0.04);">
          <h3 style="color: var(--maroon); font-size: 1.25rem; margin-bottom: 10px;">🚩 Bade Hanuman Ji & Akshayavat</h3>
          <p style="font-size: 0.95rem; color: var(--ink-2); line-height: 1.6;">Seek blessings at the unique reclining (Letee Hue) Hanuman Temple on the banks of Sangam and visit the indestructible tree Akshayavat inside Patalpuri Mandir.</p>
        </div>
        <div style="background: var(--bg-card); border: 1px solid var(--line); padding: 24px; border-radius: var(--r-md); box-shadow: 0 4px 12px rgba(0,0,0,0.04);">
          <h3 style="color: var(--maroon); font-size: 1.25rem; margin-bottom: 10px;">🏛️ Anand Bhawan & Swaraj Bhawan</h3>
          <p style="font-size: 0.95rem; color: var(--ink-2); line-height: 1.6;">Explore the ancestral home of the Nehru family, Jawahar Planetarium, and Chandra Shekhar Azad Park (Company Bagh).</p>
        </div>
        <div style="background: var(--bg-card); border: 1px solid var(--line); padding: 24px; border-radius: var(--r-md); box-shadow: 0 4px 12px rgba(0,0,0,0.04);">
          <h3 style="color: var(--maroon); font-size: 1.25rem; margin-bottom: 10px;">🛕 Alopi Devi & Mankameshwar Mandir</h3>
          <p style="font-size: 0.95rem; color: var(--ink-2); line-height: 1.6;">Darshan at the sacred Alopi Devi Shakti Peeth, Nagvasuki Temple, and historic Mankameshwar Mahadev Temple.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Detailed Itinerary Section -->
<section class="section" style="background: var(--bg-panel); border-top: 1px solid var(--line); border-bottom: 1px solid var(--line);">
  <div class="container" style="max-width: 850px;">
    <h2 style="font-family: var(--font-display); color: var(--maroon); text-align: center; margin-bottom: 30px;">Sample Prayagraj 1-Day Itinerary</h2>
    <div style="display: flex; flex-direction: column; gap: 20px;">
      <div style="background: #fff; border-left: 4px solid var(--gold); padding: 20px; border-radius: 0 var(--r-md) var(--r-md) 0; box-shadow: 0 2px 8px rgba(0,0,0,0.03);">
        <strong style="color: var(--maroon); font-size: 1.1rem;">07:00 AM — Pick-up & Sangam Transfer</strong>
        <p style="margin-top: 6px; font-size: 0.95rem; color: var(--ink-2);">Our private AC cab picks you up from Prayagraj Junction (PRYJ), Airport, or hotel and proceeds to VIP Sangam Ghat.</p>
      </div>
      <div style="background: #fff; border-left: 4px solid var(--gold); padding: 20px; border-radius: 0 var(--r-md) var(--r-md) 0; box-shadow: 0 2px 8px rgba(0,0,0,0.03);">
        <strong style="color: var(--maroon); font-size: 1.1rem;">08:00 AM — Triveni Sangam Holy Snan & Boat Ride</strong>
        <p style="margin-top: 6px; font-size: 0.95rem; color: var(--ink-2);">Board a reserved motorboat for the holy confluence of Ganga, Yamuna & Saraswati. Perform snan, rituals, and bird feeding.</p>
      </div>
      <div style="background: #fff; border-left: 4px solid var(--gold); padding: 20px; border-radius: 0 var(--r-md) var(--r-md) 0; box-shadow: 0 2px 8px rgba(0,0,0,0.03);">
        <strong style="color: var(--maroon); font-size: 1.1rem;">10:30 AM — Bade Hanuman, Akshayavat & Patalpuri Darshan</strong>
        <p style="margin-top: 6px; font-size: 0.95rem; color: var(--ink-2);">Darshan at Letee Hue Bade Hanuman Mandir, followed by Akshayavat tree and Patalpuri Temple inside Prayagraj Fort complex.</p>
      </div>
      <div style="background: #fff; border-left: 4px solid var(--gold); padding: 20px; border-radius: 0 var(--r-md) var(--r-md) 0; box-shadow: 0 2px 8px rgba(0,0,0,0.03);">
        <strong style="color: var(--maroon); font-size: 1.1rem;">01:30 PM — Sattvic Lunch & Heritage Sightseeing</strong>
        <p style="margin-top: 6px; font-size: 0.95rem; color: var(--ink-2);">Enjoy traditional North Indian pure vegetarian lunch, then visit Anand Bhawan museum, Swaraj Bhawan, and Chandra Shekhar Azad Park.</p>
      </div>
      <div style="background: #fff; border-left: 4px solid var(--gold); padding: 20px; border-radius: 0 var(--r-md) var(--r-md) 0; box-shadow: 0 2px 8px rgba(0,0,0,0.03);">
        <strong style="color: var(--maroon); font-size: 1.1rem;">05:30 PM — Sangam Evening Ganga Aarti & Drop</strong>
        <p style="margin-top: 6px; font-size: 0.95rem; color: var(--ink-2);">Witness divine evening Ganga Aarti on Triveni Sangam Ghat before drop back at Railway Station or Ayodhya / Varanasi transfer.</p>
      </div>
    </div>
  </div>
</section>

<!-- Collapsible Master Search Index Section (Collapsible Accordion with Visual Chip Tags) -->
<section class="section" style="padding: 50px 0;">
  <div class="container">
    <details style="background:var(--bg-card); border:1px solid var(--line); border-radius:var(--r-md); padding:22px 26px; cursor:pointer; box-shadow: 0 4px 15px rgba(0,0,0,0.03);">
      <summary style="display:flex; align-items:center; justify-content:space-between; list-style:none; outline:none; font-weight:700; color:var(--maroon); font-size:1.15rem; font-family:var(--font-display);">
        <span style="display:flex; align-items:center; gap:10px;">
          <span style="font-size:1.4rem;">🔍</span>
          <span>Prayagraj Tourism & Pilgrimage Master Search Index</span>
        </span>
        <span style="background:rgba(122,28,28,0.08); border:1px solid var(--line); color:var(--maroon); padding:4px 14px; border-radius:20px; font-size:0.82rem; font-weight:600; font-family:var(--font-sans);">Explore 500+ Topics (Read More ▾)</span>
      </summary>
      
      <div style="margin-top:24px; padding-top:20px; border-top:1px solid var(--line);">
        <p style="font-size:0.9rem; color:var(--ink-2); margin-bottom:18px; line-height:1.5;">Comprehensive index of search queries, destinations, temples, transport routes, and booking details for Prayagraj (Allahabad) pilgrimages:</p>
        <div style="display:flex; flex-wrap:wrap; gap:8px;">
        {chips_html}
        </div>
      </div>
    </details>
  </div>
</section>

<!-- CTA Callout -->
<section class="section" style="background: linear-gradient(135deg, var(--maroon) 0%, #4A1010 100%); color: #fff; text-align: center; padding: 60px 0;">
  <div class="container">
    <h2 style="font-family: var(--font-display); font-size: 2.2rem; color: var(--gold); margin-bottom: 15px;">Plan Your Sacred Prayagraj Yatra Today</h2>
    <p style="max-width: 650px; margin: 0 auto 30px; font-size: 1.05rem; opacity: 0.9;">Clean hotels, private AC cabs, boat booking at Sangam, and personalized assistance. Tailor-made for families and senior citizens.</p>
    <a href="https://wa.me/919235222399?text=Jai%20Shree%20Ram!%20I%20want%20to%20plan%20my%20Prayagraj%20Yatra." class="btn btn-gold btn-lg" target="_blank" rel="noopener">Connect on WhatsApp (+91 92352 22399) ➔</a>
  </div>
</section>

<!-- Footer -->
<footer class="foot">
  <div class="container foot-grid">
    <div>
      <div class="brand-txt" style="margin-bottom: 12px;">
        <span class="b-title" style="color:#fff;">AYODHYA DHARSHAN</span>
      </div>
      <p>Soulful, fully-managed pilgrimages across the holiest cities of Uttar Pradesh — guided with reverence and care.</p>
    </div>
    <div><h4>Explore</h4>
      <a href="destinations.html">Destinations</a>
      <a href="services.html">Services</a>
      <a href="yatra-cost-calculator.html">Calculator</a>
      <a href="about.html">About Us</a>
      <a href="blog.html">Blog</a>
      <a href="contact.html">Contact</a>
    </div>
    <div><h4>Cities</h4>
      <a href="ayodhya-dharshan-tour-package.html">Ayodhya</a>
      <a href="varanasi-same-day-tour-package.html">Varanasi</a>
      <a href="prayagraj-tour-package.html">Prayagraj</a>
      <a href="chitrakoot-tour-package.html">Chitrakoot</a>
      <a href="naimisharanya-tour-package.html">Naimisharanya</a>
      <a href="vindhyachal-tour-package.html">Vindhyachal</a>
      <a href="mathura-tour-package.html">Mathura</a>
      <a href="vrindavan-tour-package.html">Vrindavan</a>
    </div>
    <div><h4>Reach Us</h4>
      <a href="tel:+919235222399">+91 92352 22399</a>
      <a href="mailto:yatra@ayodhyadharshan.com">yatra@ayodhyadharshan.com</a>
      <a href="contact.html">RTO Office, Ayodhya</a>
      <a href="https://share.google/Q6wXLDvNd2VDOzNUp" target="_blank" rel="noopener">Find us on Google Maps</a>
      <a href="https://wa.me/919235222399?text=Jai%20Shree%20Ram!%20I%20want%20to%20enquire%20about%20Prayagraj%20tour%20package." target="_blank" rel="noopener">WhatsApp · 24×7</a>
    </div>
  </div>
  <div class="container foot-bottom">
    <span>© 2026 Ayodhya Dharshan · Teerth Yatra Seva</span>
    <span>॥ श्री राम जय राम जय जय राम ॥</span>
  </div>
</footer>

<script>
const navToggle=document.getElementById('navToggle'), navLinks=document.getElementById('navLinks');
navToggle?.addEventListener('click',()=>navLinks.classList.toggle('open'));
</script>

</body>
</html>
"""

with open(file_path, "w", encoding="utf-8") as f:
    f.write(enriched_html)

print("Enriched prayagraj-tour-package.html successfully!")

# Verification step
matched = 0
missing = []
for k in keywords_list:
    if k.lower() in enriched_html.lower():
        matched += 1
    else:
        missing.append(k)

pct = (matched / len(keywords_list)) * 100
print(f"Total Prayagraj Keywords Verified: {matched}/{len(keywords_list)} ({pct:.1f}%)")
if missing:
    print(f"Missing ({len(missing)}): {missing[:10]}")
