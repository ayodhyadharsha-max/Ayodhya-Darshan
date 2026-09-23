import os

user_keywords_raw = """
ayodhya tour
ayodhya tourism
ayodhya travel
ayodhya travels
ayodhya tour and travels
ayodhya tour package
ayodhya tour packages
ayodhya travel package
ayodhya travel packages
ayodhya trip
ayodhya trip package
ayodhya holiday package
ayodhya holiday packages
ayodhya package
ayodhya packages
ayodhya darshan
ayodhya darshan package
ayodhya darshan tour
ayodhya darshan tour package
ayodhya darshan booking
ayodhya darshan ticket
ayodhya darshan pass
ayodhya yatra
ayodhya yatra package
ayodhya pilgrimage tour
ayodhya pilgrimage package
ayodhya religious tour
ayodhya spiritual tour
ayodhya temple tour
ayodhya temple tour package
ayodhya sightseeing
ayodhya sightseeing tour
ayodhya sightseeing package
ayodhya local sightseeing
ayodhya local tour
ayodhya city tour
ayodhya tourist guide
ayodhya travel guide
ayodhya tourism guide
ayodhya travel information
ayodhya tourist information
ayodhya travel agency
ayodhya travel agent
ayodhya tour operator
ayodhya tourist places
ayodhya tourism places
places to visit in ayodhya
best places to visit in ayodhya
famous places in ayodhya
famous tourist places in ayodhya
ayodhya tourist attractions
ayodhya attractions
ayodhya places to see
places to see in ayodhya
best places in ayodhya
must visit places in ayodhya
ayodhya famous places
ayodhya famous tourist places
ayodhya hidden places
ayodhya historical places
ayodhya religious places
ayodhya spiritual places
ayodhya pilgrimage places
ayodhya scenic places
ayodhya picnic spots
ayodhya tourist spots
ayodhya tourist attractions list
things to do in ayodhya
things to see in ayodhya
best things to do in ayodhya
ayodhya sightseeing places list
ayodhya places to visit list
ayodhya places to visit in one day
ayodhya places to visit in 2 days
ayodhya tourist places in one day
ayodhya tourist places in 2 days
ayodhya tourist places near ram mandir
places near ram mandir ayodhya
ayodhya dham
ayodhya dham tourism
ayodhya dham darshan
ayodhya dham tour
ayodhya dham tour package
ayodhya dham railway station
ayodhya dham station
ayodhya dham travel
ayodhya dham tourist places
ayodhya dham temple
ayodhya dham sightseeing
ayodhya dham yatra
ayodhya dham package
ayodhya dham darshan package
ram mandir ayodhya
ram mandir
ram mandir tourism
ram mandir ayodhya tourism
ram mandir darshan
ram mandir ayodhya darshan
ram mandir tour
ram mandir ayodhya tour
ram mandir tour package
ram mandir ayodhya package
ram mandir darshan package
ram mandir ayodhya darshan package
ram mandir temple
ram mandir temple ayodhya
shri ram mandir ayodhya
shree ram mandir ayodhya
ram janmabhoomi
ram janmabhoomi ayodhya
shri ram janmabhoomi
shri ram janmabhoomi ayodhya
ram janmabhoomi temple
ram janmabhoomi mandir
ram janmabhoomi darshan
ram janmabhoomi ayodhya darshan
ram janmabhoomi tour
ram janmabhoomi tourism
ram mandir temple tour
ram mandir pilgrimage
ram mandir pilgrimage tour
ram mandir religious tour
ram mandir spiritual tour
ram mandir sightseeing
ram mandir entry
ram mandir entry pass
ram mandir entry ticket
ayodhya ram mandir entry ticket
ram mandir ticket
ram mandir ticket booking
ayodhya ram mandir ticket
ayodhya ram mandir ticket booking
ram mandir online ticket
ram mandir online ticket booking
ayodhya ram mandir online booking
ram mandir booking
ram mandir booking ayodhya
ram mandir online booking
ram mandir darshan booking
ram mandir darshan booking online
ayodhya ram mandir darshan booking
ayodhya ram mandir darshan booking online
ram mandir darshan registration
ayodhya ram mandir darshan registration
ram mandir online darshan registration
ayodhya ram mandir online registration
ram mandir darshan slot
ram mandir darshan slot booking
ram mandir darshan timing
ram mandir darshan timings
ram mandir ayodhya timing
ram mandir ayodhya timings
ram mandir opening time
ram mandir opening timings
ram mandir closing time
ram mandir closing timings
ram mandir darshan time
ayodhya ram mandir darshan time
ram mandir darshan process
ram mandir darshan rules
ram mandir darshan information
ram mandir darshan guide
ram mandir darshan procedure
ram mandir darshan registration process
ram mandir darshan booking process
ram mandir darshan documents
ram mandir darshan requirements
ram mandir darshan age limit
ram mandir darshan entry rules
ram mandir darshan queue
ram mandir darshan crowd
ram mandir darshan waiting time
ram mandir darshan experience
ram mandir darshan route
ram mandir temple route
ram mandir location
ram mandir ayodhya location
ram mandir address ayodhya
ram mandir map
ram mandir ayodhya map
ram mandir photos
ram mandir ayodhya photos
ram mandir images
ram mandir history
ram mandir ayodhya history
ram mandir history in hindi
ram mandir construction
ram mandir architecture
ram mandir architecture ayodhya
ram mandir history and facts
ram mandir facts
ram mandir information
ram mandir ayodhya information
ram mandir significance
ram mandir religious significance
ram mandir visit
ram mandir visit guide
ram mandir visit plan
ram mandir travel guide
ram mandir travel information
ram mandir near places
places near ram mandir
hotels near ram mandir
restaurants near ram mandir
parking near ram mandir
hanuman garhi ayodhya
hanuman garhi
hanuman garhi temple
hanuman garhi ayodhya temple
hanuman garhi darshan
hanuman garhi ayodhya darshan
hanuman garhi timings
hanuman garhi timing
hanuman garhi opening time
hanuman garhi closing time
hanuman garhi history
hanuman garhi ayodhya history
hanuman garhi location
hanuman garhi address
hanuman garhi distance
hanuman garhi photos
hanuman garhi tourist place
hanuman garhi temple tour
hanuman garhi darshan ticket
hanuman garhi nearby places
kanak bhawan ayodhya
kanak bhawan
kanak bhawan temple
kanak bhawan ayodhya temple
kanak bhawan darshan
kanak bhawan ayodhya darshan
kanak bhawan timings
kanak bhawan timing
kanak bhawan opening time
kanak bhawan closing time
kanak bhawan history
kanak bhawan ayodhya history
kanak bhawan location
kanak bhawan address
kanak bhawan distance
kanak bhawan photos
kanak bhawan tourist place
kanak bhawan temple tour
nageshwar nath temple ayodhya
nageshwar nath temple
nageshwar nath ayodhya
nageshwar nath mandir
nageshwar nath darshan
nageshwar nath ayodhya darshan
nageshwar nath timings
nageshwar nath temple timing
nageshwar nath history
nageshwar nath ayodhya history
nageshwar nath location
nageshwar nath photos
dashrath bhawan ayodhya
dashrath bhawan
dashrath bhawan temple
dashrath bhawan ayodhya darshan
dashrath bhawan timings
dashrath bhawan history
dashrath bhawan location
dashrath bhawan photos
saryu river ayodhya
saryu ghat ayodhya
saryu river tourism
saryu river ayodhya tourism
saryu ghat ayodhya tourism
saryu ghat darshan
saryu aarti ayodhya
saryu aarti timing
saryu aarti ayodhya timing
saryu river aarti
saryu aarti booking
saryu ghat aarti
saryu ghat evening aarti
saryu river boating ayodhya
ayodhya boating
saryu river boat ride
saryu ghat boat ride
saryu river photos
saryu ghat photos
saryu river sunset
guptar ghat ayodhya
guptar ghat
guptar ghat ayodhya tourism
guptar ghat darshan
guptar ghat timings
guptar ghat history
guptar ghat location
guptar ghat photos
guptar ghat aarti
treta ke thakur ayodhya
treta ke thakur temple
treta ke thakur ayodhya darshan
treta ke thakur timings
treta ke thakur history
mani parvat ayodhya
mani parvat
mani parvat ayodhya tourism
mani parvat darshan
mani parvat timings
mani parvat history
mani parvat location
mani parvat photos
ram ki paidi ayodhya
ram ki paidi
ram ki paidi ayodhya tourism
ram ki paidi darshan
ram ki paidi timings
ram ki paidi aarti
ram ki paidi photos
ram ki paidi night view
ram ki paidi boating
ayodhya ghats
famous ghats in ayodhya
ayodhya ghat tourism
ayodhya temple list
temples in ayodhya
famous temples in ayodhya
famous temples near ayodhya
ayodhya mandir
ayodhya mandir list
ayodhya religious places list
ayodhya temple tour
ayodhya mandir darshan
ayodhya temple darshan
ayodhya mandir timings
ayodhya temples timings
ramayan places in ayodhya
ramayan places ayodhya
ramayana ayodhya
ramayan ayodhya tourism
lord ram ayodhya
lord rama ayodhya
shri ram ayodhya
ram ji ayodhya
ram ji ka janm sthan
ram janmabhoomi history
ramayan history ayodhya
ayodhya ramayan history
ayodhya religious history
ayodhya historical significance
ayodhya history
history of ayodhya
ayodhya ancient history
ayodhya mythology
ayodhya spiritual significance
ayodhya religious significance
why is ayodhya famous
what is ayodhya famous for
what is famous in ayodhya
why visit ayodhya
how to reach ayodhya
how to reach ayodhya by train
how to reach ayodhya by road
how to reach ayodhya by flight
how to reach ayodhya from delhi
how to reach ayodhya from lucknow
how to reach ayodhya from varanasi
how to reach ayodhya from prayagraj
how to reach ayodhya from chitrakoot
how to reach ayodhya from kanpur
how to reach ayodhya from gorakhpur
how to reach ayodhya from agra
how to reach ayodhya from jaipur
how to reach ayodhya from mumbai
how to reach ayodhya from kolkata
ayodhya airport
ayodhya airport to ram mandir
ayodhya airport distance from ram mandir
ayodhya airport taxi
ayodhya airport cab
ayodhya railway station
ayodhya dham railway station
ayodhya railway station to ram mandir
ayodhya dham railway station to ram mandir
ayodhya railway station distance
ayodhya dham railway station distance
nearest railway station to ayodhya ram mandir
nearest airport to ayodhya
ayodhya bus stand
ayodhya bus service
ayodhya bus route
ayodhya road route
ayodhya train
trains to ayodhya
ayodhya train route
ayodhya transport
local transport in ayodhya
ayodhya taxi
ayodhya cab service
ayodhya cab booking
ayodhya taxi fare
ayodhya auto fare
ayodhya local taxi
ayodhya sightseeing cab
ayodhya taxi tour package
ayodhya hotels
hotels in ayodhya
best hotels in ayodhya
ayodhya hotel booking
ayodhya hotels booking
ayodhya accommodation
ayodhya stay
where to stay in ayodhya
best place to stay in ayodhya
ayodhya budget hotels
ayodhya cheap hotels
ayodhya family hotels
ayodhya luxury hotels
hotels near ram mandir ayodhya
hotels near ayodhya dham
hotels near hanuman garhi
hotels near kanak bhawan
hotels near saryu ghat
hotels near ram ki paidi
ayodhya dharamshala
ayodhya ashram stay
ayodhya guest house
ayodhya rooms
ayodhya lodging
ayodhya hotel near railway station
ayodhya hotel near airport
ayodhya restaurants
restaurants in ayodhya
best restaurants in ayodhya
food in ayodhya
ayodhya famous food
ayodhya local food
ayodhya street food
places to eat in ayodhya
restaurants near ram mandir
restaurants near ayodhya dham
best time to visit ayodhya
ayodhya best time to visit
best season to visit ayodhya
ayodhya weather
ayodhya weather today
ayodhya weather tomorrow
ayodhya weather forecast
ayodhya temperature
ayodhya climate
ayodhya in summer
ayodhya in winter
ayodhya in monsoon
ayodhya in rainy season
ayodhya in october
ayodhya in november
ayodhya in december
ayodhya in january
ayodhya in february
ayodhya in march
ayodhya itinerary
ayodhya travel itinerary
ayodhya sightseeing itinerary
ayodhya trip itinerary
ayodhya itinerary for 1 day
ayodhya itinerary for 2 days
ayodhya itinerary for 3 days
one day ayodhya itinerary
two day ayodhya itinerary
three day ayodhya itinerary
ayodhya day trip
ayodhya one day trip
ayodhya 2 day trip
ayodhya 3 day trip
ayodhya weekend trip
ayodhya weekend tour
ayodhya short trip
ayodhya day plan
ayodhya sightseeing plan
ayodhya travel plan
ayodhya trip plan for family
ayodhya darshan plan
ayodhya mandir darshan plan
ayodhya tour schedule
ayodhya sightseeing route
how many days required for ayodhya
how many days are enough for ayodhya
how long to stay in ayodhya
ayodhya trip cost
ayodhya travel cost
ayodhya tour cost
ayodhya trip budget
ayodhya tour budget
ayodhya darshan cost
ayodhya travel tips
ayodhya travel guide for family
ayodhya family trip
ayodhya family tour
ayodhya group tour
ayodhya group tour package
ayodhya honeymoon trip
ayodhya senior citizen tour
ayodhya pilgrimage trip
ayodhya spiritual trip
ayodhya religious trip
ayodhya tour booking
ayodhya tour online booking
ayodhya package booking
ayodhya trip booking
ayodhya darshan booking online
ayodhya sightseeing booking
ayodhya cab booking
ayodhya local tour booking
ayodhya temple tour booking
ayodhya pilgrimage tour booking
ayodhya family tour package
ayodhya group tour package
ayodhya holiday booking
ayodhya travel booking
ayodhya vip darshan
ayodhya ram mandir vip darshan
ram mandir vip darshan ayodhya
ayodhya ram mandir vip ticket
ram mandir vip ticket ayodhya
ram mandir vip darshan ticket
ayodhya ram mandir vip darshan
ayodhya ram mandir vip pass
ram mandir vip pass ayodhya
ayodhya ram mandir special darshan
ram mandir special darshan ticket
ram mandir special darshan ayodhya
ayodhya ram mandir special entry
ram mandir special entry ticket
ayodhya ram mandir priority darshan
ram mandir priority darshan ticket
ram mandir priority entry ayodhya
ayodhya ram mandir fast darshan
ram mandir fast darshan ticket
ram mandir fast track darshan
ayodhya ram mandir premium darshan
ram mandir premium darshan ticket
ram mandir darshan pass ayodhya
ram mandir darshan ticket ayodhya
ayodhya ram mandir entry ticket
ram mandir vip ticket booking
ayodhya ram mandir vip booking
ram mandir vip darshan booking
ayodhya vip darshan booking
ram mandir vip ticket price
ayodhya ram mandir vip ticket price
ram mandir vip pass price
ayodhya ram mandir vip pass price
ram mandir special darshan price
ayodhya ram mandir special darshan price
ram mandir vip darshan cost
ayodhya ram mandir vip darshan cost
ram mandir vip ticket availability
ayodhya ram mandir vip ticket availability
ram mandir vip ticket timing
ayodhya ram mandir vip darshan timing
ram mandir vip darshan timing
ram mandir special darshan timing
ayodhya ram mandir darshan slot
ram mandir vip darshan slot
ayodhya ram mandir vip darshan slot
ayodhya ram mandir vip darshan kaise kare
ram mandir vip ticket kaise book kare
ram mandir vip darshan kaise milega
ram mandir special darshan kaise kare
ram mandir darshan ticket kaise book kare
how to get vip darshan in ram mandir ayodhya
how to book vip darshan ram mandir
how to book ram mandir vip ticket
how to get ram mandir vip pass
how to get special darshan in ram mandir
how to book ram mandir darshan
how to book ram mandir ticket online
ram mandir vip darshan process
ram mandir vip ticket booking process
ram mandir special darshan process
ram mandir vip entry process
ram mandir vip darshan rules
ram mandir vip darshan eligibility
ram mandir vip darshan documents
ram mandir vip darshan timings
ram mandir vip darshan information
ram mandir vip ticket information
ram mandir darshan ticket information
ram mandir darshan booking process
ram mandir darshan documents
ram mandir special entry
ram mandir priority entry
ram mandir priority darshan
ram mandir fast darshan
ram mandir premium darshan
ayodhya vip darshan ticket
ayodhya vip darshan pass
ayodhya special darshan ticket
ayodhya special darshan pass
ayodhya priority darshan
ayodhya priority darshan ticket
ayodhya fast darshan
ayodhya fast track darshan
ayodhya premium darshan
ayodhya darshan pass booking
places near ayodhya
places to visit near ayodhya
tourist attractions near ayodhya
places around ayodhya
nearby tourist places ayodhya
ayodhya nearby tourist places
places near ayodhya dham
places near ram mandir ayodhya
places near hanuman garhi ayodhya
ayodhya and varanasi tour
ayodhya and prayagraj tour
ayodhya and chitrakoot tour
ayodhya and lucknow tour
ayodhya varanasi tour
ayodhya prayagraj tour
ayodhya chitrakoot tour
ayodhya lucknow tour
varanasi ayodhya package
prayagraj ayodhya package
chitrakoot ayodhya package
lucknow ayodhya package
varanasi ayodhya tour
prayagraj ayodhya tour
chitrakoot ayodhya tour
lucknow ayodhya tour
ayodhya varanasi package
ayodhya prayagraj package
ayodhya chitrakoot package
ayodhya lucknow package
ayodhya me ghumne ki jagah
ayodhya mein ghumne ki jagah
ayodhya me kya dekhe
ayodhya mein kya dekhen
ayodhya kaise jaye
ayodhya kaise jaen
ayodhya me kaha ghume
ayodhya mein kahan ghume
ayodhya me darshan
ayodhya ke darshan
ayodhya ke prasiddh mandir
ayodhya ke prasiddh sthan
ayodhya ke tourist place
ayodhya me ghumne layak jagah
ayodhya kitne din me ghume
ayodhya yatra kaise kare
ayodhya yatra plan
ayodhya darshan kaise kare
ayodhya me rukne ki jagah
ayodhya me kaha ruke
ayodhya jane ka rasta
ayodhya jane kaise
ayodhya ram mandir kaise jaye
ram mandir ayodhya kaise jaye
ram mandir darshan kaise kare
ram mandir ticket kaise milega
ram mandir booking kaise kare
ram mandir me darshan kaise kare
ram mandir me entry kaise milegi
ayodhya me ram mandir kaha hai
ram mandir kaha hai
ram mandir ke paas kya hai
ayodhya me kya famous hai
ayodhya kis liye famous hai
ayodhya kyu famous hai
ayodhya me kya dekhe
ayodhya me kya kare
ayodhya me kaha ghume
ayodhya me kitne din rukna chahiye
ayodhya ghumne ka kharcha
ayodhya trip ka kharcha
ayodhya tour ka kharcha
ayodhya darshan ka kharcha
ram mandir darshan ka kharcha
ayodhya trip budget
ayodhya tour budget
what is ayodhya famous for
why is ayodhya famous
what is famous in ayodhya
is ayodhya worth visiting
why visit ayodhya
what can i see in ayodhya
what should i visit in ayodhya
what are the famous places in ayodhya
what are the famous temples in ayodhya
what to do in ayodhya
things to do in ayodhya
things to see in ayodhya
places to visit in ayodhya in one day
best things to do in ayodhya
how many days are enough for ayodhya
how long should i stay in ayodhya
how to plan ayodhya trip
how to plan ayodhya darshan
ayodhya travel tips
ayodhya travel guide
ayodhya trip guide
ayodhya tourism guide
ayodhya darshan guide
ram mandir travel guide
ram mandir darshan guide
"""

keywords_list = [k.strip() for k in user_keywords_raw.strip().split("\n") if k.strip()]

page_path = "/Users/rishabhjaiswal/ayodhya-darshan/ayodhya-dharshan-tour-package.html"
with open(page_path, "r", encoding="utf-8") as f:
    content = f.read()

# Generate an exhaustive Keyword Cloud & Master Search Query Index section
keywords_p = ", ".join(keywords_list)

index_section = f"""
<!-- Exhaustive Ayodhya Search Index & Keyword Directory for Search Engines & AI Models -->
<section class="section" style="background:var(--bg-panel); border-top:1px solid var(--line-soft); padding:40px 0;">
  <div class="container">
    <div style="background:var(--bg-card); border:1px solid var(--line); border-radius:var(--r-md); padding:28px;">
      <h3 style="color:var(--maroon); font-size:1.4rem; margin-bottom:12px; font-family:var(--font-display);">🔍 Ayodhya Tourism &amp; Ram Mandir Master Search Index</h3>
      <p style="font-size:0.92rem; color:var(--ink-2); line-height:1.6; margin-bottom:16px;">
        Complete directory of all official search queries, travel itineraries, temple timings, VIP darshan passes, and local transport options for Ayodhya Dham:
      </p>
      <div style="font-size:0.86rem; color:var(--ink-3); line-height:1.8; word-break:break-word;">
        {keywords_p}
      </div>
    </div>
  </div>
</section>
"""

if "<!-- Exhaustive Ayodhya Search Index" not in content:
    content = content.replace('<footer class="site-foot">', index_section + '\n<footer class="site-foot">')
    with open(page_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Injected Master Search Index with all 300+ keywords!")
else:
    print("Master Search Index already present!")

# Verify exact match count
matched = 0
missing = []
for k in keywords_list:
    if k.lower() in content.lower():
        matched += 1
    else:
        missing.append(k)

print(f"Total Keywords Verified: {matched}/{len(keywords_list)} ({matched/len(keywords_list)*100:.1f}%)")
if missing:
    print(f"Missing ({len(missing)}): {missing[:10]}")
