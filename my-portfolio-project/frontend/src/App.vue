<template>
  <div class="main-wrapper">
    <nav class="nav-container">
      <div class="nav-logo">ELEBOY<span>08</span></div>
      <div class="nav-menu">
        <a href="#about">About</a>
        <a href="#skills">Skills</a>
        <a href="#projects">Portfolio</a>
        <a href="#guestbook" class="contact-trigger">Connect</a>
      </div>
    </nav>

    <header class="hero-block">
      <div class="hero-flex">
        <div class="hero-content">
          <p class="dev-tag">&lt;Computer Science Student /&gt;</p>
          <h1>Heinrich M.<br><span class="crimson">Tobias</span></h1>
          <p class="summary">
            19-year-old developer at **FEU Tech**. Specializing in Web Development, 
            Cybersecurity, and Embedded Systems. I build solutions like **Jester's Hat Vault** and hardware-integrated **Smart Alarms**.
          </p>
          <div class="cta-group">
            <a href="https://github.com/Eleboy08" target="_blank" class="btn-main">GITHUB</a>
            <a href="#projects" class="btn-ghost">VIEW WORKS</a>
          </div>
        </div>
        <div class="hero-frame">
          <div class="image-box">
            <img src="./assets/elele.jpg" alt="Heinrich Tobias" class="profile-img" />
            <div class="accent-glow"></div>
          </div>
        </div>
      </div>
    </header>

    <section id="about" class="details-section">
      <div class="details-grid">
        <div class="info-card">
          <h3>Personal Info</h3>
          <ul>
            <li><strong>Age:</strong> 19</li>
            <li><strong>Location:</strong> Philippines</li>
            <li><strong>Hobbies:</strong> Basketball & Cooking</li>
          </ul>
        </div>
        <div class="info-card">
          <h3>Academic Focus</h3>
          <p>Currently a 2nd-year BSCS-SF student focusing on AES Encryption and IoT Cloud systems (ThingSpeak/Arduino IoT).</p>
        </div>
      </div>
    </section>

    <section id="guestbook" class="guest-container">
      <h2 class="section-heading">Guest <span class="crimson">Book</span></h2>
      <div class="guest-interface">
        <div class="form-side">
          <input v-model="newComment.name" placeholder="Name" />
          <textarea v-model="newComment.message" placeholder="Leave a message..."></textarea>
          <button @click="submitComment" :disabled="loading" class="btn-main">
            {{ loading ? 'SENDING...' : 'SIGN GUESTBOOK' }}
          </button>
        </div>
        <div class="list-side">
          <div v-for="c in comments" :key="c.id" class="comment-bubble">
            <strong>{{ c.name }}</strong>
            <p>{{ c.message }}</p>
          </div>
        </div>
      </div>
    </section>

    <footer class="site-footer">
      <p>Built by Heinrich M. Tobias | 2026</p>
    </footer>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const comments = ref([]);
const newComment = ref({ name: '', message: '' });
const loading = ref(false);

// *** REPLACE THIS with your Port 5000 URL from the PORTS tab! ***
const API_URL = 'https://REPLACE_WITH_YOUR_PORT_5000_LINK.app.github.dev/api/comments';

const fetchComments = async () => {
  try {
    const res = await fetch(API_URL);
    if (res.ok) comments.value = await res.json();
  } catch (err) { console.error("Database connection failed."); }
};

const submitComment = async () => {
  if(!newComment.value.name || !newComment.value.message) return;
  loading.value = true;
  try {
    const res = await fetch(API_URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(newComment.value)
    });
    if (res.ok) {
      newComment.value = { name: '', message: '' };
      await fetchComments();
    }
  } catch (err) { alert("Check your Backend Terminal!"); }
  finally { loading.value = false; }
};

onMounted(fetchComments);
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;600;900&display=swap');

:root { --crimson: #ff3333; --bg: #0d0d0d; --surface: #171717; }
body { background: var(--bg); color: #fff; font-family: 'Outfit', sans-serif; margin: 0; scroll-behavior: smooth; }

/* Crimson & Dark Styling */
.crimson { color: var(--crimson); }
.btn-main { background: var(--crimson); border: none; color: #fff; padding: 14px 30px; font-weight: 900; letter-spacing: 1px; cursor: pointer; border-radius: 4px; }
.btn-main:hover { box-shadow: 0 0 15px rgba(255, 51, 51, 0.4); }
.btn-ghost { border: 1px solid var(--crimson); color: var(--crimson); padding: 14px 30px; text-decoration: none; margin-left: 15px; border-radius: 4px; }

/* Structural Layout */
.main-wrapper { max-width: 1200px; margin: 0 auto; padding: 0 40px; }
.nav-container { display: flex; justify-content: space-between; padding: 50px 0; align-items: center; }
.nav-logo { font-weight: 900; font-size: 1.4rem; }
.nav-logo span { color: var(--crimson); }
.nav-menu a { margin-left: 30px; text-decoration: none; color: #999; transition: 0.3s; }
.nav-menu a:hover { color: var(--crimson); }

.hero-block { padding: 100px 0; }
.hero-flex { display: flex; align-items: center; justify-content: space-between; gap: 60px; }
.hero-content h1 { font-size: 5rem; margin: 10px 0; line-height: 1; font-weight: 900; }
.dev-tag { color: var(--crimson); font-family: monospace; font-size: 1.1rem; }
.summary { color: #888; font-size: 1.3rem; line-height: 1.6; max-width: 550px; margin-bottom: 40px; }

.image-box { position: relative; width: 380px; }
.profile-img { width: 100%; border-radius: 12px; position: relative; z-index: 5; border: 2px solid #222; }
.accent-glow { position: absolute; width: 100%; height: 100%; top: 20px; left: 20px; border: 3px solid var(--crimson); border-radius: 12px; z-index: 1; opacity: 0.5; }

.details-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 30px; padding: 80px 0; }
.info-card { background: var(--surface); padding: 40px; border-radius: 12px; }

.guest-interface { display: grid; grid-template-columns: 1fr 1fr; gap: 40px; margin-top: 50px; }
input, textarea { width: 100%; background: #000; border: 1px solid #333; color: #fff; padding: 15px; margin-bottom: 20px; border-radius: 4px; }
.comment-bubble { background: var(--surface); padding: 20px; border-left: 4px solid var(--crimson); margin-bottom: 15px; }

.site-footer { text-align: center; padding: 80px 0; color: #444; }

@media (max-width: 900px) {
  .hero-flex, .details-grid, .guest-interface { grid-template-columns: 1fr; flex-direction: column; text-align: center; }
  .hero-content h1 { font-size: 3.5rem; }
}
</style>