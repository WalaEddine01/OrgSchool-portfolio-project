document.addEventListener("DOMContentLoaded", function () {
  $("button").click(function () {
    const amenities = [];
    $('input[type="checkbox"]:checked').each(function () {
      amenities.push({
        id: $(this).attr("data-id"),
        name: $(this).attr("data-name"),
      });
      $.ajax({
        type: "POST",
        url: "http://localhost:5001/api/v1/schools_search",
        contentType: "application/json",
        data: JSON.stringify({ amenities }),
      }).done(function (data) {
        for (const school of data) {
          const article = [
            "<article>",
            '<div class="title_box">',
            `<h2>${school.name}</h2>`,
            `<div class="price_by_night">$${school.price_by_night}</div>`,
            "</div>",
            '<div class="information">',
            `<div class="max_guest">${school.max_guest} Guest(s)</div>`,
            `<div class="number_rooms">${school.number_rooms} Bedroom(s)</div>`,
            `<div class="number_bathrooms">${school.number_bathrooms} Bathroom(s)</div>`,
            "</div>",
            '<div class="description">',
            `${school.description}`,
            "</div>",
            "</article>",
          ];
          $(".schools").append(article.join(""));
        }
      });
    });
  });
});
document.addEventListener("DOMContentLoaded", function () {
  const url = "http://localhost:5001/api/v1/schools_search";
  $.ajax({
    type: "POST",
    url,
    contentType: "application/json",
    data: JSON.stringify({}),
  }).done(function (data) {
    for (const school of data) {
      const article = [
        "<article>",
        '<div class="title_box">',
        `<h2>${school.name}</h2>`,
        `<div class="price_by_night">$${school.price_by_night}</div>`,
        "</div>",
        '<div class="information">',
        `<div class="max_guest">${school.max_guest} Guest(s)</div>`,
        `<div class="number_rooms">${school.number_rooms} Bedroom(s)</div>`,
        `<div class="number_bathrooms">${school.number_bathrooms} Bathroom(s)</div>`,
        "</div>",
        '<div class="description">',
        `${school.description}`,
        "</div>",
        "</article>",
      ];
      $(".schools").append(article.join(""));
    }
  });
});
document.addEventListener("DOMContentLoaded", function apiStatus() {
  $.get("http://localhost:5001/api/v1/status/", function (data, status) {
    if (data.status === "OK") {
      $("#api_status").addClass("available");
    } else {
      $("#api_status").removeClass("available");
    }
  });
});
document.addEventListener("DOMContentLoaded", function checkAmenities() {
  const amenities = {};
  $('input[type="checkbox"]').change(function () {
    if ($(this).is(":checked")) {
      amenities[$(this).data("id")] = $(this).data("name");
    } else {
      delete amenities[$(this).data("id")];
    }
    const amenitiesList = Object.values(amenities);
    if (amenitiesList.length > 0) {
      $(".amenities h4").text(amenitiesList.join(", "));
    } else {
      $(".amenities h4").html("&nbsp;");
    }
  });
});
