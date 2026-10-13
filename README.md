# Snow math

Driveway snow clearing arithmetic: the forecast names the kilos, the kilos name the minutes, and the drive names the ice melt.

Live at https://ilanis-agent.github.io/snowmath/

## The three tools

- **Load plan** - m3 = area x snowfall, kg = m3 x labeled 100 kg per m3 of fresh snow, with broom, shovel, blower and plow bands.
- **Time plan** - minutes = kg / labeled 15 kg per minute, with quick-clear, morning-workout and hire-it-out bands.
- **Melt plan** - kg = area x labeled 100 g per m2; bags = ceil(kg / labeled 10 kg), with doorstep, path-and-porch and rink-patrol bands.

## Formulas and limits

- Volumes, masses and times are rounded to one decimal (round half up), mirroring the oracle float-for-float.
- Every number the app borrows is labeled in the interface: snow density, shoveling rate, melt dose, bag size.
- Illustrative planning arithmetic only. Shoveling is real exertion; pace yourself, take breaks, and hire it out if your doctor has ever mentioned your heart. This is not a weather service.

## Development

- `engine.js` - calculation and render engine (browser global `SnowMath`, CommonJS for tests).
- `oracle.py` - Python mirror of the engine; regenerates `expected.json`.
- `test.js` - runs every case through the engine and compares fields and render strings: `node test.js`.
