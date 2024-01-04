var Sparkles = [];
SparkleBackground = document.querySelector(".SparkleDiv")
function generateSparkle() {
  SparkleBackground.innerHTML = "";
  
  for (var i = 0; i < 60; i++) {
    const size = Math.random() * 20 + 10; // Taille aléatoire entre 10 et 30
    const duration = Math.random() * 10 + 1; // Durée d'animation aléatoire entre 1 et 11 secondes
    topPX = Math.random() * window.innerHeight;
    rightPX = Math.random() * window.innerWidth ;
    const Sparkle = document.createElement("img");
         Sparkle.src = ["res/pixelstar.gif",];
         Sparkle.classList.add("Sparkle");
         Sparkle.style.width = size + "px"
         Sparkle.style.top = topPX  + "px"
         Sparkle.style.right = rightPX  + "px"
         Sparkle.style.animationDuration = duration +10 +  "s";
         Sparkles.push(Sparkle);
         SparkleBackground.appendChild(Sparkle);
} 
    
    
    
 }

generateSparkle()

 setInterval(generateSparkle, 8000)
 
 
