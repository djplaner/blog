
document.addEventListener('DOMContentLoaded', function() {
    new PagefindUI({
        element: "#search",
        pageSize: 5,
        showSubResults: true,
        showImages: false,
    })
	MicroModal.init()

    document.querySelector('#nav-link-search').addEventListener('click', function(ev) {
	        ev.preventDefault()
         console.log("search link clicked ")

	  MicroModal.show('modal-1', {
	  		onClose: function() { 
                console.log("search modal closed")
                document.querySelector('#nav-link-search').blur(); 
            },
	  		disableFocus: true
	  })
	  document.querySelector('.pagefind-ui__search-input').focus()
	});

}, false);
