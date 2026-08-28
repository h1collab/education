const button=document.querySelector('.menu-button');
const nav=document.querySelector('#site-nav');
button.addEventListener('click',()=>{const open=nav.classList.toggle('open');button.setAttribute('aria-expanded',String(open))});
nav.addEventListener('click',()=>{nav.classList.remove('open');button.setAttribute('aria-expanded','false')});
const sections=[...document.querySelectorAll('main section[id]')];
const links=[...document.querySelectorAll('.topbar nav a')];
const observer=new IntersectionObserver(entries=>{entries.forEach(entry=>{if(entry.isIntersecting){links.forEach(a=>a.removeAttribute('aria-current'));const active=links.find(a=>a.getAttribute('href')==='#'+entry.target.id);if(active)active.setAttribute('aria-current','page')}})},{rootMargin:'-35% 0px -55%'});
sections.forEach(section=>observer.observe(section));
