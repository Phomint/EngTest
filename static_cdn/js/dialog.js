var dialog = document.querySelector('dialog');
var showDialogButton = document.querySelector('#show-dialog');
var deleteButton = document.querySelector('#demo-show-snackbar');

if (! dialog.showModal) {
    dialogPolyfill.registerDialog(dialog);
}
showDialogButton.addEventListener('click', function() {
    dialog.showModal();
});
deleteButton.addEventListener('click',function(){
  dialog.close();
});
dialog.querySelector('.close').addEventListener('click', function() {
    dialog.close();
});
