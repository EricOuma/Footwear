// IMAGE MODAL JQUERY
$('#imageModal').on('show.bs.modal', function (event) {
    var img = $(event.relatedTarget) // Element that triggered the modal
    var name = img.data('name') // Extract info from data-* attributes
    var src = img.data('src')
    // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
    // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
    var modal = $(this)
    modal.find('.modal-title').text(name)
    modal.find('.modal-body img').attr('src', src)
  })