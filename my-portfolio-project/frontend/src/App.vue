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

    <section class="guestbook section-padding">
      <div class="container">
        <h3 class="section-title text-center">Guestbook</h3>
        <p class="subtitle text-center">Leave a message! (Powered by Vue, Flask, and Supabase)</p>
        
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

/** * IMPORTANT: REPLACE THE URL BELOW! 
 * 1. Go to the 'PORTS' tab in VS Code.
 * 2. Copy the 'Forwarded Address' for Port 5000.
 * 3. Paste it here, keeping '/api/comments' at the end.
 */
const API_URL = 'https://REPLACE_WITH_YOUR_PORT_5000_LINK.app.github.dev/api/comments'; 

const fetchComments = async () => {
  try {
    const response = await fetch(API_URL);
    if (response.ok) {
      const data = await response.json();
      comments.value = Array.isArray(data) ? data : [];
    }
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
    } else {
      alert("Error: Table 'guestbook' might be missing columns or RLS is enabled.");
    }
  } catch (error) {
    alert("Check your Backend Terminal! Is it running?");
  } finally {
    isSubmitting.value = false;
  }
};

onMounted(fetchComments);
</script>

<style scoped>
/* Same styles as before - keeping it clean for your portfolio */
:root { --bg-dark: #0a0a0a; --accent: #ff4742; --text-light: #ffffff; }
.portfolio-container { background: #0a0a0a; color: white; min-height: 100vh; font-family: sans-serif; }
.container { max-width: 1000px; margin: 0 auto; padding: 50px 20px; }
.hero { display: flex; align-items: center; justify-content: space-between; padding: 100px 20px; }
.hero-text h1 { font-size: 4rem; margin: 10px 0; }
.accent-text { color: #ff4742; letter-spacing: 2px; }
.hero-image img { width: 300px; border-radius: 10px; }
.btn.primary { background: #ff4742; color: white; padding: 15px 30px; text-decoration: none; border: none; cursor: pointer; font-weight: bold; }
.guestbook-interface { display: grid; grid-template-columns: 1fr 1fr; gap: 40px; background: #151515; padding: 30px; border: 1px solid #333; }
.form-group { margin-bottom: 15px; }
.form-group input, .form-group textarea { width: 100%; padding: 10px; background: #000; border: 1px solid #444; color: white; }
.comments-list { background: #000; padding: 15px; max-height: 300px; overflow-y: auto; }
.comment { border-bottom: 1px solid #333; padding: 10px 0; }
</style>