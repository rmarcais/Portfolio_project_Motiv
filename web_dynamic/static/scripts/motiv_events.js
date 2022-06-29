$('document').ready(function () {
  const user_id = $(".hello").attr('data-id');
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
      'https://images.unsplash.com/photo-1612872087720-bb876e2e67d1?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8dm9sbGV5YmFsbHxlbnwwfHwwfHw%3D&w=1000&q=80',
      'https://www.rnib.org.uk/sites/default/files/Stock_SSD_Football_702x400.JPG.jpg',
      'https://img.lemde.fr/2021/08/04/0/0/2500/1667/664/0/75/0/33e1bd6_5389918-01-06.jpg',
      'https://img-4.linternaute.com/F5Ba2PMEN2C3FbETxBtIF9oXWJg=/1500x/smart/578ef31fc88b496eb2c76781d7c73a61/ccmcms-linternaute/10767634.jpg'
    ];
    $.ajax({
      type: 'POST',
      url: 'http://0.0.0.0:5001/api/v1/events_search/',
      data: '{}',
      success: function (data) {
        for (let i = 0; i < data.length; i++) {
          $('section.all_users').append(`
                <div class="containers">
          <div class="product-details">
            <h1>${data[i].title}</h1>
            <div class="sousdiv">
            <h2>Description 📖:</h2>
            <div class="bio">
            
              <p class="information">${data[i].description}</p>
            </div>
            <h2>Date ⌚:</h2>
            <div class="bio">
            
              <p class="information">${data[i].date}</p>
            </div>
            <h2>Number of participants 👦:</h2>
            <div class="bio">
            
              <p class="information">${data[i].number_participants}</p>
            </div>
            </div>
            <h4 class="scroll">(scroll to see more infos)</h4>
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
    <button class="joinevent" data-id=${data[i].id} user_id=${user_id}>
    Join ! 
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
          a = Math.floor(Math.random() * 9);
        }
      },
      contentType: 'application/json'
    });
  
    $('.search_btn').click(function () {
      const eventname = $('#search_username').val()
      $('section.all_users').empty();
      $.ajax({
        type: 'POST',
        url: 'http://0.0.0.0:5001/api/v1/events_search/',
        data: JSON.stringify({ deps: Object.keys(dicod), cities: Object.keys(dicoc), sport: Object.keys(dicos), eventname: eventname}),
        success: function (data) {
          
          for (let i = 0; i < data.length; i++) {
            $('section.all_users').append(`
            <div class="containers">
            <div class="product-details">
              <h1>${data[i].title}</h1>
              <div class="sousdiv">
              <h2>Description 📖:</h2>
              <div class="bio">
              
                <p class="information">${data[i].description}</p>
              </div>
              <h2>Date ⌚:</h2>
              <div class="bio">
              
                <p class="information">${data[i].date}</p>
              </div>
              <h2>Number of participants 👦:</h2>
              <div class="bio">
              
                <p class="information">${data[i].number_participants}</p>
              </div>
              </div>
              <h4 class="scroll">(scroll to see more infos)</h4>
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
      <button class="joinevent" data-id=${data[i].id} user_id=${user_id}>
      Join ! 
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
            a = Math.floor(Math.random() * 9);
          }
        },
        contentType: 'application/json'
      });
    });
    
  
    $(document).on('click', '.showusers', function () {
      const eventid = $(this).attr("data-id");
      console.log(eventid)
        $(".offcanvas_userinfosdate").empty();
        $(".offcanvas_userinfoslocation").empty();
        $(".offcanvas_userinfosusers").empty();
        $(".offcanvas_userinfosparticipants").empty();
        $(".offcanvas_userinfosdescription").empty();
        $(".offcanvas_userinfossport").empty();
        $(".offcanvas_userinfossport").append(`<h3>Sport 🏀:</h3>`)
        $(".offcanvas_userinfosdescription").append(`<h3>Description 📖:</h3>`)
        $(".offcanvas_userinfosdate").append(`<h3>Date ⌚:</h3>`)
        $(".offcanvas_userinfosparticipants").append(`<h3>Particpants 👦:</h3>`)
        $(".offcanvas_userinfoslocation").append(`<h3>Location 🗺:</h3>`)
        $.get(`http://0.0.0.0:5001/api/v1/events/${eventid}/infos`, function (data) {
          console.log(data) 
        $(".offcanvas_userinfosdescription").append(`<li>${data.description}</li>`);
        $(".offcanvas_userinfosparticipants").append(`<li>${data.number_participants} :</li>`);
        for (let i = 0; i < data.users.length; i++) {
          $(".offcanvas_userinfosparticipants").append(`<li>${data.users[i]}</li>`);
        }
        $(".offcanvas_userinfossport").append(`<li>${data.sport}</li>`);
        $(".offcanvas_userinfosdate").append(`<li>${data.date}</li>`);
        $(".offcanvas_userinfoslocation").append(`<li>${data.location[0]}, </li>`);
        $(".offcanvas_userinfoslocation li").append(`${data.location[1]}`);
        $(".offcanvas_userinfoslocation").append(`<iframe  class="map" src="https://www.google.com/maps/embed?pb=!1m14!1m12!1m3!1d2880241.753016812!2d2.976337427332129!3d46.771539341491774!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!5e0!3m2!1sen!2sfr!4v1656239427935!5m2!1sen!2sfr" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>`);
      });
    });
      $(document).on('click', '.joinevent', function () {
        const eventid = $(this).attr('data-id');
        const user_id = $(this).attr('user_id');
        console.log(user_id);
        $.get(`http://0.0.0.0:5001/api/v1/events/${eventid}/users/${user_id}`);
        swal({
          title: "Wahooo!",
          text: "You've joined this event !",
          icon: "https://media.lesechos.com/api/v1/images/view/5e5e04b43e454609a3081d99/1280x720/0602862490248-web-tete.jpg",
          button: "Cool !",
        });
        });
      
  });
  