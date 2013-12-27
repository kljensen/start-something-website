$(document).ready(function(){

  // Are we currently trying to load the carousel?
  // 
  var loading = false,
    loaded = false,
    holderId = '#carousel-holder';

  // Function that we'll call when the screen is resized
  // or the page is first loaded.
  // 
  function loadCarousel(){

    // Don't try to load the carousel if we're 
    // already in the process of loading it. Also,
    // don't load it if we've already loaded it.
    // Finally, only try to load the carousel if we're
    // on a screen where it's visible.  In our CSS,
    // we're hiding it on small screens. Finally,
    //
    if (loading === true || loaded === true || $(holderId).is(':visible') === false) {
      return;
    }

    // Try to load the carousel. Notice that we're
    // using jQuery's Promises here (the .done and
    // .always methods, which are chainable).
    //
    loading = true;
    $.get('/carousel')
      .done(function(htmlFragment){

        // Add the carousel to the DOM
        $(holderId).html(htmlFragment);

        // Save that we're loaded
        loaded = true;

        // Unbind the callback so that it never
        // fires again
        $(window).unbind('resize', loadCarousel);

      })
      .always(function(){loading = false});
  }

  // Try to load the carousel on window resize.
  // 
  $(window).bind('resize', loadCarousel);

  // Try to load the carousel once when the DOM is ready.
  // 
  loadCarousel();
});