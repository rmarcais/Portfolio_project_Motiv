$('document').ready(function () {
    const userid = $(".hello").attr('data-id');
    console.log(userid);
    let a = 0;
    const imglist = [
        "https://www.dailymoss.com/wp-content/uploads/2019/08/Very-Funny-Profile-Pictures-5.jpg"
    ];
    $.get(`http://0.0.0.0:5001/api/v1/users/${userid}/infos`, function (data) {
        $('section.all_users').append(`
                    <div class="containers">
              <div class="product-details">
                <h1>${data.username}</h1>
                <h2>Bio 📖:</h2>
                <div class="biogr">
                  <p class="information">${data.bio}</p>
                </div>
                <h2>Sports 🏀:</h2>
                <div class="biogr">
                  <p class="information">${data.sports}</p>
                </div>
                <h2>Location 🗺:</h2>
                <div class="biogr">
                  <p class="information">${data.location}</p>
                </div>
              </div>
              <div class="product-image">
                <img src=${imglist[a]} alt="PatientTestimonialMasthead-1">
                <div class="info">
                  <h2>Description</h2>
                  <div class="wrapper">
        <button class="showusers" data-bs-toggle="offcanvas" data-bs-target="#offcanvasRight" aria-controls="offcanvasRight">
          Show info ! 
          <span></span>
          <span></span>
          <span></span>
          <span></span>
        </button>
        <button class="updateinfo">
          Update info 
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
});

$(document).on('click', '.updateinfo', function () {
    $('.heading').empty();
    $('section.all_users').empty();
    $('section.all_users').append(`
    <div class="update">
            <div class="main-block">
                <h3 class="update_h3">
                    Update you account
                </h3>
                <form method="POST" action="/user_update/${userid}">
                  <hr>
                  <label id="icon" for="name"><i class="fas fa-user"></i></label>
                  <input type="text" name="username" id="username" placeholder="Userame"/>
                  <label id="icon" for="name"><i class="fas fa-address-book"></i></label>
                  <input type="text" name="bio" id="bio" placeholder="Bio*"/>
                  <label id="icon" for="name"><i class="fas fa-search-location"></i></label>
                  <input type="text" name="department" id="department" placeholder="Department"/>
                  <label id="icon" for="name"><i class="fas fa-location-arrow"></i></label>
                  <input type="text" name="city" id="city" placeholder="City"/>
                  <label id="icon" for="name"><i class="	fas fa-basketball-ball"></i></label>
                  <input type="text" name="sports" id="sports" placeholder="Add sports (Tennis, Dance, Football...)">
                  <div class="btn-block">
                    <button type="submit" class="submit">Let's go !</button>
                    </div>
                  
                </form>
              </div>
              </div>
    `)
});
          
    
  
    $(document).on('click', '.showusers', function () {
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
  