from http.server import BaseHTTPRequestHandler, HTTPServer
import os

class PortfolioHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Serve the main page
        if self.path in ['/', '/index', '/index.html']:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            # HTML Content for One-Page Portfolio
            html_content = """
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>My Portfolio</title>
                  <style>
                    body {
                        font-family: Arial, sans-serif;
                        margin: 0;
                        padding: 0;
                        background-color: #f4f4f4;
                        text-align: center;
                         padding-bottom: 60px;
                    }
                    section {
                        padding: 50px 20px;
                    }
                    h2 {
                        color: #333;
                    }
                    p {
                        color: #666;
                        line-height: 1.6;
                    }
                    .gallery-container {
                        position: relative;
                        width: 80%;
                        margin: 0 auto;
                    }
                    .gallery {
                        display: flex;
                        justify-content: center;
                        flex-wrap: wrap;
                        gap: 30px;
                    }
                    
                    .gallery img:hover {
                         transform: scale(1.05);
                    }
                    .gallery img {
                        width: 300px;
                        height: 300px;
                        object-fit: cover;
                        border-radius: 10px;
                        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
                        transition: transform 0.3s ease;
                        
                    }
                    .carousel-buttons {
                        position: absolute;
                        top: 50%;
                        width: 100%;
                        display: flex;
                        justify-content: space-between;
                        transform: translateY(-30%);
                    }

                    .carousel-button {
                        background-color: rgba(0, 0, 0, 0.7);
                        color: white;
                        padding: 15px;
                        border: none;
                        cursor: pointer;
                        border-radius: 50%;
                        font-size: 24px;
                        transition: transform 0.3s ease, background-color 0.3s ease;
                        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
                    }

                    .carousel-button:hover {
                        transform: scale(1.2);  /* Slightly enlarge the button on hover */
                        background-color: rgba(0, 0, 0, 0.9);  /* Darker background on hover */
                    }

                    .carousel-button:focus {
                        outline: none;  /* Remove focus outline */
                    }
                    
                    header {
                        background-color: #333;
                        padding: 20px;
                        color: white;
                        font-weight: bold;
                    }
                    header h1, header p, header a {
                        color: white; 
                        font-weight: bold;
                        text-decoration: none;
                        font-size: 20px;
                        word-spacing: 30px; 
                        letter-spacing: 2px;
                         display: inline-block;
                    }
                    
                    nav a {
                        font-size: 20px;
                        font-weight: bold;
                        color: white;
                        text-decoration: none;
                        margin: 0 28px; /* Add space between words */
                        display: inline-block; /* Ensures spacing applies */
                    }

                    
                    footer {
                        background: #333;
                        color: #fff;
                        padding: 5px;
                        position: fixed;
                        bottom: 5px;
                       
                        width: 100%;   
                    }
                </style>
            </head>
            <body>
            
                <header>
                    <nav>
                        <a href="/">Home</a>
                      
                    </nav>
                </header>
            
                <!-- About Me Section -->
                
                  
                <section>
                    <h2>About Me</h2>
                    <p>I am a results-driven Software Engineer and Data Analyst with experience in website development, data management, and cloud technologies. 
                    With a strong background in Python, SQL, Java, and cloud platforms like Google Cloud, I specialize in building data-driven applications, optimizing databases, and developing efficient ETL pipelines. 
                    My expertise extends to data visualization, analytics, and statistical modeling using tools like Power BI, Tableau, Looker, and BigQuery.

                    Beyond technical skills, I am passionate about problem-solving, collaboration, and innovation, whether it's developing applications, analyzing complex datasets, or mentoring others.
                    I continuously strive to improve what I know and learn new skills.</p>
                </section>

                <!-- Languages Section -->
                <section>
                    <h2>Languages</h2>
                    <div class="gallery-container">
                        <div class="gallery" id="gallery">
                            <img src="/images/cpp_logo.png">
                            <img src="/images/C-logo.png">
                            <img src="/images/CSS-logo.png">
                            <img src="/images/React-logo.png">
                            <img src="/images/html-logo.png">
                            <img src="/images/node.png">
                            <img src="/images/Python-logo.png">
                            <img src="/images/sql.jpeg">
                            <img src="/images/js-logo.png">
                            <img src="/images/PHP.png">
                            <img src="/images/java.png">
                            <img src="/images/Typescript-logo.png">
                        </div>
                        <div class="carousel-buttons">
                            <button class="carousel-button" onclick="prevImage()">&#10094;</button>
                            <button class="carousel-button" onclick="nextImage()">&#10095;</button>
                        </div>
                    </div>
                </section>

                <!-- Softwares Section -->
                <section>
                    <h2>Some Softwares</h2>
                    <div class="gallery">
                        <img src="/images/github.png" >
                        <img src="/images/GCP-logo.png" >
                        <img src="/images/Microsoft_Excel.png" >
                        <img src="/images/postman.png" >
                        <img src="/images/Power-BI-Logo.png" >
                        <img src="/images/Tableau-Logo.png" >
                        <img src="/images/word-logo.png" >
                        <img src="/images/firebase.png" >
                        <img src="/images/figma.jpg" >
                        <img src="/images/mongo.png" >
                    </div>
                    
                 
                </section>

                <!-- Sports Section -->
                <section>
                    <h2>Sports</h2>
                    <div class="gallery">
                        <img src="/images/volleyball.jpg">
                        <img src="/images/tennis.jpg" >
                        <img src="/images/soccer.jpg">
                        <img src="/images/football.jpg" ">
                        <img src="/images/basketball.jpg" ">
                    </div>
                </section>

                <!-- Footer -->
                <footer>
                    <p>&copy; 2025 Your Name. All Rights Reserved.</p>
                </footer>

                <script>
                let currentIndex = 0;
                const images = document.querySelectorAll('#gallery img');
                const totalImages = images.length;
                const showImages = 4;

                // Show only 4 images at a time
                function displayImages() {
                    images.forEach((img, index) => {
                        img.style.display = (index >= currentIndex && index < currentIndex + showImages) ? 'block' : 'none';
                    });
                }

                // Show next set of images
                function nextImage() {
                    if (currentIndex + showImages < totalImages) {
                        currentIndex += showImages; // Move forward by 4 images
                    } else {
                        currentIndex = 0; // Loop back to the start
                    }
                    displayImages();
                }

                // Show previous set of images
                function prevImage() {
                    if (currentIndex - showImages >= 0) {
                        currentIndex -= showImages; // Move backward by 4 images
                    } else {
                        currentIndex = totalImages - showImages; // Loop to the last full set
                    }
                    displayImages();
                }

                // Initial display
                displayImages();

                </script>
            </body>
            </html>
            """
            self.wfile.write(html_content.encode('utf-8'))

        # Serve images from the "images" directory
        elif self.path.startswith('/images/'):
            image_path = self.path.lstrip('/')
            if os.path.exists(image_path):
                # Dynamically determine the image type
                extension = os.path.splitext(image_path)[1].lower()
                if extension in ['.jpg', '.jpeg']:
                    self.send_response(200)
                    self.send_header('Content-type', 'image/jpeg')
                elif extension == '.png':
                    self.send_response(200)
                    self.send_header('Content-type', 'image/png')
                else:
                    self.send_response(415)  # Unsupported Media Type
                    self.end_headers()
                    self.wfile.write(b"415 Unsupported Media Type")
                    return
                self.end_headers()
                with open(image_path, 'rb') as file:
                    self.wfile.write(file.read())
            else:
                self.send_response(404)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b"404 Not Found")
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"404 Not Found")

def run(server_class=HTTPServer, handler_class=PortfolioHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Server running on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
