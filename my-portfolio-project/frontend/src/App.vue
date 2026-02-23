<template>
  <div class="main-wrapper">
    <nav class="nav-container">
      <div class="nav-logo">ELEBOY<span>08</span></div>
      <div class="nav-links">
        <a href="#about">About</a>
        <a href="#projects">Works</a>
        <a href="#guestbook" class="btn-accent">Connect</a>
      </div>
    </nav>

    <header class="hero-section">
      <div class="hero-flex">
        <div class="hero-text">
          <p class="role-tag">// 2nd Year BSCS-SF Student</p>
          <h1>Heinrich M.<br><span class="highlight">Tobias</span></h1>
          <p class="bio">
            19-year-old student at **Asia Pacific College**. 
            Specializing in Web Security, Embedded Systems, and Cloud Integration. 
            I build secure applications and IoT solutions.
          </p>
          <div class="cta-btns">
            <a href="https://github.com/Eleboy08" target="_blank" class="btn-red">GITHUB</a>
            <a href="#projects" class="btn-outline">VIEW PROJECTS</a>
          </div>
        </div>
        <div class="hero-image">
          <div class="img-frame">
            <img src="./assets/elele.jpg" alt="Heinrich Tobias" class="profile-img" />
            <div class="glow-effect"></div>
          </div>
        </div>
      </div>
    </header>

    <section id="projects" class="project-section">
      <h2 class="title">Featured <span class="highlight">Works</span></h2>
      <div class="project-grid">
        <div class="card">
          <span class="cat">Web Security</span>
          <h3>Jester's Hat Vault</h3>
          <p>A secure file management web app using AES encryption for data protection.</p>
        </div>
        <div class="card">
          <span class="cat">IoT & Embedded</span>
          <h3>Smart Alarm System</h3>
          <p>Arduino-based wake-up solution using pressure mats and smart light synchronization.</p>
        </div>
        <div class="card">
          <span class="cat">Cloud Systems</span>
          <h3>PEMBEDS Assignment</h3>
          <p>Integration of DHT11 sensors with Arduino IoT Cloud and ThingSpeak.</p>
        </div>
      </div>
    </section>

    <section id="guestbook" class="guestbook-section">
      <h2 class="title">Guest <span class="highlight">Book</span></h2>
      <div class="guest-interface">
        <div class="form-container">
          <input v-model="newComment.name" placeholder="Your Name" required />
          <textarea v-model="newComment.message" placeholder="Write a message..." required></textarea>
          <button @click="submitComment" :disabled="loading" class="btn-red">
            {{ loading ? 'SENDING...' : 'SIGN GUESTBOOK' }}
          </button>
        </div>
        <div class="message-list">
          <div v-if="comments.length === 0" class="empty-msg">No entries yet. Be the first!</div>
          <div v-for="c in comments" :key="c.id" class="message-bubble">
            <strong>{{ c.name }}</strong>
            <p>{{ c.message }}</p>
            <span class="timestamp">{{ new Date(c.created_at).toLocaleDateString() }}</span>
          </div>
        </div>
      </div>
    </section>

    <footer class="site-footer">
      <p>&copy; 2026 Heinrich M. Tobias | Asia Pacific College</p>
    </footer>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const comments = ref([]);
const newComment = ref({ name: '', message: '' });
const loading = ref(false);

// *** REPLACE THIS with your Port 5000 Forwarded Address from the PORTS tab! ***
const API_URL = 'https://REPLACE_WITH_YOUR_PORT_5000_LINK.app.github.dev/api/comments'; 

const fetchComments = async () => {
  try {
    const res = await fetch(API_URL);
    if (res.ok) comments.value = await res.json();
  } catch (err) { console.error("Database sync failed."); }
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
  } catch (err) { alert("Error: Is the Backend terminal running?"); }
  finally { loading.value = false; }
};

onMounted(fetchComments);
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;600;900&display=swap');
:root { --red: #ff3333; --bg: #0d0d0d; --surface: #171717; }
body { background: var(--bg); color: #fff; font-family: 'Outfit', sans-serif; margin: 0; scroll-behavior: smooth; }

/* Crimson Themes */
.highlight { color: var(--red); }
.btn-red { background: var(--red); border: none; color: white; padding: 14px 30px; font-weight: 900; cursor: pointer; border-radius: 4px; text-decoration: none; display: inline-block; transition: 0.3s; }
.btn-red:hover { box-shadow: 0 0 20px rgba(255, 51, 51, 0.4); transform: translateY(-2px); }
.btn-outline { border: 1px solid var(--red); color: var(--red); padding: 14px 30px; text-decoration: none; margin-left: 15px; border-radius: 4px; display: inline-block; }
.btn-accent { color: var(--red); text-decoration: none; font-weight: 900; padding: 10px 20px; border: 1px solid var(--red); }

/* Structural Styling */
.main-wrapper { max-width: 1200px; margin: 0 auto; padding: 0 40px; }
.nav-container { display: flex; justify-content: space-between; padding: 50px 0; align-items: center; }
.nav-logo { font-weight: 900; font-size: 1.5rem; }
.nav-links a { margin-left: 25px; text-decoration: none; color: #888; font-size: 0.9rem; }

.hero-section { padding: 80px 0; }
.hero-flex { display: flex; align-items: center; justify-content: space-between; gap: 60px; }
.hero-text h1 { font-size: 5rem; line-height: 1; margin: 15px 0; font-weight: 900; }
.role-tag { color: var(--red); font-family: monospace; font-size: 1.1rem; }
.bio { font-size: 1.25rem; color: #999; line-height: 1.6; max-width: 550px; margin-bottom: 40px; }

.img-frame { position: relative; width: 360px; }
.profile-img { width: 100%; border-radius: 12px; border: 2px solid #222; position: relative; z-index: 5; }
.glow-effect { position: absolute; top: 15px; left: 15px; width: 100%; height: 100%; border: 3px solid var(--red); border-radius: 12px; z-index: 1; opacity: 0.4; }

.title { font-size: 3rem; text-align: center; margin-bottom: 60px; font-weight: 900; }
.project-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; margin-bottom: 100px; }
.card { background: var(--surface); padding: 40px; border-radius: 12px; border-bottom: 3px solid transparent; transition: 0.3s; }
.card:hover { border-bottom-color: var(--red); transform: translateY(-5px); }
.cat { color: var(--red); font-size: 0.8rem; font-weight: 900; text-transform: uppercase; }

.guest-interface { display: grid; grid-template-columns: 1fr 1.5fr; gap: 40px; background: #111; padding: 40px; border-radius: 12px; border: 1px solid #222; }
input, textarea { width: 100%; background: #000; border: 1px solid #333; color: white; padding: 15px; margin-bottom: 20px; border-radius: 4px; box-sizing: border-box; }
.message-bubble { background: #000; padding: 20px; border-left: 4px solid var(--red); margin-bottom: 15px; position: relative; }
.timestamp { font-size: 0.7rem; color: #444; position: absolute; top: 10px; right: 10px; }

.site-footer { text-align: center; padding: 80px 0; color: #444; }

@media (max-width: 900px) {
  .hero-flex, .guest-interface { grid-template-columns: 1fr; text-align: center; }
  .hero-text h1 {