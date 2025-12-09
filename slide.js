function reveal() {
    var reveals = document.querySelectorAll(".reveal");
    var timeline = document.querySelector(".timeline");
    
    if (!timeline) return;
    
    var timelineRect = timeline.getBoundingClientRect();
    var timelineCenter = timelineRect.left + timelineRect.width / 2;
  
    for (var i = 0; i < reveals.length; i++) {
      var windowHeight = window.innerHeight;
      var elementTop = reveals[i].getBoundingClientRect().top;
      var elementVisible = 50;
      var elementRect = reveals[i].getBoundingClientRect();
      var elementCenter = elementRect.left + elementRect.width / 2;
      
      // Determine if box is on left or right side
      var isLeftSide = elementCenter < timelineCenter;
      
      // Add appropriate class based on side
      if (isLeftSide) {
        reveals[i].classList.add("reveal-left");
        reveals[i].classList.remove("reveal-right");
      } else {
        reveals[i].classList.add("reveal-right");
        reveals[i].classList.remove("reveal-left");
      }
  
      if (elementTop < windowHeight - elementVisible) {
        reveals[i].classList.add("active");
      } else {
        reveals[i].classList.remove("active");
      }
    }
  }
  
  window.addEventListener("scroll", reveal);
  window.addEventListener("load", reveal); // Run once on load to set initial classes
  