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
    'https://www.dailymoss.com/wp-content/uploads/2019/08/Very-Funny-Profile-Pictures-5.jpg',
    'https://i.pinimg.com/236x/0a/2c/27/0a2c27a6a12ad00dcab815ded6654de7--racoon-zoo-book.jpg',
    'https://wtspdp.com/wp-content/uploads/2020/03/cute-24.jpg',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ0GG8PyK4wxD0t-zFh-_qsZxvBBHkj6GTDDA&usqp=CAU',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRgyoHDv6HCKOSNwfPylSr9WElIx2nWEG9Hkw&usqp=CAU',
    'https://www.sciencesetavenir.fr/assets/img/2019/10/03/cover-r4x3w1000-5d97751628f07-058-2048000.jpg',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTc7T17josoLvz7KPQCxTLRdBiC0t15hh-z8w&usqp=CAU',
    'https://wallpaperaccess.com/full/2213448.jpg',
    'https://media.istockphoto.com/photos/funny-raccoon-in-green-sunglasses-showing-a-rock-gesture-isolated-on-picture-id1154370446?b=1&k=20&m=1154370446&s=170667a&w=0&h=eIUOEU55stRtm6FiyePapOmMLZISS0Wd9f6dM5J-dwQ=',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS4d2f2bsMAnDENktLKN-Uoerp0f2e-Tc5fsA&usqp=CAU'
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
          <h2>Bio 📖:</h2>
          <div class="biog">
            <p class="information">${data[i].bio}</p>
          </div>
        </div>
        <div class="product-image">
          <img src=${imglist[a]} alt="PatientTestimonialMasthead-1">
          <div class="info">
            <h2>Description</h2>
            <div class="wrapper">
  <button class="showusers" data-bs-toggle="offcanvas" data-bs-target="#offcanvasRight" aria-controls="offcanvasRight" data-id=${data[i].id}>
    Show info ! 
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
        a = Math.floor(Math.random() * 10);
      }
    },
    contentType: 'application/json'
  });

  $('.search_btn').click(function () {
    const username = $('#search_username').val();
    $('section.all_users').empty();
    $.ajax({
      type: 'POST',
      url: 'http://0.0.0.0:5001/api/v1/users_search/',
      data: JSON.stringify({ deps: Object.keys(dicod), cities: Object.keys(dicoc), sports: Object.keys(dicos), username: username }),
      success: function (data) {
        for (let i = 0; i < data.length; i++) {
          $('section.all_users').append(`
              <div class="containers">
        <div class="product-details">
          <h1>${data[i].username}</h1>
          <h2>Bio 📖:</h2>
          <div class="biog">
            <p class="information">${data[i].bio}</p>
          </div>
        </div>
        <div class="product-image">
          <img src=${imglist[a]} alt="PatientTestimonialMasthead-1">
          <div class="info">
            <h2>Description</h2>
            <div class="wrapper">
  <button class="showusers" data-bs-toggle="offcanvas" data-bs-target="#offcanvasRight" aria-controls="offcanvasRight" data-id=${data[i].id}>
    Show info ! 
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
          a = Math.floor(Math.random() * 10);
        }
      },
      contentType: 'application/json'
    });
  });

  $(document).on('click', '.showusers', function () {
    const userid = $(this).attr('data-id');
    $('.offcanvas_userinfosbio').empty();
    $('.offcanvas_userinfossports').empty();
    $('.offcanvas_userinfosreviews').empty();
    $('.offcanvas_userinfosevents').empty();
    $('.offcanvas_userinfoslocation').empty();
    $('.offcanvas_userinfossports').append('<h3>Sports 🏀:</h3>');
    $('.offcanvas_userinfosbio').append('<h3>Bio 📖:</h3>');
    $('.offcanvas_userinfosreviews').append('<h3>Reviews ⭐:</h3>');
    $('.offcanvas_userinfosevents').append('<h3>Join events 🏆:</h3>');
    $('.offcanvas_userinfoslocation').append('<h3>Location 🗺:</h3>');
    $.get(`http://0.0.0.0:5001/api/v1/users/${userid}/infos`, function (data) {
      $('.offcanvas_userinfosbio').append(`<li>${data.bio}</li>`);
      for (let i = 0; i < data.reviews.length; i++) {
        $('.offcanvas_userinfosreviews').append(`<li>${data.reviews[i]}</li>`);
      }
      for (let i = 0; i < data.events.length; i++) {
        $('.offcanvas_userinfosevents').append(`<li>${data.events[i]}</li>`);
      }
      for (let i = 0; i < data.sports.length; i++) {
        $('.offcanvas_userinfossports').append(`<li>${data.sports[i]}</li>`);
      }
      $('.offcanvas_userinfoslocation').append(`<li>${data.location[0]}, </li>`);
      $('.offcanvas_userinfoslocation li').append(`${data.location[1]}`);
      $('.offcanvas_userinfoslocation').append('<iframe  class="map" src="https://www.google.com/maps/embed?pb=!1m14!1m12!1m3!1d2880241.753016812!2d2.976337427332129!3d46.771539341491774!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!5e0!3m2!1sen!2sfr!4v1656239427935!5m2!1sen!2sfr" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>');
    });
  });
});
