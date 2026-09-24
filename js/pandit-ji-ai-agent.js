/**
 * AYODHYA DHARSHAN - SMART AI YATRA AGENT (Pt. Ram Shastri)
 * Bulletproof Multi-Lingual Reasoning Engine
 * Explicit Handlers for Transport, Routes, Timings, VIP Passes, Prices & Guides
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
      width: 420px;
      max-width: calc(100vw - 30px);
      height: 630px;
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
          <strong>॥ जय श्री राम ॥ 🙏</strong><br>
          Pranam! Main Pt. Ram Shastri hu, Ayodhya Dharshan ka <strong>AI Yatra Assistant</strong>. Ask me anything in English, Hindi, or Hinglish — <em>How to reach Ayodhya, 3-Day Tour Prices, Kashi Darshan Time, Ram Mandir VIP Pass, Mathura Plan!</em>
        </div>

        <div class="pj-quick-prompts">
          <div class="pj-chip" onclick="pjAskPrompt('How to reach Ayodhya?')">✈️ How to reach Ayodhya</div>
          <div class="pj-chip" onclick="pjAskPrompt('Ayodhya Varanasi Prayagraj 3 day tour price?')">🚗 3-City Tour Price</div>
          <div class="pj-chip" onclick="pjAskPrompt('Kashi Vishwanath darshan me kitna time lagta hai?')">🛕 Kashi Darshan Duration</div>
          <div class="pj-chip" onclick="pjAskPrompt('Subah kitne baje nikalna chahiye jisse rush kam mile?')">🕐 Minimum Rush Timings</div>
          <div class="pj-chip" onclick="pjAskPrompt('Ram Mandir VIP Pass kaise milta hai?')">🚩 Ram Mandir Pass (Free)</div>
        </div>
      </div>

      <div class="pj-action-bar">
        <a href="tel:+919235222399">📞 Call +91 92352 22399</a>
        <a href="https://wa.me/919235222399?text=Jai%20Shree%20Ram!%20I%20have%20a%20query%20regarding%20yatra%20package." target="_blank">💬 WhatsApp Desk</a>
      </div>

      <div class="pj-chat-footer">
        <input type="text" class="pj-input" id="pjInput" placeholder="Ask anything in English / Hindi / Hinglish...">
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
    }, 200);
  }

  function appendMessage(text, sender) {
    const msg = document.createElement('div');
    msg.className = `pj-msg pj-msg-${sender}`;
    msg.innerHTML = text;
    chatBody.appendChild(msg);
    chatBody.scrollTop = chatBody.scrollHeight;
  }

  // Pure Multi-Lingual Reasoning Engine
  function generateSmartAIResponse(query) {
    const q = query.toLowerCase().trim();

    // -------------------------------------------------------------
    // LANGUAGE DETECTION LOGIC
    // -------------------------------------------------------------
    const hindiWords = [
      'kaise', 'kaisa', 'kisi', 'pahunche', 'pahunch', 'pahaunche', 'nikale', 'nikal', 'nikake', 'nikle',
      'subah', 'subha', 'subh', 'kitna', 'kitne', 'kitani', 'lagta', 'lag', 'chahiye', 'hai', 'hain', 'mein',
      'me', 'batao', 'pucha', 'puch', 'mujhe', 'muja', 'bheed', 'bataiyye', 'kya', 'bato', 'ya', 'mena',
      'tumna', 'bhai', 'ji', 'karo', 'pranam', 'namaste', 'bata', 'gaya', 'par', 'se', 'seve', 'dharshan'
    ];
    
    const containsHindiWord = hindiWords.some(w => new RegExp('\\b' + w + '\\b', 'i').test(q));

    const englishWords = [
      'how', 'where', 'when', 'what', 'which', 'can', 'is', 'are', 'tell', 'price', 'reach',
      'timing', 'timings', 'time', 'distance', 'flight', 'train', 'bus', 'hotel', 'cab', 'tour',
      'cost', 'dress', 'code', 'rules', 'booking', 'guide', 'pass', 'free', 'long', 'duration'
    ];
    const containsEnglishWord = englishWords.some(w => new RegExp('\\b' + w + '\\b', 'i').test(q));

    // If query has English markers and no Hindi markers, respond in English
    const isEnglish = containsEnglishWord && !containsHindiWord;

    // -------------------------------------------------------------
    // KEY ENTITY & INTENT FLAGS
    // -------------------------------------------------------------
    const isReach = q.includes('reach') || q.includes('kaise') || q.includes('pahunche') || q.includes('pahunch') || q.includes('get to') || q.includes('way to') || q.includes('how to go') || q.includes('route');
    
    const isKashi = q.includes('kashi') || q.includes('varanasi') || q.includes('banaras') || q.includes('vishwanath') || q.includes('visvanath') || q.includes('biswanath');
    const isAyodhya = q.includes('ayodhya') || q.includes('ram mandir') || q.includes('ram janmabhoomi') || q.includes('hanuman garhi');
    const isPrayagraj = q.includes('prayagraj') || q.includes('sangam') || q.includes('triveni') || q.includes('allahabad');
    const isMathura = q.includes('mathura') || q.includes('vrindavan') || q.includes('bihari') || q.includes('prem mandir') || q.includes('nidhivan');

    const isPrice = q.includes('price') || q.includes('cost') || q.includes('rate') || q.includes('package') || q.includes('kiraya') || q.includes('charge') || q.includes('paisa') || q.includes('paise') || q.includes('budget') || q.includes('3 day') || q.includes('3-day') || q.includes('2 day');
    
    const isDuration = q.includes('kitna time') || q.includes('kitne ghante') || q.includes('time lag') || q.includes('samay') || q.includes('duration') || q.includes('waiting') || q.includes('how long') || q.includes('how many hours');

    const isPass = q.includes('pass') || q.includes('sugam') || q.includes('vip') || q.includes('ticket') || q.includes('token') || q.includes('booking') || q.includes('rule') || q.includes('entry');

    const isTiming = q.includes('timing') || q.includes('timings') || q.includes('subah') || q.includes('subha') || q.includes('baje') || q.includes('nikal') || q.includes('nikle') || q.includes('rush') || q.includes('bheed') || q.includes('crowd');

    // -------------------------------------------------------------
    // ROUTING RANK 1: MULTI-CITY / PACKAGE / PRICE QUERIES
    // -------------------------------------------------------------
    if (isPrice || (isAyodhya && isKashi) || (isKashi && isPrayagraj) || q.includes('package') || q.includes('tour')) {
      if (isEnglish) {
        return `<strong>🚗 Ayodhya - Varanasi - Prayagraj Tour Package & Pricing:</strong><br><br>` +
        `• <strong>3-Day / 2-Night Complete Circuit:</strong><br>` +
        `  - <em>Express Cab Only Tour:</em> Starts at <strong>₹1,499 - ₹2,499 per person</strong> (Private AC Sedan/SUV + Toll + Sangam Boat + All Transfers).<br>` +
        `  - <em>Deluxe Tour (2 Nights Hotel + AC Cab + VIP Assistance):</em> Starts at <strong>₹3,499 - ₹4,999 per person</strong> (3-Star AC Hotel with Breakfast + Private Cab + Priority Darshan Assistance).<br>` +
        `  - <em>VIP Executive Package:</em> Starts at <strong>₹5,999 - ₹7,999 per person</strong> (5-Star/Luxury Hotel + Innova Crysta/Urbania + Personal Guide + VIP Passes).<br><br>` +
        `• <strong>Vehicle Options:</strong><br>` +
        `  - 1-3 Pax: AC Sedan (Dzire / Etios)<br>` +
        `  - 4-6 Pax: AC SUV (Ertiga / Innova Crysta)<br>` +
        `  - 7-18 Pax: Luxury Force Urbania / Tempo Traveller<br><br>` +
        `📞 Call/WhatsApp our Yatra Desk for instant custom quotes: <a href="tel:+919235222399"><strong>+91 92352 22399</strong></a>.`;
      }
      return `<strong>🚗 Ayodhya - Varanasi - Prayagraj Yatra Package & Pricing:</strong><br><br>` +
      `1. <strong>Same Day / Cab Only Tour:</strong> <strong>₹1,499 - ₹2,499 per person</strong> (Private AC Cab + Toll + Sangam Boat + Station/Airport Pickup-Drop).<br>` +
      `2. <strong>Deluxe Package (2 Nights Hotel + Cab + Darshan):</strong> <strong>₹3,499 - ₹4,999 per person</strong> (3-Star AC Hotel Stay + Breakfast + Private AC Sedan/SUV + VIP Assistance).<br>` +
      `3. <strong>VIP Executive Package:</strong> <strong>₹5,999 - ₹7,999 per person</strong> (Luxury Hotel + Innova Crysta/Urbania + Dedicated Guide + VIP Entry Passes).<br><br>` +
      `• <strong>Gaadi Selection:</strong><br>` +
      `  - 1-3 Log: AC Sedan (Dzire/Etios)<br>` +
      `  - 4-6 Log: AC SUV (Ertiga/Innova Crysta)<br>` +
      `  - 7-18 Log: AC Tempo Traveller / Luxury Force Urbania<br><br>` +
      `📞 Instant Booking ya discount ke liye call/WhatsApp karein: <a href="tel:+919235222399"><strong>+91 92352 22399</strong></a>.`;
    }

    // -------------------------------------------------------------
    // ROUTING RANK 2: HOW TO REACH / TRANSIT ROUTE QUERIES
    // -------------------------------------------------------------
    if (isReach) {
      if (isKashi) {
        if (isEnglish) {
          return `<strong>🛕 How to Reach Varanasi (Kashi):</strong><br><br>` +
          `• <strong>By Air (Flight):</strong> Lal Bahadur Shastri International Airport (VNS) at Babatpur, located 25 km from Varanasi main city.<br>` +
          `• <strong>By Train (Railway):</strong> Varanasi Junction (BSB), Banaras Station (BSBS), or Pt. Deen Dayal Upadhyaya Junction (DDU - 18 km).<br>` +
          `• <strong>By Road (Cab / Bus):</strong> 200 km from Ayodhya (~4 hours via NH 28 highway). Direct AC cabs available.<br><br>` +
          `📞 Need private AC cab pickup? Call: <a href="tel:+919235222399"><strong>+91 92352 22399</strong></a>.`;
        }
        return `<strong>🛕 Kashi (Varanasi) Kaise Pahuntchein:</strong><br><br>` +
        `• <strong>Hawai Jahaz (Flight):</strong> Lal Bahadur Shastri Airport (VNS) - city se 25 km door.<br>` +
        `• <strong>Train:</strong> Varanasi Junction (BSB) / Banaras (BSBS).<br>` +
        `• <strong>Sadak (Cab):</strong> Ayodhya se 200 km (~4 ghante drive).<br><br>` +
        `📞 Cab booking ke liye call karein: <a href="tel:+919235222399"><strong>+91 92352 22399</strong></a>.`;
      }

      if (isPrayagraj) {
        if (isEnglish) {
          return `<strong>🌊 How to Reach Prayagraj (Sangam):</strong><br><br>` +
          `• <strong>By Air (Flight):</strong> Prayagraj Airport, Bamrauli (IXD), 15 km from Triveni Sangam.<br>` +
          `• <strong>By Train (Railway):</strong> Prayagraj Junction (PRYJ), 6 km from Triveni Sangam Ghat.<br>` +
          `• <strong>By Road (Cab / Bus):</strong> 165 km from Ayodhya via NH 330 (~3.5 hours drive).<br><br>` +
          `📞 Private AC cab booking: <a href="tel:+919235222399"><strong>+91 92352 22399</strong></a>.`;
        }
        return `<strong>🌊 Prayagraj Kaise Pahuntchein:</strong><br><br>` +
        `• <strong>Flight:</strong> Prayagraj Airport Bamrauli (IXD) - 15 km.<br>` +
        `• <strong>Train:</strong> Prayagraj Junction (PRYJ) - 6 km.<br>` +
        `• <strong>Sadak / Cab:</strong> Ayodhya se 165 km (~3.5 ghante).<br><br>` +
        `📞 Cab booking ke liye call karein: <a href="tel:+919235222399"><strong>+91 92352 22399</strong></a>.`;
      }

      if (isMathura) {
        if (isEnglish) {
          return `<strong>🛺 How to Reach Mathura & Vrindavan:</strong><br><br>` +
          `• <strong>By Air (Flight):</strong> Delhi IGI Airport (150 km) or Agra Airport (60 km).<br>` +
          `• <strong>By Train (Railway):</strong> Mathura Junction (MTJ), 12 km from Vrindavan Banke Bihari Temple.<br>` +
          `• <strong>By Road (Cab):</strong> 2.5 hours drive from Delhi/NCR via Yamuna Expressway.<br><br>` +
          `📞 Cab booking: <a href="tel:+919235222399"><strong>+91 92352 22399</strong></a>.`;
        }
        return `<strong>🛺 Mathura & Vrindavan Kaise Pahuntchein:</strong><br><br>` +
        `• <strong>Flight:</strong> Delhi IGI Airport (150 km via Yamuna Expressway).<br>` +
        `• <strong>Train:</strong> Mathura Junction (MTJ) - Vrindavan se 12 km.<br>` +
        `• <strong>Sadak / Cab:</strong> Delhi/NCR se 2.5 ghante.<br><br>` +
        `📞 Cab booking: <a href="tel:+919235222399"><strong>+91 92352 22399</strong></a>.`;
      }

      // Default Reach -> Ayodhya
      if (isEnglish) {
        return `<strong>✈️ How to Reach Ayodhya — Complete Travel Guide:</strong><br><br>` +
        `<strong>1. By Air (Flight):</strong><br>` +
        `• <strong>Maharishi Valmiki International Airport (AYJ):</strong> Direct flights from Delhi, Mumbai, Ahmedabad, Bengaluru, Hyderabad & Kolkata. Located just 10 km (~20 mins drive) from Ram Mandir.<br>` +
        `• <strong>Lucknow Airport (LKO):</strong> 135 km from Ayodhya (approx. 2.5 hours drive via NH 27 highway).<br><br>` +
        `<strong>2. By Train (Railway):</strong><br>` +
        `• <strong>Ayodhya Dham Junction (AY):</strong> Located only 1.5 km from Ram Janmabhoomi Temple.<br>` +
        `• <strong>Ayodhya Cantt (AYC):</strong> Located 8 km from the main temple area.<br>` +
        `• Direct Vande Bharat & Amrit Bharat express trains connect Delhi, Lucknow, Anand Vihar & Varanasi.<br><br>` +
        `<strong>3. By Road (Cab / Bus):</strong><br>` +
        `• 4-Lane Highways (NH 27 & NH 330) connect Ayodhya to Lucknow (135 km), Gorakhpur (135 km), Varanasi (200 km) & Prayagraj (165 km).<br><br>` +
        `📞 Need private AC cab pickup from Airport or Station? Call: <a href="tel:+919235222399"><strong>+91 92352 22399</strong></a>.`;
      }

      return `<strong>✈️ Ayodhya Kaise Pahuntchein (Complete Route Guide):</strong><br><br>` +
      `<strong>1. Hawai Jahaz (Flight) Se:</strong><br>` +
      `• <strong>Maharishi Valmiki Airport Ayodhya (AYJ):</strong> Ram Mandir se sirf 10 km door hai. Delhi, Mumbai, Ahmedabad, Bengaluru se direct flights hain.<br>` +
      `• <strong>Lucknow Airport (LKO):</strong> Ayodhya se 135 km door hai (~2.5 ghante drive).<br><br>` +
      `<strong>2. Train (Railway) Se:</strong><br>` +
      `• <strong>Ayodhya Dham Junction (AY):</strong> Ram Mandir se sirf 1.5 km door.<br>` +
      `• <strong>Ayodhya Cantt (AYC):</strong> Main city se 8 km door.<br><br>` +
      `<strong>3. Sadak (Road / Cab) Se:</strong><br>` +
      `• Lucknow se 135 km, Gorakhpur se 135 km, Varanasi se 200 km, aur Prayagraj se 165 km door hai.<br><br>` +
      `📞 Private AC Cab pickup book karne ke liye call karein: <a href="tel:+919235222399"><strong>+91 92352 22399</strong></a>.`;
    }

    // -------------------------------------------------------------
    // ROUTING RANK 3: KASHI VISHWANATH DARSHAN DURATION
    // -------------------------------------------------------------
    if (isKashi && (isDuration || q.includes('darshan'))) {
      if (isDuration || q.includes('time') || q.includes('samay') || q.includes('ghante') || q.includes('long')) {
        if (isEnglish) {
          return `<strong>🛕 Kashi Vishwanath Temple Darshan Duration (Varanasi):</strong><br><br>` +
          `1. <strong>Sugam Darshan (VIP Pass - Gate 4):</strong> Takes approx. <strong>15 to 30 minutes</strong> for complete darshan.<br>` +
          `2. <strong>General Queue (Regular Entry):</strong><br>` +
          `   • <em>Normal Days (Wed/Thu/Fri):</em> Takes around <strong>1 to 2 hours</strong>.<br>` +
          `   • <em>Peak Days (Mondays/Sawan/Festivals):</em> Can take <strong>3 to 5 hours</strong>.<br>` +
          `3. <strong>Best Time for Fast Darshan:</strong> Early morning <strong>5:00 AM to 7:00 AM</strong> or late night <strong>8:30 PM to 9:30 PM</strong>.<br><br>` +
          `📞 For Sugam Darshan assistance & Cab booking, call: <a href="tel:+919235222399"><strong>+91 92352 22399</strong></a>.`;
        }
        return `<strong>🛕 Kashi Vishwanath Darshan Duration & Waiting Time (Varanasi):</strong><br><br>` +
        `1. <strong>Sugam Darshan (VIP Entry - Gate 4):</strong> Ticket (₹300) ke sath aaram se <strong>15 se 30 minutes</strong> mein darshan ho jate hain.<br>` +
        `2. <strong>Regular Line (General Entry):</strong><br>` +
        `   • <em>Normal Days (Wed/Thu/Fri):</em> Regular queue mein <strong>1 se 2 ghante</strong> lagte hain.<br>` +
        `   • <em>Peak Days (Monday/Sawan/Festivals):</em> <strong>3 se 5 ghante</strong> tak ka waiting time ho sakta hai.<br>` +
        `3. <strong>Best Time for Fast Darshan:</strong> Subah <strong>5:00 AM se 7:00 AM</strong> ya raat ko <strong>8:30 PM se 9:30 PM</strong>.<br><br>` +
        `📞 Assistance ke liye call karein: <a href="tel:+919235222399"><strong>+91 92352 22399</strong></a>.`;
      }
    }

    // -------------------------------------------------------------
    // ROUTING RANK 4: PASS / SUGAM / VIP RULES
    // -------------------------------------------------------------
    if (isKashi && isPass) {
      if (isEnglish) {
        return `<strong>🛕 Kashi Vishwanath Sugam Darshan Rules & VIP Pass (Varanasi):</strong><br><br>` +
        `1. <strong>Direct Entry Gate:</strong> Sugam Darshan pass holders enter via <strong>Gate No. 4 (Chhatta Dwar)</strong> for priority entry (darshan takes ~15-20 mins).<br>` +
        `2. <strong>Official Ticket Fee:</strong> Official Trust ticket fee is <strong>₹300 per person</strong> via <em>shrikashivishwanath.org</em>.<br>` +
        `3. <strong>Dress Code:</strong> Dhoti-Kurta for Men and Saree/Salwar Suit for Women.<br><br>` +
        `📞 For Varanasi Sugam ticket guidance & Cabs, call: <a href="tel:+919235222399"><strong>+91 92352 22399</strong></a>.`;
      }
      return `<strong>🛕 Kashi Vishwanath Sugam Darshan Rules & Pass (Varanasi):</strong><br><br>` +
      `1. <strong>Direct Entry Gate:</strong> Sugam Darshan pass dharakon ko <strong>Gate No. 4 (Chhatta Dwar)</strong> se direct priority entry milti hai (Darshan time ~15-20 mins).<br>` +
      `2. <strong>Official Ticket Fee:</strong> Shri Kashi Vishwanath Temple Trust ka official ticket fee <strong>₹300 per person</strong> hai.<br>` +
      `3. <strong>Online Slot:</strong> Trust ki official website <em>shrikashivishwanath.org</em> par Aadhar Card details se booking hoti hai.<br>` +
      `4. <strong>Dress Code & Rules:</strong> Dhoti-Kurta (Men) aur Saree/Salwar Suit (Women). Sparsh Darshan ke liye Dhoti/Saree mandatory hai.<br><br>` +
      `📞 Varanasi Tour & Sugam Ticket assistance ke liye call karein: <a href="tel:+919235222399"><strong>+91 92352 22399</strong></a>.`;
    }

    if (isAyodhya && isPass) {
      if (isEnglish) {
        return `<strong>🚩 Ayodhya Ram Mandir Pass Details (100% Free):</strong><br><br>` +
        `1. <strong>Official Fee ₹0 (Free):</strong> Shri Ram Janmabhoomi Teerth Kshetra Trust provides Sugam Darshan, Aarti, and Wheelchair passes completely <strong>FREE OF COST (₹0)</strong>.<br>` +
        `2. <strong>Online Booking:</strong> Book free passes 15-30 days in advance on official portal <em>srjbtkshetra.org</em>.<br>` +
        `3. <strong>Offline Desk:</strong> Limited free offline tokens issued at 6:00 AM at Mandir entrance desk (Aadhar Card mandatory).<br>` +
        `4. <strong>Our Service:</strong> Deluxe/VIP tour packages include Sugam Darshan guidance and door-step AC cab pickup! Call: <a href="tel:+919235222399"><strong>+91 92352 22399</strong></a>.`;
      }
      return `<strong>🚩 Ayodhya Ram Mandir Pass Details (100% Free):</strong><br><br>` +
      `1. <strong>Official Fee ₹0 (Free):</strong> Shri Ram Janmabhoomi Teerth Kshetra Trust dwara Sugam Darshan, Aarti aur Wheelchair passes bilkul <strong>FREE (₹0)</strong> hote hain.<br>` +
      `2. <strong>Online Booking:</strong> Official site <em>srjbtkshetra.org</em> par free Aarti/Sugam pass 15-30 din pehle book hota hai.<br>` +
      `3. <strong>Offline Token:</strong> Subah 6 AM par Mandir entry token desk par limited free slots milte hain (Aadhar Card mandatory).<br>` +
      `4. <strong>Humari Seva:</strong> Humare Deluxe/VIP yatra packages mein Sugam Darshan guidance aur door-step cab pickup free shamil hai! 📞 <a href="tel:+919235222399"><strong>+91 92352 22399</strong></a>.`;
    }

    // -------------------------------------------------------------
    // ROUTING RANK 5: MORNING DEPARTURE & MINIMUM RUSH TIMINGS
    // -------------------------------------------------------------
    if (isTiming) {
      if (isEnglish) {
        return `<strong>🌅 Minimum Rush & Best Departure Timing Guide:</strong><br><br>` +
        `To experience <strong>minimum crowd & fastest darshan</strong>, start from your hotel at these exact times:<br><br>` +
        `1. <strong>Ayodhya Ram Mandir:</strong><br>` +
        `   • <strong>Morning Slot:</strong> Leave hotel between <strong>6:00 AM – 6:30 AM</strong> to join queue before 7:00 AM (~20-30 mins darshan).<br>` +
        `   • <strong>Afternoon Slot:</strong> <strong>1:45 PM</strong> (Right after afternoon vishram break ends).<br><br>` +
        `2. <strong>Hanuman Garhi (Ayodhya):</strong> Reach between <strong>5:30 AM – 6:30 AM</strong>.<br>` +
        `3. <strong>Best Days:</strong> Wednesday, Thursday, and Friday see lowest crowd density.<br><br>` +
        `📞 For cab assistance, call: <a href="tel:+919235222399"><strong>+91 92352 22399</strong></a>.`;
      }
      return `<strong>🌅 Minimum Rush & Best Departure Timing Guide:</strong><br><br>` +
      `Subah sabse <strong>kam rush (minimum crowd)</strong> paane ke liye in nirdharit timings par hotel se nikalna chahiye:<br><br>` +
      `1. <strong>Ayodhya Ram Mandir:</strong><br>` +
      `   • <strong>Subah Slot:</strong> Hotel se subah <strong>6:00 AM se 6:30 AM</strong> tak nikal jayein, taaki 6:30 AM - 8:00 AM ke beech line mein lag sakein (~20-30 mins mein darshan).<br>` +
      `   • <strong>Afternoon Slot:</strong> Duphahar <strong>1:45 PM</strong> (12-2 PM Vishram break khulne ke turant baad bheed kam hoti hai).<br><br>` +
      `2. <strong>Hanuman Garhi:</strong> Subah <strong>5:30 AM se 6:30 AM</strong> tak pahunchein.<br><br>` +
      `3. <strong>Best Days:</strong> Wednesday, Thursday aur Friday ko sabse kam bheed hoti hai.<br><br>` +
      `📞 Assistance ke liye call karein: <a href="tel:+919235222399"><strong>+91 92352 22399</strong></a>.`;
    }

    // -------------------------------------------------------------
    // ROUTING RANK 6: SINGLE CITY GUIDES
    // -------------------------------------------------------------
    if (isKashi) {
      if (isEnglish) {
        return `<strong>🛕 Kashi Vishwanath & Varanasi Yatra Guide:</strong><br><br>` +
        `• <strong>Sugam Darshan:</strong> Priority entry from Gate No. 4 (Official Trust ticket ₹300 per person on <em>shrikashivishwanath.org</em>).<br>` +
        `• <strong>Ganga Aarti:</strong> Dashashwamedh Ghat at 6:30 PM evening (best viewed from private boat). Assi Ghat Subah-e-Banaras at 5:00 AM.<br>` +
        `• <strong>Kaal Bhairav:</strong> Essential darshan of Kaal Bhairav (Kotwal of Kashi).<br>` +
        `• <strong>Sarnath:</strong> Dhamek Stupa & Buddhist complex 10 km from Varanasi.<br>` +
        `📞 Call for 1-Day & 2-Night Varanasi packages: <a href="tel:+919235222399"><strong>+91 92352 22399</strong></a>.`;
      }
      return `<strong>🛕 Kashi Vishwanath & Varanasi Yatra Guide:</strong><br><br>` +
      `• <strong>Sugam Darshan:</strong> Gate No. 4 (Chhatta Dwar) se direct entry milti hai (Official Trust ticket ₹300 per person shrikashivishwanath.org par).<br>` +
      `• <strong>Ganga Aarti:</strong> Dashashwamedh Ghat shaam 6:30 PM (Boat se sabse sundar view). Assi Ghat Subah-e-Banaras 5:00 AM.<br>` +
      `• <strong>Kaal Bhairav:</strong> Kashi ke Kotwal Kaal Bhairav darshan zaroori hota hai.<br>` +
      `• <strong>Sarnath:</strong> Varanasi se 10 km door Dhamek Stupa & Buddha complex.<br>` +
      `📞 Varanasi 1-Day & 2-Night packages ke liye: <a href="tel:+919235222399"><strong>+91 92352 22399</strong></a>.`;
    }

    if (isAyodhya) {
      if (isEnglish) {
        return `<strong>🚩 Ayodhya Ram Mandir & Dham Yatra Guide:</strong><br><br>` +
        `• <strong>Ram Mandir:</strong> 6:00 AM to 10:00 PM (12:00 PM – 2:00 PM afternoon break).<br>` +
        `• <strong>Aarti Timings:</strong> Mangala (4:30 AM), Shringar (6:30 AM), Sandhya (7:30 PM).<br>` +
        `• <strong>Hanuman Garhi:</strong> 5:00 AM to 10:00 PM.<br>` +
        `• <strong>Sarayu Aarti:</strong> 6:30 PM at Ram Ki Paidi.<br>` +
        `📞 Call/WhatsApp for Ayodhya packages: <a href="tel:+919235222399"><strong>+91 92352 22399</strong></a>.`;
      }
      return `<strong>🚩 Ayodhya Ram Mandir & Dham Yatra Guide:</strong><br><br>` +
      `• <strong>Ram Mandir:</strong> Subah 6:00 AM se Raat 10:00 PM (12 PM - 2 PM Vishram break).<br>` +
      `• <strong>Aarti Timings:</strong> Mangala Aarti (4:30 AM), Shringar Aarti (6:30 AM), Sandhya Aarti (7:30 PM).<br>` +
      `• <strong>Hanuman Garhi:</strong> Subah 5:00 AM se Raat 10:00 PM.<br>` +
      `• <strong>Sarayu Aarti:</strong> Shaam 6:30 PM (Ram Ki Paidi).<br>` +
      `📞 Ayodhya packages ke liye call/WhatsApp: <a href="tel:+919235222399"><strong>+91 92352 22399</strong></a>.`;
    }

    if (isPrayagraj) {
      if (isEnglish) {
        return `<strong>🌊 Prayagraj Triveni Sangam Guide:</strong><br><br>` +
        `• <strong>Sangam Snan:</strong> 1.5-hour private boat tour to Ganga, Yamuna & Saraswati holy confluence.<br>` +
        `• <strong>Key Temples:</strong> Reclining Bade Hanuman Ji, Akshayavat & Patalpuri Fort Temple, Alopi Devi.<br>` +
        `• <strong>Ayodhya to Prayagraj:</strong> 165 km (~3.5 hrs drive).<br>` +
        `📞 Call for Prayagraj packages: <a href="tel:+919235222399"><strong>+91 92352 22399</strong></a>.`;
      }
      return `<strong>🌊 Prayagraj Triveni Sangam Guide:</strong><br><br>` +
      `• <strong>Sangam Snan:</strong> Private boat se Ganga, Yamuna & Saraswati milan sthal par 1.5 ghante ka snan tour.<br>` +
      `• <strong>Darshan Sthal:</strong> Reclining Bade Hanuman Ji, Akshayavat & Patalpuri Mandir (Fort ID check), Alopi Devi.<br>` +
      `• <strong>Ayodhya to Prayagraj:</strong> 165 km (~3.5 hrs drive).<br>` +
      `📞 Call for Prayagraj packages: <a href="tel:+919235222399"><strong>+91 92352 22399</strong></a>.`;
    }

    if (isMathura) {
      if (isEnglish) {
        return `<strong>🛺 Mathura & Vrindavan Braj Yatra Guide:</strong><br><br>` +
        `• <strong>Shri Krishna Janmabhoomi:</strong> 5:00 AM – 12:00 PM & 4:00 PM – 9:30 PM.<br>` +
        `• <strong>Banke Bihari (Vrindavan):</strong> 7:45 AM – 12:00 PM & 5:30 PM – 9:30 PM.<br>` +
        `• <strong>Prem Mandir:</strong> 6:30 PM grand marble illumination & musical fountain.<br>` +
        `• <strong>Nidhivan:</strong> Closed after 5:00 PM.<br>` +
        `📞 Call for Mathura/Vrindavan tour packages: <a href="tel:+919235222399"><strong>+91 92352 22399</strong></a>.`;
      }
      return `<strong>🛺 Mathura & Vrindavan Braj Yatra Guide:</strong><br><br>` +
      `• <strong>Shri Krishna Janmabhoomi:</strong> Subah 5 AM - 12 PM & 4 PM - 9.30 PM.<br>` +
      `• <strong>Banke Bihari (Vrindavan):</strong> Subah 7:45 AM - 12 PM & Shaam 5:30 PM - 9:30 PM.<br>` +
      `• <strong>Prem Mandir:</strong> Shaam 6:30 PM grand marble illumination & musical fountain.<br>` +
      `• <strong>Nidhivan:</strong> Shaam 5 PM ke baad entry closed (Raas Leela mystery).<br>` +
      `📞 Call for Mathura/Vrindavan tour packages: <a href="tel:+919235222399"><strong>+91 92352 22399</strong></a>.`;
    }

    // -------------------------------------------------------------
    // ROUTING RANK 7: GREETINGS & REASSURANCE
    // -------------------------------------------------------------
    if (q.includes('hi') || q.includes('hello') || q.includes('pranam') || q.includes('ram ram') || q.includes('jai shree ram') || q.includes('namaste')) {
      if (isEnglish) {
        return `<strong>🚩 Welcome! (Pt. Ram Shastri - AI Yatra Assistant):</strong><br><br>` +
        `Namaste! I am Pt. Ram Shastri, your dedicated AI Yatra Assistant at Ayodhya Dharshan.<br><br>` +
        `How can I assist you today? You can ask me about:<br>` +
        `• How to reach Ayodhya, Kashi, Prayagraj, Mathura<br>` +
        `• Ram Mandir Free Passes & Kashi Vishwanath ₹300 Sugam Passes<br>` +
        `• 3-Day Ayodhya-Varanasi-Prayagraj Tour Package & Cab Prices<br>` +
        `• Minimum rush timings & temple schedules<br><br>` +
        `📞 Or reach our 24x7 desk: <a href="tel:+919235222399"><strong>+91 92352 22399</strong></a>.`;
      }
      return `<strong>॥ जय श्री राम ॥ 🙏</strong><br><br>` +
      `Pranam ji! Main Pt. Ram Shastri hu, Ayodhya Dharshan ka AI Yatra Assistant. Aapko UP ke 8 major teerth sthalon (Ayodhya, Kashi, Prayagraj, Mathura, Vrindavan, Chitrakoot, Naimisharanya, Vindhyachal, Gaya) mein se kisi bhi jagah ke darshan, cab, hotel ya pricing ki jaankari chahiye, poochhein!`;
    }

    if (q.includes('sahi') || q.includes('bato') || q.includes('answer') || q.includes('jabab') || q.includes('jawab')) {
      return `<strong>🚩 Haan ji bilkul! Aap jo bhi poochhenge, uska 100% accurate aur direct jawab milega.</strong><br><br>` +
      `Aap kisi bhi teerth sthal (Ayodhya, Kashi, Prayagraj, Mathura, Vrindavan) ke baare mein poochhein:<br>` +
      `• Pahunchne ka rasta (Air, Train, Road)<br>` +
      `• Mandir darshan timings aur kam bheed (minimum rush) wala time<br>` +
      `• VIP / Sugam Darshan passes (Ayodhya Free Pass vs Kashi ₹300 Ticket)<br>` +
      `• Taxi, Private AC Cabs aur Hotels ke exact packages & rate<br><br>` +
      `📞 Direct help ke liye hamari desk: <a href="tel:+919235222399"><strong>+91 92352 22399</strong></a>.`;
    }

    // -------------------------------------------------------------
    // ROUTING RANK 8: SMART INTELLIGENT FALLBACK (DUAL-LANGUAGE)
    // -------------------------------------------------------------
    if (isEnglish) {
      return `<strong>🚩 Pt. Ram Shastri (AI Yatra Assistant):</strong><br><br>` +
      `Thank you for your question regarding <em>"${query}"</em>.<br><br>` +
      `I can provide exact details for your travel across Ayodhya, Varanasi (Kashi), Prayagraj, Mathura-Vrindavan, Chitrakoot, Naimisharanya, Vindhyachal & Gaya:<br>` +
      `• <strong>How to Reach:</strong> Flights to Ayodhya (AYJ) / Varanasi (VNS), direct trains & highway AC cabs.<br>` +
      `• <strong>VIP Passes:</strong> Ayodhya Ram Mandir (100% Free) & Kashi Vishwanath Sugam Pass (₹300).<br>` +
      `• <strong>Tour Packages:</strong> 3-Day Ayodhya-Varanasi-Prayagraj starting at ₹1,499 - ₹3,499 per person.<br><br>` +
      `📞 For immediate custom information, please call or WhatsApp our Yatra Desk:<br>` +
      `• <strong>Phone:</strong> <a href="tel:+919235222399">+91 92352 22399</a><br>` +
      `• <strong>WhatsApp:</strong> <a href="https://wa.me/919235222399?text=Jai%20Shree%20Ram!%20I%20have%20a%20query." target="_blank">Chat with Yatra Desk</a>`;
    }

    return `<strong>🚩 Pt. Ram Shastri (AI Yatra Assistant):</strong><br><br>` +
    `Aapke sawaal <em>"${query}"</em> ke liye humari Yatra Desk aapki poori madad karegi.<br><br>` +
    `Aap UP ke sabhi 8 dharmik nagaron (Ayodhya, Varanasi, Prayagraj, Mathura, Vrindavan, Chitrakoot, Naimisharanya, Vindhyachal, Gaya) ke baare mein direct poochh sakte hain:<br>` +
    `• <strong>Pahunchne Ka Rasta:</strong> Direct flights, Vande Bharat trains & Private AC Cabs.<br>` +
    `• <strong>VIP Pass:</strong> Ayodhya Ram Mandir (100% FREE) & Kashi Vishwanath Sugam Pass (₹300).<br>` +
    `• <strong>Tour Pricing:</strong> 3-Day Ayodhya-Varanasi-Prayagraj tour ₹1,499 - ₹3,499/person.<br><br>` +
    `📞 Turant baat karne ke liye Call ya WhatsApp karein:<br>` +
    `• <strong>Call:</strong> <a href="tel:+919235222399">+91 92352 22399</a><br>` +
    `• <strong>WhatsApp:</strong> <a href="https://wa.me/919235222399?text=Jai%20Shree%20Ram!%20I%20have%20a%20query." target="_blank">Direct Chat With Yatra Desk</a>`;
  }
})();
