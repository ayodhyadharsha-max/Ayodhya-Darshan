/**
 * AYODHYA DHARSHAN - PANDIT JI AI YATRA AGENT WIDGET
 * Smart Multi-Lingual Reasoning Engine (Hindi, Hinglish, English)
 * Strict Priority-Ranked Query Router
 */

(function() {
  // Inject CSS Styles
  const style = document.createElement('style');
  style.innerHTML = `
    .pj-agent-widget {
      position: fixed;
      bottom: 85px;
      right: 25px;
      z-index: 999990;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
    }
    @media (max-width: 768px) {
      .pj-agent-widget {
        bottom: 80px;
        right: 15px;
      }
    }
    .pj-launcher-btn {
      background: linear-gradient(135deg, #7A1C1C 0%, #B82E2E 50%, #D4AF37 100%);
      color: #FFF;
      border: 2px solid #FCEFD9;
      padding: 12px 20px;
      border-radius: 30px;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 10px;
      box-shadow: 0 8px 25px rgba(122, 28, 28, 0.4);
      transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
      font-weight: 700;
      font-size: 0.92rem;
    }
    .pj-launcher-btn:hover {
      transform: scale(1.05) translateY(-3px);
      box-shadow: 0 12px 30px rgba(122, 28, 28, 0.5);
    }
    .pj-pulse-dot {
      width: 10px;
      height: 10px;
      background-color: #25D366;
      border-radius: 50%;
      box-shadow: 0 0 0 0 rgba(37, 211, 102, 0.7);
      animation: pj-pulse 1.8s infinite;
    }
    @keyframes pj-pulse {
      0% { box-shadow: 0 0 0 0 rgba(37, 211, 102, 0.7); }
      70% { box-shadow: 0 0 0 10px rgba(37, 211, 102, 0); }
      100% { box-shadow: 0 0 0 0 rgba(37, 211, 102, 0); }
    }
    .pj-chat-modal {
      position: fixed;
      bottom: 95px;
      right: 25px;
      width: 410px;
      max-width: calc(100vw - 30px);
      height: 620px;
      max-height: calc(100vh - 120px);
      background: #FAF7F2;
      border: 1px solid rgba(212, 175, 55, 0.4);
      border-radius: 20px;
      box-shadow: 0 15px 40px rgba(0, 0, 0, 0.25);
      display: none;
      flex-direction: column;
      overflow: hidden;
      z-index: 999999;
      animation: pj-slide-up 0.3s ease-out;
    }
    @keyframes pj-slide-up {
      from { opacity: 0; transform: translateY(20px); }
      to { opacity: 1; transform: translateY(0); }
    }
    .pj-modal-header {
      background: linear-gradient(135deg, #7A1C1C 0%, #4A0E0E 100%);
      color: #FFF;
      padding: 16px 20px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 2px solid #D4AF37;
    }
    .pj-header-info {
      display: flex;
      align-items: center;
      gap: 12px;
    }
    .pj-avatar {
      width: 42px;
      height: 42px;
      background: #FFF;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.4rem;
      border: 2px solid #D4AF37;
    }
    .pj-header-text h4 {
      margin: 0;
      font-size: 1.05rem;
      color: #FCEFD9;
      font-weight: 700;
    }
    .pj-header-text p {
      margin: 2px 0 0;
      font-size: 0.75rem;
      color: rgba(255, 255, 255, 0.85);
      display: flex;
      align-items: center;
      gap: 5px;
    }
    .pj-close-btn {
      background: none;
      border: none;
      color: #FFF;
      font-size: 1.5rem;
      cursor: pointer;
      padding: 0;
      line-height: 1;
    }
    .pj-chat-body {
      flex: 1;
      padding: 16px;
      overflow-y: auto;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }
    .pj-msg {
      max-width: 88%;
      padding: 12px 16px;
      border-radius: 16px;
      font-size: 0.9rem;
      line-height: 1.5;
      word-break: break-word;
    }
    .pj-msg-bot {
      align-self: flex-start;
      background: #FFFFFF;
      color: #2D241E;
      border: 1px solid #E8DFD1;
      border-top-left-radius: 4px;
      box-shadow: 0 2px 8px rgba(0,0,0,0.03);
    }
    .pj-msg-user {
      align-self: flex-end;
      background: #7A1C1C;
      color: #FFF;
      border-top-right-radius: 4px;
    }
    .pj-quick-prompts {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      margin-top: 8px;
    }
    .pj-chip {
      background: #FFF;
      border: 1px solid #D4AF37;
      color: #7A1C1C;
      padding: 6px 12px;
      border-radius: 15px;
      font-size: 0.78rem;
      cursor: pointer;
      font-weight: 600;
      transition: all 0.2s;
    }
    .pj-chip:hover {
      background: #7A1C1C;
      color: #FFF;
    }
    .pj-chat-footer {
      padding: 12px;
      background: #FFF;
      border-top: 1px solid #E8DFD1;
      display: flex;
      gap: 8px;
    }
    .pj-input {
      flex: 1;
      border: 1px solid #CCC;
      border-radius: 20px;
      padding: 10px 16px;
      font-size: 0.9rem;
      outline: none;
    }
    .pj-input:focus {
      border-color: #7A1C1C;
    }
    .pj-send-btn {
      background: #7A1C1C;
      color: #FFF;
      border: none;
      width: 40px;
      height: 40px;
      border-radius: 50%;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .pj-action-bar {
      display: flex;
      justify-content: space-around;
      padding: 8px 12px;
      background: #FFF9F0;
      border-top: 1px solid #F0E6D2;
      font-size: 0.8rem;
    }
    .pj-action-bar a {
      color: #7A1C1C;
      text-decoration: none;
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: 4px;
    }
  `;
  document.head.appendChild(style);

  // Render Widget HTML
  const widgetDiv = document.createElement('div');
  widgetDiv.className = 'pj-agent-widget';
  widgetDiv.innerHTML = `
    <button class="pj-launcher-btn" id="pjLauncher">
      <span class="pj-pulse-dot"></span>
      <span>🚩 Pt. Ram Shastri - AI Yatra Assistant</span>
    </button>

    <div class="pj-chat-modal" id="pjModal">
      <div class="pj-modal-header">
        <div class="pj-header-info">
          <div class="pj-avatar">🚩</div>
          <div class="pj-header-text">
            <h4>Pt. Ram Shastri (AI Agent)</h4>
            <p><span class="pj-pulse-dot"></span> Smart 24x7 Yatra Assistant</p>
          </div>
        </div>
        <button class="pj-close-btn" id="pjClose">&times;</button>
      </div>

      <div class="pj-chat-body" id="pjChatBody">
        <div class="pj-msg pj-msg-bot">
          <strong>॥ जय श्री राम ॥</strong><br>
          Pranam! Main Ayodhya Dharshan ka <strong>Smart AI Yatra Agent</strong> hu. Aap Hindi, Hinglish ya English mein kuch bhi poochhein — <em>Ayodhya Varanasi Prayagraj 3-Day Tour cost, Kashi Vishwanath Sugam Darshan rules, Ram Mandir timings, Mathura, Hotels ya Cab fares!</em>
        </div>

        <div class="pj-quick-prompts">
          <div class="pj-chip" onclick="pjAskPrompt('Ayodhya Varanasi Prayagraj 3 day tour price?')">🚗 3-City Package Cost</div>
          <div class="pj-chip" onclick="pjAskPrompt('Kashi Vishwanath Sugam Darshan rules kya hain?')">🛕 Kashi Sugam Darshan (₹300)</div>
          <div class="pj-chip" onclick="pjAskPrompt('Subah kitne baje nikalna chahiye darshan ke liye?')">🕐 Minimum Rush Timing</div>
          <div class="pj-chip" onclick="pjAskPrompt('Ram Mandir VIP Pass kaise milta hai?')">🚩 Ram Mandir Pass (Free)</div>
          <div class="pj-chip" onclick="pjAskPrompt('Mathura Vrindavan best 1-day itinerary')">🛺 Mathura Vrindavan Plan</div>
        </div>
      </div>

      <div class="pj-action-bar">
        <a href="tel:+919235222399">📞 Call +91 92352 22399</a>
        <a href="https://wa.me/919235222399?text=Jai%20Shree%20Ram!%20I%20want%20to%20enquire%20about%20yatra%20package." target="_blank">💬 WhatsApp Desk</a>
      </div>

      <div class="pj-chat-footer">
        <input type="text" class="pj-input" id="pjInput" placeholder="Kuch bhi poochhein (Hindi/Hinglish/English)...">
        <button class="pj-send-btn" id="pjSend">➔</button>
      </div>
    </div>
  `;
  document.body.appendChild(widgetDiv);

  // Toggle Modal Logic
  const launcher = document.getElementById('pjLauncher');
  const modal = document.getElementById('pjModal');
  const closeBtn = document.getElementById('pjClose');
  const chatBody = document.getElementById('pjChatBody');
  const input = document.getElementById('pjInput');
  const sendBtn = document.getElementById('pjSend');

  launcher.addEventListener('click', () => {
    modal.style.display = modal.style.display === 'flex' ? 'none' : 'flex';
  });

  closeBtn.addEventListener('click', () => {
    modal.style.display = 'none';
  });

  window.pjAskPrompt = function(query) {
    input.value = query;
    handleSend();
  };

  sendBtn.addEventListener('click', handleSend);
  input.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') handleSend();
  });

  function handleSend() {
    const text = input.value.trim();
    if (!text) return;

    // Append User Message
    appendMessage(text, 'user');
    input.value = '';

    // Generate Smart AI Response
    setTimeout(() => {
      const reply = generateSmartAIResponse(text);
      appendMessage(reply, 'bot');
    }, 300);
  }

  function appendMessage(text, sender) {
    const msg = document.createElement('div');
    msg.className = `pj-msg pj-msg-${sender}`;
    msg.innerHTML = text;
    chatBody.appendChild(msg);
    chatBody.scrollTop = chatBody.scrollHeight;
  }

  // Priority-Ranked Disambiguated Intent Router
  function generateSmartAIResponse(query) {
    const q = query.toLowerCase();

    // Normalized Helper Variables
    const isPrice = q.includes('price') || q.includes('cost') || q.includes('rate') || q.includes('package') || q.includes('budget') || q.includes('kharcha') || q.includes('fare') || q.includes('charges') || q.includes('quote');
    const isMultiCity = (q.includes('ayodhya') && q.includes('varanasi')) || (q.includes('varanasi') && q.includes('prayagraj')) || (q.includes('ayodhya') && q.includes('prayagraj')) || q.includes('3 day') || q.includes('3-day') || q.includes('2 day') || q.includes('circuit');

    // 1. MULTI-CITY & PACKAGE PRICE QUERIES (HIGHEST PRIORITY - Prevents single city guide hijacking!)
    if (isMultiCity || (isPrice && (q.includes('tour') || q.includes('trip') || q.includes('yatra') || q.includes('package')))) {
      return `<strong>🚗 Ayodhya - Varanasi - Prayagraj Tour Package & Price Details:</strong><br><br>
      • <strong>3-Day / 2-Night Complete Circuit:</strong><br>
        - <em>Same Day / Cab Only Circuit:</em> From <strong>₹1,499 - ₹2,499 per person</strong> (Private AC Cab + Toll + Sangam Boat + Station/Airport Transfers).<br>
        - <em>Deluxe Package (2 Nights Hotel + Cab + Darshan):</em> From <strong>₹3,499 - ₹4,999 per person</strong> (3-Star AC Hotel Stay with Breakfast + Dedicated AC Vehicle + Priority Darshan Assistance).<br>
        - <em>VIP Executive Package:</em> From <strong>₹5,999 - ₹7,999 per person</strong> (Luxury Hotel + Innova Crysta / Urbania + Sugam Darshan Passes + Personal Guide).<br><br>
      • <strong>Vehicle Fleet Assignment:</strong><br>
        - 1-3 Pax: AC Sedan (Dzire / Etios)<br>
        - 4-6 Pax: AC SUV (Ertiga / Innova Crysta)<br>
        - 7-8 Pax: AC Tempo Traveller (9-12 Seater) / 2 Ertigas<br>
        - 9-18 Pax: Luxury Force Urbania<br><br>
      • <strong>Booking Policy:</strong> 25%-30% advance token lock, balance 70%-75% on Day 1 arrival.<br><br>
      📞 Customized Itinerary & Group Discount ke liye call/WhatsApp: <strong>+91 92352 22399</strong>.`;
    }

    // 2. KASHI / VARANASI SUGAM DARSHAN PASS SPECIFIC QUERY
    if ((q.includes('kashi') || q.includes('varanasi') || q.includes('vishwanath')) && (q.includes('sugam') || q.includes('pass') || q.includes('ticket') || q.includes('rule') || q.includes('gate'))) {
      return `<strong>🛕 Kashi Vishwanath Sugam Darshan Rules & Pass Details (Varanasi):</strong><br><br>
      1. <strong>Direct Entry Gate:</strong> Sugam Darshan ticket dharakon ko <strong>Gate No. 4 (Chhatta Dwar)</strong> se direct priority entry milti hai bina aam lambi line mein khade hue (Darshan time ~15-20 mins).<br>
      2. <strong>Official Ticket Fee:</strong> Shri Kashi Vishwanath Temple Trust dwara Sugam Darshan ka official ticket fee <strong>₹300 per person</strong> hai.<br>
      3. <strong>Online Booking:</strong> Trust ki official website <em>shrikashivishwanath.org</em> par Aadhar Card / ID details se online slot book hota hai.<br>
      4. <strong>Dress Code:</strong> Dhoti-Kurta (Male) aur Saree/Salwar Suit (Female) recommended hai. Sparsh Darshan ke liye Dhoti/Saree mandatory hai.<br>
      5. <strong>Prohibited Items:</strong> Mobile phone, camera, smartwatches, leather belts aur metal objects Corridor ke andar allowed nahi hain (Lockers Gate No. 4 par available hain).<br>
      6. <strong>Humari Seva:</strong> Humare Varanasi tour packages mein Sugam Darshan ticket assistance aur local guide support shamil rehta hai! 📞 <strong>+91 92352 22399</strong>.`;
    }

    // 3. AYODHYA RAM MANDIR PASS SPECIFIC QUERY
    if ((q.includes('ayodhya') || q.includes('ram mandir') || q.includes('ram janmabhoomi')) && (q.includes('pass') || q.includes('vip') || q.includes('sugam') || q.includes('token') || q.includes('free'))) {
      return `<strong>🚩 Ayodhya Ram Mandir VIP & Sugam Darshan Details:</strong><br><br>
      1. <strong>100% Free Pass (Official ₹0):</strong> Shri Ram Janmabhoomi Teerth Kshetra Trust dwara Sugam Darshan, Aarti aur Wheelchair passes bilkul <strong>FREE OF COST (₹0)</strong> hote hain.<br>
      2. <strong>Online Booking:</strong> Trust ki official website <em>srjbtkshetra.org</em> par free Sugam Darshan / Aarti pass 15-30 din pehle book hota hai.<br>
      3. <strong>Offline Token Desk:</strong> Subah 6 AM par Mandir entrance token desk par limited free offline slots milte hain (Aadhar Card mandatory).<br>
      4. <strong>Humari Seva:</strong> Humare Deluxe/VIP yatra packages mein Sugam Darshan guidance, slot assistance aur door-step AC cab service free shamil hai! 📞 <strong>+91 92352 22399</strong>.`;
    }

    // 4. RUSH & DEPARTURE TIMING QUERY
    const isMorning = q.includes('subah') || q.includes('subha') || q.includes('subh') || q.includes('morn');
    const isDeparture = q.includes('nikle') || q.includes('nikal') || q.includes('nikale') || q.includes('nikake') || q.includes('baje') || q.includes('jana') || q.includes('jaye') || q.includes('time') || q.includes('samay');
    const isCrowd = q.includes('rush') || q.includes('bheed') || q.includes('crowd') || q.includes('kam') || q.includes('line');

    if (isCrowd || (isMorning && isDeparture) || q.includes('kitne baje') || q.includes('kitna baje') || q.includes('kab nikal') || q.includes('kab jana')) {
      return `<strong>🌅 Minimum Rush & Best Departure Timing Guide:</strong><br><br>
      Darshan ke liye sabse <strong>kam rush (minimum crowd)</strong> paane ke liye aapko in nirdharit timings par hotel se nikalna chahiye:<br><br>
      1. <strong>Ayodhya Ram Mandir:</strong><br>
         • <strong>Best Subah Timing:</strong> Hotel se subah <strong>6:00 AM se 6:30 AM</strong> tak nikal jayein, taaki 6:30 AM se 8:00 AM ke beech line mein lag sakein (~20-30 minutes mein aaram se darshan ho jate hain).<br>
         • <strong>Afternoon Slot:</strong> Duphahar <strong>1:45 PM</strong> par pahunchein (12 PM - 2 PM Vishram break khulne ke turant baad bheed kafi kam rehti hai).<br><br>
      2. <strong>Hanuman Garhi:</strong><br>
         • Subah <strong>5:30 AM se 6:30 AM</strong> tak pahunchein (76 seedhiyan aaram se bina rush ke chadh sakte hain).<br><br>
      3. <strong>Best Days:</strong> Wednesday, Thursday aur Friday ko sabse kam bheed hoti hai. (Tuesday, Saturday & Sunday ko heavy rush hota hai).<br><br>
      📞 Private AC Cab & VIP Darshan assistance ke liye call karein: <strong>+91 92352 22399</strong>.`;
    }

    // 5. SINGLE CITY GUIDES (Only evaluated if multi-city or pricing didn't match)
    if (q.includes('kashi') || q.includes('varanasi') || q.includes('banaras') || q.includes('sarnath')) {
      return `<strong>🛕 Kashi Vishwanath & Varanasi Yatra Guide:</strong><br><br>
      • <strong>Sugam Darshan:</strong> Gate No. 4 (Chhatta Dwar) se direct entry milti hai (Official Trust ticket ₹300 per person shrikashivishwanath.org par).<br>
      • <strong>Ganga Aarti:</strong> Dashashwamedh Ghat shaam 6:30 PM (Boat se sabse sundar view). Assi Ghat Subah-e-Banaras 5:00 AM.<br>
      • <strong>Kaal Bhairav:</strong> Kashi ke Kotwal Kaal Bhairav darshan zaroori hota hai.<br>
      • <strong>Sarnath:</strong> Varanasi se 10 km door Dhamek Stupa & Buddha complex.<br>
      📞 Varanasi 1-Day & 2-Night packages ke liye: <strong>+91 92352 22399</strong>.`;
    }

    if (q.includes('ayodhya') || q.includes('ram mandir') || q.includes('ram janmabhoomi') || q.includes('hanuman garhi')) {
      return `<strong>🚩 Ayodhya Ram Mandir & Dham Yatra Guide:</strong><br><br>
      • <strong>Ram Mandir:</strong> Subah 6:00 AM se Raat 10:00 PM (12 PM - 2 PM Vishram break).<br>
      • <strong>Aarti Timings:</strong> Mangala Aarti (4:30 AM), Shringar Aarti (6:30 AM), Sandhya Aarti (7:30 PM).<br>
      • <strong>Hanuman Garhi:</strong> Subah 5:00 AM se Raat 10:00 PM.<br>
      • <strong>Sarayu Aarti:</strong> Shaam 6:30 PM (Ram Ki Paidi).<br>
      📞 Ayodhya packages ke liye call/WhatsApp: <strong>+91 92352 22399</strong>.`;
    }

    if (q.includes('prayagraj') || q.includes('sangam') || q.includes('triveni') || q.includes('allahabad')) {
      return `<strong>🌊 Prayagraj Triveni Sangam Guide:</strong><br><br>
      • <strong>Sangam Snan:</strong> Private boat se Ganga, Yamuna & Saraswati milan sthal par 1.5 ghante ka snan tour.<br>
      • <strong>Darshan Sthal:</strong> Reclining Bade Hanuman Ji, Akshayavat & Patalpuri Mandir (Fort ID check), Alopi Devi.<br>
      • <strong>Ayodhya to Prayagraj:</strong> 165 km (~3.5 hrs drive).`;
    }

    if (q.includes('mathura') || q.includes('vrindavan') || q.includes('bihari') || q.includes('prem mandir') || q.includes('nidhivan')) {
      return `<strong>🛺 Mathura & Vrindavan Braj Yatra Guide:</strong><br><br>
      • <strong>Shri Krishna Janmabhoomi:</strong> Subah 5 AM - 12 PM & 4 PM - 9.30 PM.<br>
      • <strong>Banke Bihari (Vrindavan):</strong> Subah 7:45 AM - 12 PM & Shaam 5:30 PM - 9:30 PM (Curtain jhanka every 2 mins).<br>
      • <strong>Prem Mandir:</strong> Shaam 6:30 PM grand marble illumination & musical fountain.<br>
      • <strong>Nidhivan:</strong> Shaam 5 PM ke baad entry closed (Raas Leela mystery).`;
    }

    if (q.includes('chitrakoot') || q.includes('kamadgiri') || q.includes('godavari')) {
      return `<strong>🏹 Chitrakoot Dham Yatra Guide:</strong><br><br>
      • <strong>Ramghat Aarti:</strong> Har shaam 6:30 PM Mandakini river bank.<br>
      • <strong>Kamadgiri Parikrama:</strong> 5 km paved path (E-rickshaw/Doli available).<br>
      • <strong>Gupt Godavari:</strong> Natural stream caves tour.<br>
      • <strong>Hanuman Dhara:</strong> Hilltop shrine (360 steps ya Ropeway).`;
    }

    if (q.includes('naimisharanya') || q.includes('neemsar') || q.includes('chakra tirth')) {
      return `<strong>📜 Naimisharanya (Neemsar) Guide:</strong><br><br>
      • 88,000 Rishiyon ki tapobhoomi jahan Ved Vyas ji ne 18 Puranon ki rachna ki.<br>
      • <strong>Pramukh Sthal:</strong> Circular Chakra Tirth snan, Maa Lalita Devi Shaktipeeth, Vyas Gaddi, Dadhichi Kund.<br>
      • <strong>Distance:</strong> Lucknow se 90 km (~2.5 hrs drive). 1-day trip ideal hai.`;
    }

    if (q.includes('vindhyachal') || q.includes('vindhyavasini')) {
      return `<strong>🔱 Vindhyachal Dham Guide:</strong><br><br>
      • <strong>Maa Vindhyavasini Shaktipeeth:</strong> VIP Darshan & Pucca Ghat Ganga Snan.<br>
      • <strong>Trikon Parikrama:</strong> Maa Vindhyavasini -> Kali Khoh -> Ashtabhuja Devi (Ropeway available).<br>
      • <strong>Distance:</strong> Varanasi se 65 km (~1.5 hrs drive).`;
    }

    if (q.includes('gaya') || q.includes('bodhgaya') || q.includes('vishnupad')) {
      return `<strong>🪔 Gaya Pitru Pind Daan Guide:</strong><br><br>
      • <strong>Vishnupad Mandir:</strong> Bhagwan Vishnu ke 40cm charan chinha par pinda daan.<br>
      • <strong>Bodhgaya:</strong> Mahabodhi Temple & 80ft Great Buddha statue.<br>
      • <strong>Distance:</strong> Varanasi se 250 km (NH 19).`;
    }

    // GENERAL GREETING OR GENERAL QUERY
    if (q.includes('hi') || q.includes('hello') || q.includes('pranam') || q.includes('ram ram') || q.includes('jai shree ram') || q.includes('namaste')) {
      return `<strong>॥ जय श्री राम ॥</strong><br><br>
      Pranam! Main Pt. Ram Shastri, Ayodhya Dharshan ka <strong>AI Yatra Assistant</strong> hu. Aapko Ayodhya Ram Mandir, Kashi Vishwanath, Triveni Sangam Prayagraj, Mathura, Vrindavan, Chitrakoot, Naimisharanya, Vindhyachal ya Gaya ke baare mein jo bhi jaankari chahiye, poochhein!`;
    }

    // Dynamic Smart AI Fallback
    return `<strong>🚩 Pt. Ram Shastri (AI Agent Response):</strong><br><br>
    Aapne pucha: <em>"${query}"</em><br><br>
    Humare pass Uttar Pradesh ke sabhi 8 major teerth sthalon (Ayodhya, Varanasi, Prayagraj, Mathura, Vrindavan, Chitrakoot, Naimisharanya, Vindhyachal, Gaya) ki complete jaankari aur yatra packages available hain.<br><br>
    Aap specific tour price, mandir timings, VIP pass, Kashi Vishwanath Sugam Darshan, minimum rush hours, cabs ya hotels ke baare mein poochh sakte hain, ya humare Yatra Desk se direct baat karein:<br>
    📞 <strong>Call:</strong> <a href="tel:+919235222399">+91 92352 22399</a><br>
    💬 <strong>WhatsApp:</strong> <a href="https://wa.me/919235222399?text=Jai%20Shree%20Ram!%20I%20have%20a%20query." target="_blank">Direct Chat With Yatra Desk</a>`;
  }
})();
