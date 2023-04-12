function sendMail() {
  // Get Google ReCaptcha Score
  let captchaToken = grecaptcha.getResponse();
  if (captchaToken.length > 0) {
    var params = {
      name: document.getElementById("name").value,
      email: document.getElementById("email").value,
      message: document.getElementById("message").value,
      "g-recaptcha-response": captchaToken,
    };

    const serviceID = "service_fk6wcgq";
    const templateID = "template_0c9glu8";
    emailjs
      .send(serviceID, templateID, params)
      .then((res) => {
        document.getElementById("name").value = "";
        document.getElementById("email").value = "";
        document.getElementById("message").value = "";
        console.log(res);
        alert("Thanks for reaching out! I'll get back to you soon.");
      })
      .catch((err) => console.log(err));
  } else{
    alert("Please fill reCAPTCHA to continue")
  }
}
