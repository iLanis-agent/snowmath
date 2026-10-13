(function (root) {
  "use strict";
  var FRESH_KG_M3 = 100; // labeled fresh-snow density, kg per m3
  var RATE_KG_MIN = 15;  // labeled shoveling rate, kg per minute
  var MELT_G_M2 = 100;   // labeled ice-melt dose, grams per m2
  var BAG_KG = 10;       // labeled ice-melt bag, kg

  function round1(x) { return Math.round(x * 10) / 10; }
  function plural(n, word, form) { return n + " " + (n === 1 ? word : (form || word + "s")); }

  function snowKg(areaM2, snowCm) {
    var m3 = round1(areaM2 * snowCm / 100);
    var kg = round1(m3 * FRESH_KG_M3);
    return { m3: m3, kg: kg };
  }

  function loadPlan(areaM2, snowCm) {
    if (!(areaM2 > 0) || !(snowCm > 0)) return { error: "the area and the snowfall must be positive" };
    var s = snowKg(areaM2, snowCm);
    var verdict;
    if (s.kg <= 50) verdict = "a broom job";
    else if (s.kg <= 600) verdict = "a shovel job";
    else if (s.kg <= 2000) verdict = "a blower job";
    else verdict = "a plow job";
    return { m3: s.m3, kg: s.kg, verdict: verdict };
  }

  function timePlan(areaM2, snowCm) {
    if (!(areaM2 > 0) || !(snowCm > 0)) return { error: "the area and the snowfall must be positive" };
    var s = snowKg(areaM2, snowCm);
    var minutes = round1(s.kg / RATE_KG_MIN);
    var verdict;
    if (minutes <= 15) verdict = "a quick clear";
    else if (minutes <= 45) verdict = "a morning workout";
    else verdict = "a hire-it-out afternoon";
    return { kg: s.kg, minutes: minutes, verdict: verdict };
  }

  function meltPlan(areaM2) {
    if (!(areaM2 > 0)) return { error: "the area must be positive" };
    var kg = round1(areaM2 * MELT_G_M2 / 1000);
    var bags = Math.ceil(kg / BAG_KG);
    var verdict;
    if (kg <= 5) verdict = "a doorstep sprinkle";
    else if (kg <= 20) verdict = "a path and a porch";
    else verdict = "a rink patrol";
    return { kg: kg, bags: bags, verdict: verdict };
  }

  function renderLoad(r, areaM2, snowCm) {
    return "Your " + areaM2 + " m2 drive under " + snowCm + " cm of fresh snow holds " + r.m3 + " m3 - "
      + r.kg + " kg at a labeled " + FRESH_KG_M3 + " kg per m3, " + r.verdict + ".";
  }

  function renderTime(r) {
    return "That " + r.kg + " kg at a labeled " + RATE_KG_MIN + " kg a minute asks " + r.minutes
      + " minutes of shoveling - " + r.verdict + ".";
  }

  function renderMelt(r, areaM2) {
    return "Your " + areaM2 + " m2 drive at a labeled " + MELT_G_M2 + " g per m2 asks " + r.kg
      + " kg of ice melt - " + plural(r.bags, "bag") + " of labeled " + BAG_KG + " kg, " + r.verdict + ".";
  }

  var api = { loadPlan: loadPlan, timePlan: timePlan, meltPlan: meltPlan, renderLoad: renderLoad, renderTime: renderTime, renderMelt: renderMelt };
  if (typeof module !== "undefined" && module.exports) module.exports = api; else root.SnowMath = api;
})(this);
