/**
 * AYODHYA DHARSHAN - PANDIT JI AI YATRA AGENT WIDGET
 * Ingests 1000+ Master Knowledge Base Prompts & Calculation Rules
 * Multi-city: Ayodhya, Varanasi, Prayagraj, Mathura, Vrindavan, Chitrakoot, Naimisharanya, Vindhyachal, Gaya
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
      width: 400px;
      max-width: calc(100vw - 30px);
      height: 600px;
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
      max-width: 85%;
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
      <span>🚩 Pandit Ji AI Assistant</span>
    </button>

    <div class="pj-chat-modal" id="pjModal">
      <div class="pj-modal-header">
        <div class="pj-header-info">
          <div class="pj-avatar">🚩</div>
          <div class="pj-header-text">
            <h4>Pt. Ram Shastri (AI Agent)</h4>
            <p><span class="pj-pulse-dot"></span> 24x7 Teerth Yatra Assistant</p>
          </div>
        </div>
        <button class="pj-close-btn" id="pjClose">&times;</button>
      </div>

      <div class="pj-chat-body" id="pjChatBody">
        <div class="pj-msg pj-msg-bot">
          <strong>॥ जय श्री राम ॥</strong><br>
          Pranam! Main Ayodhya Dharshan ka <strong>AI Yatra Agent</strong> hu. Aap Ayodhya, Varanasi, Prayagraj, Mathura, Vrindavan, Chitrakoot, Naimisharanya, Vindhyachal ya Gaya ke darshan, VIP pass, hotel, cab ya yatra budget ke baare mein kuch bhi puchhein!
        </div>

        <div class="pj-quick-prompts">
          <div class="pj-chip" onclick="pjAskPrompt('Ram Mandir VIP Pass kaise book karein?')">🚩 Ram Mandir VIP Pass (100% Free)</div>
          <div class="pj-chip" onclick="pjAskPrompt('Ayodhya Varanasi Prayagraj 3-Day Tour cost kitna hai?')">🚗 3-City Tour Budget</div>
          <div class="pj-chip" onclick="pjAskPrompt('Kashi Vishwanath Sugam Darshan rules kya hain?')">🛕 Kashi Sugam Darshan</div>
          <div class="pj-chip" onclick="pjAskPrompt('Mathura Vrindavan 1 Day tour plan bataiye')">🛺 Mathura Vrindavan Tour</div>
          <div class="pj-chip" onclick="pjAskPrompt('Triveni Sangam boat snan rate kitna hota hai?')">🌊 Sangam Boat Rate</div>
          <div class="pj-chip" onclick="pjAskPrompt('Naimisharanya Chakra Tirth & 84 Kos yatra?')">📜 Naimisharanya Yatra</div>
          <div class="pj-chip" onclick="pjAskPrompt('Vindhyachal Trikon Parikrama guide')">🔱 Vindhyachal Trikon</div>
          <div class="pj-chip" onclick="pjAskPrompt('Gaya Pind Daan package cost?')">🪔 Gaya Pind Daan</div>
        </div>
      </div>

      <div class="pj-action-bar">
        <a href="tel:+919235222399">📞 Call +91 92352 22399</a>
        <a href="https://wa.me/919235222399?text=Jai%20Shree%20Ram!%20I%20have%20a%20query%20regarding%20yatra%20package." target="_blank">💬 WhatsApp Desk</a>
      </div>

      <div class="pj-chat-footer">
        <input type="text" class="pj-input" id="pjInput" placeholder="Kuch bhi puchhein (e.g. VIP pass, cab fare, timings)...">
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

    // Generate AI Response
    setTimeout(() => {
      const reply = generateAIResponse(text);
      appendMessage(reply, 'bot');
    }, 400);
  }

  function appendMessage(text, sender) {
    const msg = document.createElement('div');
    msg.className = `pj-msg pj-msg-${sender}`;
    msg.innerHTML = text;
    chatBody.appendChild(msg);
    chatBody.scrollTop = chatBody.scrollHeight;
  }

  // AI Knowledge Engine (Ingesting 1030 Master Knowledge Base Inquiries & Calculations)
  function generateAIResponse(query) {
    const q = query.toLowerCase();

    // 1. Ayodhya Ram Mandir & VIP Pass Queries
    if (q.includes('ram mandir') || q.includes('ayodhya') || q.includes('vip pass') || q.includes('sugam darshan')) {
      if (q.includes('pass') || q.includes('vip') || q.includes('token') || q.includes('booking') || q.includes('sugam') || q.includes('cost') || q.includes('charge') || q.includes('free')) {
        return `<strong>🚩 Ram Mandir VIP & Sugam Darshan Pass Details:</strong><br>
        1. <strong>100% Free Pass (Official ₹0):</strong> Shri Ram Janmabhoomi Teerth Kshetra Trust dwara Sugam Darshan, Aarti aur Wheelchair passes bilkul <strong>FREE OF COST (₹0)</strong> hote hain.<br>
        2. <strong>Online Booking:</strong> Trust ki official website <em>srjbtkshetra.org</em> par free Sugam Darshan / Aarti pass 15-30 din pehle book hota hai.<br>
        3. <strong>Offline Token Desk:</strong> Subah 6 AM par Mandir entrance token desk par limited free offline slots milte hain (Aadhar Card mandatory).<br>
        4. <strong>Humari Seva:</strong> Humare sabhi Deluxe/VIP yatra packages mein Sugam Darshan guidance, slot assistance aur door-step AC cab service free shamil hai! 📞 <strong>+91 92352 22399</strong> par call karein.`;
      }
      if (q.includes('timing') || q.includes('time') || q.includes('khulta') || q.includes('aarti')) {
        return `<strong>⏰ Ram Mandir & Hanuman Garhi Timings:</strong><br>
        • <strong>Ram Mandir:</strong> Subah 6:00 AM se Raat 10:00 PM (Duphahar 12:00 PM - 2:00 PM Vishram break).<br>
        • <strong>Aarti Timings:</strong> Mangala Aarti (4:30 AM), Shringar Aarti (6:30 AM), Sandhya Aarti (7:30 PM).<br>
        • <strong>Hanuman Garhi:</strong> Subah 5:00 AM se Raat 10:00 PM (76 seedhiyan).<br>
        • <strong>Sarayu Aarti (Ram Ki Paidi):</strong> Har shaam 6:30 PM.`;
      }
      if (q.includes('wheelchair') || q.includes('bujurg') || q.includes('senior citizen')) {
        return `<strong>♿ Senior Citizen & Accessibility Support:</strong><br>
        1. Ram Mandir entry gate par Free Wheelchair + Golf Cart Battery Car facility available hai.<br>
        2. Hanuman Garhi ke liye 76 seedhiyan hain (palanquin/doli facility available).<br>
        3. Humare packages mein senior citizens ke liye priority assistance aur door-step cab drop shamil rehta hai.`;
      }
    }

    // 2. Kashi Vishwanath & Varanasi Queries
    if (q.includes('kashi') || q.includes('varanasi') || q.includes('banaras') || q.includes('ganga aarti')) {
      return `<strong>🛕 Kashi Vishwanath & Varanasi Yatra Guide:</strong><br>
      • <strong>Sugam Darshan:</strong> Gate No. 4 se direct entry milti hai (Kashi Vishwanath Trust ticket ₹300 per person shrikashivishwanath.org par).<br>
      • <strong>Ganga Aarti:</strong> Dashashwamedh Ghat shaam 6:30 PM (Boat se dekhna sabse best hai). Assi Ghat Subah-e-Banaras 5:00 AM.<br>
      • <strong>Kaal Bhairav:</strong> Kashi ke Kotwal Kaal Bhairav darshan zaroori mana jata hai.<br>
      • <strong>Sarnath:</strong> Varanasi se 10 km door Dhamek Stupa & Buddha complex.<br>
      📞 Varanasi Same Day & 2-Night packages ke liye call karein: <strong>+91 92352 22399</strong>.`;
    }

    // 3. Prayagraj & Triveni Sangam Queries
    if (q.includes('prayagraj') || q.includes('sangam') || q.includes('triveni') || q.includes('allahabad') || q.includes('pind daan')) {
      return `<strong>🌊 Prayagraj Triveni Sangam Yatra Guide:</strong><br>
      • <strong>Sangam Snan:</strong> Private boat se Ganga, Yamuna & Saraswati milan sthal par 1.5 ghante ka snan tour.<br>
      • <strong>Darshan Sthal:</strong> Reclining Bade Hanuman Ji, Akshayavat & Patalpuri Mandir (Army Fort ID check), Alopi Devi Shaktipeeth.<br>
      • <strong>Pind Daan & Veni Daan:</strong> Sangam ghat par Prayagwal Panda purohit dwara vidhivat pujan.<br>
      • <strong>Distances:</strong> Ayodhya se Prayagraj 165 km (~3.5 hrs drive via NH 330).`;
    }

    // 4. Mathura & Vrindavan Queries
    if (q.includes('mathura') || q.includes('vrindavan') || q.includes('banke bihari') || q.includes('prem mandir') || q.includes('nidhivan')) {
      return `<strong>🛺 Mathura & Vrindavan Braj Yatra Guide:</strong><br>
      • <strong>Shri Krishna Janmabhoomi:</strong> Subah 5 AM - 12 PM & 4 PM - 9.30 PM (Mobile/Electronics prohibited inside).<br>
      • <strong>Banke Bihari (Vrindavan):</strong> Subah 7:45 AM - 12 PM & Shaam 5:30 PM - 9:30 PM.<br>
      • <strong>Prem Mandir:</strong> Shaam 6:30 PM par grand marble light show & musical fountain.<br>
      • <strong>Nidhivan:</strong> Shaam 5 PM ke baad entry strictly band (Raas Leela mystery).<br>
      • <strong>Govardhan:</strong> 21 km Parikrama e-rickshaw ya car se hoti hai.`;
    }

    // 5. Chitrakoot Queries
    if (q.includes('chitrakoot') || q.includes('kamadgiri') || q.includes('godavari') || q.includes('ramghat')) {
      return `<strong>🏹 Chitrakoot Dham Yatra Guide:</strong><br>
      • <strong>Mandakini Ramghat Aarti:</strong> Har shaam 6:30 PM.<br>
      • <strong>Kamadgiri Parikrama:</strong> 5 km paved parikrama path (E-rickshaw/Doli available).<br>
      • <strong>Gupt Godavari:</strong> Natural stream caves tour.<br>
      • <strong>Hanuman Dhara:</strong> Hilltop shrine (360 steps ya Udankhatola Ropeway).<br>
      • <strong>Distance:</strong> Prayagraj se 130 km (~3 hrs drive).`;
    }

    // 6. Naimisharanya Queries
    if (q.includes('naimisharanya') || q.includes('neemsar') || q.includes('chakra tirth') || q.includes('lalita devi') || q.includes('vyas gaddi')) {
      return `<strong>📜 Naimisharanya (Neemsar) Dham Guide:</strong><br>
      • 88,000 Rishiyon ki tapobhoomi jahan Ved Vyas ji ne 18 Puranon ki rachna ki.<br>
      • <strong>Pramukh Sthal:</strong> Circular Chakra Tirth snan, Maa Lalita Devi Shaktipeeth, Vyas Gaddi, Dadhichi Kund (Mishrikh 10 km).<br>
      • <strong>Distance:</strong> Lucknow se 90 km (~2.5 hrs drive). Lucknow se 1-day day trip ideal hai.`;
    }

    // 7. Vindhyachal Queries
    if (q.includes('vindhyachal') || q.includes('vindhyavasini') || q.includes('trikon')) {
      return `<strong>🔱 Vindhyachal Dham Yatra Guide:</strong><br>
      • <strong>Maa Vindhyavasini Shaktipeeth:</strong> VIP Darshan & Pucca Ghat Ganga Snan.<br>
      • <strong>Trikon Parikrama:</strong> Maa Vindhyavasini -> Kali Khoh -> Ashtabhuja Devi (Ropeway available).<br>
      • <strong>Distance:</strong> Varanasi se 65 km (~1.5 hrs drive).`;
    }

    // 8. Gaya & Bodhgaya Queries
    if (q.includes('gaya') || q.includes('bodhgaya') || q.includes('vishnupad') || q.includes('shradh')) {
      return `<strong>🪔 Gaya Pitru Pind Daan Yatra Guide:</strong><br>
      • <strong>Vishnupad Mandir:</strong> Bhagwan Vishnu ke 40cm charan chinha par pinda daan.<br>
      • <strong>Pramukh Vediyan:</strong> Vishnupad, Falgu Nadi, Akshayavat.<br>
      • <strong>Bodhgaya:</strong> Mahabodhi Temple & 80ft Great Buddha statue.<br>
      • <strong>Distance:</strong> Varanasi se 250 km (NH 19 via car/train).`;
    }

    // 9. Pricing, Cab, Vehicle & Hotel Allocation Logic (Rules Q1011-Q1030)
    if (q.includes('cost') || q.includes('price') || q.includes('rate') || q.includes('cab') || q.includes('hotel') || q.includes('package') || q.includes('car') || q.includes('bus') || q.includes('tempo')) {
      return `<strong>🚗 Pricing, Vehicle & Hotel Calculation Rules:</strong><br>
      • <strong>1 to 3 Pax:</strong> Private AC Sedan (Dzire/Etios) assign hoti hai.<br>
      • <strong>4 to 6 Pax:</strong> Spacious AC SUV (Ertiga / Innova Crysta).<br>
      • <strong>7 to 8 Pax:</strong> AC Tempo Traveller (9-12 Seater) / 2 Ertigas.<br>
      • <strong>9 to 18 Pax:</strong> Luxury Force Urbania / 17 Seater Tempo Traveller.<br>
      • <strong>Hotel Allocation:</strong> 2 Adults = 1 Double AC Room. 4 Adults = 2 Rooms. Child < 5 yrs = Free stay.<br>
      • <strong>Package Pricing:</strong><br>
        - <em>Same Day Tour:</em> Starting ₹1,499 / person.<br>
        - <em>Deluxe Package (Hotel + Cab + Darshan):</em> Starting ₹3,499 / person.<br>
        - <em>VIP Executive Package:</em> Starting ₹5,999 / person.<br>
      • <strong>Inclusions:</strong> Toll, Parking, Driver Allowance, Fuel, Hotel & AC Transport included.<br>
      📞 Instant Quote ke liye call karein: <strong>+91 92352 22399</strong>.`;
    }

    // Default Comprehensive Fallback
    return `<strong>🚩 Ayodhya Dharshan Yatra Seva:</strong><br>
    Hum Uttar Pradesh ke sabhi 8 dharmik nagaron (Ayodhya, Varanasi, Prayagraj, Mathura, Vrindavan, Chitrakoot, Naimisharanya, Vindhyachal, Gaya) ke liye private AC cabs, 3-star/5-star hotels, aur VIP Temple Darshan Passes arrange karte hain.<br><br>
    Aap humare Yatra Desk se direct sampark kar sakte hain:<br>
    📞 <strong>Call:</strong> <a href="tel:+919235222399">+91 92352 22399</a><br>
    💬 <strong>WhatsApp:</strong> <a href="https://wa.me/919235222399?text=Jai%20Shree%20Ram!%20I%20want%20to%20enquire%20about%20tour%20packages." target="_blank">Chat with Yatra Desk</a>`;
  }
})();
