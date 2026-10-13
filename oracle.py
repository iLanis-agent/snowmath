import json, math

def jsnum(x):
    return int(x) if isinstance(x, float) and x == int(x) else x
def plural(n, word, form=None): return str(jsnum(n)) + " " + (word if n == 1 else (form or word + "s"))
def fmt(x): return str(jsnum(x))
def round1(x): return jsnum(math.floor(x * 10 + 0.5) / 10)

FRESH_KG_M3 = 100
RATE_KG_MIN = 15
MELT_G_M2 = 100
BAG_KG = 10

def snow_kg(areaM2, snowCm):
    m3 = round1(areaM2 * snowCm / 100)
    kg = round1(m3 * FRESH_KG_M3)
    return m3, kg

def load_plan(areaM2, snowCm):
    if not (areaM2 > 0) or not (snowCm > 0):
        return {"error": "the area and the snowfall must be positive"}
    m3, kg = snow_kg(areaM2, snowCm)
    if kg <= 50: verdict = "a broom job"
    elif kg <= 600: verdict = "a shovel job"
    elif kg <= 2000: verdict = "a blower job"
    else: verdict = "a plow job"
    return {"m3": m3, "kg": kg, "verdict": verdict}

def time_plan(areaM2, snowCm):
    if not (areaM2 > 0) or not (snowCm > 0):
        return {"error": "the area and the snowfall must be positive"}
    m3, kg = snow_kg(areaM2, snowCm)
    minutes = round1(kg / RATE_KG_MIN)
    if minutes <= 15: verdict = "a quick clear"
    elif minutes <= 45: verdict = "a morning workout"
    else: verdict = "a hire-it-out afternoon"
    return {"kg": kg, "minutes": minutes, "verdict": verdict}

def melt_plan(areaM2):
    if not (areaM2 > 0):
        return {"error": "the area must be positive"}
    kg = round1(areaM2 * MELT_G_M2 / 1000)
    bags = math.ceil(kg / BAG_KG)
    if kg <= 5: verdict = "a doorstep sprinkle"
    elif kg <= 20: verdict = "a path and a porch"
    else: verdict = "a rink patrol"
    return {"kg": kg, "bags": bags, "verdict": verdict}

def render_load(r, areaM2, snowCm):
    return ("Your " + fmt(areaM2) + " m2 drive under " + fmt(snowCm) + " cm of fresh snow holds " + fmt(r["m3"]) + " m3 - "
            + fmt(r["kg"]) + " kg at a labeled " + fmt(FRESH_KG_M3) + " kg per m3, " + r["verdict"] + ".")

def render_time(r, *args):
    return ("That " + fmt(r["kg"]) + " kg at a labeled " + fmt(RATE_KG_MIN) + " kg a minute asks " + fmt(r["minutes"])
            + " minutes of shoveling - " + r["verdict"] + ".")

def render_melt(r, areaM2):
    return ("Your " + fmt(areaM2) + " m2 drive at a labeled " + fmt(MELT_G_M2) + " g per m2 asks " + fmt(r["kg"])
            + " kg of ice melt - " + plural(r["bags"], "bag") + " of labeled " + fmt(BAG_KG) + " kg, " + r["verdict"] + ".")

cases = []
def add(fn, f, rf, args):
    r = f(*args)
    c = {"fn": fn, "args": args, "result": r}
    if "error" not in r: c["render"] = rf(r, *args)
    cases.append(c)

for a in [[40,10],[20,2],[40,25],[100,30],[60,15],[30,5],[80,20],[50,12],[0,10],[40,0]]:
    add("loadPlan", load_plan, render_load, a)
for a in [[40,10],[20,2],[100,30],[40,25],[60,15],[30,5],[80,20],[50,12],[0,10],[50,0]]:
    add("timePlan", time_plan, render_time, a)
for a in [[40],[100],[250],[10],[60],[150],[25],[200],[0],[80]]:
    add("meltPlan", melt_plan, render_melt, a)
json.dump(cases, open("expected.json", "w"), separators=(",", ":"))
print(len(cases), "cases")
