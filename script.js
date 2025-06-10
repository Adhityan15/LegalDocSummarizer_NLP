document.addEventListener("DOMContentLoaded", function () {
  const form = document.querySelector("form");
  const loadingDiv = document.getElementById("loading");

  form.addEventListener("submit", function () {
    loadingDiv.style.display = "block";
  });
});
