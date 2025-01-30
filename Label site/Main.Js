document.addEventListener("DOMContentLoaded", function() {

    const form = document.querySelector("form");
    
    form.addEventListener("submit", function(event) {
        const name = document.getElementById("name").value;
        const email = document.getElementById("email").value;
        const message = document.getElementById("message").value;

        if (!name || !email || !message) {
            alert("Tous les champs sont obligatoires. Veuillez les remplir.");
            event.preventDefault(); 
        } else {
            alert("Votre message a été envoyé avec succès !");
        }
    });

  
    const links = document.querySelectorAll('nav a');

    links.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            const targetSection = document.querySelector(targetId);

          
            targetSection.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        });
    });
});