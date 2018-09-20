var modalTriggers = document.querySelectorAll('[data-toggle="modal"]');

// Getting the target modal of every button and applying listeners
for (var i = modalTriggers.length - 1; i >= 0; i--) {
  var t = modalTriggers[i].getAttribute('data-target');
  var id = '#' + modalTriggers[i].getAttribute('id');

  modalProcess(t, id);
}

/**
 * It applies the listeners to modal and modal triggers
 * @param  {string} selector [The Dialog ID]
 * @param  {string} button   [The Dialog triggering Button ID]
 */
function modalProcess(selector, button) {
  var dialog = document.querySelector(selector);
  var showDialogButton = document.querySelector(button);

  if (dialog) {
    if (!dialog.showModal) {
      dialogPolyfill.registerDialog(dialog);
    }
    showDialogButton.addEventListener('click', function() {
      dialog.showModal();
    });
    dialog.querySelector('.close').addEventListener('click', function() {
      dialog.close();
    });
  }
}
