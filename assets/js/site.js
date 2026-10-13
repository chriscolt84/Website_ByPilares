/* ByPilares: mobile navigation, contact form, footer year. */
(function () {
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('site-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      toggle.textContent = open ? 'Cerrar' : 'Menú';
    });
  }

  var year = document.getElementById('year');
  if (year) year.textContent = String(new Date().getFullYear());

  /* Contact form. Set data-endpoint on the form to a Formspree (or similar) URL
     that accepts a JSON POST. See README.md, "Contact form". */
  var form = document.getElementById('contact-form');
  if (!form) return;
  var status = document.getElementById('form-status');
  function say(msg) { status.textContent = msg; status.hidden = false; }

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    if (!form.checkValidity()) { form.reportValidity(); return; }
    var endpoint = form.getAttribute('data-endpoint');
    if (!endpoint) {
      say('Gracias. El formulario todavía no está conectado; mientras tanto, escríbenos por nuestras redes.');
      return;
    }
    var data = {};
    new FormData(form).forEach(function (v, k) { data[k] = v; });
    var btn = form.querySelector('button[type="submit"]');
    btn.disabled = true;
    fetch(endpoint, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: JSON.stringify(data) })
      .then(function (r) {
        if (!r.ok) throw new Error(String(r.status));
        form.reset();
        say('Gracias por escribir. Te respondemos pronto.');
      })
      .catch(function () { say('No pudimos enviar tu mensaje. Inténtalo de nuevo en unos minutos.'); })
      .then(function () { btn.disabled = false; });
  });
})();
