import '@/css/main.css';
import 'flowbite';
import htmx from 'htmx.org';
import Alpine from 'alpinejs';
import { sayHello } from "./important.js";

// Make HTMX globally accessible
window.htmx = htmx;

// Make Alpine globally accessible
window.Alpine = Alpine
 
Alpine.start()

console.log('Hello from Vite');
sayHello('BugBytesss');