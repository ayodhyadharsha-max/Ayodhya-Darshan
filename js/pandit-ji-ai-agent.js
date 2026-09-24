/**
 * AYODHYA DHARSHAN - PANDIT JI AI YATRA AGENT WIDGET
 * Smart Multi-Lingual Reasoning Engine (Hindi, Hinglish, English)
 * Robust Spelling & Fuzzy NLP Intent Matcher
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
          Pranam! Main Ayodhya Dharshan ka <strong>Smart AI Yatra Agent</strong> hu. Aap Hindi, Hinglish ya English mein kuch bhi poochhein — <em>Rush kam kab milega, Kashi Vishwanath Sugam Darshan rules, Ram Mandir timings, Mathura, Prayagraj, Hotels ya Cab fares!</em>
        </div>

        <div class="pj-quick-prompts">
          <div class="pj-chip" onclick="pjAskPrompt('Subah kitne baje nikalna chahiye darshan ke liye?')">🕐 Minimum Rush & Departure Time</div>
          <div class="pj-chip" onclick="pjAskPrompt('Kashi Vishwanath Sugam Darshan rules kya hain?')">🛕 Kashi Sugam Darshan (₹300)</div>
          <div class="pj-chip" onclick="pjAskPrompt('Ram Mandir VIP Pass kaise milta hai?')">🚩 Ayodhya Ram Mandir Pass (Free)</div>
          <div class="pj-chip" onclick="pjAskPrompt('Ayodhya Varanasi Prayagraj 3 day tour price?')">🚗 3-City Package Cost</div>
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

  // Robust NLP Intent Engine (Handles Spelling Variations & Conversational Queries)
  function generateSmartAIResponse(query) {
    const q = query.toLowerCase();

    // Normalizing common spelling variations
    const isMorning = q.includes('subah') || q.includes('subha') || q.includes('subh') || q.includes('morn');
    const isDeparture = q.includes('nikle') || q.includes('nikal') || q.includes('nikale') || q.includes('nikake') || q.includes('baje') || q.includes('jana') || q.includes('jaye') || q.includes('time') || q.includes('samay');
    const isCrowd = q.includes('rush') || q.includes('bheed') || q.includes('crowd') || q.includes('kam') || q.includes('line');

    // 1. RUSH & DEPARTURE TIMING QUERY (Subah kitne baje nikalna / jana chahiye jisse rush kam mile)
    if (isCrowd || (isMorning && isDeparture) || (q.includes('kitne baje') || q.includes('kitna baje') || q.includes('kab nikal') || q.includes('kab jana') || q.includes('kab nikalna'))) {
      return `<strong>🌅 Minimum Rush & Best Departure Timing Guide:</strong><br><br>
      Darshan ke liye sabse <strong>kam rush (minimum crowd)</strong> paane ke liye aapko in nirdharit timings par hotel se nikalna chahiye:<br><br>
      1. <strong>Ayodhya Ram Mandir:</strong><br>
         • <strong>Best Subah Timing:</strong> Hotel se subah <strong>6:00 AM se 6:30 AM</strong> tak nikal jayein, taaki 6:30 AM se 8:00 AM ke beech line mein lag sakein (~20-30 minutes mein aaram se darshan ho jate hain).<br>
         • <strong>Afternoon Slot:</strong> Duphahar <strong>1:45 PM</strong> par pahunchein (12 PM - 2 PM Vishram break khulne ke turant baad bheed kafi kam rehti hai).<br><br>
      2. <strong>Hanuman Garhi:</strong><br>
         • Subah <strong>5:30 AM se 6:30 AM</strong> tak pahunchein. Iss samay 76 seedhiyan bina rush ke aaram se chadh sakte hain.<br><br>
      3. <strong>Kashi Vishwanath (Varanasi):</strong><br>
         • Sugam Darshan pass ke sath subah <strong>6:00 AM - 7:30 AM</strong> ya Mangala Aarti ke turant baad Gate No. 4 se fastest entry milti hai.<br><br>
      4. <strong>Best Days:</strong> Wednesday, Thursday aur Friday ko sabse kam bheed hoti hai. (Tuesday, Saturday & Sunday ko heavy rush hota hai).<br><br>
      📞 Private AC Cab & VIP Darshan assistance ke liye call karein: <strong>+91 92352 22399</strong>.`;
    }

    // 2. KASHI / VARANASI SPECIFIC QUERY
    if (q.includes('kashi') || q.includes('varanasi') || q.includes('banaras') || q.includes('vishwanath') || q.includes('sarnath')) {
      if (q.includes('sugam') || q.includes('pass') || q.includes('ticket') || q.includes('rule') || q.includes('vip') || q.includes('gate') || q.includes('cost') || q.includes('fee')) {
        return `<strong>🛕 Kashi Vishwanath Sugam Darshan Rules & Pass Details (Varanasi):</strong><br><br>
        1. <strong>Direct Entry Gate:</strong> Sugam Darshan ticket dharakon ko <strong>Gate No. 4 (Chhatta Dwar)</strong> se direct priority entry milti hai bina aam lambi line mein khade hue (Darshan time ~15-20 mins).<br>
        2. <strong>Official Ticket Fee:</strong> Shri Kashi Vishwanath Temple Trust dwara Sugam Darshan ka official ticket fee <strong>₹300 per person</strong> hai.<br>
        3. <strong>Online Booking:</strong> Trust ki official website <em>shrikashivishwanath.org</em> par Aadhar Card / ID details se online slot book hota hai.<br>
        4. <strong>Dress Code:</strong> Dhoti-Kurta (Male) aur Saree/Salwar Suit (Female) recommended hai. Sparsh Darshan ke liye Dhoti/Saree mandatory hai.<br>
        5. <strong>Prohibited Items:</strong> Mobile phone, camera, smartwatches, leather belts aur metal objects Corridor ke andar allowed nahi hain (Lockers Gate No. 4 par available hain).<br>
        6. <strong>Humari Seva:</strong> Humare Varanasi tour packages mein Sugam Darshan ticket assistance aur local guide support shamil rehta hai! 📞 <strong>+91 92352 22399</strong>.`;
      }
      return `<strong>🛕 Kashi Vishwanath & Varanasi Yatra Guide:</strong><br><br>
      • <strong>Sugam Darshan:</strong> Gate No. 4 (Chhatta Dwar) se direct entry milti hai (Official Trust ticket ₹300 per person shrikashivishwanath.org par).<br>
      • <strong>Ganga Aarti:</strong> Dashashwamedh Ghat shaam 6:30 PM (Boat se sabse sundar view). Assi Ghat Subah-e-Banaras 5:00 AM.<br>
      • <strong>Kaal Bhairav:</strong> Kashi ke Kotwal Kaal Bhairav darshan zaroori hota hai.<br>
      • <strong>Sarnath:</strong> Varanasi se 10 km door Dhamek Stupa & Buddha complex.<br>
      📞 Varanasi 1-Day & 2-Night packages ke liye: <strong>+91 92352 22399</strong>.`;
    }

    // 3. AYODHYA RAM MANDIR SPECIFIC QUERY
    if (q.includes('ayodhya') || q.includes('ram mandir') || q.includes('ram janmabhoomi') || q.includes('hanuman garhi')) {
      if (q.includes('pass') || q.includes('vip') || q.includes('sugam') || q.includes('token') || q.includes('ticket') || q.includes('booking') || q.includes('cost') || q.includes('free')) {
        return `<strong>🚩 Ayodhya Ram Mandir VIP & Sugam Darshan Details:</strong><br><br>
        1. <strong>100% Free Pass (Official ₹0):</strong> Shri Ram Janmabhoomi Teerth Kshetra Trust dwara Sugam Darshan, Aarti aur Wheelchair passes bilkul <strong>FREE OF COST (₹0)</strong> hote hain.<br>
        2. <strong>Online Booking:</strong> Trust ki official website <em>srjbtkshetra.org</em> par free Sugam Darshan / Aarti pass 15-30 din pehle book hota hai.<br>
        3. <strong>Offline Token Desk:</strong> Subah 6 AM par Mandir entrance token desk par limited free offline slots milte hain (Aadhar Card mandatory).<br>
        4. <strong>Humari Seva:</strong> Humare Deluxe/VIP yatra packages mein Sugam Darshan guidance, slot assistance aur door-step AC cab service free shamil hai! 📞 <strong>+91 92352 22399</strong>.`;
      }
      if (q.includes('timing') || q.includes('time') || q.includes('khulta') || q.includes('aarti')) {
        return `<strong>⏰ Ram Mandir & Hanuman Garhi Timings:</strong><br><br>
        • <strong>Ram Mandir:</strong> Subah 6:00 AM se Raat 10:00 PM (Duphahar 12:00 PM - 2:00 PM Vishram break).<br>
        • <strong>Aarti Timings:</strong> Mangala Aarti (4:30 AM), Shringar Aarti (6:30 AM), Sandhya Aarti (7:30 PM).<br>
        • <strong>Hanuman Garhi:</strong> Subah 5:00 AM se Raat 10:00 PM (76 seedhiyan).<br>
        • <strong>Sarayu Aarti (Ram Ki Paidi):</strong> Har shaam 6:30 PM.`;
      }
      if (q.includes('wheelchair') || q.includes('bujurg') || q.includes('senior')) {
        return `<strong>♿ Senior Citizen & Accessibility Support (Ayodhya):</strong><br><br>
        1. Ram Mandir entrance gate par Free Wheelchair + Golf Cart Battery Car facility available hai.<br>
        2. Hanuman Garhi ke liye 76 seedhiyan hain (palanquin/doli facility available).<br>
        3. Humare packages mein senior citizens ke liye priority assistance aur door-step cab drop shamil rehta hai.`;
      }
    }

    // 4. PRAYAGRAJ / TRIVENI SANGAM
    if (q.includes('prayagraj') || q.includes('sangam') || q.includes('triveni') || q.includes('allahabad')) {
      return `<strong>🌊 Prayagraj Triveni Sangam Guide:</strong><br><br>
      • <strong>Sangam Snan:</strong> Private boat se Ganga, Yamuna & Saraswati milan sthal par 1.5 ghante ka snan tour.<br>
      • <strong>Darshan Sthal:</strong> Reclining Bade Hanuman Ji, Akshayavat & Patalpuri Mandir (Fort ID check), Alopi Devi.<br>
      • <strong>Ayodhya to Prayagraj:</strong> 165 km (~3.5 hrs drive).`;
    }

    // 5. MATHURA & VRINDAVAN
    if (q.includes('mathura') || q.includes('vrindavan') || q.includes('bihari') || q.includes('prem mandir') || q.includes('nidhivan')) {
      return `<strong>🛺 Mathura & Vrindavan Braj Yatra Guide:</strong><br><br>
      • <strong>Shri Krishna Janmabhoomi:</strong> Subah 5 AM - 12 PM & 4 PM - 9.30 PM.<br>
      • <strong>Banke Bihari (Vrindavan):</strong> Subah 7:45 AM - 12 PM & Shaam 5:30 PM - 9:30 PM (Curtain jhanka every 2 mins).<br>
      • <strong>Prem Mandir:</strong> Shaam 6:30 PM grand marble illumination & musical fountain.<br>
      • <strong>Nidhivan:</strong> Shaam 5 PM ke baad entry closed (Raas Leela mystery).`;
    }

    // 6. CHITRAKOOT
    if (q.includes('chitrakoot') || q.includes('kamadgiri') || q.includes('godavari')) {
      return `<strong>🏹 Chitrakoot Dham Yatra Guide:</strong><br><br>
      • <strong>Ramghat Aarti:</strong> Har shaam 6:30 PM Mandakini river bank.<br>
      • <strong>Kamadgiri Parikrama:</strong> 5 km paved path (E-rickshaw/Doli available).<br>
      • <strong>Gupt Godavari:</strong> Natural stream caves tour.<br>
      • <strong>Hanuman Dhara:</strong> Hilltop shrine (360 steps ya Ropeway).`;
    }

    // 7. NAIMISHARANYA
    if (q.includes('naimisharanya') || q.includes('neemsar') || q.includes('chakra tirth')) {
      return `<strong>📜 Naimisharanya (Neemsar) Guide:</strong><br><br>
      • 88,000 Rishiyon ki tapobhoomi jahan Ved Vyas ji ne 18 Puranon ki rachna ki.<br>
      • <strong>Pramukh Sthal:</strong> Circular Chakra Tirth snan, Maa Lalita Devi Shaktipeeth, Vyas Gaddi, Dadhichi Kund.<br>
      • <strong>Distance:</strong> Lucknow se 90 km (~2.5 hrs drive). 1-day trip ideal hai.`;
    }

    // 8. VINDHYACHAL
    if (q.includes('vindhyachal') || q.includes('vindhyavasini')) {
      return `<strong>🔱 Vindhyachal Dham Guide:</strong><br><br>
      • <strong>Maa Vindhyavasini Shaktipeeth:</strong> VIP Darshan & Pucca Ghat Ganga Snan.<br>
      • <strong>Trikon Parikrama:</strong> Maa Vindhyavasini -> Kali Khoh -> Ashtabhuja Devi (Ropeway available).<br>
      • <strong>Distance:</strong> Varanasi se 65 km (~1.5 hrs drive).`;
    }

    // 9. GAYA
    if (q.includes('gaya') || q.includes('bodhgaya') || q.includes('vishnupad')) {
      return `<strong>🪔 Gaya Pitru Pind Daan Guide:</strong><br><br>
      • <strong>Vishnupad Mandir:</strong> Bhagwan Vishnu ke 40cm charan chinha par pinda daan.<br>
      • <strong>Bodhgaya:</strong> Mahabodhi Temple & 80ft Great Buddha statue.<br>
      • <strong>Distance:</strong> Varanasi se 250 km (NH 19).`;
    }

    // 10. COST & CAB CALCULATION / HOTEL ALLOCATION RULES
    if (q.includes('cost') || q.includes('price') || q.includes('rate') || q.includes('cab') || q.includes('hotel') || q.includes('package') || q.includes('car') || q.includes('sedan') || q.includes('ertiga') || q.includes('innova') || q.includes('tempo') || q.includes('budget') || q.includes('kharcha')) {
      return `<strong>🚗 Pricing, Vehicle & Hotel Allocation Rules:</strong><br><br>
      • <strong>1 to 3 Pax:</strong> Private AC Sedan (Dzire/Etios) assign hoti hai.<br>
      • <strong>4 to 6 Pax:</strong> Spacious AC SUV (Ertiga / Innova Crysta).<br>
      • <strong>7 to 8 Pax:</strong> AC Tempo Traveller (9-12 Seater) / 2 Ertigas.<br>
      • <strong>9 to 18 Pax:</strong> Luxury Force Urbania / 17 Seater Tempo Traveller.<br>
      • <strong>Room Allocation:</strong> 2 Adults = 1 Double AC Room. 4 Adults = 2 Rooms. Child < 5 yrs = Free stay.<br>
      • <strong>Package Rates:</strong><br>
        - <em>Same Day Tour:</em> Starting ₹1,499 / person.<br>
        - <em>Deluxe Package (Hotel + Cab + Darshan):</em> Starting ₹3,499 / person.<br>
        - <em>VIP Executive Package:</em> Starting ₹5,999 / person.<br>
      • <strong>Inclusions:</strong> Toll, Parking, Driver Allowance, Fuel, Hotel Stay & AC Transport included.<br>
      📞 Custom Quote ke liye call/WhatsApp: <strong>+91 92352 22399</strong>.`;
    }

    // 11. GENERAL GREETING OR GENERAL QUERY
    if (q.includes('hi') || q.includes('hello') || q.includes('pranam') || q.includes('ram ram') || q.includes('jai shree ram') || q.includes('namaste')) {
      return `<strong>॥ जय श्री राम ॥</strong><br><br>
      Pranam! Main Pt. Ram Shastri, Ayodhya Dharshan ka <strong>AI Yatra Assistant</strong> hu. Aapko Ayodhya Ram Mandir, Kashi Vishwanath, Triveni Sangam Prayagraj, Mathura, Vrindavan, Chitrakoot, Naimisharanya, Vindhyachal ya Gaya ke baare mein jo bhi jaankari chahiye, poochhein!`;
    }

    // Dynamic Smart AI Fallback with direct context matching
    return `<strong>🚩 Pt. Ram Shastri (AI Agent Response):</strong><br><br>
    Aapne pucha: <em>"${query}"</em><br><br>
    Humare pass Uttar Pradesh ke sabhi 8 major teerth sthalon (Ayodhya, Varanasi, Prayagraj, Mathura, Vrindavan, Chitrakoot, Naimisharanya, Vindhyachal, Gaya) ki complete jaankari aur yatra packages available hain.<br><br>
    Aap specific mandir timings, VIP pass, Kashi Vishwanath Sugam Darshan, minimum rush hours, cabs ya hotels ke baare mein poochh sakte hain, ya humare Yatra Desk se direct baat karein:<br>
    📞 <strong>Call:</strong> <a href="tel:+919235222399">+91 92352 22399</a><br>
    💬 <strong>WhatsApp:</strong> <a href="https://wa.me/919235222399?text=Jai%20Shree%20Ram!%20I%20have%20a%20query." target="_blank">Direct Chat With Yatra Desk</a>`;
  }
})();
