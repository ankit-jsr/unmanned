// Waitlist embeds, one Tally form per profession.
// To go live: paste each form's ID (the part after tally.so/r/) below. Nothing else changes.
// Until an ID is filled in, the page shows a short "opening soon" note instead of a broken form.
(function () {
  var FORMS = {
    "grant-writers": "",
    "researchers": "",
    "newsletter-operators": ""
  };

  var box = document.querySelector("[data-waitlist]");
  if (!box) return;
  var id = FORMS[box.getAttribute("data-waitlist")] || "";
  var fallback = box.querySelector(".waitlist-fallback");

  if (!/^[A-Za-z0-9]+$/.test(id)) {
    if (fallback) fallback.hidden = false;
    return;
  }

  var frame = document.createElement("iframe");
  frame.src = "https://tally.so/embed/" + id +
    "?alignLeft=1&hideTitle=1&transparentBackground=1&dynamicHeight=1";
  frame.title = "Join the waitlist";
  frame.loading = "lazy";
  frame.width = "100%";
  frame.height = "180";
  frame.style.border = "0";
  box.appendChild(frame);

  // Tally's script resizes the frame to fit the form. Optional: the form works without it.
  var s = document.createElement("script");
  s.src = "https://tally.so/widgets/embed.js";
  s.async = true;
  document.body.appendChild(s);
})();
