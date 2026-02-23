<template>
  <div class="portfolio-container">
    
    <header class="hero">
      <div class="hero-container">
        <div class="hero-text">
          <span class="accent-text">CREATIVE DEVELOPER</span>
          <h1>HEINRICH M.<br>TOBIAS</h1>
          <p class="tagline">2nd-Year BSCS-SF Student building secure web apps, tinkering with Arduino, and connecting the dots.</p>
          <div class="social-links">
            <a href="https://github.com/Eleboy08" target="_blank" class="btn primary">Watch Portfolio</a>
          </div>
        </div>

        <div class="hero-image">
          <img src="./assets/profile.jpg" alt="Heinrich M. Tobias" />
        </div>
      </div>
    </header>

    <section class="about section-padding">
      <div class="container text-center">
        <h3 class="section-title">About Me</h3>
        <p class="about-text">
          I'm a 19-year-old computer science student with a focus on web development, embedded systems, and cybersecurity. I enjoy working across the stack, from designing sleek UIs with Vue.js to setting up secure database architectures and IoT hardware. When I'm away from the keyboard, you'll usually find me cooking or on the basketball court.
        </p>
      </div>
    </section>

    <section class="projects section-padding dark-bg">
      <div class="container">
        <h3 class="section-title text-center">Recent Projects</h3>
        <div class="project-grid">
          
          <div class="project-card">
            <h4>Jester's Hat Vault</h4>
            <p>A functional web application designed for secure file management utilizing AES encryption to keep user data private.</p>
            <span class="tech-tag">HTML/CSS/JS</span>
          </div>

          <div class="project-card">
            <h4>Smart Alarm System</h4>
            <p>An IoT wake-up solution using an Arduino Uno R4, pressure-sensitive mats, and smart lighting integration mapped via Lean Canvas.</p>
            <span class="tech-tag">Arduino / Embedded</span>
          </div>

        </div>
      </div>
    </section>

    <section class="guestbook section-padding">
      <div class="container">
        <h3 class="section-title text-center">Guestbook</h3>
        <p class="subtitle text-center">Leave a message! (Powered by Vue, Flask API, and Supabase)</p>
        
        <div class="guestbook-interface">
          <form @submit.prevent="submitComment" class="comment-form">
            <div class="form-group">
              <label for="name">Name</label>
              <input type="text" id="name" v-model="newComment.name" required placeholder="Your name" />
            </div>
            <div class="form-group">
              <label for="message">Message</label>
              <textarea id="message" v-model="newComment.message" required placeholder="What's on your mind?"></textarea>
            </div>
            <button type="submit" class="btn primary full-width" :disabled="isSubmitting">
              {{ isSubmitting ? 'Sending...' : 'Sign Guestbook' }}
            </button>
          </form>

          <div class="comments-list">
            <h4>Recent Messages</h4>
            <div v-if="comments.length === 0" class="no-comments">No messages yet. Be the first!</div>
            <div v-else class="comment" v-for="comment in comments" :key="comment.id">
              <strong>{{ comment.name }}</strong>
              <p>{{ comment.message }}</p>
              <small>{{ new Date(comment.created_at).toLocaleDateString() }}</small>
            </div>
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
const isSubmitting = ref(false);

// Change this to your Render URL once deployed!
const API_URL = 'http://127.0.0.1:5000/api/comments'; 

const fetchComments = async () => {
  try {
    const response = await fetch(API_URL);
    if (!response.ok) throw new Error('Network response was not ok');
    const data = await response.json();
    comments.value = data;
  } catch (error) {
    console.error("Error fetching comments:", error);
  }
};

const submitComment = async () => {
  if (!newComment.value.name || !newComment.value.message) return;
  
  isSubmitting.value = true;
  try {
    const response = await fetch(API_URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(newComment.value)
    });
    
    if (response.ok) {
      await fetchComments(); 
      newComment.value = { name: '', message: '' }; 
    }
  } catch (error) {
    console.error("Error submitting comment:", error);
  } finally {
    isSubmitting.value = false;
  }
};

onMounted(() => {
  fetchComments();
});
</script>

<style scoped>
/* --- THEME VARIABLES --- */
:root {
  --bg-dark: #0a0a0a;
  --bg-card: #151515;
  --accent: #ff4742;
  --accent-hover: #e03e39;
  --text-light: #ffffff;
  --text-muted: #a0a0a0;
  --border-color: #333333;
}

.portfolio-container {
  background-color: var(--bg-dark);
  color: var(--text-light);
  min-height: 100vh;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

.section-padding {
  padding: 100px 0;
}

.text-center {
  text-align: center;
}

.dark-bg {
  background-color: #050505;
}

.section-title {
  font-size: 2.5rem;
  margin-bottom: 20px;
  text-transform: uppercase;
  letter-spacing: 2px;
}

.subtitle {
  color: var(--text-muted);
  margin-bottom: 40px;
}

/* --- HERO SECTION --- */
.hero {
  padding: 120px 20px 60px;
  overflow: hidden;
}

.hero-container {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 50px;
}

.hero-text {
  flex: 1;
}

.accent-text {
  color: var(--accent);
  font-size: 0.9rem;
  letter-spacing: 3px;
  text-transform: uppercase;
  position: relative;
  display: inline-block;
  margin-bottom: 20px;
}

.accent-text::before {
  content: "";
  position: absolute;
  left: -40px;
  top: 50%;
  width: 30px;
  height: 2px;
  background-color: var(--accent);
}

.hero-text h1 {
  font-size: 4.5rem;
  line-height: 1.1;
  margin-bottom: 20px;
  text-transform: uppercase;
  font-weight: 800;
}

.tagline {
  font-size: 1.2rem;
  color: var(--text-muted);
  margin-bottom: 40px;
  max-width: 500px;
  line-height: 1.6;
}

.hero-image {
  flex: 1;
  display: flex;
  justify-content: flex-end;
}

.hero-image img {
  max-width: 100%;
  height: auto;
  max-height: 600px;
  object-fit: cover;
  filter: drop-shadow(-20px 20px 30px rgba(0,0,0,0.8));
}

/* --- BUTTONS --- */
.btn {
  display: inline-block;
  padding: 15px 35px;
  text-decoration: none;
  font-weight: 700;
  letter-spacing: 1px;
  cursor: pointer;
  transition: all 0.3s ease;
  border: none;
  text-transform: uppercase;
}

.btn.primary {
  background-color: var(--accent);
  color: white;
}

.btn.primary:hover:not(:disabled) {
  background-color: var(--accent-hover);
}

.btn.primary:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.full-width {
  width: 100%;
}

/* --- ABOUT SECTION --- */
.about-text {
  max-width: 800px;
  margin: 0 auto;
  font-size: 1.1rem;
  line-height: 1.8;
  color: var(--text-muted);
}

/* --- PROJECTS SECTION --- */
.project-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 30px;
  margin-top: 40px;
}

.project-card {
  background: var(--bg-card);
  padding: 40px 30px;
  border: 1px solid var(--border-color);
  transition: transform 0.3s ease, border-color 0.3s ease;
}

.project-card:hover {
  transform: translateY(-5px);
  border-color: var(--accent);
}

.project-card h4 {
  font-size: 1.5rem;
  margin-bottom: 15px;
  color: var(--text-light);
}

.project-card p {
  color: var(--text-muted);
  margin-bottom: 20px;
  line-height: 1.6;
}

.tech-tag {
  display: inline-block;
  background: rgba(255, 71, 66, 0.1);
  color: var(--accent);
  padding: 6px 15px;
  font-size: 0.85rem;
  letter-spacing: 1px;
  text-transform: uppercase;
}

/* --- GUESTBOOK SECTION --- */
.guestbook-interface {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 40px;
  background: var(--bg-card);
  padding: 40px;
  border: 1px solid var(--border-color);
}

.form-group {
  margin-bottom: 20px;
}

.form-group label {
  display: block;
  margin-bottom: 8px;
  font-weight: 600;
  color: var(--text-muted);
}

.form-group input,
.form-group textarea {
  width: 100%;
  padding: 15px;
  background-color: #0a0a0a;
  border: 1px solid var(--border-color);
  color: var(--text-light);
  font-size: 1rem;
}

.form-group input:focus,
.form-group textarea:focus {
  outline: none;
  border-color: var(--accent);
}

.form-group textarea {
  height: 150px;
  resize: vertical;
}

.comments-list {
  background: #0a0a0a;
  padding: 20px;
  border: 1px solid var(--border-color);
  max-height: 400px;
  overflow-y: auto;
}

.comments-list h4 {
  margin-bottom: 20px;
  color: var(--accent);
}

.comment {
  padding: 15px 0;
  border-bottom: 1px solid var(--border-color);
}

.comment:last-child {
  border-bottom: none;
}

.comment strong {
  display: block;
  margin-bottom: 5px;
  color: var(--text-light);
}

.comment p {
  color: var(--text-muted);
  margin-bottom: 8px;
}

.comment small {
  color: #666;
}

/* --- MOBILE RESPONSIVENESS --- */
@media (max-width: 900px) {
  .hero-container {
    flex-direction: column-reverse;
    text-align: center;
  }
  
  .hero-text {
    text-align: center;
  }
  
  .accent-text::before {
    display: none;
  }

  .hero-text h1 {
    font-size: 3rem;
  }
  
  .hero-image {
    justify-content: center;
  }

  .guestbook-interface {
    grid-template-columns: 1fr;
  }
}
</style>