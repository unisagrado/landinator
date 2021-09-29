const forms = [].slice.call(document.querySelectorAll('form'))
forms.map((el) => {
  
  function onSubmit(e){
    e.preventDefault();
    const form = e.currentTarget;

    const button = form.querySelector('button[type=submit]');
    button.disabled = true;
    button.innerHTML = 'Enviando...'

    form.submit();
  }
  
  el.addEventListener('submit', onSubmit);
});