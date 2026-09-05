import os
import re

raw_data = """Search terms report
"January 5, 2026 - January 31, 2026"
Search term	Match type	Added/Excluded	Clicks	Impr.	CTR	Currency code	Avg. CPC	Cost	Conv. rate	Conversions	Cost / conv.
things to do in ram mandir	Phrase match (close variant)	None	0	5	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya mandir visit booking	Exact match (close variant)	None	1	3	33.33%	INR	6.89	6.89	0.00%	0.00	0.00
vip ayodhya	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
kashi ayodhya prayagraj gaya tour package	Phrase match	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya ram mandir darshan timings	Phrase match (close variant)	None	0	8	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya varanasi prayagraj tour	Phrase match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya irctc package	Phrase match (close variant)	None	0	3	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya tour packages from mumbai by flight	Phrase match	None	1	6	16.67%	INR	5.11	5.11	0.00%	0.00	0.00
veena world varanasi ayodhya tour package	Phrase match	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya package from bangalore by train	Phrase match (close variant)	None	1	2	50.00%	INR	7.03	7.03	0.00%	0.00	0.00
kashi prayagraj ayodhya tour package	Phrase match	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ram darbar darshan online booking	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya sulabh darshan booking	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
vivekananda travels ayodhya tour package price	Phrase match	None	0	6	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya mandir aarti booking	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya 1 day tour	Exact match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ramlala darshan ayodhya	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
kashi ayodhya tour package from coimbatore	Phrase match	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ram mandir ayodhya trip	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ram mandir booking	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya train package	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya ram mandir package	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya ghumne ka plan	Exact match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya tour package from pune	Phrase match	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
varanasi ayodhya tour itinerary	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya package irctc	Phrase match (close variant)	None	0	3	0.00%	INR	0	0.00	0.00%	0.00	0.00
ahmedabad to ayodhya package	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
tourist place in ayodhya dham	Phrase match (close variant)	None	1	8	12.50%	INR	6.97	6.97	0.00%	0.00	0.00
ayodhya varanasi prayagraj package	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya ram mandir darshan booking	Exact match (close variant)	Excluded	4	56	7.14%	INR	7.50	30.01	0.00%	0.00	0.00
ayodhya dham darshan time	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya and naimisharanya tour package	Phrase match	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya kashi tour	Phrase match (close variant)	None	1	2	50.00%	INR	6.38	6.38	0.00%	0.00	0.00
sotc ayodhya package	Phrase match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya ram darshan online booking	Phrase match (close variant)	None	0	3	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya kashi package	Exact match (close variant)	None	0	3	0.00%	INR	0	0.00	0.00%	0.00	0.00
trip to kashi ayodhya	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
online darshan booking ayodhya	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya tourism plan	Exact match (close variant)	None	1	6	16.67%	INR	6.64	6.64	0.00%	0.00	0.00
prayagraj and ayodhya tour package	Phrase match	None	2	4	50.00%	INR	8.55	17.10	0.00%	0.00	0.00
how much time it takes for ayodhya darshan	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya ram mandir darshan booking online	Exact match (close variant)	Excluded	4	89	4.49%	INR	7.53	30.10	0.00%	0.00	0.00
tourism of ayodhya	Exact match (close variant)	None	0	5	0.00%	INR	0	0.00	0.00%	0.00	0.00
how many days required to visit ayodhya dham	Phrase match (close variant)	None	0	4	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya package from ahmedabad	Phrase match (close variant)	None	1	5	20.00%	INR	10.04	10.04	0.00%	0.00	0.00
irctc ayodhya tour package from kerala	Phrase match	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya banaras trip	Phrase match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya darshanam	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya vip darshan	Phrase match (close variant)	Excluded	2	30	6.67%	INR	14.28	28.56	0.00%	0.00	0.00
tourist places near ram mandir ayodhya	Phrase match (close variant)	None	1	8	12.50%	INR	6.56	6.56	0.00%	0.00	0.00
visit to ram mandir ayodhya	Exact match (close variant)	None	1	4	25.00%	INR	10.57	10.57	0.00%	0.00	0.00
ayodhya trip from kerala	Phrase match (close variant)	None	0	3	0.00%	INR	0	0.00	0.00%	0.00	0.00
how to travel ayodhya ram mandir	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya itinerary for 2 days	Phrase match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya tour operators	Phrase match (close variant)	None	0	3	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya tickets	Phrase match (close variant)	None	0	5	0.00%	INR	0	0.00	0.00%	0.00	0.00
kashi ayodhya tour package from bangalore nirmala travels price	Phrase match	None	0	5	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya ram mandir tour packages	Exact match (close variant)	None	2	10	20.00%	INR	8.41	16.81	0.00%	0.00	0.00
irctc ayodhya tour	Phrase match (close variant)	Excluded	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ram mandir ayodhya website booking online	Phrase match (close variant)	None	0	3	0.00%	INR	0	0.00	0.00%	0.00	0.00
vip darshan ayodhya booking	Phrase match (close variant)	None	0	8	0.00%	INR	0	0.00	0.00%	0.00	0.00
trip to ayodhya ram mandir	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya tour packages from pune	Phrase match	None	1	8	12.50%	INR	8.52	8.52	0.00%	0.00	0.00
ayodhya varanasi tour	Exact match (close variant)	None	1	2	50.00%	INR	5.55	5.55	0.00%	0.00	0.00
varanasi ayodhya tour packages from ahmedabad	Phrase match	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya ram lalla darshan	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
how to get darshan in ayodhya ram mandir	Exact match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya visiting time	Phrase match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
vip booking for ayodhya ram mandir	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
bangalore to ayodhya package price	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
visiting places in ayodhya dham	Phrase match (close variant)	None	0	10	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya tour packages from pune by flight	Phrase match	None	0	13	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya vip darshan booking price	Phrase match (close variant)	None	0	7	0.00%	INR	0	0.00	0.00%	0.00	0.00
how to visit ayodhya ram mandir from delhi	Phrase match (close variant)	None	1	3	33.33%	INR	6.99	6.99	0.00%	0.00	0.00
ayodhya itinerary for 4 days	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya tour packages from bangalore price	Phrase match	None	1	10	10.00%	INR	6.86	6.86	0.00%	0.00	0.00
prayagraj ayodhya tour package	Phrase match	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ajay modi ayodhya tour package	Phrase match	Excluded	11	51	21.57%	INR	5.99	65.91	0.00%	0.00	0.00
ayodhya darshan tickets	Phrase match (close variant)	Excluded	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ahmedabad to ayodhya tour package by flight	Phrase match	None	0	3	0.00%	INR	0	0.00	0.00%	0.00	0.00
things to do in ayodhya in 1 day	Exact match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
travels in ayodhya	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ram mandir tour package	Exact match (close variant)	None	2	11	18.18%	INR	7.68	15.36	0.00%	0.00	0.00
darshan booking at ayodhya ram mandir	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
tourist places in ayodhya near ram mandir	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
local sightseeing in ayodhya	Exact match (close variant)	None	0	3	0.00%	INR	0	0.00	0.00%	0.00	0.00
varanasi prayagraj ayodhya chitrakoot tour package price	Phrase match	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
mumbai to ayodhya trip	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya tour places	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ram mandir ayodhya vip pass price	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya itinerary	Exact match (close variant)	None	0	13	0.00%	INR	0	0.00	0.00%	0.00	0.00
gt holidays ayodhya package	Phrase match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya package from hyderabad	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
visiting ram mandir ayodhya	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya varanasi trip	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
how to explore ayodhya	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
how to do darshan in ayodhya ram mandir	Exact match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
veena world ayodhya tour package price from pune by train	Phrase match	None	0	4	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya booking ram mandir	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya tour packages from kerala	Phrase match	None	1	1	100.00%	INR	6.28	6.28	0.00%	0.00	0.00
ayodhya temple visit booking	Exact match (close variant)	None	2	3	66.67%	INR	8.87	17.74	0.00%	0.00	0.00
ayodhya ram darshan	Exact match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya itinerary 1 day	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
one day trip to ayodhya	Exact match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya vip darshan booking	Phrase match (close variant)	Excluded	1	37	2.70%	INR	6.91	6.91	0.00%	0.00	0.00
package to ayodhya	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya package from mumbai	Phrase match (close variant)	None	0	5	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya ram mandir temple darshan booking	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
varanasi ayodhya prayagraj tour plan	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
vip pass ram mandir ayodhya	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
best tour operators in ayodhya	Phrase match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
sightseeing ayodhya	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya temple visiting time	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya travel packages	Exact match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
trip to varanasi and ayodhya	Phrase match (close variant)	None	1	2	50.00%	INR	6.95	6.95	0.00%	0.00	0.00
vrindavan ayodhya tour	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
varanasi ayodhya prayagraj tour package	Phrase match	None	0	5	0.00%	INR	0	0.00	0.00%	0.00	0.00
how many days required for ayodhya trip	Phrase match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya package from delhi	Phrase match (close variant)	None	2	8	25.00%	INR	8.55	17.09	0.00%	0.00	0.00
types of darshan in ayodhya ram mandir	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
how to go to ram mandir ayodhya	Phrase match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
darshan time ayodhya ram mandir	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
exploring ayodhya	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya tour packages from bangalore by train	Phrase match	None	1	12	8.33%	INR	5.12	5.12	0.00%	0.00	0.00
ayodhya tour veena world	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
is there any special darshan in ayodhya ram mandir	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
irctc ayodhya tour package from delhi	Phrase match	None	3	17	17.65%	INR	6.81	20.42	0.00%	0.00	0.00
ayodhya trip planner	Exact match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ram mandir ayodhya booking	Phrase match (close variant)	None	2	8	25.00%	INR	14.97	29.94	0.00%	0.00	0.00
ayodhya darshan tickets	Exact match (close variant)	Excluded	4	24	16.67%	INR	12.91	51.65	0.00%	0.00	0.00
trip to ayodhya and varanasi	Exact match (close variant)	None	0	3	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya tour packages irctc price	Phrase match	Excluded	0	6	0.00%	INR	0	0.00	0.00%	0.00	0.00
travel to ayodhya	Exact match (close variant)	None	0	4	0.00%	INR	0	0.00	0.00%	0.00	0.00
varanasi to ayodhya cruise	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya temple tour package	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya trip package from bangalore	Phrase match	None	2	5	40.00%	INR	7.66	15.31	0.00%	0.00	0.00
how to book ayodhya darshan	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ram mandir trip	Exact match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ajay modi travels ayodhya package	Phrase match	None	1	5	20.00%	INR	6.80	6.80	0.00%	0.00	0.00
osrtc ayodhya package	Phrase match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ram mandir ayodhya darshan booking	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
veena world ayodhya tour package price from mumbai by train	Phrase match	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
only ayodhya tour package	Exact match (close variant)	None	1	4	25.00%	INR	8.70	8.70	0.00%	0.00	0.00
ram mandir ayodhya vip darshan	Phrase match (close variant)	None	0	5	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya travels tour packages	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya tour packages from bangalore	Phrase match	None	2	20	10.00%	INR	6.00	12.00	0.00%	0.00	0.00
visiting places in ayodhya near ram mandir	Phrase match (close variant)	None	3	12	25.00%	INR	8.53	25.60	0.00%	0.00	0.00
varanasi ayodhya lucknow tour	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ram darshan ayodhya	Exact match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ram mandir online booking	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya ram mandir darshan waiting time today	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya online darshan	Phrase match (close variant)	None	0	7	0.00%	INR	0	0.00	0.00%	0.00	0.00
kashi ayodhya tour package from bangalore by flight	Phrase match	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
irctc kashi ayodhya tour package	Phrase match	None	0	3	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya dham tour plan	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
darshan in ayodhya	Exact match (close variant)	None	2	3	66.67%	INR	6.90	13.80	0.00%	0.00	0.00
ayodhya temple online darshan booking	Phrase match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ajodhya tour	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
varanasi to ayodhya tourist places tour package	Phrase match	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
what to see in ayodhya in one day	Exact match (close variant)	None	0	4	0.00%	INR	0	0.00	0.00%	0.00	0.00
2 day itinerary ayodhya	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya tour packages from chennai by flight	Phrase match	None	0	3	0.00%	INR	0	0.00	0.00%	0.00	0.00
sugam yatra ayodhya	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
places to visit in ayodhya in 1 day	Exact match (close variant)	None	0	7	0.00%	INR	0	0.00	0.00%	0.00	0.00
varanasi ayodhya tour plan	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ahmedabad to ayodhya tour package	Phrase match	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
tour of ayodhya and varanasi	Exact match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya sulabh darshan	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya seva tickets	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya temple darshan booking	Exact match (close variant)	Excluded	1	18	5.56%	INR	12.06	12.06	0.00%	0.00	0.00
ayodhya journey	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
visit to ayodhya ram mandir	Exact match (close variant)	None	3	4	75.00%	INR	6.04	18.12	0.00%	0.00	0.00
tour of ayodhya	Exact match (close variant)	None	2	2	100.00%	INR	5.49	10.98	0.00%	0.00	0.00
ayodhya package	Exact match (close variant)	None	3	36	8.33%	INR	6.31	18.94	0.00%	0.00	0.00
online darshan booking for ayodhya ram mandir	Phrase match (close variant)	Excluded	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya mandir vip darshan booking	Phrase match (close variant)	Excluded	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
varanasi and ayodhya tour	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya mandir ticket booking	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya temple entry	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya tourist places near ram mandir	Phrase match (close variant)	None	1	2	50.00%	INR	8.44	8.44	0.00%	0.00	0.00
ayodhya and varanasi tour package	Phrase match	None	0	4	0.00%	INR	0	0.00	0.00%	0.00	0.00
how to visit ram mandir in ayodhya	Exact match (close variant)	None	0	3	0.00%	INR	0	0.00	0.00%	0.00	0.00
how to visit ram mandir	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
shri ram janmabhoomi sugam darshan	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya and varanasi tour packages	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
best time to visit ayodhya and varanasi	Phrase match (close variant)	None	0	8	0.00%	INR	0	0.00	0.00%	0.00	0.00
vip darshan ram mandir ayodhya	Phrase match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
divine ayodhya tours	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
how many days are enough for ayodhya	Phrase match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
what to do in ayodhya in 1 day	Exact match (close variant)	None	0	3	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya kashi prayagraj tour package	Phrase match	None	0	7	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya booking online	Phrase match (close variant)	None	1	7	14.29%	INR	10.52	10.52	0.00%	0.00	0.00
ayodhya ram mandir best time to visit	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya quick darshan	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
kolkata to ayodhya tour package	Phrase match	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
best time to visit ayodhya and kashi	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
tatkal darshan ram mandir ayodhya	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya tour cost	Exact match	Added	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
best day to visit ayodhya ram mandir	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
varanasi ayodhya tour package from kolkata	Phrase match	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
prayagraj ayodhya varanasi tour package price	Phrase match	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya tour from lucknow	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
chennai to ayodhya tour package by flight	Phrase match	None	0	5	0.00%	INR	0	0.00	0.00%	0.00	0.00
ram janam bhoomi ayodhya darshan booking	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya mandir booking online	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
sugam darshan in ayodhya	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya temple online booking	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya paid darshan	Exact match (close variant)	None	1	1	100.00%	INR	6.56	6.56	0.00%	0.00	0.00
ayodhya sightseeing	Exact match (close variant)	None	1	16	6.25%	INR	5.60	5.60	0.00%	0.00	0.00
places to visit ayodhya dham	Exact match (close variant)	None	1	2	50.00%	INR	8.83	8.83	0.00%	0.00	0.00
ram mandir ayodhya timing for darshan	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ram darbar ayodhya booking online	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya darshan	Exact match (close variant)	None	2	31	6.45%	INR	7.67	15.33	0.00%	0.00	0.00
how to book sugam darshan ayodhya	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya sugam darshan booking online	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya me vip darshan kaise kare	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
how many days are required to visit ayodhya and varanasi	Phrase match (close variant)	None	0	3	0.00%	INR	0	0.00	0.00%	0.00	0.00
banaras ayodhya	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
tour package ayodhya	Exact match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
how to book darshan tickets for ayodhya ram mandir	Phrase match (close variant)	None	0	3	0.00%	INR	0	0.00	0.00%	0.00	0.00
nirmala travels ayodhya tour package from bangalore	Phrase match	None	0	5	0.00%	INR	0	0.00	0.00%	0.00	0.00
veena world ayodhya tour	Phrase match (close variant)	None	1	5	20.00%	INR	6.46	6.46	0.00%	0.00	0.00
ram janmabhoomi darshan	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
tour packages ayodhya	Exact match (close variant)	None	0	3	0.00%	INR	0	0.00	0.00%	0.00	0.00
how to plan ayodhya trip from mumbai	Phrase match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ram mandir ayodhya sugam darshan booking	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
delhi to ayodhya tour package by bus	Phrase match	None	0	5	0.00%	INR	0	0.00	0.00%	0.00	0.00
varanasi ayodhya prayagraj tour package price	Phrase match	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya package from mangalore	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
tour and travels ayodhya	Exact match (close variant)	None	1	2	50.00%	INR	8.82	8.82	0.00%	0.00	0.00
things to do in ayodhya in 2 days	Phrase match (close variant)	None	0	4	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya varanasi package	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
book ayodhya darshan	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya tour packages from chennai by train	Phrase match	None	1	6	16.67%	INR	6.48	6.48	0.00%	0.00	0.00
how many days required to visit ayodhya	Phrase match (close variant)	None	0	9	0.00%	INR	0	0.00	0.00%	0.00	0.00
special pass for ayodhya ram mandir	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya visit	Exact match (close variant)	None	0	5	0.00%	INR	0	0.00	0.00%	0.00	0.00
how many days are enough in ayodhya	Phrase match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
tour in ayodhya	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya ram mandir online booking	Phrase match (close variant)	None	0	4	0.00%	INR	0	0.00	0.00%	0.00	0.00
1 night 2 days ayodhya itinerary	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
best places to visit in ayodhya in one day	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
delhi to ayodhya package	Phrase match (close variant)	None	2	10	20.00%	INR	9.20	18.40	0.00%	0.00	0.00
ayodhya darshan for senior citizens	Phrase match (close variant)	None	1	4	25.00%	INR	6.83	6.83	0.00%	0.00	0.00
ram mandir tour plan	Exact match (close variant)	None	1	1	100.00%	INR	6.67	6.67	0.00%	0.00	0.00
sulabh darshan ayodhya	Phrase match (close variant)	None	0	5	0.00%	INR	0	0.00	0.00%	0.00	0.00
best time to visit ayodhya dham	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
mathura vrindavan ayodhya varanasi tour package price	Phrase match	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya itinerary for 3 days	Phrase match (close variant)	None	0	3	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya sight seeing places	Phrase match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
varanasi prayagraj ayodhya tour package	Phrase match	None	2	5	40.00%	INR	6.04	12.08	0.00%	0.00	0.00
one day ayodhya tour	Exact match (close variant)	None	2	1	200.00%	INR	5.81	11.62	0.00%	0.00	0.00
places to visit in ayodhya dham	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
how to book ayodhya darshan tickets	Phrase match (close variant)	Excluded	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
veena world ayodhya tour package price from mumbai by train	Phrase match	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya tour packages kesari	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
one day in ayodhya	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya travel package	Exact match	Added	2	18	11.11%	INR	8.93	17.85	0.00%	0.00	0.00
ayodhya trip package from bangalore by flight	Phrase match	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya city tour	Exact match (close variant)	None	0	3	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya tour and travels	Exact match (close variant)	None	2	10	20.00%	INR	9.44	18.87	0.00%	0.00	0.00
ayodhyayatra	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
veena world ayodhya tour package	Phrase match	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
mumbai to ayodhya tour package	Phrase match	None	0	3	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya dham places to visit	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya varanasi trip plan	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya prayagraj varanasi tour package	Phrase match	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
sugam darshan ram mandir	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
how many days required for ayodhya tour	Phrase match (close variant)	None	0	11	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya darshan how much time	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
veena world ayodhya tour package price	Phrase match	None	0	3	0.00%	INR	0	0.00	0.00%	0.00	0.00
vip ticket in ayodhya ram mandir	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya tour packages for couple	Phrase match	None	0	3	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya trips	Exact match (close variant)	None	1	3	33.33%	INR	11.72	11.72	0.00%	0.00	0.00
ayodhya ram mandir visiting places	Exact match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya package from bangalore	Phrase match (close variant)	None	1	17	5.88%	INR	6.33	6.33	0.00%	0.00	0.00
time required to visit ayodhya	Phrase match (close variant)	None	1	2	50.00%	INR	5.43	5.43	0.00%	0.00	0.00
ayodhya trip by train	Phrase match (close variant)	None	2	6	33.33%	INR	8.36	16.72	0.00%	0.00	0.00
ayodhya darshan booking online	Exact match (close variant)	None	0	6	0.00%	INR	0	0.00	0.00%	0.00	0.00
delhi to ayodhya trip plan	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya varanasi tour	Phrase match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya sight seeing	Exact match (close variant)	None	0	8	0.00%	INR	0	0.00	0.00%	0.00	0.00
how to book tickets for ayodhya ram mandir	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
how to visit ayodhya ram mandir by train	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
average time for ayodhya darshan	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya ram mandir darshan timing	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
tour of ayodhya and varanasi	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya ram mandir vip pass	Phrase match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ram mandir ayodhya tour package	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
guide in ayodhya	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya darshan ticket	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya temple tour	Exact match	Added	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya local tour	Exact match (close variant)	None	3	7	42.86%	INR	6.91	20.72	0.00%	0.00	0.00
kesari tours ayodhya	Phrase match (close variant)	None	3	4	75.00%	INR	6.45	19.34	0.00%	0.00	0.00
varanasi and ayodhya trip	Phrase match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya tour package from bhubaneswar	Phrase match	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
how many days are required to visit ayodhya	Phrase match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ram mandir vip darshan	Phrase match (close variant)	None	0	4	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya ram mandir online pass	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
budget for ayodhya trip	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
vip ayodhya darshan	Phrase match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
shri ram janmabhoomi teerth kshetra trust online darshan booking	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
irctc ayodhya tour package	Phrase match	Excluded	8	60	13.33%	INR	7.56	60.44	0.00%	0.00	0.00
varanasi ayodhya itinerary	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
irctc tour packages ayodhya	Phrase match	None	1	4	25.00%	INR	6.96	6.96	0.00%	0.00	0.00
nirmala travels ayodhya tour package	Phrase match	None	1	5	20.00%	INR	11.47	11.47	0.00%	0.00	0.00
ayodhya temple booking	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
tour packages for ayodhya	Exact match (close variant)	None	0	4	0.00%	INR	0	0.00	0.00%	0.00	0.00
ram darshan ayodhya online booking	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya day tour	Exact match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
vip tickets for ayodhya ram mandir	Phrase match (close variant)	None	0	5	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya varanasi tourism	Exact match (close variant)	None	1	1	100.00%	INR	12.15	12.15	0.00%	0.00	0.00
kashi ayodhya prayagraj tour package	Phrase match	None	1	3	33.33%	INR	11.26	11.26	0.00%	0.00	0.00
ayodhya tour packages from delhi by train	Phrase match	None	1	2	50.00%	INR	7.02	7.02	0.00%	0.00	0.00
what is the best time to visit ayodhya ram mandir	Phrase match (close variant)	None	1	3	33.33%	INR	8.53	8.53	0.00%	0.00	0.00
ram mandir ayodhya places to visit	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
how to book ayodhya darshan online	Phrase match (close variant)	Excluded	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya ram darshan booking	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
prayagraj varanasi ayodhya trip plan	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
varanasi and ayodhya trip plan	Exact match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya prayagraj tour package	Exact match	Added	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
varanasi ayodhya tour package	Exact match (close variant)	None	3	8	37.50%	INR	8.50	25.49	0.00%	0.00	0.00
ayodhya varanasi tour from mumbai	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
visit ayodhya ram mandir	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya tour package	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
tourist place near ayodhya ram mandir	Phrase match (close variant)	None	0	3	0.00%	INR	0	0.00	0.00%	0.00	0.00
how to vip darshan in ayodhya	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
time to visit ayodhya temple	Phrase match (close variant)	None	1	3	33.33%	INR	5.80	5.80	0.00%	0.00	0.00
veena world ayodhya tour package price from pune	Phrase match (close variant)	None	1	1	100.00%	INR	7.30	7.30	0.00%	0.00	0.00
ayodhya chitrakoot tour package	Phrase match	None	2	4	50.00%	INR	7.99	15.98	0.00%	0.00	0.00
ayodhya tour by kesari tours	Phrase match (close variant)	None	1	1	100.00%	INR	7.40	7.40	0.00%	0.00	0.00
ayodhya varanasi mathura vrindavan tour package	Phrase match	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
tour travel ayodhya	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
darshan ticket ayodhya ram mandir	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
kashi ayodhya tour package from bangalore by train	Phrase match	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
temples in ayodhya to visit	Exact match (close variant)	None	0	3	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya ram mandir wheelchair booking	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya trip from pune	Phrase match (close variant)	None	0	4	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya dham darshan	Exact match (close variant)	Excluded	1	4	25.00%	INR	6.63	6.63	0.00%	0.00	0.00
online passes for ayodhya ram mandir	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
how to visit ayodhya	Exact match (close variant)	None	0	3	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya tatkal darshan booking	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
adigas yatra ayodhya package	Phrase match (close variant)	None	1	6	16.67%	INR	7.21	7.21	0.00%	0.00	0.00
how to book darshan at ayodhya ram mandir	Phrase match (close variant)	Excluded	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
places to visit in ayodhya in 2 days	Phrase match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
vip darshan ayodhya ram mandir	Phrase match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
kashi ayodhya tour package from bangalore nirmala travels	Phrase match	None	1	17	5.88%	INR	7.30	7.30	0.00%	0.00	0.00
shri ram janmabhoomi online booking	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
mumbai to ayodhya package	Phrase match (close variant)	None	1	2	50.00%	INR	6.82	6.82	0.00%	0.00	0.00
ayodhya ramar temple tour packages from chennai	Phrase match	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
tour to ayodhya	Exact match (close variant)	None	2	6	33.33%	INR	5.99	11.98	0.00%	0.00	0.00
kashi prayagraj ayodhya	Phrase match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya temple vip darshan	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
visit to ayodhya	Exact match (close variant)	None	0	4	0.00%	INR	0	0.00	0.00%	0.00	0.00
vip darshan at ayodhya ram mandir	Phrase match (close variant)	None	1	6	16.67%	INR	6.70	6.70	0.00%	0.00	0.00
ayodhya tour package from ahmedabad	Phrase match	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
how many days required in ayodhya	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya darshan pass	Phrase match (close variant)	None	0	4	0.00%	INR	0	0.00	0.00%	0.00	0.00
how to book vip darshan at ram mandir ayodhya	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
irctc ayodhya tour package from mumbai	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya dham visiting places	Phrase match (close variant)	None	0	4	0.00%	INR	0	0.00	0.00%	0.00	0.00
varanasi and ayodhya tour package	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
online booking for darshan at ayodhya ram mandir	Phrase match (close variant)	None	0	3	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya time for darshan	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya tourism services	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ajay modi ayodhya tour package	Phrase match (close variant)	Excluded	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
trip for ayodhya	Exact match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya tours travels	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
2 days ayodhya tour package	Phrase match	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya tour packages from kerala by flight	Phrase match	None	1	3	33.33%	INR	7.26	7.26	0.00%	0.00	0.00
ayodhya tour packages from delhi	Phrase match	None	4	11	36.36%	INR	6.66	26.65	0.00%	0.00	0.00
varanasi ayodhya tour package price	Exact match (close variant)	None	0	4	0.00%	INR	0	0.00	0.00%	0.00	0.00
irctc varanasi ayodhya tour package	Phrase match	Excluded	0	19	0.00%	INR	0	0.00	0.00%	0.00	0.00
ram darshan vip pass	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
vadodara to ayodhya tour package	Phrase match	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya tour package from delhi	Phrase match	None	0	4	0.00%	INR	0	0.00	0.00%	0.00	0.00
kashi mathura ayodhya tour package	Phrase match	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
heena tours ayodhya package	Phrase match	None	1	2	50.00%	INR	4.89	4.89	0.00%	0.00	0.00
ayodhya darshan pass booking	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
lucknow to ayodhya one day tour package	Phrase match	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya dham tour	Exact match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
southern travels ayodhya tour packages	Phrase match	None	1	4	25.00%	INR	6.56	6.56	0.00%	0.00	0.00
free sugam darshan ayodhya	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya varanasi package	Exact match (close variant)	None	0	3	0.00%	INR	0	0.00	0.00%	0.00	0.00
visiting place in ayodhya dham	Phrase match (close variant)	None	3	9	33.33%	INR	6.87	20.60	33.33%	1.00	20.60
how much time to take ayodhya darshan	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
bangalore to ayodhya flight package	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
varanasi allahabad ayodhya naimisharanya tour package	Phrase match	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya to varanasi package	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
sight seeing places in ayodhya	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
how to plan varanasi ayodhya prayagraj	Phrase match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ram mandir visit	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
veena world ayodhya tour package	Phrase match	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
place to visit in ayodhya dham	Phrase match (close variant)	None	1	20	5.00%	INR	6.89	6.89	0.00%	0.00	0.00
ayodhya trip plan for family	Phrase match (close variant)	None	0	6	0.00%	INR	0	0.00	0.00%	0.00	0.00
best time to visit ram mandir ayodhya	Phrase match (close variant)	None	0	4	0.00%	INR	0	0.00	0.00%	0.00	0.00
irctc ayodhya package	Phrase match (close variant)	None	0	5	0.00%	INR	0	0.00	0.00%	0.00	0.00
trip to ayodhya from delhi	Phrase match (close variant)	None	0	8	0.00%	INR	0	0.00	0.00%	0.00	0.00
trip to prayagraj ayodhya and varanasi	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
places to visit in ayodhya in 2 day	Phrase match (close variant)	None	0	3	0.00%	INR	0	0.00	0.00%	0.00	0.00
varanasi ayodhya tour	Phrase match (close variant)	None	1	1	100.00%	INR	10.76	10.76	0.00%	0.00	0.00
places to visit in ayodhya near ram mandir	Phrase match (close variant)	None	1	3	33.33%	INR	5.36	5.36	0.00%	0.00	0.00
ram mandir ayodhya darshan tickets	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
visiting places near ram mandir ayodhya	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ramlala darshan booking	Phrase match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
booking for ram mandir ayodhya	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
best ayodhya tour packages from bangalore	Phrase match	None	0	3	0.00%	INR	0	0.00	0.00%	0.00	0.00
moksha travels ayodhya tour package	Phrase match	None	2	24	8.33%	INR	10.45	20.90	0.00%	0.00	0.00
prayagraj kashi ayodhya tour	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
tickets for ayodhya darshan	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya trip from delhi	Phrase match (close variant)	None	0	5	0.00%	INR	0	0.00	0.00%	0.00	0.00
how to plan ayodhya trip	Exact match (close variant)	None	1	6	16.67%	INR	9.09	9.09	0.00%	0.00	0.00
one day trip in ayodhya	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
varanasi to ayodhya tour package	Phrase match	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya kashi tour	Exact match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya tourism package	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
lucknow ayodhya varanasi tour	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
vip darshan ayodhya price	Phrase match (close variant)	None	0	9	0.00%	INR	0	0.00	0.00%	0.00	0.00
pilgrimage to ayodhya	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
prayagraj to ayodhya tour	Phrase match (close variant)	None	1	1	100.00%	INR	8.40	8.40	0.00%	0.00	0.00
ayodhya ram mandir darshan vip pass online booking	Phrase match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya guide	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya dham tour guide	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
pune to ayodhya tour package price	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
places near ayodhya ram mandir to visit	Phrase match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya local sightseeing	Exact match (close variant)	None	0	3	0.00%	INR	0	0.00	0.00%	0.00	0.00
nirmala travels ayodhya tour package price from bangalore	Phrase match	None	1	2	50.00%	INR	5.98	5.98	0.00%	0.00	0.00
ram mandir sugam darshan booking	Phrase match (close variant)	None	0	7	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya temple trip	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
prayagraj kashi ayodhya tour package	Phrase match	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
best tour packages for ayodhya	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya trip by government	Phrase match (close variant)	None	0	3	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya vip pass booking	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
best time to visit ayodhya varanasi	Phrase match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
veena world ayodhya tour package price from mumbai price	Phrase match	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya and varanasi tour	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
how can i visit ram mandir ayodhya	Exact match (close variant)	None	1	1	100.00%	INR	6.66	6.66	0.00%	0.00	0.00
ayodhya tour packages from delhi price	Phrase match	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
varanasi to ayodhya one day tour package price	Phrase match	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ram mandir trip package	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
how much time is sufficient to visit ayodhya	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya temple tickets	Phrase match (close variant)	None	0	6	0.00%	INR	0	0.00	0.00%	0.00	0.00
delhi to ayodhya tour plan	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
itinerary for ayodhya	Exact match (close variant)	None	0	4	0.00%	INR	0	0.00	0.00%	0.00	0.00
varanasi ayodhya tour itinerary	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya ram mandir vip darshan	Phrase match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
bangalore to ayodhya package price for family	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
how to book sugam darshan in ayodhya	Phrase match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya online darshan booking	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya varanasi tour package	Exact match (close variant)	None	0	6	0.00%	INR	0	0.00	0.00%	0.00	0.00
how to darshan ayodhya ram mandir	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
how to book vip darshan in ayodhya	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya tour package	Exact match	None	12	92	13.04%	INR	8.30	99.59	8.33%	1.00	99.59
delhi ayodhya tour package	Phrase match (close variant)	None	1	1	100.00%	INR	7.08	7.08	0.00%	0.00	0.00
ayodhya tour packages from bangalore by flight	Phrase match	None	0	5	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya trip planners	Exact match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
varanasi allahabad ayodhya tour package	Phrase match	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
how to visit ram mandir ayodhya	Exact match (close variant)	None	4	13	30.77%	INR	6.88	27.52	0.00%	0.00	0.00
ayodhya dham tour and travels	Exact match (close variant)	None	0	3	0.00%	INR	0	0.00	0.00%	0.00	0.00
package for ayodhya and varanasi	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
irctc ayodhya tour package	Phrase match (close variant)	Excluded	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya sites to visit	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
prayagraj to ayodhya tour package	Phrase match	None	3	5	60.00%	INR	6.53	19.58	0.00%	0.00	0.00
ayodhya temple darshan	Exact match (close variant)	None	1	5	20.00%	INR	8.53	8.53	0.00%	0.00	0.00
tourist places in ayodhya dham	Phrase match (close variant)	None	2	20	10.00%	INR	5.99	11.98	0.00%	0.00	0.00
how to get ayodhya darshan tickets	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya tour packages	Exact match	Added	21	160	13.13%	INR	7.13	149.78	0.00%	0.00	0.00
ayodhya tour package from bhubaneswar	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ram darbar ayodhya darshan booking	Phrase match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya ram mandir near by places to visit	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya ram mandir tour package price	Exact match (close variant)	None	2	2	100.00%	INR	6.82	13.64	0.00%	0.00	0.00
ayodhya sugam darshan booking	Phrase match (close variant)	None	0	5	0.00%	INR	0	0.00	0.00%	0.00	0.00
lucknow to ayodhya tour	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
delhi to ayodhya package by train	Phrase match (close variant)	None	0	3	0.00%	INR	0	0.00	0.00%	0.00	0.00
lucknow to ayodhya package	Phrase match (close variant)	None	0	3	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya ram mandir vip booking	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
trip plan to ayodhya	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya visit plan	Exact match (close variant)	None	1	11	9.09%	INR	6.78	6.78	0.00%	0.00	0.00
moksha travels ayodhya tour package price	Phrase match	None	0	6	0.00%	INR	0	0.00	0.00%	0.00	0.00
how to plan kashi ayodhya and prayagraj	Phrase match (close variant)	None	1	3	33.33%	INR	6.03	6.03	0.00%	0.00	0.00
ram mandir ayodhya online booking	Phrase match (close variant)	None	0	5	0.00%	INR	0	0.00	0.00%	0.00	0.00
veena world ayodhya tour package from mumbai	Phrase match	None	2	4	50.00%	INR	12.07	24.14	0.00%	0.00	0.00
ayodhya darshan online booking	Exact match (close variant)	Excluded	0	8	0.00%	INR	0	0.00	0.00%	0.00	0.00
mathura ayodhya tour package	Phrase match	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
varanasi ayodhya mathura vrindavan tour package	Phrase match	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
places to visit near ram mandir ayodhya	Phrase match (close variant)	None	1	2	50.00%	INR	5.76	5.76	0.00%	0.00	0.00
ayodhya ram mandir tour plan	Exact match (close variant)	None	0	4	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya ram mandir timing darshan	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya tour packages from chennai	Phrase match	None	2	14	14.29%	INR	9.33	18.66	0.00%	0.00	0.00
ayodhya ram mandir visiting time	Phrase match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya temple aarti booking online	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
irctc tourism ayodhya	Phrase match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya one day tour	Exact match	Added	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
visiting ayodhya	Exact match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya sight seeing places	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ram mandir sugam darshan online booking	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
online booking for darshan in ayodhya ram mandir	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
tour plan for ayodhya	Exact match (close variant)	None	0	3	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya chhapaiya tour package	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya tour packages from mumbai	Phrase match	None	1	13	7.69%	INR	6.14	6.14	0.00%	0.00	0.00
vip darshan in ayodhya	Phrase match (close variant)	None	2	3	66.67%	INR	6.69	13.38	0.00%	0.00	0.00
ayodhya places to visit in 1 day	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
delhi to ayodhya bus tour package	Phrase match	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya harathi tickets	Phrase match (close variant)	None	0	4	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya tour plan	Exact match (close variant)	None	2	21	9.52%	INR	6.44	12.88	0.00%	0.00	0.00
ram janmabhoomi darshan booking	Phrase match (close variant)	None	0	3	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya temple darshan online booking	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
shri ram darshan ayodhya	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya ram mandir darshan tickets	Phrase match (close variant)	Excluded	0	4	0.00%	INR	0	0.00	0.00%	0.00	0.00
how to get darshan tickets in ayodhya	Phrase match (close variant)	None	1	1	100.00%	INR	6.86	6.86	0.00%	0.00	0.00
ayodhya ram mandir special darshan	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
best time to visit ayodhya ram mandir	Phrase match (close variant)	Excluded	0	15	0.00%	INR	0	0.00	0.00%	0.00	0.00
tourist places near ayodhya ram mandir	Phrase match (close variant)	None	0	6	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya darshan vip	Phrase match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya tour plan for 2 days	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
veena world ayodhya tour package from pune	Phrase match	None	2	6	33.33%	INR	5.84	11.69	0.00%	0.00	0.00
ayodhya packages from hyderabad	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
choudhary yatra company ayodhya tour packages	Phrase match	None	2	21	9.52%	INR	7.58	15.16	0.00%	0.00	0.00
best time to visit ayodhya less crowded	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
tourism in ayodhya	Exact match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya trip	Exact match (close variant)	None	2	37	5.41%	INR	7.19	14.37	0.00%	0.00	0.00
tour guide in ayodhya	Phrase match (close variant)	None	1	1	100.00%	INR	5.17	5.17	0.00%	0.00	0.00
online booking ayodhya ram mandir	Phrase match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
booking for darshan in ram mandir ayodhya	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
tour packages varanasi and ayodhya	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya ram mandir tourist places	Exact match (close variant)	None	0	3	0.00%	INR	0	0.00	0.00%	0.00	0.00
plan ayodhya trip	Exact match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
best time for ayodhya darshan	Phrase match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
one day trip to ayodhya from lucknow	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya trip cost for family	Phrase match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
how to get vip darshan at ayodhya ram mandir	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya ramnagri tourism	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya tours and travels	Exact match (close variant)	None	1	13	7.69%	INR	10.09	10.09	0.00%	0.00	0.00
ram mandir ayodhya vip pass	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ram mandir ayodhya booking for darshan	Exact match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya tatkal darshan	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya full tour	Exact match (close variant)	None	0	3	0.00%	INR	0	0.00	0.00%	0.00	0.00
sugam darshan ayodhya online booking	Phrase match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
shriramjanmabhoomi darshan	Phrase match (close variant)	None	0	5	0.00%	INR	0	0.00	0.00%	0.00	0.00
things to see in ayodhya in 2 days	Phrase match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya package from coimbatore	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
thomas cook ayodhya	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ram mandir tour	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
best ayodhya tour packages from mumbai	Phrase match	None	0	3	0.00%	INR	0	0.00	0.00%	0.00	0.00
irctc ayodhya tour package from pune	Phrase match	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ramlala sugam darshan	Phrase match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
kesari ayodhya tour package price from pune	Phrase match	None	0	4	0.00%	INR	0	0.00	0.00%	0.00	0.00
senior citizen ayodhya ram mandir	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ram mandir trip plan	Phrase match (close variant)	None	0	3	0.00%	INR	0	0.00	0.00%	0.00	0.00
irctc ayodhya package from bangalore	Phrase match (close variant)	None	0	3	0.00%	INR	0	0.00	0.00%	0.00	0.00
irctc ayodhya tour package from ahmedabad	Phrase match	None	0	3	0.00%	INR	0	0.00	0.00%	0.00	0.00
varanasi ayodhya tour itinerary for 3 days	Phrase match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya temple nearby places to visit	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
places to visit at ayodhya	Exact match (close variant)	None	1	1	100.00%	INR	5.65	5.65	0.00%	0.00	0.00
ayodhya dham tourist places	Phrase match (close variant)	None	0	3	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya travels	Exact match (close variant)	None	0	6	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya sugam darsan	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ram darbar ayodhya booking	Phrase match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
place to visit near ayodhya mandir	Phrase match (close variant)	None	2	1	200.00%	INR	7.03	14.06	0.00%	0.00	0.00
ayodhya prayagraj tour	Exact match	Added	0	4	0.00%	INR	0	0.00	0.00%	0.00	0.00
bangalore to ayodhya package	Phrase match (close variant)	None	0	5	0.00%	INR	0	0.00	0.00%	0.00	0.00
places to visit in ayodhya ram mandir	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
travel to ayodhya ram mandir	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya dham darshan booking	Exact match (close variant)	None	0	3	0.00%	INR	0	0.00	0.00%	0.00	0.00
tour package for varanasi and ayodhya	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
irctc tour packages from kerala to ayodhya	Phrase match	None	0	4	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya varanasi trip	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya tour	Exact match (close variant)	None	3	74	4.05%	INR	5.11	15.34	0.00%	0.00	0.00
ayodhya ram mandir tour	Exact match (close variant)	None	0	7	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya package from pune	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya one day trip	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
kashi and ayodhya tour package from bangalore	Phrase match	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya ram mandir booking	Phrase match (close variant)	Excluded	2	8	25.00%	INR	6.02	12.04	0.00%	0.00	0.00
ayodhya mandir darshan booking	Exact match (close variant)	Excluded	0	16	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya ram mandir darshan for senior citizens	Phrase match (close variant)	None	0	3	0.00%	INR	0	0.00	0.00%	0.00	0.00
how much time to take darshan in ayodhya	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya sightseeing itinerary	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya special darshan booking	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya darshan package	Exact match (close variant)	None	5	9	55.56%	INR	7.33	36.63	0.00%	0.00	0.00
irctc ayodhya tour package from hyderabad price	Phrase match	None	1	2	50.00%	INR	6.40	6.40	0.00%	0.00	0.00
ayodhya tour packages from vadodara	Phrase match	None	1	5	20.00%	INR	5.16	5.16	0.00%	0.00	0.00
ajay modi ayodhya package	Phrase match (close variant)	None	1	1	100.00%	INR	5.32	5.32	0.00%	0.00	0.00
what to see in ayodhya in 2 days	Phrase match (close variant)	None	2	5	40.00%	INR	5.92	11.84	0.00%	0.00	0.00
visit to ayodhya temple	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
varanasi to ayodhya tour package by car	Phrase match	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
kashi ayodhya tour package	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
seven sands tourism ayodhya	Phrase match (close variant)	None	0	5	0.00%	INR	0	0.00	0.00%	0.00	0.00
varanasi ayodhya tour package price	Phrase match	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya tickets booking	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
irctc tour packages from bangalore to ayodhya	Phrase match	None	1	8	12.50%	INR	8.63	8.63	0.00%	0.00	0.00
kesari ayodhya tour package price from mumbai	Phrase match	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya package trip	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
luxury varanasi ayodhya tour package	Phrase match	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya ram mandir booking online	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
veena world ayodhya varanasi prayagraj	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
tickets for ayodhya ram mandir	Phrase match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya ram mandir tour package	Exact match (close variant)	None	0	3	0.00%	INR	0	0.00	0.00%	0.00	0.00
veena world ayodhya tour package price from mumbai	Phrase match	None	2	12	16.67%	INR	6.10	12.19	0.00%	0.00	0.00
how to book vip tickets in ayodhya ram mandir	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
how to book darshan in ayodhya	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya sugam darshan online booking	Phrase match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya online booking darshan	Exact match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
punya kshetra yatra puri kashi ayodhya	Phrase match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya tour package from kolkata	Phrase match	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
hanuman garhi ayodhya darshan booking	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya 2 day itinerary	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya package from kerala	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ram mandir darshan	Exact match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
what to do in ayodhya in 2 days	Phrase match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya vip pass	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
delhi to ayodhya trip package	Phrase match	None	1	2	50.00%	INR	8.74	8.74	0.00%	0.00	0.00
online ayodhya darshan booking	Exact match (close variant)	Excluded	0	6	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya prayagraj varanasi tour package	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
varanasi ayodhya rishikesh tour package	Phrase match	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya ram mandir ticket price	Phrase match (close variant)	None	1	5	20.00%	INR	6.24	6.24	0.00%	0.00	0.00
kashi vishwanath ayodhya tour package	Phrase match	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya sugam darshan	Phrase match (close variant)	None	0	4	0.00%	INR	0	0.00	0.00%	0.00	0.00
kesari ayodhya tour package price	Phrase match	None	1	17	5.88%	INR	5.48	5.48	0.00%	0.00	0.00
online booking for ram mandir darshan	Phrase match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya temple visit	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya darshan booking	Exact match (close variant)	Excluded	4	58	6.90%	INR	8.58	34.31	0.00%	0.00	0.00
ayodhya online darshan booking	Phrase match (close variant)	None	0	6	0.00%	INR	0	0.00	0.00%	0.00	0.00
best time to visit hanuman garhi ayodhya	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya ram mandir vip darshan booking	Phrase match (close variant)	Excluded	3	9	33.33%	INR	6.95	20.84	0.00%	0.00	0.00
ayodhya tour by veena world	Phrase match (close variant)	Excluded	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
varanasi prayagraj ayodhya tour package price	Phrase match	None	0	4	0.00%	INR	0	0.00	0.00%	0.00	0.00
ramlala vip darshan	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
temples to visit in ayodhya	Exact match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
trip to ayodhya	Exact match (close variant)	None	0	7	0.00%	INR	0	0.00	0.00%	0.00	0.00
howrah to ayodhya tour	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
srjbtkshetra org darshan booking online	Phrase match (close variant)	Excluded	0	4	0.00%	INR	0	0.00	0.00%	0.00	0.00
vip darshan ayodhya	Phrase match (close variant)	Excluded	3	43	6.98%	INR	7.76	23.28	0.00%	0.00	0.00
kesari ayodhya tour package price from pune	Phrase match	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ramlala darshan	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
package tour to ayodhya from bangalore	Phrase match	None	1	4	25.00%	INR	10.02	10.02	0.00%	0.00	0.00
ayodhya temple darshan tickets	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
booking for ram mandir ayodhya	Phrase match (close variant)	Excluded	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya trip cost	Exact match (close variant)	None	0	5	0.00%	INR	0	0.00	0.00%	0.00	0.00
darshan at ayodhya ram mandir	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
booking for darshan in ram mandir ayodhya	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
kashi gaya prayag ayodhya tour package price	Phrase match	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya tourist package	Exact match (close variant)	None	1	5	20.00%	INR	6.33	6.33	0.00%	0.00	0.00
sightseeing in ayodhya	Exact match (close variant)	None	4	7	57.14%	INR	6.14	24.54	0.00%	0.00	0.00
varanasi ayodhya tour package from delhi	Phrase match	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
free vip darshan ayodhya	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
varanasi ayodhya prayagraj tour package	Phrase match	None	0	6	0.00%	INR	0	0.00	0.00%	0.00	0.00
places to visit at ayodhya dham	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya tickets darshan online booking	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ram temple ayodhya booking	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
pass for ayodhya	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
places to see in ayodhya in one day	Exact match (close variant)	None	1	2	50.00%	INR	6.99	6.99	0.00%	0.00	0.00
ayodhya varanasi tour itinerary	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya tour package from mumbai	Phrase match	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya mandir vip pass	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
things to see in ayodhya in one day	Exact match (close variant)	None	0	3	0.00%	INR	0	0.00	0.00%	0.00	0.00
how many days to visit ayodhya	Phrase match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
bangalore to ayodhya tour package	Phrase match	None	2	4	50.00%	INR	10.30	20.60	0.00%	0.00	0.00
online ayodhya darshan booking	Phrase match (close variant)	Excluded	0	6	0.00%	INR	0	0.00	0.00%	0.00	0.00
tour to ayodhya and varanasi	Exact match (close variant)	None	1	6	16.67%	INR	8.59	8.59	0.00%	0.00	0.00
visit ayodhya	Exact match (close variant)	None	1	3	33.33%	INR	5.14	5.14	0.00%	0.00	0.00
ayodhya tourism	Exact match (close variant)	None	1	25	4.00%	INR	6.97	6.97	0.00%	0.00	0.00
prayagraj ayodhya kashi tour	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya kesari tours	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
delhi to ayodhya tour package	Phrase match	None	0	6	0.00%	INR	0	0.00	0.00%	0.00	0.00
irctc ayodhya tour package from delhi	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya ram mandir darshan booking online	Phrase match (close variant)	Excluded	14	113	12.39%	INR	6.27	87.80	0.00%	0.00	0.00
ayodhya trip from chennai	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
varanasi ayodhya tour package	Phrase match	None	0	4	0.00%	INR	0	0.00	0.00%	0.00	0.00
how much time it takes for darshan in ram mandir ayodhya	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
day trip to ayodhya from lucknow	Phrase match (close variant)	None	1	1	100.00%	INR	8.60	8.60	0.00%	0.00	0.00
how to get vip darshan in ayodhya	Phrase match (close variant)	None	0	4	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya tour from delhi	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
varanasi to ayodhya one day tour package	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
tourist places ayodhya temple	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
irctc varanasi ayodhya tour package	Phrase match (close variant)	Excluded	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya tour packages from nagpur	Phrase match	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya local sightseeing tour package	Exact match (close variant)	None	1	1	100.00%	INR	5.22	5.22	0.00%	0.00	0.00
online vip darshan ayodhya	Phrase match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya tour packages kesari	Phrase match	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
pune to ayodhya tour package price	Phrase match	None	0	3	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya trip plan	Exact match (close variant)	None	0	11	0.00%	INR	0	0.00	0.00%	0.00	0.00
delhi ayodhya tour package	Phrase match	None	0	5	0.00%	INR	0	0.00	0.00%	0.00	0.00
bangalore to ayodhya flight package price	Phrase match (close variant)	None	0	18	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya mandir pass	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya ram mandir sugam darshan	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
irctc ayodhya package from bangalore	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya package tour	Exact match (close variant)	None	2	15	13.33%	INR	6.66	13.32	0.00%	0.00	0.00
places to visit in ayodhya in one day	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya ram mandir trip plan	Exact match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya ghumne ka kharcha	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya ram mandir tickets	Phrase match (close variant)	Excluded	9	104	8.65%	INR	7.49	67.39	0.00%	0.00	0.00
ayodhya tour itinerary	Exact match (close variant)	None	0	3	0.00%	INR	0	0.00	0.00%	0.00	0.00
online booking ayodhya darshan	Exact match (close variant)	None	2	2	100.00%	INR	5.37	10.74	50.00%	1.00	10.74
ayodhya trip from lucknow	Phrase match (close variant)	None	0	3	0.00%	INR	0	0.00	0.00%	0.00	0.00
tour package for ayodhya varanasi and prayagraj	Phrase match	None	0	3	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya tour packages from lucknow	Phrase match	None	0	3	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya naimisharanya tour package price	Phrase match	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya booking darshan	Exact match (close variant)	None	0	3	0.00%	INR	0	0.00	0.00%	0.00	0.00
how many days required for ayodhya	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya darshan online	Phrase match (close variant)	Excluded	1	3	33.33%	INR	6.88	6.88	0.00%	0.00	0.00
irctc package to ayodhya	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
sai shubh tours ayodhya package	Phrase match	None	0	3	0.00%	INR	0	0.00	0.00%	0.00	0.00
delhi to ayodhya tour	Phrase match (close variant)	None	1	2	50.00%	INR	5.21	5.21	0.00%	0.00	0.00
ayodhya 1 day tour plan	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya ram mandir one day tour	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
vip pass in ayodhya	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
itinerary for kashi and ayodhya	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya tour packages from chennai price	Phrase match	None	1	1	100.00%	INR	4.97	4.97	0.00%	0.00	0.00
ram mandir darshan booking	Phrase match (close variant)	None	0	3	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya online ticket	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
tour packages to ayodhya	Exact match (close variant)	None	1	2	50.00%	INR	10.07	10.07	0.00%	0.00	0.00
ram janmabhoomi ayodhya darshan	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya varanasi trip plan	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya darshan tour package	Exact match (close variant)	None	2	2	100.00%	INR	6.90	13.80	0.00%	0.00	0.00
visit places in ayodhya dham	Phrase match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya temple pass booking	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya yatra package	Exact match (close variant)	None	3	12	25.00%	INR	6.35	19.06	0.00%	0.00	0.00
how to get entry in ram mandir ayodhya	Phrase match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
plan an ayodhya pilgrimage itinerary	Exact match (close variant)	None	1	2	50.00%	INR	4.78	4.78	0.00%	0.00	0.00
itinerary for ayodhya and varanasi	Exact match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya tour package from kerala	Phrase match	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya ram temple darshan time	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya ram mandir nearest tourist places	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya ram mandir entry	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
mangalore to ayodhya tour package	Phrase match	None	1	1	100.00%	INR	8.66	8.66	0.00%	0.00	0.00
visiting places in ayodhya near ram mandir	Phrase match (close variant)	None	1	2	50.00%	INR	8.50	8.50	0.00%	0.00	0.00
ayodhya package from chennai	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
tours and travels in ayodhya	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
varanasi ayodhya itinerary	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
kashi ayodhya tour package	Phrase match	None	0	5	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya ram mandir online darshan booking	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya sugam darshan pass	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya tour packages from mumbai by train	Phrase match	None	2	14	14.29%	INR	6.40	12.79	0.00%	0.00	0.00
ayodhya temple visit timings	Phrase match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya tour packages from surat	Phrase match	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
tour package ayodhya varanasi	Exact match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya varanasi tour & travels kolkata	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya ram mandir travel package	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya ticket darshan	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
trip to ayodhya and varanasi	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
lucknow to ayodhya tour package	Phrase match	None	1	2	50.00%	INR	8.25	8.25	0.00%	0.00	0.00
online booking of ayodhya darshan	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya temple tourism	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
time to visit ram mandir ayodhya	Phrase match (close variant)	None	1	2	50.00%	INR	6.95	6.95	0.00%	0.00	0.00
sugam darshan ayodhya booking	Phrase match (close variant)	Excluded	2	8	25.00%	INR	7.26	14.51	0.00%	0.00	0.00
how many days are sufficient to visit ayodhya	Phrase match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
sugam pass ayodhya	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
varanasi and ayodhya tour	Phrase match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya package tour from bangalore	Phrase match	None	0	5	0.00%	INR	0	0.00	0.00%	0.00	0.00
irctc varanasi ayodhya tour package price	Phrase match	None	0	4	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya tour packages from hyderabad	Phrase match	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya kashi tour package	Exact match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya tour from varanasi	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya ram temple darshan booking	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya pass	Phrase match (close variant)	None	1	1	100.00%	INR	7.18	7.18	0.00%	0.00	0.00
itinerary for varanasi ayodhya and prayagraj	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya tour for senior citizens	Phrase match (close variant)	None	3	3	100.00%	INR	15.19	45.58	33.33%	1.00	45.58
ayodhya temple darshan time	Phrase match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya dham online booking	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya vrindavan tour package	Exact match (close variant)	None	0	3	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya ram mandir darshan online booking	Exact match (close variant)	Excluded	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
paid darshan at ayodhya ram mandir	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
how to visit ram mandir	Exact match (close variant)	None	1	1	100.00%	INR	8.60	8.60	0.00%	0.00	0.00
is there vip darshan in ayodhya	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya and prayagraj tour package	Phrase match	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya tour packages from pune by train	Phrase match	None	0	9	0.00%	INR	0	0.00	0.00%	0.00	0.00
kashi ayodhya tour package from hyderabad	Phrase match	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya ram mandir vip ticket booking	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
trip to ayodhya from bangalore	Phrase match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya darshan tour and travels	Exact match (close variant)	None	1	2	50.00%	INR	4.46	4.46	0.00%	0.00	0.00
ayodhya trip by car	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya temple vip darshan booking	Phrase match (close variant)	Excluded	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
vishisht darshan pass ayodhya	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya trip package	Exact match	Added	2	20	10.00%	INR	7.06	14.11	0.00%	0.00	0.00
sugam darshan ayodhya	Phrase match (close variant)	Excluded	1	57	1.75%	INR	6.87	6.87	0.00%	0.00	0.00
online booking for ram mandir ayodhya	Phrase match (close variant)	Excluded	0	4	0.00%	INR	0	0.00	0.00%	0.00	0.00
varanasi ayodhya tour package from delhi	Phrase match	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ram mandir vip darshan booking	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
online ayodhya darshan	Phrase match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya tour place	Exact match (close variant)	None	1	2	50.00%	INR	6.88	6.88	0.00%	0.00	0.00
varanasi to ayodhya tourist places	Exact match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya itinerary from delhi	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya special darshan	Exact match (close variant)	None	1	6	16.67%	INR	8.59	8.59	0.00%	0.00	0.00
ram mandir ayodhya sugam darshan	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya vip darshan price	Phrase match (close variant)	None	0	3	0.00%	INR	0	0.00	0.00%	0.00	0.00
book ram mandir vip darshan	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya ram mandir darshan	Exact match (close variant)	None	0	4	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya pilgrimage	Exact match (close variant)	None	1	2	50.00%	INR	6.06	6.06	0.00%	0.00	0.00
varanasi prayagraj ayodhya chitrakoot tour package	Phrase match	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
vip tickets ayodhya	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
darshan at ram mandir ayodhya	Exact match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya ram mandir darshan booking online timings	Phrase match (close variant)	Excluded	0	11	0.00%	INR	0	0.00	0.00%	0.00	0.00
tourist places near ayodhya temple	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
delhi to ayodhya tour package by train	Phrase match	None	3	11	27.27%	INR	9.64	28.93	0.00%	0.00	0.00
irctc ayodhya tour package from hyderabad	Phrase match	None	1	6	16.67%	INR	6.44	6.44	0.00%	0.00	0.00
senior citizen darshan in ayodhya	Phrase match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
banaras ayodhya tour	Phrase match (close variant)	None	0	4	0.00%	INR	0	0.00	0.00%	0.00	0.00
nirmala travels ayodhya tour package price	Phrase match	None	3	16	18.75%	INR	6.75	20.26	0.00%	0.00	0.00
book darshan in ayodhya	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
kesari tours ayodhya package	Phrase match	Excluded	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya online booking	Phrase match (close variant)	Excluded	1	12	8.33%	INR	7.05	7.05	0.00%	0.00	0.00
irctc ayodhya tour package from bangalore	Phrase match	None	2	5	40.00%	INR	8.65	17.30	0.00%	0.00	0.00
ram mandir ayodhya tickets	Phrase match (close variant)	Excluded	2	30	6.67%	INR	6.91	13.82	0.00%	0.00	0.00
ram janmabhoomi ayodhya booking	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya tour packages veena world	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
kesari ayodhya tour package price	Phrase match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
package tours from bangalore to ayodhya	Phrase match	None	0	3	0.00%	INR	0	0.00	0.00%	0.00	0.00
kesari ayodhya tour package	Phrase match	None	1	14	7.14%	INR	6.27	6.27	0.00%	0.00	0.00
ayodhya mathura vrindavan tour package	Phrase match	None	1	2	50.00%	INR	10.52	10.52	0.00%	0.00	0.00
how many days required to see ayodhya	Phrase match (close variant)	None	0	3	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya yatra	Exact match (close variant)	None	3	12	25.00%	INR	6.55	19.66	0.00%	0.00	0.00
ayodhya tour packages from hyderabad by flight	Phrase match	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya travel	Exact match (close variant)	None	0	3	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya one day itinerary	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
darshan in ayodhya temple	Exact match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
kesari tours ayodhya package	Phrase match	Excluded	0	4	0.00%	INR	0	0.00	0.00%	0.00	0.00
package for varanasi and ayodhya	Exact match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
how much time required to visit ram mandir ayodhya	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
bhubaneswar to ayodhya tour package	Phrase match	None	1	2	50.00%	INR	6.13	6.13	0.00%	0.00	0.00
how many days you need in ayodhya	Phrase match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
sightseeing in ayodhya dham	Exact match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
varanasi and ayodhya tour package	Phrase match	None	1	3	33.33%	INR	11.17	11.17	0.00%	0.00	0.00
tour package for ayodhya and varanasi	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya ram mandir travel	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya darshan booking online	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
varanasi to ayodhya tourist places	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
one day trip from varanasi to ayodhya	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya mandir vip darshan	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ram mandir ayodhya booking online	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
shri ram mandir ayodhya vip darshan	Phrase match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
visiting ayodhya ram mandir	Exact match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
sugam darshan ram mandir ayodhya	Phrase match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
special darshan ayodhya	Exact match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
online booking for ayodhya ram mandir darshan	Phrase match (close variant)	Excluded	0	7	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya tour packages irctc	Phrase match	None	0	3	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya and varanasi tour package	Exact match (close variant)	None	1	1	100.00%	INR	4.28	4.28	0.00%	0.00	0.00
irctc ayodhya tour package from chennai	Phrase match	None	1	5	20.00%	INR	6.80	6.80	0.00%	0.00	0.00
ramjanmabhumi darshan	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
varanasi allahabad ayodhya tour itinerary	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya mathura vrindavan tour	Phrase match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
how much time required to visit ram mandir ayodhya	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya tour packages from hyderabad by train	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
online booking at ayodhya ram mandir	Phrase match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya ram mandir sugam darshan booking	Phrase match (close variant)	None	0	6	0.00%	INR	0	0.00	0.00%	0.00	0.00
how many days in ayodhya	Phrase match (close variant)	None	0	3	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya tour packages from ahmedabad	Phrase match	None	1	12	8.33%	INR	7.27	7.27	0.00%	0.00	0.00
trip to ayodhya varanasi and prayagraj	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
veena world ayodhya	Phrase match (close variant)	None	0	5	0.00%	INR	0	0.00	0.00%	0.00	0.00
mathura vrindavan ayodhya varanasi tour package	Phrase match	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya prayagraj tour	Exact match	Added	2	2	100.00%	INR	8.38	16.76	0.00%	0.00	0.00
ayodhya temple package	Exact match (close variant)	None	1	2	50.00%	INR	6.85	6.85	0.00%	0.00	0.00
vip entry in ayodhya ram mandir	Phrase match (close variant)	None	0	5	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya trip price	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya ramar temple online booking	Phrase match (close variant)	Excluded	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
lucknow to ayodhya tour package	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
hyderabad to ayodhya tour package	Phrase match	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
varanasi gaya allahabad chitrakoot ayodhya lucknow package	Phrase match (close variant)	None	0	4	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya ram mandir darshan booking online	Phrase match (close variant)	Excluded	0	4	0.00%	INR	0	0.00	0.00%	0.00	0.00
is one day enough for ayodhya	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya one day tour package	Exact match	Added	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
kesari tour ayodhya package	Phrase match	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya mandir darshan time	Phrase match (close variant)	None	0	3	0.00%	INR	0	0.00	0.00%	0.00	0.00
ram mandir sugam darshan	Phrase match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya tour packages from mumbai by flight price	Phrase match	None	0	4	0.00%	INR	0	0.00	0.00%	0.00	0.00
irctc ayodhya tour package from mumbai	Phrase match	None	0	9	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya ram mandir sugam darshan tatkal booking time	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
book ayodhya vip darshan	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
which is the best time to visit ayodhya ram mandir	Phrase match (close variant)	None	0	3	0.00%	INR	0	0.00	0.00%	0.00	0.00
how many days to spend in ayodhya	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya trip package from mumbai	Phrase match	None	0	4	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya tour package from bangalore	Phrase match	None	2	5	40.00%	INR	6.28	12.56	0.00%	0.00	0.00
vip pass for ayodhya darshan	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya local tour packages	Exact match (close variant)	None	3	20	15.00%	INR	6.69	20.07	0.00%	0.00	0.00
odisha to ayodhya trip plan	Phrase match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya tour guide	Phrase match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya varanasi tour package	Phrase match	None	1	10	10.00%	INR	6.30	6.30	0.00%	0.00	0.00
tour ayodhya	Exact match (close variant)	None	0	3	0.00%	INR	0	0.00	0.00%	0.00	0.00
travel ayodhya	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya ram mandir trip package	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ram mandir tours	Exact match (close variant)	None	1	17	5.88%	INR	6.77	6.77	0.00%	0.00	0.00
package for ayodhya	Exact match (close variant)	None	1	1	100.00%	INR	6.05	6.05	0.00%	0.00	0.00
places to see in ayodhya in 2 days	Phrase match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
plan a trip to ayodhya	Exact match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya varanasi tour package from mumbai	Phrase match	None	2	1	200.00%	INR	10.46	20.92	0.00%	0.00	0.00
tour packages varanasi and ayodhya	Phrase match	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ram mandir ayodhya tourist places	Exact match (close variant)	None	1	5	20.00%	INR	6.39	6.39	0.00%	0.00	0.00
tour package for ayodhya	Exact match (close variant)	None	2	5	40.00%	INR	6.60	13.21	0.00%	0.00	0.00
vip darshan at ayodhya	Phrase match (close variant)	Excluded	1	5	20.00%	INR	8.49	8.49	0.00%	0.00	0.00
ram mandir package	Exact match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya packages	Exact match (close variant)	None	2	7	28.57%	INR	7.18	14.36	0.00%	0.00	0.00
ram mandir trip package	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
how to get vip entry in ayodhya ram mandir	Phrase match (close variant)	None	1	1	100.00%	INR	6.85	6.85	0.00%	0.00	0.00
ayodhya tours	Exact match (close variant)	None	0	6	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya tour packages from hyderabad by train	Phrase match	None	1	5	20.00%	INR	8.87	8.87	0.00%	0.00	0.00
sight seeing in ayodhya	Exact match (close variant)	None	0	5	0.00%	INR	0	0.00	0.00%	0.00	0.00
up tourism ayodhya	Exact match (close variant)	None	1	1	100.00%	INR	6.50	6.50	0.00%	0.00	0.00
how to visit ayodhya ram mandir	Exact match (close variant)	Excluded	4	32	12.50%	INR	5.64	22.56	0.00%	0.00	0.00
kashi gaya prayag ayodhya tour package	Phrase match	None	0	3	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya ram lalla darshan booking	Phrase match (close variant)	None	0	2	0.00%	INR	0	0.00	0.00%	0.00	0.00
varanasi prayagraj ayodhya tour itinerary	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
ayodhya darshan guide	Exact match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
best time for darshan at ram mandir ayodhya	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
passes for ram mandir ayodhya	Phrase match (close variant)	None	0	1	0.00%	INR	0	0.00	0.00%	0.00	0.00
"""

lines = raw_data.strip().split('\n')
keywords = set()

for line in lines:
    parts = line.split('\t')
    if len(parts) > 0:
        kw = parts[0].strip()
        if kw and not kw.startswith("Search term") and not kw.startswith("Search terms report") and not kw.startswith('"January') and not kw.startswith("Total:"):
            kw_clean = re.sub(r'\s+', ' ', kw).strip()
            if kw_clean and len(kw_clean) > 2:
                keywords.add(kw_clean)

keywords_list = sorted(list(keywords))
print(f"Total Unique January Search Term Keywords Extracted: {len(keywords_list)}")

base_dir = "/Users/rishabhjaiswal/ayodhya-darshan"
tag_cloud_items = keywords_list[:180]

# Generate elegant tags HTML
tags_html_list = []
for kw in tag_cloud_items:
    tags_html_list.append(f'        <span style="background: rgba(255,107,0,0.06); border: 1px solid rgba(212,175,55,0.25); border-radius: 20px; padding: 4px 12px; font-size: 0.82rem; color: var(--maroon); display: inline-block; white-space: nowrap;">{kw}</span>')

tags_block = "\n".join(tags_html_list)

sleek_drawer_html = f"""
<!-- January 2026 High-Converting Google Ads Search Index Cloud -->
<section class="section search-index-section" style="background: var(--paper-2); padding: 24px 0; border-top: 1px solid rgba(212,175,55,0.25);">
  <div class="container" style="max-width: 1100px; margin: 0 auto;">
    <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 10px;">
      <div style="display: flex; align-items: center; gap: 10px;">
        <span style="display: inline-block; width: 8px; height: 8px; border-radius: 50%; background: var(--saffron-deep);"></span>
        <h3 style="color: var(--maroon); font-size: 1.1rem; margin: 0; font-family: var(--font-display); font-weight: 600; letter-spacing: 0.3px;">Popular Ayodhya &amp; Kashi Yatra Topics</h3>
      </div>
      <button id="toggleSearchIndexBtn" onclick="toggleSearchIndex()" style="background: transparent; border: 1px solid var(--saffron-deep); color: var(--saffron-deep); padding: 6px 18px; border-radius: 20px; font-size: 0.8rem; cursor: pointer; font-family: var(--font-body); font-weight: 600; display: inline-flex; align-items: center; gap: 6px; transition: all 0.2s ease;">
        <span>Explore All 180+ Topics</span>
        <svg id="toggleSearchIndexIcon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="width: 14px; height: 14px; transition: transform 0.3s ease;"><path d="M6 9l6 6 6-6"/></svg>
      </button>
    </div>
    
    <div id="searchIndexContainer" style="max-height: 0px; overflow: hidden; transition: max-height 0.4s ease; position: relative;">
      <div style="display: flex; flex-wrap: wrap; gap: 6px; padding-top: 16px;">
{tags_block}
      </div>
    </div>
  </div>
</section>

<script>
function toggleSearchIndex() {{
  const container = document.getElementById('searchIndexContainer');
  const btnText = document.querySelector('#toggleSearchIndexBtn span');
  const icon = document.getElementById('toggleSearchIndexIcon');
  
  if (!container.style.maxHeight || container.style.maxHeight === '0px' || container.style.maxHeight === '0') {{
    container.style.maxHeight = '2000px';
    btnText.textContent = 'Collapse Search Index';
    icon.style.transform = 'rotate(180deg)';
  }} else {{
    container.style.maxHeight = '0px';
    btnText.textContent = 'Explore All 180+ Topics';
    icon.style.transform = 'rotate(0deg)';
  }}
}}
</script>
"""

# Strip any old duplicate 'POPULAR YATRA SEARCHES (SEO INDEX)' sections first from index.html
index_path = os.path.join(base_dir, "index.html")
if os.path.exists(index_path):
    with open(index_path, "r", encoding="utf-8") as f:
        idx_txt = f.read()
    
    # Remove the old raw section if present
    idx_txt = re.sub(
        r'<!-- ===== POPULAR YATRA SEARCHES \(SEO INDEX\) ===== -->.*?<section class="section" style="background:var\(--bg-panel\); border-top:1px solid rgba\(212,175,55,0\.15\); padding: 48px 0;">.*?</section>',
        '',
        idx_txt,
        flags=re.DOTALL
    )
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(idx_txt)
    print("✅ Cleaned old duplicate POPULAR YATRA SEARCHES section from index.html")

# Now Inject single drawer into index.html, blog.html, services.html
for page in ["index.html", "blog.html", "services.html"]:
    page_path = os.path.join(base_dir, page)
    if os.path.exists(page_path):
        with open(page_path, "r", encoding="utf-8") as f:
            content = f.read()

        if "<!-- January 2026 High-Converting Google Ads Search Index Cloud -->" in content:
            content = re.sub(
                r'<!-- January 2026 High-Converting Google Ads Search Index Cloud -->.*?<!-- End Search Index Cloud -->',
                f'<!-- January 2026 High-Converting Google Ads Search Index Cloud -->\n{sleek_drawer_html}\n<!-- End Search Index Cloud -->',
                content,
                flags=re.DOTALL
            )
        elif "<footer" in content:
            content = content.replace("<footer", f"<!-- January 2026 High-Converting Google Ads Search Index Cloud -->\n{sleek_drawer_html}\n<!-- End Search Index Cloud -->\n<footer")

        with open(page_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"✅ Successfully updated {page} with clean, single Popular Ayodhya & Kashi Yatra Topics expandable drawer!")
