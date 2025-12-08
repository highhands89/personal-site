// Test version without reCAPTCHA for localhost testing
function sendMail() {
  // Validate form fields
  const name = document.getElementById("name").value.trim();
  const email = document.getElementById("email").value.trim();
  const message = document.getElementById("message").value.trim();

  if (!name || !email || !message) {
    alert("Please fill in all fields before submitting.");
    return;
  }

  // Validate email format
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(email)) {
    alert("Please enter a valid email address.");
    return;
  }

  var params = {
    name: name,
    email: email,
    message: message,
    // No reCAPTCHA token for test version
  };

  const serviceID = "service_fk6wcgq";
  const templateID = "template_0c9glu8";
  
  // Disable button during submission
  const submitBtn = document.querySelector(".btn");
  const originalText = submitBtn.textContent;
  submitBtn.disabled = true;
  submitBtn.textContent = "Sending...";

  emailjs
    .send(serviceID, templateID, params)
    .then((res) => {
      console.log("EmailJS Success:", res);
      document.getElementById("name").value = "";
      document.getElementById("email").value = "";
      document.getElementById("message").value = "";
      alert("Thanks for reaching out! I'll get back to you soon.");
      submitBtn.disabled = false;
      submitBtn.textContent = originalText;
    })
    .catch((err) => {
      console.error("EmailJS Error:", err);
      alert("Sorry, there was an error sending your message. Please try again or email me directly at kl@rangetrainerpro.com\n\nError: " + (err.text || err.message || "Unknown error"));
      submitBtn.disabled = false;
      submitBtn.textContent = originalText;
      
      // Log detailed error for debugging
      console.error("Full error object:", err);
      if (err.text) {
        console.error("Error details:", err.text);
      }
    });
}

