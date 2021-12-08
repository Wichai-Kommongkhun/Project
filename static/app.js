const navSlide = () => {
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.nav-links');
    const navLinks = document.querySelectorAll('.nav-links li');
    // Toggle
        burger.addEventListener('click', () => {
            nav.classList.toggle('nav-active');

            navLinks.forEach((link, home) => {
            
                if(link.style.animation){
                    link.style.animation = ''
    
                } else {
                    link.style.animation = `navLinkFade 0.5 ease forwards ${home / 7 + 1}s`; 
                }
            });
            // X
            burger.classList.toggle('toggle');
        });

        
    
}

navSlide();
