/**
 * AYODHYA DHARSHAN - SMART AI YATRA AGENT (Pt. Ram Shastri)
 * Generative Conversational Engine (Hindi, Hinglish, English)
 * Advanced Multi-Lingual NLP & Spelling Variation Engine
 */

(function() {
  // Inject UI Styles
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
            <p><span class="pj-pulse-dot"></span> Smart 24x7 Yatra Guru</p>
          </div>
        </div>
        <button class="pj-close-btn" id="pjClose">&times;</button>
      </div>

      <div class="pj-chat-body" id="pjChatBody">
        <div class="pj-msg pj-msg-bot">
          <strong>॥ जय श्री राम ॥ 🙏</strong><br>
          Pranam ji! Main Pt. Ram Shastri hu, aapka personal <strong>AI Yatra Assistant</strong>. Aap apni language (Hindi, Hinglish ya English) mein jo bhi poochhenge, main aapko bilkul accurate aur easy jawab dunga!
        </div>

        <div class="pj-quick-prompts">
          <div class="pj-chip" onclick="pjAskPrompt('Kashi Vishwanath darshan me kitna time lagta hai?')">🛕 Kashi Darshan Duration</div>
          <div class="pj-chip" onclick="pjAskPrompt('Ayodhya Varanasi Prayagraj 3 day tour price?')">🚗 3-City Tour Price</div>
          <div class="pj-chip" onclick="pjAskPrompt('Subah kitne baje nikalna chahiye jisse rush kam mile?')">🕐 Minimum Rush Timings</div>
          <div class="pj-chip" onclick="pjAskPrompt('Kashi Vishwanath Sugam Darshan rules kya hain?')">🛕 Kashi Sugam Pass (₹300)</div>
          <div class="pj-chip" onclick="pjAskPrompt('Ram Mandir VIP Pass kaise milta hai?')">🚩 Ram Mandir Pass (Free)</div>
        </div>
      </div>

      <div class="pj-action-bar">
        <a href="tel:+919235222399">📞 Call +91 92352 22399</a>
        <a href="https://wa.me/919235222399?text=Jai%20Shree%20Ram!%20I%20want%20to%20enquire%20about%20yatra%20package." target="_blank">💬 WhatsApp Desk</a>
      </div>

      <div class="pj-chat-footer">
        <input type="text" class="pj-input" id="pjInput" placeholder="Aap apni language mein kuch bhi poochhein...">
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

    // Generate Smart Conversational AI Response
    setTimeout(() => {
      const reply = generateConversationalAIResponse(text);
      appendMessage(reply, 'bot');
    }, 250);
  }

  function appendMessage(text, sender) {
    const msg = document.createElement('div');
    msg.className = `pj-msg pj-msg-${sender}`;
    msg.innerHTML = text;
    chatBody.appendChild(msg);
    chatBody.scrollTop = chatBody.scrollHeight;
  }

  // Generative Conversational Reasoning Engine
  function generateConversationalAIResponse(query) {
    const q = query.toLowerCase();

    // Check language tone
    const isPureEnglish = /^[a-zA-Z0-9\s\?\!\,\.\'\"]+$/.test(query) && (q.includes('what') || q.includes('how') || q.includes('where') || q.includes('when') || q.includes('is') || q.includes('can') || q.includes('the'));

    // Normalize spelling variations for Kashi / Vishwanath / Banaras
    const isKashi = q.includes('kashi') || q.includes('varanasi') || q.includes('banaras') || q.includes('vishwanath') || q.includes('visvanath') || q.includes('biswanath') || q.includes('sarnath');
    const isDuration = q.includes('kitna time') || q.includes('kitne ghante') || q.includes('time lag') || q.includes('samay') || q.includes('duration') || q.includes('waiting') || q.includes('line') || q.includes('queue');

    // 1. KASHI VISHWANATH DARSHAN TIME & DURATION SPECIFIC QUERY (Highest Priority for Kashi Vishwanath Timing Questions)
    if (isKashi && (isDuration || q.includes('darshan'))) {
      if (isDuration || q.includes('time') || q.includes('samay') || q.includes('ghante')) {
        return `<strong>🛕 Kashi Vishwanath Darshan Duration & Waiting Time (Varanasi):</strong><br><br>` +
        `Kashi Vishwanath Corridor mein darshan karne mein kitna samay lagta hai, iska complete breakdown below hai:<br><br>` +
        `1. <strong>Sugam Darshan (VIP Entry - Gate 4):</strong><br>` +
        `   • Sugam Darshan ticket (₹300) ke sath aaram se <strong>15 se 30 minutes</strong> mein darshan ho jate hain.<br><br>` +
        `2. <strong>Regular Line (General Entry):</strong><br>` +
        `   • <em>Normal Days (Wed/Thu/Fri):</em> Regular queue mein <strong>1 se 2 ghante</strong> ka samay lagta hai.<br>` +
        `   • <em>Peak Days (Monday/Sawan/Festivals):</em> Regular line mein <strong>3 se 5 ghante</strong> tak ka waiting time ho sakta hai.<br><br>` +
        `3. <strong>Best Time for Fast Darshan:</strong><br>` +
        `   • Subah <strong>5:00 AM se 7:00 AM</strong> (Mangala Aarti ke turant baad) ya raat ko <strong>8:30 PM se 9:30 PM</strong> par sabse kam line milti hai.<br><br>` +
        `📞 Sugam Darshan booking assistance & Varanasi Cab/Hotel booking ke liye: <strong>+91 92352 22399</strong>.`;
      }
    }

    // 2. MULTI-CITY PACKAGE & TOUR PRICE QUERIES
    if ((q.includes('ayodhya') && q.includes('varanasi')) || (q.includes('varanasi') && q.includes('prayagraj')) || q.includes('3 day') || q.includes('3-day') || q.includes('2 day') || (q.includes('price') && q.includes('tour')) || (q.includes('cost') && q.includes('tour')) || q.includes('package')) {
      if (isPureEnglish) {
        return `<strong>🚗 Ayodhya - Varanasi - Prayagraj Tour Package & Price:</strong><br><br>` +
        `• <strong>3-Day / 2-Night Complete Circuit:</strong><br>` +
        `  - <em>Express Cab Only Tour:</em> Starts at <strong>₹1,499 - ₹2,499 per person</strong> (Private AC Sedan/SUV + Toll + Sangam Boat + All Transfers).<br>` +
        `  - <em>Deluxe Tour (2 Nights Hotel + AC Cab + VIP Assistance):</em> Starts at <strong>₹3,499 - ₹4,999 per person</strong> (3-Star AC Hotel with Breakfast + Private Cab + Priority Darshan Assistance).<br>` +
        `  - <em>VIP Executive Package:</em> Starts at <strong>₹5,999 - ₹7,999 per person</strong> (5-Star/Luxury Hotel + Innova Crysta/Urbania + Personal Guide + VIP Passes).<br><br>` +
        `• <strong>Vehicle Options:</strong><br>` +
        `  - 1-3 Pax: AC Sedan (Dzire / Etios)<br>` +
        `  - 4-6 Pax: AC SUV (Ertiga / Innova Crysta)<br>` +
        `  - 7-18 Pax: Luxury Force Urbania / Tempo Traveller<br><br>` +
        `📞 Call/WhatsApp our Yatra Desk for instant custom quotes: <strong>+91 92352 22399</strong>.`;
      }
      return `<strong>🚗 Ayodhya - Varanasi - Prayagraj Yatra Package & Pricing:</strong><br><br>` +
      `Ji bilkul! 3-Day Ayodhya, Varanasi aur Prayagraj yatra ke liye humare pass 3 budget options hain:<br><br>` +
      `1. <strong>Same Day / Cab Only Tour:</strong> <strong>₹1,499 - ₹2,499 per person</strong> (Private AC Cab + Toll + Sangam Boat + Station/Airport Pickup-Drop).<br>` +
      `2. <strong>Deluxe Package (2 Nights Hotel + Cab + Darshan):</strong> <strong>₹3,499 - ₹4,999 per person</strong> (3-Star AC Hotel Stay + Breakfast + Private AC Sedan/SUV + VIP Assistance).<br>` +
      `3. <strong>VIP Executive Package:</strong> <strong>₹5,999 - ₹7,999 per person</strong> (Luxury Hotel + Innova Crysta/Urbania + Dedicated Guide + VIP Entry Passes).<br><br>` +
      `• <strong>Gaadi Selection:</strong><br>` +
      `  - 1-3 Log: AC Sedan (Dzire/Etios)<br>` +
      `  - 4-6 Log: AC SUV (Ertiga/Innova Crysta)<br>` +
      `  - 7-18 Log: AC Tempo Traveller / Luxury Force Urbania<br><br>` +
      `📞 Instant Booking ya discount ke liye call/WhatsApp karein: <strong>+91 92352 22399</strong>.`;
    }

    // 3. KASHI VISHWANATH SUGAM DARSHAN RULES (Varanasi)
    if (isKashi && (q.includes('sugam') || q.includes('pass') || q.includes('ticket') || q.includes('rule') || q.includes('gate') || q.includes('vip'))) {
      return `<strong>🛕 Kashi Vishwanath Sugam Darshan Rules & Pass (Varanasi):</strong><br><br>` +
      `1. <strong>Direct Entry Gate:</strong> Sugam Darshan pass dharakon ko <strong>Gate No. 4 (Chhatta Dwar)</strong> se direct priority entry milti hai (Darshan time ~15-20 mins).<br>` +
      `2. <strong>Official Ticket Fee:</strong> Shri Kashi Vishwanath Temple Trust ka official ticket fee <strong>₹300 per person</strong> hai.<br>` +
      `3. <strong>Online Slot:</strong> Trust ki official website <em>shrikashivishwanath.org</em> par Aadhar Card details se booking hoti hai.<br>` +
      `4. <strong>Dress Code & Rules:</strong> Dhoti-Kurta (Men) aur Saree/Salwar Suit (Women). Sparsh Darshan ke liye Dhoti/Saree mandatory hai. Mobile phones & leather belts Corridor ke andar prohibited hain (Lockers Gate 4 par available hain).<br><br>` +
      `📞 Varanasi Tour & Sugam Ticket assistance ke liye call karein: <strong>+91 92352 22399</strong>.`;
    }

    // 4. AYODHYA RAM MANDIR PASS RULES (100% Free)
    if ((q.includes('ayodhya') || q.includes('ram mandir') || q.includes('ram janmabhoomi')) && (q.includes('pass') || q.includes('vip') || q.includes('sugam') || q.includes('token') || q.includes('free') || q.includes('charge'))) {
      return `<strong>🚩 Ayodhya Ram Mandir Pass Details (100% Free):</strong><br><br>` +
      `1. <strong>Official Fee ₹0 (Free):</strong> Shri Ram Janmabhoomi Teerth Kshetra Trust dwara Sugam Darshan, Aarti aur Wheelchair passes bilkul <strong>FREE (₹0)</strong> hote hain.<br>` +
      `2. <strong>Online Booking:</strong> Official site <em>srjbtkshetra.org</em> par free Aarti/Sugam pass 15-30 din pehle book hota hai.<br>` +
      `3. <strong>Offline Token:</strong> Subah 6 AM par Mandir entry token desk par limited free slots milte hain (Aadhar Card mandatory).<br>` +
      `4. <strong>Humari Seva:</strong> Humare Deluxe/VIP yatra packages mein Sugam Darshan guidance aur door-step cab pickup free shamil hai! 📞 <strong>+91 92352 22399</strong>.`;
    }

    // 5. RUSH & DEPARTURE TIMING (Subah kitne baje nikalein / jana chahiye jisse bheed kam mile)
    const isMorning = q.includes('subah') || q.includes('subha') || q.includes('subh') || q.includes('morn');
    const isDeparture = q.includes('nikle') || q.includes('nikal') || q.includes('nikale') || q.includes('nikake') || q.includes('baje') || q.includes('jana') || q.includes('jaye') || q.includes('time') || q.includes('samay');
    const isCrowd = q.includes('rush') || q.includes('bheed') || q.includes('crowd') || q.includes('kam') || q.includes('line');

    if (isCrowd || (isMorning && isDeparture) || q.includes('kitne baje') || q.includes('kitna baje') || q.includes('kab nikal') || q.includes('kab jana')) {
      return `<strong>🌅 Minimum Rush & Best Departure Timing Guide:</strong><br><br>` +
      `Subah sabse <strong>kam rush (minimum crowd)</strong> paane ke liye in nirdharit timings par hotel se nikalna chahiye:<br><br>` +
      `1. <strong>Ayodhya Ram Mandir:</strong><br>` +
      `   • <strong>Subah Slot:</strong> Hotel se subah <strong>6:00 AM se 6:30 AM</strong> tak nikal jayein, taaki 6:30 AM - 8:00 AM ke beech line mein lag sakein (~20-30 mins mein darshan).<br>` +
      `   • <strong>Afternoon Slot:</strong> Duphahar <strong>1:45 PM</strong> (12-2 PM Vishram break khulne ke turant baad bheed kam hoti hai).<br><br>` +
      `2. <strong>Hanuman Garhi:</strong> Subah <strong>5:30 AM se 6:30 AM</strong> tak pahunchein.<br><br>` +
      `3. <strong>Best Days:</strong> Wednesday, Thursday aur Friday ko sabse kam bheed hoti hai.<br><br>` +
      `📞 Assistance ke liye call karein: <strong>+91 92352 22399</strong>.`;
    }

    // 6. GENERAL KASHI / VARANASI GUIDE
    if (isKashi) {
      return `<strong>🛕 Kashi Vishwanath & Varanasi Yatra Guide:</strong><br><br>` +
      `• <strong>Sugam Darshan:</strong> Gate No. 4 (Chhatta Dwar) se direct entry milti hai (Official Trust ticket ₹300 per person shrikashivishwanath.org par).<br>` +
      `• <strong>Ganga Aarti:</strong> Dashashwamedh Ghat shaam 6:30 PM (Boat se sabse sundar view). Assi Ghat Subah-e-Banaras 5:00 AM.<br>` +
      `• <strong>Kaal Bhairav:</strong> Kashi ke Kotwal Kaal Bhairav darshan zaroori hota hai.<br>` +
      `• <strong>Sarnath:</strong> Varanasi se 10 km door Dhamek Stupa & Buddha complex.<br>` +
      `📞 Varanasi 1-Day & 2-Night packages ke liye: <strong>+91 92352 22399</strong>.`;
    }

    // 7. AYODHYA MANDIR GUIDE
    if (q.includes('ayodhya') || q.includes('ram mandir') || q.includes('ram janmabhoomi') || q.includes('hanuman garhi')) {
      return `<strong>🚩 Ayodhya Ram Mandir & Dham Yatra Guide:</strong><br><br>` +
      `• <strong>Ram Mandir:</strong> Subah 6:00 AM se Raat 10:00 PM (12 PM - 2 PM Vishram break).<br>` +
      `• <strong>Aarti Timings:</strong> Mangala Aarti (4:30 AM), Shringar Aarti (6:30 AM), Sandhya Aarti (7:30 PM).<br>` +
      `• <strong>Hanuman Garhi:</strong> Subah 5:00 AM se Raat 10:00 PM.<br>` +
      `• <strong>Sarayu Aarti:</strong> Shaam 6:30 PM (Ram Ki Paidi).<br>` +
      `📞 Ayodhya packages ke liye call/WhatsApp: <strong>+91 92352 22399</strong>.`;
    }

    // 8. PRAYAGRAJ
    if (q.includes('prayagraj') || q.includes('sangam') || q.includes('triveni') || q.includes('allahabad')) {
      return `<strong>🌊 Prayagraj Triveni Sangam Guide:</strong><br><br>` +
      `• <strong>Sangam Snan:</strong> Private boat se Ganga, Yamuna & Saraswati milan sthal par 1.5 ghante ka snan tour.<br>` +
      `• <strong>Darshan Sthal:</strong> Reclining Bade Hanuman Ji, Akshayavat & Patalpuri Mandir (Fort ID check), Alopi Devi.<br>` +
      `• <strong>Ayodhya to Prayagraj:</strong> 165 km (~3.5 hrs drive).`;
    }

    // 9. MATHURA & VRINDAVAN
    if (q.includes('mathura') || q.includes('vrindavan') || q.includes('bihari') || q.includes('prem mandir') || q.includes('nidhivan')) {
      return `<strong>🛺 Mathura & Vrindavan Braj Yatra Guide:</strong><br><br>` +
      `• <strong>Shri Krishna Janmabhoomi:</strong> Subah 5 AM - 12 PM & 4 PM - 9.30 PM.<br>` +
      `• <strong>Banke Bihari (Vrindavan):</strong> Subah 7:45 AM - 12 PM & Shaam 5:30 PM - 9:30 PM.<br>` +
      `• <strong>Prem Mandir:</strong> Shaam 6:30 PM grand marble illumination & musical fountain.<br>` +
      `• <strong>Nidhivan:</strong> Shaam 5 PM ke baad entry closed (Raas Leela mystery).`;
    }

    // 10. CHITRAKOOT
    if (q.includes('chitrakoot') || q.includes('kamadgiri') || q.includes('godavari')) {
      return `<strong>🏹 Chitrakoot Dham Yatra Guide:</strong><br><br>` +
      `• <strong>Ramghat Aarti:</strong> Har shaam 6:30 PM Mandakini river bank.<br>` +
      `• <strong>Kamadgiri Parikrama:</strong> 5 km paved path (E-rickshaw/Doli available).<br>` +
      `• <strong>Gupt Godavari:</strong> Natural stream caves tour.<br>` +
      `• <strong>Hanuman Dhara:</strong> Hilltop shrine (360 steps ya Ropeway).`;
    }

    // 11. NAIMISHARANYA
    if (q.includes('naimisharanya') || q.includes('neemsar') || q.includes('chakra tirth')) {
      return `<strong>📜 Naimisharanya (Neemsar) Guide:</strong><br><br>` +
      `• 88,000 Rishiyon ki tapobhoomi jahan Ved Vyas ji ne 18 Puranon ki rachna ki.<br>` +
      `• <strong>Pramukh Sthal:</strong> Circular Chakra Tirth snan, Maa Lalita Devi Shaktipeeth, Vyas Gaddi, Dadhichi Kund.<br>` +
      `• <strong>Distance:</strong> Lucknow se 90 km (~2.5 hrs drive).`;
    }

    // 12. VINDHYACHAL
    if (q.includes('vindhyachal') || q.includes('vindhyavasini')) {
      return `<strong>🔱 Vindhyachal Dham Guide:</strong><br><br>` +
      `• <strong>Maa Vindhyavasini Shaktipeeth:</strong> VIP Darshan & Pucca Ghat Ganga Snan.<br>` +
      `• <strong>Trikon Parikrama:</strong> Maa Vindhyavasini -> Kali Khoh -> Ashtabhuja Devi (Ropeway available).<br>` +
      `• <strong>Distance:</strong> Varanasi se 65 km (~1.5 hrs drive).`;
    }

    // 13. GAYA
    if (q.includes('gaya') || q.includes('bodhgaya') || q.includes('vishnupad')) {
      return `<strong>🪔 Gaya Pitru Pind Daan Guide:</strong><br><br>` +
      `• <strong>Vishnupad Mandir:</strong> Bhagwan Vishnu ke 40cm charan chinha par pinda daan.<br>` +
      `• <strong>Bodhgaya:</strong> Mahabodhi Temple & 80ft Great Buddha statue.<br>` +
      `• <strong>Distance:</strong> Varanasi se 250 km (NH 19).`;
    }

    // GREETINGS
    if (q.includes('hi') || q.includes('hello') || q.includes('pranam') || q.includes('ram ram') || q.includes('jai shree ram') || q.includes('namaste')) {
      return `<strong>॥ जय श्री राम ॥ 🙏</strong><br><br>` +
      `Pranam ji! Main Pt. Ram Shastri hu, Ayodhya Dharshan ka AI Yatra Assistant. Aapko UP ke 8 major teerth sthalon (Ayodhya, Kashi, Prayagraj, Mathura, Vrindavan, Chitrakoot, Naimisharanya, Vindhyachal, Gaya) mein se kisi bhi jagah ke darshan, cab, hotel ya pricing ki jaankari chahiye, poochhein!`;
    }

    // Conversational Generative Natural Response
    return `<strong>🚩 Pt. Ram Shastri (AI Agent):</strong><br><br>` +
    `Ji pranam! Aapne pucha: <em>"${query}"</em>.<br><br>` +
    `Ayodhya Dharshan Seva Desk aapko UP ke sabhi 8 major teerth nagaron (Ayodhya, Varanasi, Prayagraj, Mathura, Vrindavan, Chitrakoot, Naimisharanya, Vindhyachal, Gaya) mein private AC cabs, hotels aur priority mandir darshan assistance provide karti hai.<br><br>` +
    `Aap Kashi Vishwanath darshan time, Sugam Darshan passes, minimum rush hours, cabs ya hotels ke baare mein poochh sakte hain, ya humare Yatra Desk se direct sampark karein:<br>` +
    `📞 <strong>Call:</strong> <a href="tel:+919235222399">+91 92352 22399</a><br>` +
    `💬 <strong>WhatsApp:</strong> <a href="https://wa.me/919235222399?text=Jai%20Shree%20Ram!%20I%20have%20a%20query." target="_blank">Direct WhatsApp Chat</a>`;
  }
})();
