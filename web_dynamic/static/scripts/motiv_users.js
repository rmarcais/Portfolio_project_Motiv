$('document').ready(function () {
  const dicos = {};
  const dicod = {};
  const dicoc = {};
  $('.sport input[type="checkbox"]').change(function () {
    if (this.checked === true) {
      dicos[$(this).attr('data-id')] = $(this).attr('data-name');
    } else {
      delete dicos[$(this).attr('data-id')];
    }
    $('.sport h4').text(Object.values(dicos).join(', '));
  });
  $('.location input[type="checkbox"].depinput').change(function () {
    if (this.checked === true) {
      dicod[$(this).attr('data-id')] = $(this).attr('data-name');
    } else {
      delete dicod[$(this).attr('data-id')];
    }
    $('.location h4').text(Object.values(dicod).join(', '));
  });
  $('.location input[type="checkbox"].cityinput').change(function () {
    if (this.checked === true) {
      dicoc[$(this).attr('data-id')] = $(this).attr('data-name');
    } else {
      delete dicoc[$(this).attr('data-id')];
    }
    $('.location h4').text(Object.values(dicoc).join(', '));
  });
  let a = 0;
  const imglist = [
    'https://www.ihteachenglish.com/sites/default/files/styles/standard_header_mobile/public/resource/iStock-533861572-smaller.jpg?itok=EmHGfKoR',
    'https://static.nike.com/a/images/f_auto,cs_srgb/w_1536,c_limit/b858f2bd-d574-4147-ad85-4fb7e6c397b6/comment-trouver-son-allure-de-running-optimale.jpg',
    'https://domf5oio6qrcr.cloudfront.net/medialibrary/8853/rhythmic-dancing-shiloette-iStock_000087684873_Medium.jpg',
    'https://www.australiangeographic.com.au/wp-content/uploads/2018/06/surfer_bells_beach.jpg',
    'https://lepetitjournal.com/sites/default/files/inline-images/45190F89-5997-4F74-8CD2-4E5D47D77D5B.jpeg',
    'https://images.unsplash.com/photo-1612872087720-bb876e2e67d1?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8dm9sbGV5YmFsbHxlbnwwfHwwfHw%3D&w=1000&q=80'
  ];
  $.ajax({
    type: 'POST',
    url: 'http://0.0.0.0:5001/api/v1/users_search/',
    data: '{}',
    success: function (data) {
      for (let i = 0; i < data.length; i++) {
        $('section.all_users').append(`
              <div class="containers">
        <div class="product-details">
          <h1>${data[i].username}</h1>
          <h2>Bio:</h2>
          <div class="bio">
            <p class="information">${data[i].bio}</p>
          </div>
        </div>
        <div class="product-image">
          <img src=${imglist[a]} alt="PatientTestimonialMasthead-1">
          <div class="info">
            <h2>Description</h2>
            <div class="wrapper">
  <button class="showusers" data-bs-toggle="offcanvas" data-bs-target="#offcanvasRight" aria-controls="offcanvasRight" data-id=${data[i].id}>
    Show infos ! 
    <span></span>
    <span></span>
    <span></span>
    <span></span>
  </button>
</div>
          </div>
        </div>
      </div>
      `);
        a = Math.floor(Math.random() * 6);
      }
    },
    contentType: 'application/json'
  });

  $('.search_btn').click(function () {
    const username = $('#search_username').val()
    $('section.all_users').empty();
    $.ajax({
      type: 'POST',
      url: 'http://0.0.0.0:5001/api/v1/users_search/',
      data: JSON.stringify({ deps: Object.keys(dicod), cities: Object.keys(dicoc), sports: Object.keys(dicos), username: username}),
      success: function (data) {
        
        for (let i = 0; i < data.length; i++) {
          $('section.all_users').append(`
              <div class="containers">
        <div class="product-details">
          <h1>${data[i].username}</h1>
          <h2>Bio:</h2>
          <div class="bio">
            <p class="information">${data[i].bio}</p>
          </div>
        </div>
        <div class="product-image">
          <img src=${imglist[a]} alt="PatientTestimonialMasthead-1">
          <div class="info">
            <h2>Description</h2>
            <div class="wrapper">
  <button class="showusers" data-bs-toggle="offcanvas" data-bs-target="#offcanvasRight" aria-controls="offcanvasRight" data-id=${data[i].id}>
    Hover Here! 
    <span></span>
    <span></span>
    <span></span>
    <span></span>
  </button>
</div>
          </div>
        </div>
      </div>
      `);
          a = Math.floor(Math.random() * 6);
        }
      },
      contentType: 'application/json'
    });
  });
  

  $(document).on('click', '.showusers', function () {
    const userid = $(this).attr('data-id');
    $(".offcanvas_userinfosbio").empty();
    $(".offcanvas_userinfossports").empty();
    $(".offcanvas_userinfosreviews").empty();
    $(".offcanvas_userinfosevents").empty();
    $(".offcanvas_userinfoslocation").empty();
    $(".offcanvas_userinfossports").append(`<h3>Sports 🏀:</h3>`)
    $(".offcanvas_userinfosbio").append(`<h3>Bio 📖:</h3>`)
    $(".offcanvas_userinfosreviews").append(`<h3>Reviews ⭐:</h3>`)
    $(".offcanvas_userinfosevents").append(`<h3>Join events 🏆:</h3>`)
    $(".offcanvas_userinfoslocation").append(`<h3>Location 🗺:</h3>`)
    $.get(`http://0.0.0.0:5001/api/v1/users/${userid}/infos`, function (data) {
        $(".offcanvas_userinfosbio").append(`<li>${data.bio}</li>`);
        for (let i = 0; i < data.reviews.length; i++) {
          $(".offcanvas_userinfosreviews").append(`<li>${data.reviews[i]}</li>`);
        }
        for (let i = 0; i < data.events.length; i++) {
          $(".offcanvas_userinfosevents").append(`<li>${data.events[i]}</li>`);
        }
        for (let i = 0; i < data.sports.length; i++) {
        $(".offcanvas_userinfossports").append(`<li>${data.sports[i]}</li>`);
        }
        $(".offcanvas_userinfoslocation").append(`<li>${data.location[0]}, </li>`);
        $(".offcanvas_userinfoslocation li").append(`${data.location[1]}`);
        $(".offcanvas_userinfoslocation").append(`<iframe  class="map" src="https://www.google.com/maps/embed?pb=!1m14!1m12!1m3!1d2880241.753016812!2d2.976337427332129!3d46.771539341491774!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!5e0!3m2!1sen!2sfr!4v1656239427935!5m2!1sen!2sfr" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>`);

    
    })
  });

});
