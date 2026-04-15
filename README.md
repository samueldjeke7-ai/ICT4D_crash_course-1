# ICT4D_crash_course-1
A way for me to understand better each course

Usage
-

This project visualizes historical flood events in an interactive map using Leaflet and data from floodarchive.xlsx.

Local testing
-

Browsers block fetching local files (file://) for security reasons. To test the map, run a simple local HTTP server in the project folder and open the pages via http://localhost.

Options:

1. Python 3 (recommended):

   python -m http.server 8000

   Then open http://localhost:8000/index.html or http://localhost:8000/map.html

2. Node (http-server):

   npm install -g http-server
   http-server -p 8000

   Then open http://localhost:8000/index.html or http://localhost:8000/map.html

What works
-

- Interactive map using Leaflet with clustering and circle markers
- Reads flood data from floodarchive.xlsx via SheetJS
- Popups show basic event details

Next steps / recommendations
-

- Validate Excel headers and types; handle missing or invalid lat/long
- Sanitize popup content to avoid HTML injection
- Add loading/progress feedback for large files; consider server-side preprocessing or Web Workers for big datasets
- Add accessibility improvements (aria-labels, keyboard navigation)

Developer notes
-

Open the pages through an HTTP server as described above. If Excel doesn't load, check the browser console for CORS or file errors.
