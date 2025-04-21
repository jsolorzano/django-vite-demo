import {defineConfig} from 'vite';
import {resolve} from 'path';
import tailwindcss from '@tailwindcss/vite'

export default defineConfig({
    server: {
      host: true,
      allowedHosts: true,
      cors: {
        "origin": "*",
        "methods": "GET,HEAD,PUT,PATCH,POST,DELETE",
        "preflightContinue": false,
        "optionsSuccessStatus": 204
      }
    },
    base: "/static/",
    resolve: {
      alias: {
        '@': resolve('./static')
      }
    },
    build: {
      manifest: "manifest.json",
      outDir: resolve("./assets"),
      assetsDir: "django-assets",
      rollupOptions: {
        input: {
          test: resolve('./static/js/main.js')
        }
      }
    },
    plugins: [
      tailwindcss(),
    ]
})