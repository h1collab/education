const sfide=[
  "Spiegalo senza usare la parola del titolo.",
  "Trova un esempio nella tua giornata.",
  "Disegnalo in trenta secondi.",
  "Inventa un errore credibile e fallo correggere.",
  "Collegalo a una notizia o a un'altra materia.",
  "Difendi l'idea opposta per un minuto.",
  "Trasformalo in una domanda da quiz.",
  "Spiegalo come se avessi sette anni."
];
document.querySelectorAll(".challenge-button").forEach(button=>{
  button.addEventListener("click",()=>{
    const output=button.parentElement.querySelector(".challenge-output");
    output.textContent=sfide[Math.floor(Math.random()*sfide.length)];
    output.classList.add("pop");
    setTimeout(()=>output.classList.remove("pop"),350);
  });
});
document.querySelectorAll(".reveal-answer").forEach(button=>{
  button.addEventListener("click",()=>{
    const answer=button.parentElement.querySelector(".answer");
    answer.hidden=!answer.hidden;
    button.textContent=answer.hidden?"Mostra come argomentare":"Nascondi la traccia";
  });
});
const progress=document.createElement("div");
progress.className="reading-progress";
progress.setAttribute("aria-hidden","true");
document.body.append(progress);
const controls=document.createElement("div");
controls.className="classroom-controls";
controls.innerHTML='<button type="button" class="presentation-toggle" aria-pressed="false">📽 Modalità lezione</button><button type="button" class="calm-toggle" aria-pressed="false">☁ Modalità calma</button>';
document.body.append(controls);
controls.querySelector(".presentation-toggle").addEventListener("click",event=>{
  const active=document.body.classList.toggle("presentation-mode");
  event.currentTarget.setAttribute("aria-pressed",String(active));
});
controls.querySelector(".calm-toggle").addEventListener("click",event=>{
  const active=document.body.classList.toggle("calm-mode");
  event.currentTarget.setAttribute("aria-pressed",String(active));
});
addEventListener("scroll",()=>{
  const available=document.documentElement.scrollHeight-innerHeight;
  progress.style.width=(available?scrollY/available*100:100)+"%";
},{passive:true});

const courseSearch=document.querySelector("#course-search");
if(courseSearch){
  const cards=[...document.querySelectorAll(".catalog-card")];
  const years=[...document.querySelectorAll(".catalog-year")];
  const status=document.querySelector(".search-status");
  courseSearch.addEventListener("input",()=>{
    const query=courseSearch.value.trim().toLocaleLowerCase("it");
    let visible=0;
    cards.forEach(card=>{
      const match=!query||card.textContent.toLocaleLowerCase("it").includes(query);
      card.hidden=!match;
      if(match) visible+=1;
    });
    years.forEach(year=>{
      year.hidden=query&&!year.querySelector(".catalog-card:not([hidden])");
    });
    status.textContent=query
      ? visible===1
        ? "1 corso trovato."
        : visible+" corsi trovati."
      : "Tutti i corsi sono visibili.";
  });
}
