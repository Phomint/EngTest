(function() {
  'use strict';
  var snackbarContainer = document.querySelector('#demo-snackbar-example');
  var showSnackbarButton = document.querySelector('#demo-show-snackbar');
  var handler = function(event) {
    showSnackbarButton.style.backgroundColor = '';
  };
  showSnackbarButton.addEventListener('click', function() {
    'use strict';
    var data = {
      message: 'Deletado com Sucesso!',
      timeout: 5000,
      actionHandler: handler,
      actionText: 'Desfazer'
    };
    snackbarContainer.MaterialSnackbar.showSnackbar(data);
  });
}());
