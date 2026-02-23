import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vite.dev/config/
export default defineConfig({
  plugins: [vue()],
  build: {
    // Ensures the production build goes into a folder Vercel can easily find
    outDir: 'dist', 
    emptyOutDir: true,
  },
  server: {
    proxy: {
      // This allows you to test your Flask API locally during development
      '/api': 'http://127.0.0.1:5000'
    }
  }
})