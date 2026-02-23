<template>
  <div class="app-container">
    <nav class="navbar">
      <div class="logo">ELEBOY<span>.08</span></div>
      <div class="nav-links">
        <a href="#about">About</a>
        <a href="#projects">Projects</a>
        <a href="#guestbook">Guestbook</a>
      </div>
    </nav>

    <header class="hero">
      <div class="hero-content">
        <div class="hero-text">
          <h2 class="greeting">Hi, I'm</h2>
          <h1 class="name">Heinrich M. <span>Tobias</span></h1>
          <p class="bio">2nd Year BSCS-SF Student | Web Dev | Cybersecurity | Arduino Tinkerer</p>
          <div class="hero-btns">
            <a href="https://github.com/Eleboy08" target="_blank" class="btn-primary">View GitHub</a>
          </div>
        </div>
        <div class="hero-visual">
          <div class="profile-frame">
            <img src="./assets/profile.jpg" alt="Profile" />
          </div>
        </div>
      </div>
    </header>

    <section id="guestbook" class="guestbook-section">
      <h2 class="section-title">Guestbook</h2>
      <div class="guestbook-grid">
        <div class="form-container">
          <form @submit.prevent="submitComment">
            <input v-model="newComment.name" placeholder="Your Name" required />
            <textarea v-model="newComment.message" placeholder="Leave a message..." required></textarea>
            <button type="submit" :disabled="loading">{{ loading ? 'Sending...' : 'Post Message' }}</button>
          </form>
        </div>
        <div class="messages-container">
          <div v-for="c in comments" :key="c.id" class="message-card">
            <h4>{{ c.name }}</h4>
            <p>{{ c.message }}</p>
            <span class="date">{{ new Date(c.created_at).toLocaleDateString() }}</span>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const comments = ref([]);
const newComment = ref({ name: '', message: '' });
const loading = ref(false);

// PASTE YOUR PORT 5000 LINK HERE!
const API_URL = 'https://PASTE_YOUR_LINK_HERE/api/comments';

const fetchComments = async () => {
  try {
    const res = await fetch(API_URL);
    if (res.ok) comments.value = await res.json();
  } catch (err) { console.error(err); }
};

const submitComment = async () => {
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
  } catch (err) { alert("Check if Backend is running!"); }
  finally { loading.value = false; }
};

onMounted(fetchComments);
</script>

<style>
:root { --primary: #ff4742; --bg: #0a0a0a; --card: #151515; --text: #ffffff; }
body { background: var(--bg); color: var(--text); font-family: 'Inter', sans-serif; margin: 0; }
.app-container { max-width: 1200px; margin: 0 auto; padding: 0 20px; }

/* Navbar */
.navbar { display: flex; justify-content: space-between; padding: 30px 0; }
.logo { font-weight: 800; font-size: 1.5rem; }
.logo span { color: var(--primary); }
.nav-links a { margin-left: 30px; text-decoration: none; color: #888; transition: 0.3s; }
.nav-links a:hover { color: var(--primary); }

/* Hero */
.hero { padding: 100px 0; }
.hero-content { display: flex; align-items: center; justify-content: space-between; gap: 50px; }
.hero-text h1 { font-size: 4.5rem; margin: 0; }
.hero-text h1 span { color: var(--primary); }
.bio { color: #888; font-size: 1.2rem; margin: 20px 0; }
.profile-frame { width: 350px; height: 350px; border: 4px solid var(--primary); position: relative; }
.profile-frame img { width: 100%; height: 100%; object-fit: cover; position: absolute; top: 15px; left: 15px; }

/* Guestbook */
.guestbook-section { padding: 100px 0; }
.guestbook-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 40px; }
input, textarea { width: 100%; background: var(--card); border: 1px solid #333; color: white; padding: 15px; margin-bottom: 15px; }
button { background: var(--primary); color: white; border: none; padding: 15px 30px; font-weight: bold; cursor: pointer; width: 100%; }
.message-card { background: var(--card); padding: 20px; border-left: 4px solid var(--primary); margin-bottom: 15px; }
.message-card h4 { margin: 0; color: var(--primary); }
.date { font-size: 0.8rem; color: #555; }
</style>